"""Check source links in the selected provider sample; keep errors and no-match distinct."""
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import canonical_url, key
from article_factory.research.pages import fetch_page
from article_factory.research.service import read_json, save_json

directory = Path(sys.argv[1])
rows = read_json(directory / "backlinks.json")
urls = sorted({r["source_url"] for r in rows})
target_hosts = {urlsplit(r["target_url"]).netloc for r in rows}

def check(url):
    try:
        page, _ = fetch_page(url)
        return url, {"http_status": page["http_status"], "final_url": page["url"], "checked_at": page["captured_at"],
                     "links": [{"url": canonical_url(l["url"]), "text": l["text"], "rel": l["rel"], "placement": l["placement"]} for l in page["links"] if urlsplit(canonical_url(l["url"])).netloc in target_hosts]}
    except Exception as exc:
        return url, {"http_status": None, "error": str(exc), "links": None}

with ThreadPoolExecutor(max_workers=3) as pool:
    checked = dict(pool.map(check, urls))
save_json(directory / "backlink-source-verification.json", checked)
for row in rows:
    result = checked[row["source_url"]]
    matches = [l for l in (result["links"] or []) if l["url"] == row["target_url"]]
    row["verification"] = {"status": "unavailable" if result["links"] is None else "target_and_anchor_found" if any(key(l["text"]) == key(row["anchor"]) for l in matches) else "target_found_anchor_differs" if matches else "not_found_in_fetched_html",
                           "checked_at": result.get("checked_at"), "method": "ordinary_http_html_parse_no_js"}
save_json(directory / "backlinks.json", rows)
print({s: sum(r["verification"]["status"] == s for r in rows) for s in sorted({r["verification"]["status"] for r in rows})})
