from __future__ import annotations

import argparse
import json
import sys
import traceback
from pathlib import Path
from typing import Any

from .ai_memory import export_ai_memory
from .cli import init_project
from .codex_task import create_codex_task
from .db import KnowledgeDb
from .generator import generate_articles
from .graph import export_graph
from .graph_bootstrap import bootstrap_graph_memory
from .settings import DEFAULT_DB
from .workflow import prepare_codex_workflow


def text_result(value: Any) -> dict[str, Any]:
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, indent=2)
    return {"content": [{"type": "text", "text": value}]}


class ArticleFactoryMcp:
    def __init__(self, root: Path):
        self.root = root.resolve()
        init_project(self.root)

    @property
    def db_path(self) -> Path:
        return self.root / DEFAULT_DB

    def tools(self) -> list[dict[str, Any]]:
        return [
            {
                "name": "article_factory_status",
                "description": "Return knowledge base counts and database path.",
                "inputSchema": {"type": "object", "properties": {}},
            },
            {
                "name": "article_factory_search",
                "description": "Search source chunks and semantic clusters.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "game": {"type": "string", "default": "all"},
                        "count": {"type": "integer", "default": 8},
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "article_factory_topics",
                "description": "List article topic ideas from semantic clusters.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "game": {"type": "string", "default": "all"},
                        "language": {"type": "string", "default": "en"},
                        "count": {"type": "integer", "default": 10},
                        "include_restricted": {"type": "boolean", "default": False},
                    },
                },
            },
            {
                "name": "article_factory_draft",
                "description": "Generate article prompts, evidence packs, briefs, or full drafts via configured LLM.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "spec": {"type": "string"},
                        "count": {"type": "integer", "default": 1},
                        "game": {"type": "string"},
                        "language": {"type": "string", "default": "en"},
                        "llm": {"type": "string", "default": "none", "enum": ["none", "template", "ollama", "openai"]},
                        "model": {"type": "string"},
                        "include_restricted": {"type": "boolean", "default": False},
                    },
                    "required": ["spec"],
                },
            },
            {
                "name": "article_factory_codex_task",
                "description": "Prepare a Codex-only writing task with prompts and evidence packs. No external LLM is called.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "spec": {"type": "string"},
                        "count": {"type": "integer", "default": 10},
                        "game": {"type": "string"},
                        "language": {"type": "string", "default": "en"},
                        "include_restricted": {"type": "boolean", "default": False},
                    },
                    "required": ["spec"],
                },
            },
            {
                "name": "article_factory_prepare",
                "description": "Run ingest, create Codex writing task, export ai-memory snapshot, and export knowledge graph.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "spec": {"type": "string"},
                        "count": {"type": "integer", "default": 10},
                        "game": {"type": "string"},
                        "language": {"type": "string", "default": "en"},
                        "rebuild": {"type": "boolean", "default": False},
                        "include_restricted": {"type": "boolean", "default": False},
                    },
                    "required": ["spec"],
                },
            },
            {
                "name": "article_factory_export_memory",
                "description": "Export markdown memory snapshot for ai-memory or Obsidian.",
                "inputSchema": {"type": "object", "properties": {}},
            },
            {
                "name": "article_factory_export_graph",
                "description": "Export knowledge graph JSON and Mermaid files.",
                "inputSchema": {
                    "type": "object",
                    "properties": {"limit_topics": {"type": "integer", "default": 120}},
                },
            },
            {
                "name": "article_factory_graph_bootstrap",
                "description": "Export and traverse every graph node and edge, verify mandatory memory markers, and write the session audit receipt.",
                "inputSchema": {
                    "type": "object",
                    "properties": {"limit_topics": {"type": "integer", "default": 120}},
                },
            },
        ]

    def call_tool(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        db = KnowledgeDb(self.db_path)
        db.init()
        try:
            if name == "article_factory_status":
                return text_result(
                    {
                        "sources": db.conn.execute("SELECT COUNT(*) AS c FROM sources").fetchone()["c"],
                        "chunks": db.conn.execute("SELECT COUNT(*) AS c FROM chunks").fetchone()["c"],
                        "semantic_clusters": db.conn.execute("SELECT COUNT(*) AS c FROM semantic_clusters").fetchone()["c"],
                        "topic_ideas": db.conn.execute("SELECT COUNT(*) AS c FROM topic_ideas").fetchone()["c"],
                        "published_articles": db.conn.execute("SELECT COUNT(*) AS c FROM published_articles").fetchone()["c"],
                        "db": str(self.db_path),
                    }
                )
            if name == "article_factory_search":
                query = str(args.get("query", ""))
                game = str(args.get("game", "all"))
                count = int(args.get("count", 8))
                chunks = [
                    {"source": row["source_path"], "heading": row["heading"], "excerpt": row["body"][:800]}
                    for row in db.search_chunks(query, limit=count)
                ]
                clusters = [
                    {
                        "game": row["game"],
                        "cluster": row["cluster"],
                        "main_query": row["main_query"],
                        "frequency": row["frequency"],
                        "difficulty": row["difficulty"],
                    }
                    for row in db.search_clusters(query, game=game, limit=count)
                ]
                return text_result({"chunks": chunks, "clusters": clusters})
            if name == "article_factory_topics":
                rows = db.list_topics(
                    str(args.get("game", "all")),
                    str(args.get("language", "en")),
                    int(args.get("count", 10)),
                    include_restricted=bool(args.get("include_restricted", False)),
                )
                return text_result([dict(row) for row in rows])
            if name == "article_factory_draft":
                manifest = generate_articles(
                    self.db_path,
                    self.root / "output",
                    str(args.get("spec", "")),
                    count=int(args.get("count", 1)),
                    game=args.get("game"),
                    language=args.get("language"),
                    llm_provider=str(args.get("llm", "none")),
                    model=args.get("model"),
                    include_restricted=bool(args.get("include_restricted", False)),
                )
                return text_result(manifest)
            if name == "article_factory_codex_task":
                return text_result(
                    create_codex_task(
                        self.root,
                        str(args.get("spec", "")),
                        count=int(args.get("count", 10)),
                        game=args.get("game"),
                        language=args.get("language"),
                        include_restricted=bool(args.get("include_restricted", False)),
                    )
                )
            if name == "article_factory_prepare":
                return text_result(
                    prepare_codex_workflow(
                        self.root,
                        str(args.get("spec", "")),
                        count=int(args.get("count", 10)),
                        game=args.get("game"),
                        language=args.get("language"),
                        rebuild=bool(args.get("rebuild", False)),
                        include_restricted=bool(args.get("include_restricted", False)),
                    )
                )
            if name == "article_factory_export_memory":
                return text_result(export_ai_memory(self.db_path, self.root / "memory" / "ai-memory-export"))
            if name == "article_factory_export_graph":
                return text_result(
                    export_graph(
                        self.db_path,
                        self.root / "memory" / "graph",
                        limit_topics=int(args.get("limit_topics", 120)),
                    )
                )
            if name == "article_factory_graph_bootstrap":
                return text_result(
                    bootstrap_graph_memory(
                        self.root,
                        limit_topics=int(args.get("limit_topics", 120)),
                    )
                )
            raise ValueError(f"Unknown tool: {name}")
        finally:
            db.close()


def serve(root: Path) -> int:
    server = ArticleFactoryMcp(root)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            method = request.get("method")
            request_id = request.get("id")
            if method == "initialize":
                result = {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "article-factory", "version": "0.1.0"},
                }
            elif method == "tools/list":
                result = {"tools": server.tools()}
            elif method == "tools/call":
                params = request.get("params") or {}
                result = server.call_tool(str(params.get("name")), params.get("arguments") or {})
            else:
                raise ValueError(f"Unsupported method: {method}")
            response = {"jsonrpc": "2.0", "id": request_id, "result": result}
        except Exception as exc:
            print(traceback.format_exc(), file=sys.stderr)
            response = {
                "jsonrpc": "2.0",
                "id": request.get("id") if "request" in locals() else None,
                "error": {"code": -32000, "message": str(exc)},
            }
        print(json.dumps(response, ensure_ascii=False), flush=True)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Article Factory MCP stdio server.")
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    return serve(Path(args.root))


if __name__ == "__main__":
    raise SystemExit(main())
