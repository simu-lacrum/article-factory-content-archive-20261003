from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .db import KnowledgeDb
from .io_utils import read_text, relpath, slugify, write_text


def node(node_id: str, label: str, kind: str, **props: Any) -> dict[str, Any]:
    return {"id": node_id, "label": label, "kind": kind, "props": props}


def edge(source: str, target: str, relation: str, **props: Any) -> dict[str, Any]:
    return {"source": source, "target": target, "relation": relation, "props": props}


def export_graph(db_path: Path, output_dir: Path, limit_topics: int = -1) -> dict[str, Any]:
    db = KnowledgeDb(db_path)
    db.init()
    root = db_path.parent.parent
    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, Any]] = []
    for row in db.conn.execute("SELECT id, path, kind, title FROM sources ORDER BY id").fetchall():
        source_id = f"source:{row['id']}"
        nodes[source_id] = node(source_id, row["title"] or row["path"], "source", path=row["path"], source_kind=row["kind"])
    for row in db.conn.execute("SELECT id, source_id, heading, slug FROM chunks ORDER BY id").fetchall():
        chunk_id = f"chunk:{row['id']}"
        nodes[chunk_id] = node(chunk_id, row["heading"], "chunk", slug=row["slug"])
        edges.append(edge(f"source:{row['source_id']}", chunk_id, "contains"))
    for row in db.conn.execute(
        "SELECT id, source_id, game, cluster, main_query, frequency, difficulty FROM semantic_clusters ORDER BY id"
    ).fetchall():
        cluster_id = f"cluster:{row['id']}"
        nodes[cluster_id] = node(
            cluster_id,
            row["cluster"],
            "semantic_cluster",
            game=row["game"],
            main_query=row["main_query"],
            frequency=row["frequency"],
            metric_status="legacy_unverified",
            difficulty=row["difficulty"],
        )
        edges.append(edge(f"source:{row['source_id']}", cluster_id, "defines_cluster"))
    for row in db.conn.execute(
        """
        SELECT id, game, language, title, cluster, main_query, source_kind, source_ref, risk_level, score
        FROM topic_ideas
        ORDER BY score DESC
        LIMIT ?
        """,
        (-1,),
    ).fetchall():
        topic_id = f"topic:{row['id']}"
        nodes[topic_id] = node(
            topic_id,
            row["title"],
            "topic",
            game=row["game"],
            language=row["language"],
            main_query=row["main_query"],
            risk_level=row["risk_level"],
            score=row["score"],
        )
        if row["source_kind"] == "semantic_csv" and f"cluster:{row['source_ref']}" in nodes:
            edges.append(edge(f"cluster:{row['source_ref']}", topic_id, "suggests_topic"))
        elif row["source_kind"] in {"cluster_map", "curated_topic_seed"}:
            source = db.conn.execute("SELECT id FROM sources WHERE path=?", (row["source_ref"],)).fetchone()
            if source:
                edges.append(edge(f"source:{source['id']}", topic_id, "curates_topic"))
    for row in db.conn.execute("SELECT id, title, game, language, url FROM published_articles ORDER BY id").fetchall():
        published_id = f"published:{row['id']}"
        nodes[published_id] = node(
            published_id,
            row["title"],
            "published_article",
            game=row["game"],
            language=row["language"],
            url=row["url"],
        )
    for row in db.conn.execute("SELECT id, pattern, note FROM topic_exclusions ORDER BY id").fetchall():
        exclusion_id = f"exclusion:{row['id']}"
        nodes[exclusion_id] = node(exclusion_id, row["pattern"], "topic_exclusion", note=row["note"])
        for topic in list(nodes.values()):
            if topic["kind"] != "topic":
                continue
            haystack = f"{topic['label']} {topic['props'].get('main_query', '')}".lower()
            if row["pattern"].lower() in haystack:
                edges.append(edge(exclusion_id, topic["id"], "blocks_topic"))
    load_explicit_graph_facts(root, nodes, edges)
    from .research.service import active_core
    core = active_core(root)
    if core:
        study_id = f"research:{core['study_id']}"
        nodes[study_id] = node(study_id, core['study_id'], "seo_research", market=core['market'], coverage=core['coverage'])
        for cluster in core['clusters']:
            cluster_id = f"research-cluster:{cluster['id']}"
            nodes[cluster_id] = node(cluster_id, cluster['title'], "research_cluster", game=cluster['game'],
                                     reader_job=cluster['reader_job'], primary_query=cluster['primary_query'],
                                     article_target_query=cluster.get('article_target_query', cluster['primary_query']),
                                     research_state=cluster.get('research_state'),
                                     validated_query_subsets=[g['queries'] for g in cluster.get('validated_query_subsets', [])],
                                     section_parent_id=cluster.get('section_parent_id'),
                                     grouping_basis=cluster['grouping_basis'], publication_action=cluster.get('publication_action'),
                                     primary_site=cluster.get('primary_site'), existing_url=cluster.get('existing_url'))
            edges.append(edge(study_id, cluster_id, "proposes_editorial_cluster"))
            if cluster.get('section_parent_id'):
                edges.append(edge(cluster_id, f"research-cluster:{cluster['section_parent_id']}", "included_as_section"))
            for topic in db.conn.execute("SELECT id FROM topic_ideas WHERE source_kind='seo_research' AND source_ref=?", (cluster['id'],)):
                edges.append(edge(cluster_id, f"topic:{topic['id']}", "informs_writing_task"))
        for item in core['keywords']:
            keyword_id = f"keyword:{item['id']}"
            nodes[keyword_id] = node(keyword_id, item['query'], "researched_keyword", game=item['game'],
                                     language=item['language'], volume=item['volume'], metric=item['metric'], discovery=item['discovery'])
            edges.append(edge(study_id, keyword_id, "researches_keyword"))
            if f"research-cluster:{item['cluster_id']}" in nodes:
                edges.append(edge(f"research-cluster:{item['cluster_id']}", keyword_id, "groups_query_hypothesis"))
    graph = {"nodes": list(nodes.values()), "edges": edges}
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "knowledge-graph.json"
    mermaid_path = output_dir / "knowledge-graph.mmd"
    write_text(json_path, json.dumps(graph, ensure_ascii=False, indent=2) + "\n")
    write_text(mermaid_path, graph_to_mermaid(graph))
    db.close()
    return {"json": str(json_path), "mermaid": str(mermaid_path), "nodes": len(nodes), "edges": len(edges)}


