from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .ai_memory import export_ai_memory
from .codex_task import create_codex_task
from .db import KnowledgeDb
from .graph_bootstrap import bootstrap_graph_memory
from .ingest import ingest_workspace
from .io_utils import write_text
from .published import load_published_csv, load_topic_exclusions
from .settings import DEFAULT_DB
from .topics import rebuild_topic_ideas


def prepare_codex_workflow(
    root: Path,
    spec: str,
    *,
    count: int | None = None,
    game: str | None = None,
    language: str | None = None,
    rebuild: bool = False,
    links: Path | None = None,
    include_restricted: bool = False,
) -> dict[str, Any]:
    stats = ingest_workspace(root / DEFAULT_DB, root, rebuild=rebuild, links_file=links)
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    published_count = load_published_csv(db, root / "published" / "articles.csv")
    exclusion_count = load_topic_exclusions(db, root / "published" / "avoid_topics.txt")
    db.close()
    topics = rebuild_topic_ideas(root / DEFAULT_DB, root)
    task = create_codex_task(
        root,
        spec,
        count=count,
        game=game,
        language=language,
        include_restricted=include_restricted,
    )
    memory = export_ai_memory(root / DEFAULT_DB, root / "memory" / "ai-memory-export")
    graph = bootstrap_graph_memory(root)
    result = {
        "spec": spec,
        "ingest": {
            "sources": stats.sources,
            "chunks": stats.chunks,
            "clusters": stats.clusters,
            "wiki_pages": stats.wiki_pages,
            "warnings": stats.warnings or [],
            "topic_ideas_rebuilt": topics,
            "published_articles": published_count,
            "topic_exclusions": exclusion_count,
        },
        "task": task,
        "memory": memory,
        "graph": graph,
        "next_step": f"Open and follow {task['task']}",
    }
    current_path = root / "CURRENT_CODEX_TASK.md"
    write_text(current_path, current_task_markdown(result))
    result["current_task"] = str(current_path)
    write_text(root / "output" / "codex_tasks" / task["run_id"] / "prepare-result.json", json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return result


def current_task_markdown(result: dict[str, Any]) -> str:
    task = result["task"]
    lines = [
        "# Current Codex Article Task",
        "",
        "This project is Codex-first. Do not call an external LLM API. Codex writes the articles itself.",
        "",
        "## User Spec",
        "",
        result["spec"],
        "",
        "## Main Task File",
        "",
        f"[TASK.md]({task['task']})",
        "",
        "## Output",
        "",
        f"- Articles directory: `{task['article_dir']}`",
        f"- Manifest: `{task['manifest']}`",
        f"- Article index: `{task['index']}`",
        "",
        "## Required Finish Check",
        "",
        f"Run `python -m article_factory review output\\runs\\{task['run_id']}.json` and fix every issue.",
        "",
        "## Memory",
        "",
        f"- ai-memory export: `{result['memory']['output_dir']}`",
        f"- graph JSON: `{result['graph']['json']}`",
        f"- graph Mermaid: `{result['graph']['mermaid']}`",
        f"- full graph traversal: nodes `{result['graph']['nodes']}`, edges `{result['graph']['edges']}`",
        f"- mandatory session report: `{result['graph']['report']}`",
    ]
    return "\n".join(lines) + "\n"
