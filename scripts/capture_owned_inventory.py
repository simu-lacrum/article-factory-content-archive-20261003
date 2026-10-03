"""Read public site coverage to prevent recommending duplicate articles."""
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.pages import fetch_page
from article_factory.research.service import save_json
from article_factory.research.models import identity

directory = Path(sys.argv[1])
seeds = ["https://cheatsgaming.com/latest", "https://deadlockhacks.com/", "https://counterskrikecheats.com/", "https://cluster.center/en/cs2", "https://cluster.center/en/deadlock", "https://melonity.gg/en"]
queue, seen, pages = seeds[:], set(), []
while queue and len(seen) < 14:
    url = queue.pop(0)
    if url in seen:
        continue
    seen.add(url)
    try:
        page, html = fetch_page(url)
        page["role"] = "owned_site"
        save_json(directory / "owned-pages" / (identity(url) + ".json"), page)
        pages.append(page)
        if "cheatsgaming.com/latest" in url:
            queue.extend(link["url"] for link in page["links"] if link["text"].strip().lower() == "next" and "cheatsgaming.com/latest" in link["url"])
        print(json.dumps({"url": url, "words": page["words"]}), flush=True)
    except Exception as exc:
        save_json(directory / "owned-pages" / (identity(url) + ".json"), {"url": url, "error": str(exc), "role": "owned_site"})
        print(json.dumps({"url": url, "error": str(exc)}), flush=True)
inventory = {}
for page in pages:
    for link in page["links"]:
        if link["relationship"] == "internal" and len(link["text"]) > 20 and link["placement"] == "editorial":
            inventory.setdefault(link["url"], link["text"])
save_json(directory / "owned-inventory.json", {"captured_at": "2026-09-21", "links": [{"url": url, "title": title} for url, title in inventory.items()]})
