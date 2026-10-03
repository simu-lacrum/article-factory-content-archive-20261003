from __future__ import annotations

import html
import json
import re
from pathlib import Path

from build_publication_packages import markdown_to_html

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "output" / "articles" / "20261002-backlink-12"
OUT_DIR = ROOT / "output" / "publish" / "20261002-backlink-12"

ALLOCATIONS = {
    "dzen": ["01-skinchanger-ks2-kak-proverit-katalog-i-vidimost.md", "09-chity-dota-2-kak-chitat-katalog-i-funkcii.md"],
    "tumblr": ["02-skinchanger-dota-2-cs2-cosmetic-checklist.md", "03-chity-ks2-kak-proverit-privatnyy-produkt.md"],
    "blogger": ["04-chity-dedlok-kak-sravnit-podderzhku-i-funkcii.md", "05-chity-dlya-igr-kak-chitat-katalog.md"],
    "gitbook": ["06-cheats-for-cs2-private-product-page-checklist.md", "12-chity-na-dedlok-kak-proverit-stranicu.md"],
    "github-pages": ["07-deadlock-cheats-hacks-private-page-evidence.md", "08-cheats-for-games-cross-game-research-checklist.md"],
    "substack": ["11-cheats-deadlock-high-level-product-checklist.md"],
    "telegraph": ["10-dota-2-cheats-private-page-evidence-checklist.md"],
}


def frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", markdown, flags=re.S)
    if not match:
        return {}, markdown
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            data[m.group(1)] = m.group(2).strip().strip('"')
    return data, markdown[match.end():]


def images(body: str) -> list[dict[str, str]]:
    slots = []
    for block in re.findall(r"<!--\s*IMAGE_SLOT_\d+([\s\S]*?)-->", body):
        src = re.search(r"Source image:\s*(https?://\S+)", block)
        alt = re.search(r"Alt text:\s*(.+)", block)
        caption = re.search(r"Caption:\s*(.+)", block)
        if src:
            slots.append({"src": src.group(1), "alt": (alt.group(1).strip() if alt else "Article image"), "caption": (caption.group(1).strip() if caption else "")})
    return slots


def slug(title: str) -> str:
    text = title.lower().replace("—", " ").replace("–", " ")
    text = re.sub(r"[^a-z0-9а-яё]+", "-", text, flags=re.I).strip("-")
    return text[:90]


def html_with_images(body: str, pics: list[dict[str, str]]) -> str:
    clean = re.sub(r"<!--\s*IMAGE_SLOT_\d+[\s\S]*?-->", "", body).strip()
    rendered = markdown_to_html(clean)
    figures = "".join(
        f'<figure><img src="{html.escape(p["src"], quote=True)}" alt="{html.escape(p["alt"], quote=True)}" loading="lazy"><figcaption>{html.escape(p["caption"])}</figcaption></figure>'
        for p in pics
    )
    marker = re.search(r"</h1>\s*", rendered)
    if marker:
        return rendered[:marker.end()] + figures + rendered[marker.end():]
    return figures + rendered


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {"created_at": "20261002", "source_run": "20261002-backlink-12", "platforms": {}}
    for platform, names in ALLOCATIONS.items():
        pdir = OUT_DIR / platform
        pdir.mkdir(parents=True, exist_ok=True)
        records = []
        for index, name in enumerate(names, 1):
            source = ARTICLE_DIR / name
            raw = source.read_text(encoding="utf-8")
            meta, body = frontmatter(raw)
            pics = images(body)
            stem = slug(meta.get("title", source.stem))
            md_name = f"{index:02d}-{stem}.md"
            html_name = f"{index:02d}-{stem}.html"
            # Keep front matter out of platform body, but retain the original source markdown for review.
            clean_body = re.sub(r"<!--\s*IMAGE_SLOT_\d+[\s\S]*?-->", "", body).strip() + "\n"
            (pdir / md_name).write_text(clean_body, encoding="utf-8")
            (pdir / html_name).write_text(html_with_images(body, pics), encoding="utf-8")
            records.append({
                "source": str(source),
                "markdown": str(pdir / md_name),
                "html": str(pdir / html_name),
                "title": meta.get("title", source.stem),
                "description": meta.get("description", ""),
                "slug": stem,
                "language": meta.get("language", ""),
                "game": meta.get("game", ""),
                "target_url": meta.get("target_url", ""),
                "target_anchors": meta.get("target_anchors", ""),
                "images": pics,
                "status": "ready",
            })
        manifest["platforms"][platform] = records
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    plan = {
        "max_posts_per_platform": 2,
        "excluded_platforms": ["medium"],
        "allocations": {k: [r["title"] for r in v] for k, v in manifest["platforms"].items()},
        "note": "Dzen and Telegraph are fresh platform choices; other assignments avoid exact target URLs already found in the local publication bundles where possible.",
    }
    (OUT_DIR / "platform_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "README.md").write_text("# Backlink article package — 2026-10-02\n\n12 articles, 7 platforms, no Medium, no more than two posts per platform. Every package includes a real image URL and target anchor metadata.\n", encoding="utf-8")
    print(json.dumps({"output": str(OUT_DIR), "platforms": len(ALLOCATIONS), "articles": sum(len(v) for v in ALLOCATIONS.values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
