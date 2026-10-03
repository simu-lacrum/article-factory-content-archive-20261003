from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "output" / "publish" / "20260910-melonity-product-t2-6"
REPO = ROOT / "output" / "publish" / "20260910-t2-27" / "github-repo-prep"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


manifest = json.loads((PACKAGE / "manifest.json").read_text(encoding="utf-8"))
item = manifest["platforms"]["github"]
body = Path(item["markdown"]).read_text(encoding="utf-8").strip() + "\n"
image_match = re.search(r"!\[([^\]]*)\]\((https?://[^)]+)\)", body)
image_alt = image_match.group(1) if image_match else ""
image_url = image_match.group(2) if image_match else ""
front_matter = "\n".join(
    [
        "---",
        f"title: {yaml_string(item['title'])}",
        f"seo_title: {yaml_string(item['seo_title'])}",
        f"description: {yaml_string(item['description'])}",
        f"permalink: {yaml_string('/guides/' + item['slug'] + '/')}",
        f"language: {yaml_string(item['language'])}",
        f"image: {yaml_string(image_url)}",
        f"image_alt: {yaml_string(image_alt)}",
        "layout: default",
        "---",
        "",
    ]
)
destination = REPO / "guides" / f"{item['slug']}.md"
destination.write_text(front_matter + body, encoding="utf-8")
print(destination)
