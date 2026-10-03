from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

from build_publication_packages import markdown_to_html, parse_article


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "20260911-112757"
SOURCE_DIR = ROOT / "output" / "articles" / RUN_ID
OUTPUT = ROOT / "output" / "publish" / "20260911-metaskins-t2-6"
PLATFORMS = ["substack", "notion", "gitbook", "github", "justpasteme", "rentry"]


def main() -> None:
    sources = sorted(SOURCE_DIR.glob("*.md"))
    if len(sources) != len(PLATFORMS):
        raise SystemExit(f"Expected {len(PLATFORMS)} articles, found {len(sources)}")

    manifest: dict[str, object] = {
        "created_at": "2026-09-11",
        "run_id": RUN_ID,
        "total": len(sources),
        "targets": ["https://metaskins.gg/", "https://metaskins.gg/en"],
        "platforms": {},
    }

    for platform, source in zip(PLATFORMS, sources, strict=True):
        metadata, markdown = parse_article(source)
        markdown = re.sub(
            r"\n## Internal-link suggestions\s*\n.*\Z", "\n", markdown, flags=re.S
        ).strip() + "\n"
        markdown = re.sub(
            r"^> (?:Image placement|Размещение изображения):.*\n\n?",
            "",
            markdown,
            flags=re.M,
        )
        slug = metadata["slug"]
        platform_dir = OUTPUT / platform
        platform_dir.mkdir(parents=True, exist_ok=True)
        markdown_path = platform_dir / f"{slug}.md"
        html_path = platform_dir / f"{slug}.html"
        markdown_path.write_text(markdown, encoding="utf-8")
        html_fragment = markdown_to_html(markdown)
        if platform in {"substack", "notion", "gitbook", "justpasteme"}:
            html_fragment = re.sub(r"\A<h1>.*?</h1>\s*", "", html_fragment, count=1, flags=re.S)
        html_path.write_text(
            '<!doctype html><html><head><meta charset="utf-8"></head><body>'
            + html_fragment
            + "</body></html>\n",
            encoding="utf-8",
        )
        if platform == "rentry":
            (platform_dir / f"{slug}-source.html").write_text(
                '<!doctype html><html><head><meta charset="utf-8"></head>'
                '<body><pre style="white-space:pre-wrap">'
                + escape(markdown)
                + "</pre></body></html>\n",
                encoding="utf-8",
            )
        manifest["platforms"][platform] = {
            "source": str(source),
            "markdown": str(markdown_path),
            "html": str(html_path),
            "title": metadata["title"],
            "seo_title": metadata.get("seo_title", metadata["title"]),
            "description": metadata["description"],
            "slug": slug,
            "language": metadata["language"],
            "game": metadata["game"],
            "target_url": metadata["target_url"],
            "target_anchor": metadata["target_anchor"],
            "status": "ready",
        }

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"output": str(OUTPUT), "total": len(sources)}, indent=2))


if __name__ == "__main__":
    main()
