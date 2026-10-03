from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "output" / "publish" / "20260913-network-7x10"
PUBLICATIONS = BASE / "publications.json"
BUNDLES = BASE / "bundles.json"
PUBLISHED_CSV = ROOT / "published" / "articles.csv"


def main() -> None:
    publications = json.loads(PUBLICATIONS.read_text(encoding="utf-8"))
    bundles = json.loads(BUNDLES.read_text(encoding="utf-8"))
    existing: set[str] = set()
    if PUBLISHED_CSV.exists():
        with PUBLISHED_CSV.open(encoding="utf-8-sig", newline="") as handle:
            existing = {row.get("url", "").rstrip("/") for row in csv.DictReader(handle)}

    added = 0
    skipped = 0
    for host, posts in publications.items():
        by_title = {item["title"]: item for item in bundles[host]}
        for post in posts:
            url = post["url"].rstrip("/")
            if url in existing:
                skipped += 1
                continue
            target = by_title[post["title"]]["target_url"].lower()
            game = "dota2" if "dota-2" in target or "melonity.gg/en" in target else "deadlock" if "deadlock" in target else "cs2"
            slug = urlparse(url).path.rstrip("/").split("/")[-1]
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "article_factory",
                    "published",
                    "add",
                    "--title",
                    post["title"],
                    "--slug",
                    slug,
                    "--game",
                    game,
                    "--language",
                    "en",
                    "--url",
                    post["url"],
                ],
                cwd=ROOT,
                check=True,
                stdout=subprocess.DEVNULL,
            )
            existing.add(url)
            added += 1
    print(json.dumps({"added": added, "skipped": skipped, "total_public": added + skipped}, indent=2))


if __name__ == "__main__":
    main()
