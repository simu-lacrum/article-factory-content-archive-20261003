from __future__ import annotations

import json
import re
from pathlib import Path

from build_network_deadlock_dota_20260926 import TARGETS, markdown_to_html

ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "20260926-platforms-12x9"
BASE_DIR = ROOT / "output" / "articles" / "20260926-network-12x7"
OUT_DIR = ROOT / "output" / "publish" / RUN_ID

PLATFORMS = {
    "substack": ("Substack", "search-intent briefing"),
    "notion": ("Notion", "structured research note"),
    "gitbook": ("GitBook", "documentation entry"),
    "github-pages": ("GitHub Pages", "versioned editorial page"),
    "github": ("GitHub", "repository note"),
    "justpasteme": ("JustPasteMe", "plain-language reference"),
    "rentry": ("Rentry", "compact reading note"),
    "tumblr": ("Tumblr", "short-form editorial post"),
    "blogger": ("Blogger", "long-form blog guide"),
}

LENSES = [
    "deadlock cheats", "deadlock hacks", "Deadlock cheat guide", "Dota 2 cheats", "Dota 2 hacks", "Dota 2 cheat research", "source-checked game tools", "feature scope", "risk-aware game research"
]

def rewrite_article(source: str, target: dict, platform: str, display: str, lens: str, index: int) -> tuple[str, dict]:
    base_title = target["titles"][index % len(target["titles"])]
    suffix = {"substack": "Brief", "notion": "Research Note", "gitbook": "Reference", "github-pages": "Field Guide", "github": "Repository Note", "justpasteme": "Explainer", "rentry": "Quick Read", "tumblr": "Editorial Note", "blogger": "Guide"}[platform]
    title = f"{base_title} — {suffix}"
    anchor = LENSES[index % len(LENSES)]
    body = source
    body = re.sub(r'^title: ".*?"$', f'title: "{title}"', body, count=1, flags=re.M)
    body = re.sub(r'^description: ".*?"$', f'description: "{title}. A {lens} note covering scope, evidence, freshness, and practical stop conditions."', body, count=1, flags=re.M)
    body = re.sub(r'^anchor: ".*?"$', f'anchor: "{anchor}"', body, count=1, flags=re.M)
    body = re.sub(r'^source_host: ".*?"$', f'source_host: "{platform}"', body, count=1, flags=re.M)
    body = re.sub(r'^image_placement: .*?$', f'image_placement: "Hero image below the opening; retain source attribution in the platform caption when available."', body, count=1, flags=re.M)
    body = re.sub(r'^# .*?$', f'# {title}', body, count=1, flags=re.M)
    body = re.sub(r'\[[^\]]+\]\(' + re.escape(target["url"]) + r'\)', f'[{anchor}]({target["url"]})', body)
    data = {"platform": platform, "display": display, "index": index + 1, "title": title, "anchor": anchor, "target_url": target["url"], "image": target["image"]}
    return body, data

def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bundles = {}
    source_files = sorted(BASE_DIR.glob("*.md"))[:12]
    if len(source_files) != 12:
        raise SystemExit(f"expected 12 canonical source files, found {len(source_files)}")
    for pi, (platform, (display, lens)) in enumerate(PLATFORMS.items()):
        pdir = OUT_DIR / platform
        pdir.mkdir(parents=True, exist_ok=True)
        records = []
        for ti, (source_path, target) in enumerate(zip(source_files, TARGETS)):
            source = source_path.read_text(encoding="utf-8")
            body, data = rewrite_article(source, target, platform, display, lens, ti + pi)
            filename = f"{ti+1:02d}-{re.sub(r'[^a-z0-9]+','-',data['title'].lower()).strip('-')[:86]}.md"
            (pdir / filename).write_text(body, encoding="utf-8")
            (pdir / filename.replace('.md', '.html')).write_text(markdown_to_html(body), encoding="utf-8")
            records.append(data | {"file": filename})
        bundles[platform] = records
    (OUT_DIR / "bundles.json").write_text(json.dumps(bundles, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "README.md").write_text("# Additional platform package\n\n108 prepared variants: 12 target pages for Substack, Notion, GitBook, GitHub Pages, GitHub, JustPasteMe, Rentry, Tumblr, and Blogger.\n", encoding="utf-8")
    print(json.dumps({"platforms": len(PLATFORMS), "articles": len(PLATFORMS) * 12, "dir": str(OUT_DIR)}, indent=2))

if __name__ == "__main__":
    main()
