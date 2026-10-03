"""Import the retained, manually observed public Semrush sample without guessing missing data."""
import csv
import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import key
from article_factory.research.service import read_json, save_json, import_metrics

directory = Path(sys.argv[1])
raw = read_json(directory / "raw" / "semrush-public-observations.json")
study = read_json(directory / "study.json")
clusters = {c["id"]: c for c in study["clusters"]}
rows, excluded = [], []
for capture in raw["captures"]:
    existing = next(k for k in study["keywords"] if k["query"] == capture["query"])
    entries = [(capture["query"], capture["volume"], capture["difficulty"], existing["cluster_id"], "primary_lookup")]
    entries += [(*entry, "related_keyword_in_selected_database") for entry in capture["related"]]
    for query, volume, difficulty, cid, origin in entries:
        if cid.startswith("exclude_"):
            excluded.append({"query": query, "volume": volume, "country": "US", "reason": cid,
                             "source_url": capture["source_url"], "captured_at": capture["captured_at"]})
            continue
        c = clusters[cid]
        item = next((k for k in study["keywords"] if key(k["query"]) == key(query) and k["game"] == c["game"]), None)
        if item is None:
            item = {"query": query, "game": c["game"], "language": "en", "cluster_id": cid,
                    "intent": "navigational_commercial" if query == "midnight cs2 cheat" else c.get("intent", "mixed"),
                    "scope": "legitimate_commands" if cid.endswith("-commands") else c.get("scope", "third_party_software"), "sources": []}
            study["keywords"].append(item)
        item.update(discovery="observed", discovery_note="Visible Semrush keyword output; estimated demand, not an independent Google exact count")
        item["sources"] = sorted(set(item.get("sources", []) + [capture["source_url"]]))
        row = {"query": query, "game": c["game"], "language": "en", "country": "US", "engine": "google",
               "provider": raw["provider"], "period": raw["period"], "period_basis": raw["period_basis"],
               "match_type": raw["match_type"], "volume": volume, "volume_basis": raw["volume_basis"],
               "measurement_window_end": "", "source_url": capture["source_url"], "captured_at": capture["captured_at"],
               "provider_difficulty": difficulty, "observation_kind": origin,
               "precision": "rounded_display" if volume >= 1000 else "provider_display"}
        rows.append(row)
        if origin == "primary_lookup" and "gb_volume" in capture:
            rows.append({**row, "country": "GB", "volume": capture["gb_volume"], "provider_difficulty": None,
                         "observation_kind": "country_breakdown_in_us_lookup", "precision": "rounded_display" if capture["gb_volume"] >= 1000 else "provider_display"})
    if not capture["results"]:
        continue
    results = []
    for rank, url in enumerate(capture["results"], 1):
        kind, page_type = "organic", "unclassified"
        if "youtube.com" in url:
            kind, page_type = "video", "video"
        elif "github.com" in url:
            kind, page_type = "code_reference", "repository"
        elif any(t in url for t in ("/forum", "reddit.com", "steamcommunity.com")):
            kind, page_type = "forum", "discussion"
        elif "medium.com" in url:
            kind, page_type = "article", "comparison"
        elif any(t in url.lower() for t in ("console_commands", "console-commands", "wiki/cheats", "gamefaqs", "liveabout")):
            kind, page_type = "article", "command_reference"
        elif any(t in url for t in ("anyx.gg", "undetek.com", "melonity.gg", "exloader.net")):
            kind, page_type = "product", "commercial_page"
        results.append({"url": url, "rank": rank, "rank_basis": "provider_reported_undated", "type": kind, "page_type": page_type})
    snapshot = {"query": capture["query"], "game": capture["game"], "language": "en", "engine": "google",
                "country_requested": "US", "country_observed": "US", "country_basis": "provider_selected_database_not_browser_geolocation",
                "method": "semrush_public_provider_snapshot", "session_cohort": "semrush-free-20260921",
                "captured_at": capture["captured_at"], "serp_collection_date": None, "grouping_eligible": False,
                "grouping_note": "The provider did not expose the SERP collection date; do not validate contemporaneous overlap",
                "source_file": "raw/semrush-public-observations.json", "results": results}
    study["serps"] = [s for s in study["serps"] if not (s["query"] == snapshot["query"] and s["method"] == snapshot["method"])] + [snapshot]

study["metric_policy"] = {k: raw[k] for k in ("provider", "period", "period_basis", "match_type")}
study["limitations"] = [note for note in study["limitations"] if not note.startswith("Volumes, CPC")]
note = "Public Semrush metrics cover only a small subset, captured September 21, 2026. They are modeled rolling monthly averages; the reporting month and close-variant semantics were not exposed. Remaining volume is unknown."
if note not in study["limitations"]:
    study["limitations"].append(note)
for c in study["clusters"]:
    measured = [r for r in rows if r["country"] == "US" and any(k["query"] == r["query"] and k["cluster_id"] == c["id"] for k in study["keywords"])]
    if measured:
        c["research_state"] = "partial_provider_metrics_serp_grouping_still_unvalidated"
        c["measured_query_count"] = len(measured)
save_json(directory / "study.json", study)
save_json(directory / "excluded-provider-suggestions.json", excluded)
path = directory / "semrush-public-metrics.csv"
with path.open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(import_metrics(directory, path))
with (directory / "uk-observed-metrics.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(r for r in rows if r["country"] == "GB")
