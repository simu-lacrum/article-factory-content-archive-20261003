"""Normalize published article link anchors to game-specific search phrases.

This only changes visible anchor text and the metadata ``anchor`` field. URLs,
images, and explanatory prose remain untouched; the four extra Blogger drafts
are handled separately below because their titles also used the generic
``tool`` wording.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISH = ROOT / "output" / "publish" / "20260926-platforms-12x9"


DEADLOCK = [
    "deadlock cheats",
    "deadlock hacks",
    "deadlock cheat guide",
    "deadlock cheats research",
    "deadlock hacks guide",
    "deadlock cheats checklist",
    "deadlock hacks research",
    "deadlock cheat guide",
    "deadlock cheats",
    "deadlock hacks",
    "deadlock cheats comparison",
    "deadlock hacks review",
]
DOTA = [
    "dota 2 cheats",
    "dota 2 hacks",
    "dota 2 cheat guide",
    "melonity dota 2 cheats",
    "dota 2 cheats research",
    "dota 2 hacks guide",
    "dota 2 cheats checklist",
    "dota 2 hacks research",
    "dota 2 cheats",
    "dota 2 hacks",
    "dota 2 cheats comparison",
    "dota 2 hacks review",
]
CS2 = [
    "cs2 cheats",
    "cs2 hacks",
    "cs2 cheat guide",
    "cs2 cheats research",
    "cs2 hacks guide",
    "cs2 cheats checklist",
    "cs2 hacks research",
    "cs2 cheat guide",
    "cs2 cheats",
    "cs2 hacks",
    "cs2 cheats comparison",
    "cs2 hacks review",
]


def article_number(path: Path) -> int:
    m = re.match(r"(\d+)-", path.name)
    return int(m.group(1)) if m else 1


def target_family(url: str) -> str | None:
    u = url.lower()
    if "cluster.center/en/cs2" in u or "cheatsgaming.com/games/cs2" in u:
        return "cs2"
    if "melonity.gg/en/cs2" in u:
        return "cs2"
    if (
        "cluster.center/en/deadlock" in u
        or "deadlockhacks.com" in u
        or "cheatsgaming.com/games/deadlock" in u
        or "melonity.gg/en/deadlock" in u
    ):
        return "deadlock"
    if (
        "cluster.center/en" in u
        or "cluster.center/ru" in u
        or "dota2cheat.com" in u
        or "melonity.gg" in u
        or "cheatsgaming.com/games/dota-2" in u
    ):
        return "dota"
    return None


def anchor_for(url: str, n: int) -> str | None:
    family = target_family(url)
    if family == "deadlock":
        return DEADLOCK[(max(1, n) - 1) % len(DEADLOCK)]
    if family == "cs2":
        return CS2[(max(1, n) - 1) % len(CS2)]
    if family == "dota":
        return DOTA[(max(1, n) - 1) % len(DOTA)]
    return None


MD_LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
HTML_LINK = re.compile(
    r"(<a\b[^>]*\bhref\s*=\s*[\"'])(https?://[^\"']+)([\"'][^>]*>)(.*?)(</a>)",
    re.IGNORECASE | re.DOTALL,
)


def normalize_text(text: str, n: int) -> tuple[str, int]:
    changed = 0

    def md_repl(match: re.Match[str]) -> str:
        nonlocal changed
        label, url = match.group(1), match.group(2)
        anchor = anchor_for(url, n)
        if not anchor:
            return match.group(0)
        changed += int(label != anchor)
        return f"[{anchor}]({url})"

    text = MD_LINK.sub(md_repl, text)

    def html_repl(match: re.Match[str]) -> str:
        nonlocal changed
        prefix, url, middle, label, suffix = match.groups()
        anchor = anchor_for(html.unescape(url), n)
        if not anchor:
            return match.group(0)
        changed += int(re.sub(r"\s+", " ", html.unescape(label)).strip() != anchor)
        return f"{prefix}{url}{middle}{anchor}{suffix}"

    text = HTML_LINK.sub(html_repl, text)

    # Keep the front-matter field aligned with the visible link.  The source
    # set uses both ``target_url``-then-``anchor`` and ``anchor``-then-
    # ``target_url`` order, so parse the small YAML header as a unit.
    header_match = re.match(r"(?s)^---\n(.*?)\n---", text)
    if header_match:
        header = header_match.group(1)
        target_match = re.search(r'(?m)^\s*target_url:\s*["\']?([^"\'\n]+)', header)
        anchor_match = re.search(r'(?m)^(\s*anchor:\s*["\'])([^"\']+)(["\'])', header)
        if target_match and anchor_match:
            anchor = anchor_for(target_match.group(1).strip(), n)
            if anchor and anchor_match.group(2) != anchor:
                start, end = anchor_match.span(2)
                header = header[:start] + anchor + header[end:]
                text = text[: header_match.start(1)] + header + text[header_match.end(1) :]
                changed += 1
    return text, changed


def update_files() -> dict[str, int]:
    totals: dict[str, int] = {}
    for platform in [
        "substack",
        "notion",
        "gitbook",
        "github-pages",
        "github",
        "github-work",
        "justpasteme",
        "rentry",
        "tumblr",
        "blogger",
        "blogger-cluster-links",
    ]:
        folder = PUBLISH / platform
        if not folder.exists():
            continue
        count = 0
        for path in folder.rglob("*"):
            if path.suffix.lower() not in {".md", ".html"}:
                continue
            old = path.read_text(encoding="utf-8")
            new, changed = normalize_text(old, article_number(path))
            if new != old:
                path.write_text(new, encoding="utf-8")
            count += changed
        totals[platform] = count

    bundles = PUBLISH / "bundles.json"
    data = json.loads(bundles.read_text(encoding="utf-8"))
    count = 0
    for entries in data.values():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            old = entry.get("anchor")
            anchor = anchor_for(entry.get("target_url", ""), int(entry.get("file", "0-").split("-", 1)[0] or 1))
            if anchor and old != anchor:
                entry["anchor"] = anchor
                count += 1
    bundles.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    totals["bundles.json"] = count
    return totals


if __name__ == "__main__":
    print(json.dumps(update_files(), ensure_ascii=False, indent=2))
