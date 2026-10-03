from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .ai_memory import export_ai_memory
from .codex_task import create_codex_task
from .db import KnowledgeDb
from .doctor import doctor
from .generator import generate_articles
from .graph import export_graph
from .graph_bootstrap import bootstrap_graph_memory
from .ingest import ingest_workspace, materialize_link_sources
from .io_utils import write_text
from .published import append_published_csv, ensure_avoid_topics_file, ensure_published_file, load_published_csv, load_topic_exclusions
from .quality import review_manifest
from .settings import DEFAULT_DB
from .topics import rebuild_topic_ideas
from .visual_fidelity import DEFAULT_REFERENCE_DIR, analyze_warm_story_fidelity
from .workflow import prepare_codex_workflow


def init_project(root: Path) -> None:
    (root / ".article-factory").mkdir(exist_ok=True)
    (root / "knowledge" / "raw").mkdir(parents=True, exist_ok=True)
    (root / "knowledge" / "agent_memory" / "sources").mkdir(parents=True, exist_ok=True)
    (root / "knowledge" / "agent_memory" / "rules").mkdir(parents=True, exist_ok=True)
    (root / "knowledge" / "wiki").mkdir(parents=True, exist_ok=True)
    (root / "output" / "articles").mkdir(parents=True, exist_ok=True)
    (root / "output" / "briefs").mkdir(parents=True, exist_ok=True)
    (root / "output" / "prompts").mkdir(parents=True, exist_ok=True)
    (root / "published").mkdir(exist_ok=True)
    config_path = root / "config" / "article_factory.json"
    if not config_path.exists():
        write_text(
            config_path,
            json.dumps(
                {
                    "default_language": "en",
                    "default_game": "dota2",
                    "default_llm_provider": "none",
                    "ollama_model": "llama3.1:8b",
                    "openai_model": "gpt-4.1-mini",
                    "article_rules": {
                        "must_use_evidence_pack": True,
                        "no_unsupported_current_facts": True,
                        "no_operational_anti_cheat_evasion_or_cheat_implementation": True,
                        "native_ad_integration": True,
                    },
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )
    published_path = root / "published" / "articles.csv"
    exclusions_path = root / "published" / "avoid_topics.txt"
    ensure_published_file(published_path)
    ensure_avoid_topics_file(exclusions_path)
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    load_published_csv(db, published_path)
    load_topic_exclusions(db, exclusions_path)
    db.close()


def command_init(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    print(f"Initialized article factory in {root}")
    return 0


def command_ingest(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    stats = ingest_workspace(root / DEFAULT_DB, root, rebuild=args.rebuild, links_file=Path(args.links).resolve() if args.links else None)
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    published_count = load_published_csv(db, root / "published" / "articles.csv")
    exclusion_count = load_topic_exclusions(db, root / "published" / "avoid_topics.txt")
    db.close()
    topics = rebuild_topic_ideas(root / DEFAULT_DB, root)
    print(
        json.dumps(
            {
                "sources": stats.sources,
                "chunks": stats.chunks,
                "clusters": stats.clusters,
                "wiki_pages": stats.wiki_pages,
                "topic_ideas": topics,
                "published_articles": published_count,
                "topic_exclusions": exclusion_count,
                "warnings": stats.warnings or [],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def command_materialize_links(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    stats = materialize_link_sources(
        root,
        links_file=Path(args.links).resolve() if args.links else None,
        force=args.force,
    )
    print(
        json.dumps(
            {
                "link_source_files": stats.files,
                "fetched": stats.fetched,
                "skipped": stats.skipped,
                "outputs": stats.outputs or [],
                "warnings": stats.warnings or [],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def command_topics(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    rows = db.list_topics(args.game, args.language, args.count, include_restricted=args.include_restricted)
    for i, row in enumerate(rows, start=1):
        print(f"{i}. [{row['game']}/{row['language']}/{row['risk_level']}] score={row['score']:.2f} {row['title']}")
        print(f"   cluster: {row['cluster']}")
        print(f"   main query: {row['main_query']}")
    db.close()
    return 0


def command_search(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    print("Chunks:")
    for row in db.search_chunks(args.query, limit=args.count):
        print(f"- {row['source_path']} / {row['heading']}")
    print("\nClusters:")
    for row in db.search_clusters(args.query, game=args.game, limit=args.count):
        print(f"- [{row['game']}] {row['cluster']} -> {row['main_query']}")
    db.close()
    return 0


def command_draft(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    if not (root / DEFAULT_DB).exists():
        ingest_workspace(root / DEFAULT_DB, root, rebuild=False)
        rebuild_topic_ideas(root / DEFAULT_DB, root)
    manifest = generate_articles(
        root / DEFAULT_DB,
        root / "output",
        args.spec,
        count=args.count,
        game=args.game,
        language=args.language,
        llm_provider=args.llm,
        model=args.model,
        mark_used=args.mark_used,
        include_restricted=args.include_restricted,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


def command_codex_task(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    if not (root / DEFAULT_DB).exists():
        ingest_workspace(root / DEFAULT_DB, root, rebuild=False)
        rebuild_topic_ideas(root / DEFAULT_DB, root)
    result = create_codex_task(
        root,
        args.spec,
        count=args.count,
        game=args.game,
        language=args.language,
        include_restricted=args.include_restricted,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def command_prepare(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    result = prepare_codex_workflow(
        root,
        args.spec,
        count=args.count,
        game=args.game,
        language=args.language,
        rebuild=args.rebuild,
        links=Path(args.links).resolve() if args.links else None,
        include_restricted=args.include_restricted,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def command_review(args: argparse.Namespace) -> int:
    manifest = Path(args.manifest).resolve()
    output = Path(args.output).resolve() if args.output else manifest.with_suffix(".review.json")
    result = review_manifest(manifest, output)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["total"] and not any(result[k] for k in ("fail", "needs_review", "not_generated")) else 2


def command_visual_fidelity(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    candidate = Path(args.candidate).resolve()
    references = (
        Path(args.references).resolve()
        if args.references
        else (root / DEFAULT_REFERENCE_DIR).resolve()
    )
    result = analyze_warm_story_fidelity(candidate, references, accent=args.accent)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 2


def command_published(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    init_project(root)
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    if args.action == "load":
        count = load_published_csv(db, root / "published" / "articles.csv")
        print(json.dumps({"loaded": count}, ensure_ascii=False, indent=2))
    elif args.action == "add":
        if not args.title:
            raise SystemExit("published add requires --title")
        append_published_csv(
            root / "published" / "articles.csv",
            title=args.title,
            slug=args.slug,
            game=args.game,
            language=args.language,
            url=args.url,
            published_at=args.published_at,
            notes=args.notes,
        )
        db.upsert_published_article(
            title=args.title,
            slug=args.slug,
            game=args.game,
            language=args.language,
            url=args.url,
            published_at=args.published_at,
            notes=args.notes,
        )
        db.conn.commit()
        print(json.dumps({"added": args.title}, ensure_ascii=False, indent=2))
    db.close()
    return 0


def command_status(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    db = KnowledgeDb(root / DEFAULT_DB)
    db.init()
    stats = {
        "sources": db.conn.execute("SELECT COUNT(*) AS c FROM sources").fetchone()["c"],
        "chunks": db.conn.execute("SELECT COUNT(*) AS c FROM chunks").fetchone()["c"],
        "semantic_clusters": db.conn.execute("SELECT COUNT(*) AS c FROM semantic_clusters").fetchone()["c"],
        "topic_ideas": db.conn.execute("SELECT COUNT(*) AS c FROM topic_ideas").fetchone()["c"],
        "published_articles": db.conn.execute("SELECT COUNT(*) AS c FROM published_articles").fetchone()["c"],
        "topic_exclusions": db.conn.execute("SELECT COUNT(*) AS c FROM topic_exclusions").fetchone()["c"],
        "runs": db.conn.execute("SELECT COUNT(*) AS c FROM article_runs").fetchone()["c"],
        "db": str((root / DEFAULT_DB).resolve()),
    }
    db.close()
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    print(json.dumps(doctor(root), ensure_ascii=False, indent=2))
    return 0


def command_ai_memory(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    result = export_ai_memory(root / DEFAULT_DB, root / "memory" / "ai-memory-export")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def command_graph(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if args.action == "export":
        result = export_graph(root / DEFAULT_DB, root / "memory" / "graph", limit_topics=args.limit_topics)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.action == "bootstrap":
        result = bootstrap_graph_memory(root, limit_topics=args.limit_topics)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="article-factory", description="Local SEO knowledge base and article generator.")
    parser.add_argument("--root", default=".", help="Workspace root. Defaults to current directory.")
    sub = parser.add_subparsers(dest="command", required=True)
    from .research.cli import register_parser
    register_parser(sub)

    p_init = sub.add_parser("init", help="Create folders, config, and database.")
    p_init.set_defaults(func=command_init)

    p_ingest = sub.add_parser("ingest", help="Ingest local markdown/CSV sources and rebuild topic ideas.")
    p_ingest.add_argument("--rebuild", action="store_true", help="Recreate the database before ingest.")
    p_ingest.add_argument("--links", help="Optional text file with one URL per line to materialize as markdown and ingest.")
    p_ingest.set_defaults(func=command_ingest)

    p_materialize = sub.add_parser("materialize-links", help="Fetch URL lists into local markdown agent-memory files.")
    p_materialize.add_argument("--links", help="Optional text file with one URL per line. Persistent lists live in knowledge/link_sources/.")
    p_materialize.add_argument("--force", action="store_true", help="Refresh existing materialized markdown files.")
    p_materialize.set_defaults(func=command_materialize_links)

    p_topics = sub.add_parser("topics", help="Show best topic ideas.")
    p_topics.add_argument("--count", type=int, default=10)
    p_topics.add_argument("--game", default="all")
    p_topics.add_argument("--language", default="en", choices=["all", "en", "ru"])
    p_topics.add_argument("--include-restricted", action="store_true", help="Include high-risk topics that require manual review.")
    p_topics.set_defaults(func=command_topics)

    p_search = sub.add_parser("search", help="Search indexed source chunks and semantic clusters.")
    p_search.add_argument("query")
    p_search.add_argument("--count", type=int, default=8)
    p_search.add_argument("--game", default="all")
    p_search.set_defaults(func=command_search)

    p_draft = sub.add_parser("draft", help="Generate article prompts, briefs, or full drafts through a provider.")
    p_draft.add_argument("--spec", required=True, help="Natural-language content task.")
    p_draft.add_argument("--count", type=int)
    p_draft.add_argument("--game")
    p_draft.add_argument("--language", choices=["all", "en", "ru"])
    p_draft.add_argument("--llm", default="none", choices=["none", "template", "ollama", "openai"])
    p_draft.add_argument("--model")
    p_draft.add_argument("--mark-used", action="store_true", help="Mark selected topics as used after generation.")
    p_draft.add_argument("--include-restricted", action="store_true", help="Allow restricted topics in automatic selection.")
    p_draft.set_defaults(func=command_draft)

    p_codex = sub.add_parser("codex-task", help="Prepare a Codex-only writing task with prompts and evidence packs.")
    p_codex.add_argument("--spec", required=True, help="Natural-language content task.")
    p_codex.add_argument("--count", type=int)
    p_codex.add_argument("--game")
    p_codex.add_argument("--language", choices=["all", "en", "ru"])
    p_codex.add_argument("--include-restricted", action="store_true", help="Allow restricted topics in automatic selection.")
    p_codex.set_defaults(func=command_codex_task)

    p_prepare = sub.add_parser("prepare", help="Run ingest, Codex task creation, ai-memory export, and graph export.")
    p_prepare.add_argument("--spec", required=True, help="Natural-language content task.")
    p_prepare.add_argument("--count", type=int)
    p_prepare.add_argument("--game")
    p_prepare.add_argument("--language", choices=["all", "en", "ru"])
    p_prepare.add_argument("--rebuild", action="store_true", help="Recreate the database before ingest.")
    p_prepare.add_argument("--links", help="Optional text file with one URL per line to materialize as markdown and ingest.")
    p_prepare.add_argument("--include-restricted", action="store_true", help="Allow restricted topics in automatic selection.")
    p_prepare.set_defaults(func=command_prepare)

    p_review = sub.add_parser("review", help="Run quality checks for a generation manifest.")
    p_review.add_argument("manifest")
    p_review.add_argument("--output")
    p_review.set_defaults(func=command_review)

    p_visual = sub.add_parser(
        "visual-fidelity",
        help="Compare a generated branch-B image with the persistent warm-story reference profile.",
    )
    p_visual.add_argument("candidate", help="Path to the generated image to audit.")
    p_visual.add_argument(
        "--references",
        help="Reference directory. Defaults to the persistent warm-story reference set.",
    )
    p_visual.add_argument(
        "--accent",
        required=True,
        help="Mapped brand color as hex; in branch B this is the dominant field replacing yellow/amber. Examples: #635FD5 or #FF1469.",
    )
    p_visual.set_defaults(func=command_visual_fidelity)

    p_published = sub.add_parser("published", help="Load or update published-article memory.")
    p_published.add_argument("action", choices=["load", "add"])
    p_published.add_argument("--title")
    p_published.add_argument("--slug")
    p_published.add_argument("--game")
    p_published.add_argument("--language", choices=["en", "ru"])
    p_published.add_argument("--url")
    p_published.add_argument("--published-at")
    p_published.add_argument("--notes")
    p_published.set_defaults(func=command_published)

    p_status = sub.add_parser("status", help="Print database stats.")
    p_status.set_defaults(func=command_status)

    p_doctor = sub.add_parser("doctor", help="Check local dependencies and generation providers.")
    p_doctor.set_defaults(func=command_doctor)

    p_memory = sub.add_parser("ai-memory", help="Export a markdown snapshot suitable for ai-memory/wiki-style memory.")
    p_memory.add_argument("action", choices=["export"])
    p_memory.set_defaults(func=command_ai_memory)

    p_graph = sub.add_parser("graph", help="Export or fully traverse the knowledge graph for a new Codex session.")
    p_graph.add_argument("action", choices=["export", "bootstrap"])
    p_graph.add_argument("--limit-topics", type=int, default=-1, help="Compatibility option; bootstrap always exports the complete graph.")
    p_graph.set_defaults(func=command_graph)

    return parser


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