def load_explicit_graph_facts(root: Path, nodes: dict[str, dict[str, Any]], edges: list[dict[str, Any]]) -> None:
    facts_dir = root / "knowledge" / "graph_facts"
    if not facts_dir.exists():
        return
    for path in sorted(facts_dir.glob("*.json")):
        try:
            data = json.loads(read_text(path))
        except (json.JSONDecodeError, OSError):
            continue
        source_file = relpath(path, root)
        for item in data.get("entities", []):
            item_id = item.get("id")
            if not item_id:
                continue
            label = item.get("label") or item_id
            kind = item.get("kind") or "entity"
            props = {k: v for k, v in item.items() if k not in {"id", "label", "kind", "props"}}
            nested_props = item.get("props")
            if isinstance(nested_props, dict):
                props.update(nested_props)
            props["graph_fact_file"] = source_file
            nodes.setdefault(item_id, node(item_id, label, kind, **props))
        for item in data.get("relations", []):
            source = item.get("source")
            target = item.get("target")
            relation = item.get("relation")
            if not source or not target or not relation:
                continue
            if source not in nodes:
                nodes[source] = node(source, source, "entity_stub", graph_fact_file=source_file)
            if target not in nodes:
                nodes[target] = node(target, target, "entity_stub", graph_fact_file=source_file)
            props = {k: v for k, v in item.items() if k not in {"source", "target", "relation", "props"}}
            nested_props = item.get("props")
            if isinstance(nested_props, dict):
                props.update(nested_props)
            props["graph_fact_file"] = source_file
            edges.append(edge(source, target, relation, **props))


def graph_to_mermaid(graph: dict[str, Any], max_edges: int = 160) -> str:
    lines = ["flowchart LR"]
    labels: dict[str, str] = {}
    for item in graph["nodes"]:
        safe_id = safe_mermaid_id(item["id"])
        labels[item["id"]] = safe_id
        label = str(item["label"]).replace('"', "'")
        if len(label) > 48:
            label = label[:45] + "..."
        lines.append(f'  {safe_id}["{label}"]')
    for item in graph["edges"][:max_edges]:
        source = labels.get(item["source"])
        target = labels.get(item["target"])
        if not source or not target:
            continue
        relation = item["relation"].replace('"', "'")
        lines.append(f'  {source} -->|"{relation}"| {target}')
    return "\n".join(lines) + "\n"


def safe_mermaid_id(value: str) -> str:
    return "n_" + slugify(value).replace("-", "_")
