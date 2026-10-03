"""Add a small, game-relevant SEO link block to the prepared articles.

The links are distributed across Dota 2 and CS2 material so each target has
natural surrounding context instead of repeating four identical links in every
post.  Existing images and source links are not changed.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH = ROOT / "output" / "publish" / "20260926-platforms-12x9"
MARKER = "seo-product-links-20260927"


def links_for(path: Path) -> list[tuple[str, str]]:
    name = path.name.lower()
    if "03-cs2-context-first-research" in name:
        return [
            ("скинченджер для КС2", "https://metaskins.gg/"),
            ("skinchanger cs2 & dota 2", "https://melonity.gg/en"),
        ]
    if not name[:2].isdigit():
        # GitBook/Pages source docs are selected by their directory.
        p = str(path).lower().replace("\\", "/")
        if "/cs2" in p or p.endswith("/cs2.md"):
            return [
                ("скинченджер для КС2", "https://metaskins.gg/"),
                ("skinchanger cs2 & dota 2", "https://melonity.gg/en"),
            ]
        if "/dota-2" in p:
            n = sum(path.stem.encode("utf-8")) % 3
            choices = [
                [("читы Dota 2", "https://melonity.gg/"), ("скинченджер для Dota 2", "https://metaskins.gg/")],
                [("dota 2 cheats", "https://melonity.gg/en"), ("скинченджер для КС2", "https://metaskins.gg/")],
                [("skinchanger cs2 & dota 2", "https://melonity.gg/en"), ("скинченджер для Dota 2", "https://metaskins.gg/")],
            ]
            return choices[n]
        return []
    index = int(name.split("-", 1)[0])
    if index < 7 or index > 11:
        return []
    options = {
        7: [("читы Dota 2", "https://melonity.gg/"), ("скинченджер для Dota 2", "https://metaskins.gg/")],
        8: [("dota 2 cheats", "https://melonity.gg/en"), ("скинченджер для КС2", "https://metaskins.gg/")],
        9: [("skinchanger cs2 & dota 2", "https://melonity.gg/en"), ("скинченджер для Dota 2", "https://metaskins.gg/")],
        10: [("читы Dota 2", "https://melonity.gg/"), ("dota 2 cheats", "https://melonity.gg/en")],
        11: [("skinchanger cs2 & dota 2", "https://melonity.gg/en"), ("скинченджер для КС2", "https://metaskins.gg/")],
    }
    return options[index]


def block(path: Path, links: list[tuple[str, str]]) -> str:
    if path.suffix.lower() == ".md":
        items = " и ".join(f"[{label}]({url})" for label, url in links)
        return f"\n\n<!-- {MARKER} -->\n## Related game searches\nFor related game and cosmetic research, see {items}."
    items = " и ".join(f'<a href="{url}" target="_blank" rel="noopener">{label}</a>' for label, url in links)
    return f'\n  <!-- {MARKER} -->\n  <h2>Related game searches</h2>\n  <p>For related game and cosmetic research, see {items}.</p>'


def add(path: Path, links: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    if not links or MARKER in text:
        return False
    extra = block(path, links)
    if path.suffix.lower() == ".html" and "</article>" in text:
        text = text.replace("</article>", extra + "\n</article>", 1)
    else:
        text += extra
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for folder in PUBLISH.iterdir():
        if not folder.is_dir() or folder.name == "notion":
            continue
        for path in folder.rglob("*"):
            if path.suffix.lower() not in {".md", ".html"}:
                continue
            if add(path, links_for(path)):
                changed.append(str(path.relative_to(PUBLISH)))
    print(f"added link blocks: {len(changed)}")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()
