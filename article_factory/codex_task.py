from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .generator import generate_articles
from .io_utils import slugify, write_text
from .settings import DEFAULT_DB


def create_codex_task(
    root: Path,
    spec: str,
    *,
    count: int | None = None,
    game: str | None = None,
    language: str | None = None,
    include_restricted: bool = False,
) -> dict[str, Any]:
    manifest = generate_articles(
        root / DEFAULT_DB,
        root / "output",
        spec,
        count=count,
        game=game,
        language=language,
        llm_provider="none",
        include_restricted=include_restricted,
    )
    run_id = manifest["created_at"]
    task_dir = root / "output" / "codex_tasks" / run_id
    article_dir = root / "output" / "articles" / run_id
    manifest_path = root / "output" / "runs" / f"{run_id}.json"
    article_dir.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir(parents=True, exist_ok=True)
    for index, item in enumerate(manifest.get("items", []), start=1):
        target = article_dir / f"{index:02d}-{slugify(item['title'])}.md"
        item["brief"] = item["output"]
        item["output"] = str(target)
        item["status"] = "article"
    write_text(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    task_path = task_dir / "TASK.md"
    index_path = task_dir / "ARTICLE_INDEX.md"
    write_text(task_path, task_markdown(manifest, article_dir))
    write_text(index_path, index_markdown(manifest, article_dir))
    return {
        "run_id": run_id,
        "task": str(task_path),
        "index": str(index_path),
        "manifest": str(manifest_path),
        "article_dir": str(article_dir),
        "items": len(manifest.get("items", [])),
    }


def task_markdown(manifest: dict[str, Any], article_dir: Path) -> str:
    lines = [
        "# Codex Article Task",
        "",
        "You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.",
        "",
        "## User Spec",
        "",
        manifest["spec"]["raw"],
        "",
        "## Output Directory",
        "",
        f"`{article_dir}`",
        "",
        "## Required Workflow",
        "",
        "1. Run `python -m article_factory graph bootstrap`; require PASS and 100% node/edge coverage.",
        "2. Read `memory/graph/SESSION_BOOTSTRAP.md` and every required file it lists, including `SEO_ARTICLE_RULES.md` and the full visual prompt guide.",
        "3. Read `knowledge/agent_memory/products/product-map.md`.",
        "4. For each item below, read the `prompt` and `evidence` files.",
        "5. Write a complete article to the target output path.",
        "6. Use only facts supported by the evidence pack or mark uncertainty explicitly.",
        "7. Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body. Use those inputs silently and write from an expert editorial voice.",
        "8. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.",
        "9. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.",
        "10. Do not use markdown tables. Use lists, numbered lists, and comparison lists.",
        "11. Match the imported Medium style: direct, practical, conversational, lightly slangy, gamer-aware, no water, no bureaucratic wording, no academic filler.",
        "12. Number generated assets across the run and alternate style branches: odd = B warm narrative, even = A tactile industrial; real screenshots do not consume an index.",
        "13. Build every generated-image prompt with `article-editorial-poster-v1`, target Nano Banana Pro by default, and use the exact mapped color (Cluster #635FD5; Melonity #FF1469) with the correct branch role: small 3–8% accent in A, dominant 35–70% field replacing yellow/amber in B. Require a QA score of at least 80/100. Every B asset must actually attach two persistent warm-story reference files with explicit composition and render/palette/typography roles and pass 4/5 reference fidelity.",
        "14. After writing all articles, run `python -m article_factory review output\\runs\\" + manifest["created_at"] + ".json`.",
        "15. Fix every `fail` or `needs_review` finding before considering the task done.",
        "",
        "## Articles",
        "",
    ]
    for index, item in enumerate(manifest["items"], start=1):
        target = article_dir / f"{index:02d}-{slugify(item['title'])}.md"
        lines.extend(
            [
                f"### {index}. {item['title']}",
                "",
                f"- Game: `{item['game']}`",
                f"- Language: `{item['language']}`",
                f"- Prompt: `{item['prompt']}`",
                f"- Evidence: `{item['evidence']}`",
                f"- Target: `{target}`",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def index_markdown(manifest: dict[str, Any], article_dir: Path) -> str:
    lines = ["# Article Index", ""]
    for index, item in enumerate(manifest["items"], start=1):
        target = article_dir / f"{index:02d}-{slugify(item['title'])}.md"
        lines.append(f"{index}. [{item['title']}]({target})")
    return "\n".join(lines) + "\n"
