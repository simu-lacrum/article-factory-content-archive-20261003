from __future__ import annotations

import json
from collections import Counter, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .graph import export_graph
from .io_utils import file_sha256, read_text, text_sha256, write_text
from .settings import DEFAULT_DB


class GraphBootstrapError(RuntimeError):
    """Raised when the project graph cannot be traversed or mandatory memory is missing."""


def bootstrap_graph_memory(
    root: Path,
    *,
    limit_topics: int = -1,
    export_first: bool = True,
) -> dict[str, Any]:
    """Export and audit the complete graph, then resolve mandatory session reading.

    Coverage is literal: every node is visited across every connected component and
    every edge is validated and recorded. Edges are treated as undirected only for
    traversal coverage; their original direction and relation remain in the receipt.
    """

    root = root.resolve()
    output_dir = root / "memory" / "graph"
    output_dir.mkdir(parents=True, exist_ok=True)
    if export_first:
        export_graph(root / DEFAULT_DB, output_dir, limit_topics=limit_topics)

    graph_path = output_dir / "knowledge-graph.json"
    if not graph_path.exists():
        raise GraphBootstrapError(f"Knowledge graph does not exist: {graph_path}")

    try:
        graph = json.loads(read_text(graph_path))
    except json.JSONDecodeError as exc:
        raise GraphBootstrapError(f"Knowledge graph is invalid JSON: {exc}") from exc

    nodes = graph.get("nodes")
    edges = graph.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise GraphBootstrapError("Knowledge graph must contain node and edge arrays.")

    node_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(nodes):
        if not isinstance(item, dict) or not item.get("id"):
            raise GraphBootstrapError(f"Node at index {index} has no id.")
        node_id = str(item["id"])
        if node_id in node_by_id:
            raise GraphBootstrapError(f"Duplicate node id: {node_id}")
        node_by_id[node_id] = item

    adjacency: dict[str, set[str]] = {node_id: set() for node_id in node_by_id}
    inspected_edges: list[dict[str, Any]] = []
    for index, item in enumerate(edges):
        if not isinstance(item, dict):
            raise GraphBootstrapError(f"Edge at index {index} is not an object.")
        source = str(item.get("source") or "")
        target = str(item.get("target") or "")
        relation = str(item.get("relation") or "")
        if not source or not target or not relation:
            raise GraphBootstrapError(f"Edge at index {index} is incomplete.")
        if source not in node_by_id or target not in node_by_id:
            raise GraphBootstrapError(
                f"Edge at index {index} points to a missing node: {source} -> {target}"
            )
        adjacency[source].add(target)
        adjacency[target].add(source)
        canonical = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        inspected_edges.append(
            {
                "index": index,
                "source": source,
                "target": target,
                "relation": relation,
                "sha256": text_sha256(canonical),
            }
        )

    visited: set[str] = set()
    traversal_order: list[str] = []
    components: list[list[str]] = []
    for start in sorted(node_by_id):
        if start in visited:
            continue
        queue: deque[str] = deque([start])
        visited.add(start)
        component: list[str] = []
        while queue:
            current = queue.popleft()
            traversal_order.append(current)
            component.append(current)
            for neighbor in sorted(adjacency[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        components.append(component)

    total_nodes = len(node_by_id)
    total_edges = len(edges)
    if len(visited) != total_nodes:
        raise GraphBootstrapError(
            f"Incomplete node traversal: visited {len(visited)} of {total_nodes}."
        )
    if len(inspected_edges) != total_edges:
        raise GraphBootstrapError(
            f"Incomplete edge inspection: inspected {len(inspected_edges)} of {total_edges}."
        )

    mandatory_nodes: list[dict[str, Any]] = []
    required_file_origins: dict[str, set[str]] = {}
    required_markers: dict[str, set[str]] = {}
    directives: list[str] = []
    for node_id in traversal_order:
        item = node_by_id[node_id]
        props = item.get("props") if isinstance(item.get("props"), dict) else {}
        is_mandatory = item.get("kind") == "mandatory_instruction" or bool(
            props.get("mandatory_on_session_start")
        )
        if not is_mandatory:
            continue
        mandatory_nodes.append(
            {
                "id": node_id,
                "label": item.get("label") or node_id,
                "kind": item.get("kind"),
                "version": props.get("version"),
                "priority": props.get("priority"),
            }
        )
        directive = props.get("session_directive")
        if directive:
            directives.append(str(directive))
        requested: list[str] = []
        canonical_file = props.get("canonical_file")
        if canonical_file:
            requested.append(str(canonical_file))
        extra_files = props.get("required_files")
        if isinstance(extra_files, list):
            requested.extend(str(value) for value in extra_files if value)
        for relative in requested:
            normalized = relative.replace("\\", "/")
            required_file_origins.setdefault(normalized, set()).add(node_id)
        marker_map = props.get("required_markers")
        if isinstance(marker_map, dict):
            for relative, markers in marker_map.items():
                normalized = str(relative).replace("\\", "/")
                if isinstance(markers, list):
                    required_markers.setdefault(normalized, set()).update(
                        str(marker) for marker in markers if marker
                    )

    if not mandatory_nodes:
        raise GraphBootstrapError(
            "No mandatory_instruction node exists. The session cannot prove that required memory was loaded."
        )

    required_reading: list[dict[str, Any]] = []
    for relative in sorted(required_file_origins):
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise GraphBootstrapError(
                f"Mandatory reading escapes the project root: {relative}"
            ) from exc
        if not candidate.is_file():
            raise GraphBootstrapError(f"Mandatory reading is missing: {relative}")
        content = read_text(candidate)
        markers = sorted(required_markers.get(relative, set()))
        missing_markers = [marker for marker in markers if marker not in content]
        if missing_markers:
            raise GraphBootstrapError(
                f"Mandatory reading {relative} is missing required markers: {missing_markers}"
            )
        required_reading.append(
            {
                "path": relative,
                "sha256": file_sha256(candidate),
                "bytes": candidate.stat().st_size,
                "lines": len(content.splitlines()),
                "words": len(content.split()),
                "markers_verified": markers,
                "required_by": sorted(required_file_origins[relative]),
            }
        )

    node_kind_counts = Counter(str(item.get("kind") or "unknown") for item in nodes)
    relation_counts = Counter(str(item.get("relation") or "unknown") for item in edges)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    graph_sha = file_sha256(graph_path)
    receipt = {
        "status": "PASS",
        "generated_at": now,
        "project_root": str(root),
        "graph": {
            "path": str(graph_path.relative_to(root)).replace("\\", "/"),
            "sha256": graph_sha,
            "nodes_total": total_nodes,
            "nodes_visited": len(visited),
            "edges_total": total_edges,
            "edges_inspected": len(inspected_edges),
            "node_coverage_percent": 100.0,
            "edge_coverage_percent": 100.0,
            "connected_components": len(components),
            "traversal": "deterministic breadth-first traversal of every undirected connected component, including isolated nodes",
        },
        "node_kind_counts": dict(sorted(node_kind_counts.items())),
        "relation_counts": dict(sorted(relation_counts.items())),
        "mandatory_nodes": mandatory_nodes,
        "mandatory_directives": sorted(set(directives)),
        "required_reading": required_reading,
        "visited_node_ids": traversal_order,
        "component_node_ids": components,
        "inspected_edges": inspected_edges,
    }
    receipt_path = output_dir / "session-bootstrap.json"
    write_text(receipt_path, json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

    report_path = output_dir / "SESSION_BOOTSTRAP.md"
    write_text(report_path, _bootstrap_markdown(receipt))
    return {
        "status": "PASS",
        "graph": receipt["graph"]["path"],
        "json": str(graph_path),
        "mermaid": str(output_dir / "knowledge-graph.mmd"),
        "graph_sha256": graph_sha,
        "nodes": f"{len(visited)}/{total_nodes}",
        "edges": f"{len(inspected_edges)}/{total_edges}",
        "components": len(components),
        "mandatory_nodes": len(mandatory_nodes),
        "required_reading": [item["path"] for item in required_reading],
        "report": str(report_path),
        "receipt": str(receipt_path),
    }


def _bootstrap_markdown(receipt: dict[str, Any]) -> str:
    graph = receipt["graph"]
    lines = [
        "# Session Memory Bootstrap",
        "",
        f"Status: **{receipt['status']}**",
        f"Generated: `{receipt['generated_at']}`",
        f"Graph SHA-256: `{graph['sha256']}`",
        "",
        "This report proves that the bootstrap command traversed the complete exported graph. It is not a substitute for reading the mandatory files below.",
        "",
        "## Coverage",
        "",
        f"- Nodes visited: **{graph['nodes_visited']}/{graph['nodes_total']} (100%)**",
        f"- Edges inspected: **{graph['edges_inspected']}/{graph['edges_total']} (100%)**",
        f"- Connected components traversed: **{graph['connected_components']}**",
        f"- Method: {graph['traversal']}",
        "",
        "## Required action",
        "",
        "Read every file in the next section completely before planning, researching, writing, or editing. If the current task includes articles or visuals, apply the visual prompt guide and its Nano Banana Pro contract directly.",
        "",
        "## Required reading",
        "",
    ]
    for index, item in enumerate(receipt["required_reading"], start=1):
        lines.append(
            f"{index}. `{item['path']}` - {item['lines']} lines, {item['words']} words, SHA-256 `{item['sha256']}`"
        )
    lines.extend(["", "## Mandatory graph instructions", ""])
    for item in receipt["mandatory_nodes"]:
        version = f" v{item['version']}" if item.get("version") else ""
        lines.append(f"- `{item['id']}` - {item['label']}{version}")
    if receipt["mandatory_directives"]:
        lines.extend(["", "## Directives", ""])
        for item in receipt["mandatory_directives"]:
            lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Audit receipt",
            "",
            "The machine-readable receipt `memory/graph/session-bootstrap.json` records every visited node ID, every connected component, and a SHA-256 receipt for every inspected edge.",
            "",
        ]
    )
    return "\n".join(lines)
