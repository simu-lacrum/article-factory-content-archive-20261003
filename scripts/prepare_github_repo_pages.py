from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(r"C:\Users\User\Desktop\articles")
PACKAGE = ROOT / "output" / "publish" / "20260910-t2-27"
REPO = PACKAGE / "github-repo-prep"
MANIFEST = json.loads((PACKAGE / "manifest.json").read_text(encoding="utf-8"))


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


pages = REPO / "guides"
pages.mkdir(parents=True, exist_ok=True)

for item in MANIFEST["platforms"]["github"]:
    slug = item["slug"]
    body = Path(item["markdown"]).read_text(encoding="utf-8").strip() + "\n"
    image_match = re.search(r"!\[([^\]]*)\]\((https?://[^)]+)\)", body)
    image_alt = image_match.group(1) if image_match else ""
    image_url = image_match.group(2) if image_match else ""
    front_matter = "\n".join(
        [
            "---",
            f"title: {yaml_string(item['title'])}",
            f"seo_title: {yaml_string(item['title'])}",
            f"description: {yaml_string(item['description'])}",
            f"permalink: {yaml_string('/guides/' + slug + '/')}",
            f"language: {yaml_string(item['language'])}",
            f"image: {yaml_string(image_url)}",
            f"image_alt: {yaml_string(image_alt)}",
            "layout: default",
            "---",
            "",
        ]
    )
    (pages / f"{slug}.md").write_text(front_matter + body, encoding="utf-8")

print(f"Prepared {len(MANIFEST['platforms']['github'])} GitHub Pages articles in {pages}")
