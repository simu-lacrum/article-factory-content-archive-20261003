from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "output" / "publish" / "20260913-network-7x10"


def main() -> None:
    bundles = json.loads((BASE / "bundles.json").read_text(encoding="utf-8"))
    publications = json.loads((BASE / "publications.json").read_text(encoding="utf-8"))
    verification = json.loads((BASE / "verification.json").read_text(encoding="utf-8"))
    lines = [
        "# Network Publication Results",
        "",
        "## Summary",
        "",
        "- Prepared articles: 84 (70 original targets + 14 Dota 2 add-ons).",
        f"- Public URLs verified: {verification['pass']}/{verification['total']}.",
        "- Pages10 submissions under platform review: 12.",
        "- Public-link checks: target URL, expected anchor, dofollow relation, source image URL, and image alt text.",
        "- Meta descriptions were entered only where the platform exposed a field; these hosted editors did not expose one on the verified public posts.",
        "- Article Factory review: 70/70 PASS for run 20260913-085721 and 14/14 PASS for run 20260913-101654.",
        "",
        "## Anchor Strategy",
        "",
        "- Cluster CS2 and Deadlock links include cheats/hacks variants, branded/contextual phrasing, and two naked URLs on PointBlog.",
        "- Both Dota 2 targets use rotated anchors across the seven networks, including `dota 2 cheats`, `dota 2 hacks`, `top dota 2 cheats`, and related natural variants.",
        "",
    ]

    for host, posts in publications.items():
        by_title = {item["title"]: item for item in bundles[host]}
        lines.extend([f"## {host} — public", ""])
        for post in posts:
            item = by_title[post["title"]]
            lines.append(
                f"- [{post['title']}]({post['url']}) — anchor `{item['anchor']}` → {item['target_url']}"
            )
        lines.append("")

    lines.extend(["## pages10.com — under review", ""])
    for item in bundles["pages10.com"]:
        lines.append(
            f"- {item['title']} — anchor `{item['anchor']}` → {item['target_url']} — `Article Under Review`"
        )
    lines.extend(
        [
            "",
            "Pages10 has accepted all twelve submissions but does not expose them in the public post list until moderation is complete.",
            "",
        ]
    )
    (BASE / "PUBLICATION_RESULTS.md").write_text("\n".join(lines), encoding="utf-8")
    print(BASE / "PUBLICATION_RESULTS.md")


if __name__ == "__main__":
    main()
