"""Inspect known public candidate pages, retaining only backlink observations.

This is a selected sample, not a full backlink index or provider export.
"""
import csv
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.pages import fetch_page, anchor_kind
from article_factory.research.models import canonical_url, identity
from article_factory.research.service import read_json, save_json

directory = Path(sys.argv[1])
candidates = read_json(directory / "backlink-public-candidates.json")
brands = ["Umbrella", "uc.zone", "umbrella-dota.com", "Octarine", "octarine.cc", "Avalanche", "avalan.cc", "Tsuki", "tsuki.gg"]

def inspect(candidate):
    checked_at = datetime.now(timezone.utc).isoformat()
    result = {**candidate, "checked_at": checked_at, "method": "ordinary_http_html_parse_no_js"}
    try:
        page, _ = fetch_page(candidate["source_url"])
        result.update(http_status=page["http_status"], final_url=page["url"], html_sha256=page["sha256"])
        links = {}
        for link in page["links"]:
            target = canonical_url(link["url"])
            if urlsplit(target).netloc not in candidate["target_hosts"]:
                continue
            token = identity(target, link["text"])
            if token not in links:
                query = "dota 2 cheats" if candidate["games"] == ["dota2"] else "deadlock cheats" if candidate["games"] == ["deadlock"] else ""
                links[token] = {"source_url": candidate["source_url"], "target_url": target, "observed_href": link["url"],
                               "anchor": link["text"], "anchor_kind": anchor_kind(link["text"], target, query, brands),
                               "target_keyword": query, "games": candidate["games"], "source_context": candidate["source_context"],
                               "placement": link["placement"], "rel": link["rel"], "checked_at": checked_at,
                               "verification_status": "target_and_anchor_found", "occurrences": 0,
                               "evidence_type": "verified_public_page_sample_not_provider_index"}
            links[token]["occurrences"] += 1
        result.update(links=list(links.values()), status="links_confirmed" if links else "not_found_in_fetched_html")
    except Exception as exc:
        result.update(status="unavailable", http_status=exc.code if isinstance(exc, HTTPError) else None, error=f"{type(exc).__name__}: {exc}", links=[])
    return result

with ThreadPoolExecutor(max_workers=3) as pool:
    observations = list(pool.map(inspect, candidates))
rows = [link for observation in observations for link in observation["links"]]
save_json(directory / "public-backlink-observations.json", observations)
save_json(directory / "public-backlink-sample.json", rows)
fields = ["source_url", "target_url", "observed_href", "anchor", "anchor_kind", "target_keyword", "games", "source_context", "placement", "rel", "checked_at", "verification_status", "occurrences", "evidence_type"]
with (directory / "public-backlink-sample.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    from article_factory.research.service import safe_cell
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows({k: safe_cell(" | ".join(v) if isinstance(v, list) else v) for k, v in row.items()} for row in rows)
summary = {"scope": "Manually selected public source pages; not a full profile, representative distribution or acquisition plan",
           "checked_at": datetime.now(timezone.utc).isoformat(), "candidate_pages": len(observations),
           "page_status_counts": dict(Counter(o["status"] for o in observations)), "confirmed_unique_link_rows": len(rows),
           "confirmed_source_hosts": sorted({urlsplit(r["source_url"]).netloc for r in rows}),
           "targets": {host: {"links": sum(urlsplit(r["target_url"]).netloc == host for r in rows),
                              "anchor_counts": dict(Counter(r["anchor_kind"] for r in rows if urlsplit(r["target_url"]).netloc == host))}
                       for host in sorted({urlsplit(r["target_url"]).netloc for r in rows})},
           "health_score": None, "full_referring_domain_counts": None,
           "limitations": ["Search-selected sources are selection-biased.", "No link found in static HTML does not prove historical removal or absence in JavaScript output.", "403 pages and hidden-link placeholders are not confirmed incoming links.", "A user complaint on a vendor-hosted issue tracker is not a statement or endorsement by that vendor.", "Automated reputation reports do not establish product quality or the value of a backlink.", "Exact counts classify this sample only; no optimal anchor percentages are inferred."]}
save_json(directory / "public-backlink-summary.json", summary)
print(summary)
