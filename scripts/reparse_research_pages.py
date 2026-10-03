"""Re-extract saved HTML without another network request."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.pages import extract_page
from article_factory.research.service import save_json

directory = Path(sys.argv[1])
study = json.loads((directory / "study.json").read_text(encoding="utf-8"))
targets = {u: c["primary_query"] for c in study["clusters"] for u in c.get("competitor_urls", [])}
for path in (directory / "pages").glob("*.json"):
    old = json.loads(path.read_text(encoding="utf-8"))
    if not old.get("raw_file"):
        continue
    html = (directory / old["raw_file"]).read_text(encoding="utf-8")
    requested = old.get("requested_url", old["url"])
    rule = study.get("extraction_rules", {}).get(requested, study.get("extraction_rules", {}).get(old["url"]))
    new = extract_page(html, old["url"], targets.get(requested, ""), study.get("brands", []), rule)
    new.update({k: old[k] for k in ("requested_url", "http_status", "raw_file", "captured_at") if k in old})
    save_json(path, new)
print("Saved pages re-extracted")
