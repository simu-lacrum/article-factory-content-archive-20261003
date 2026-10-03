from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .models import identity, validate_study
from .pages import fetch_page
from .service import build_study, import_metrics, import_backlinks, import_serps, read_json, save_json


def register_parser(subparsers) -> None:
    parser = subparsers.add_parser("research", help="Build evidence-led semantic cores, crawl sampled rivals, or import real volume metrics.")
    parser.add_argument("action", choices=["build", "fetch", "import-metrics", "import-backlinks", "import-serps", "activate", "status"])
    parser.add_argument("study", help="Study directory containing study.json, relative to --root.")
    parser.add_argument("--input", help="Provider CSV for metrics/backlinks, or a JSON snapshot list for SERPs.")
    parser.add_argument("--refresh", action="store_true", help="Refetch previously saved pages.")
    parser.set_defaults(func=command_research)


def command_research(args) -> int:
    root = Path(args.root).resolve()
    directory = (root / args.study).resolve()
    if not directory.is_relative_to(root):
        raise ValueError("Study must be inside workspace")
    study = read_json(directory / "study.json")
    validate_study(study)
    if args.action == "fetch":
        targets = {u: c["primary_query"] for c in study.get("clusters", []) for u in c.get("competitor_urls", [])}
        results = []
        def crawl(url, query):
            path = directory / "pages" / (identity(url) + ".json")
            if path.exists() and not args.refresh:
                cached = read_json(path)
                return {"url": url, "status": "cached" if cached.get("http_status") == 200 else "cached_failure", "error": cached.get("error")}
            try:
                page, html = fetch_page(url, query, study.get("brands", []), study.get("extraction_rules", {}).get(url))
                raw_path = directory / "raw" / (identity(url) + ".html")
                raw_path.parent.mkdir(parents=True, exist_ok=True)
                raw_path.write_text(html, encoding="utf-8")
                page["raw_file"] = str(raw_path.relative_to(directory))
                save_json(path, page)
                return {"url": url, "status": page["http_status"], "words": page["words"]}
            except Exception as exc:
                failure = {"url": url, "http_status": None, "error": f"{type(exc).__name__}: {exc}"}
                save_json(path, failure)
                return failure
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = [pool.submit(crawl, u, q) for u, q in targets.items()]
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                print(json.dumps(result, ensure_ascii=False), flush=True)
        return 0 if all(r.get("status") in {200, "cached"} for r in results) else 2
    if args.action in {"import-metrics", "import-backlinks", "import-serps"}:
        if not args.input:
            raise ValueError(f"{args.action} requires --input")
        importer = {"import-metrics": import_metrics, "import-backlinks": import_backlinks, "import-serps": import_serps}[args.action]
        result = importer(directory, (root / args.input).resolve())
    elif args.action == "activate":
        result = build_study(directory)
        save_json(root / "config" / "research.json", {"active_study": directory.relative_to(root).as_posix()})
        from ..settings import DEFAULT_DB
        from ..topics import rebuild_topic_ideas
        result = {"active_study": args.study, "topics": rebuild_topic_ideas(root / DEFAULT_DB, root), "coverage": result["coverage"]}
    elif args.action == "build":
        result = build_study(directory)
        result = {"core": str(directory / "core.json"), "coverage": result["coverage"]}
    else:
        result = read_json(directory / "core.json")["coverage"]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0
