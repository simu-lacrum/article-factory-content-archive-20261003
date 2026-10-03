from __future__ import annotations

import json
import re
from pathlib import Path

from build_publication_packages import markdown_to_html, parse_article


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "20260910-172115"
SOURCE_DIR = ROOT / "output" / "articles" / RUN_ID
OUTPUT = ROOT / "output" / "publish" / "20260910-melonity-product-t2-6"
PLATFORMS = ["substack", "notion", "gitbook", "github", "justpasteme", "rentry"]


def main() -> None:
    sources = sorted(SOURCE_DIR.glob("*.md"))
    if len(sources) != len(PLATFORMS):
        raise SystemExit(f"Expected {len(PLATFORMS)} articles, found {len(sources)}")

    manifest: dict[str, object] = {
        "created_at": "2026-09-10",
        "run_id": RUN_ID,
        "total": len(sources),
        "target_url": "https://cheatsgaming.com/shop/dota-2/melonity-dota2-cheat",
        "platforms": {},
    }

    for platform, source in zip(PLATFORMS, sources, strict=True):
        metadata, markdown = parse_article(source)
        markdown = re.sub(
            r"\n## Internal-link suggestions\s*\n.*\Z", "\n", markdown, flags=re.S
        ).strip() + "\n"
        slug = metadata["slug"]
        platform_dir = OUTPUT / platform
        platform_dir.mkdir(parents=True, exist_ok=True)
        markdown_path = platform_dir / f"{slug}.md"
        html_path = platform_dir / f"{slug}.html"
        markdown_path.write_text(markdown, encoding="utf-8")
        html_path.write_text(markdown_to_html(markdown), encoding="utf-8")
        manifest["platforms"][platform] = {
            "source": str(source),
            "markdown": str(markdown_path),
            "html": str(html_path),
            "title": metadata["title"],
            "seo_title": metadata["seo_title"],
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
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "total": len(sources),
                "platforms": PLATFORMS,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
