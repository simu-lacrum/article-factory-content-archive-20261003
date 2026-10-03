"""Add the retained first-page Keyword Magic sample with explicit source preference."""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import key
from article_factory.research.service import read_json, save_json, import_metrics

directory = Path(sys.argv[1])
raw = read_json(directory / "raw" / "semrush-keyword-magic.json")
study = read_json(directory / "study.json")
clusters = {c["id"]: c for c in study["clusters"]}
rows = []
excluded = read_json(directory / "excluded-provider-suggestions.json")
for capture in raw["captures"]:
    for query, provider_intent, display, difficulty, cid in capture["rows"]:
        volume = int(float(display[:-1]) * 1000) if display.endswith("K") else int(display)
        row = {"query": query, "game": capture["game"], "language": "en", "country": raw["country"], "engine": "google",
               **{k: raw[k] for k in ("provider", "period", "period_basis", "match_type", "volume_basis", "captured_at", "source_url")},
               "volume": volume, "provider_volume_display": display, "precision": "rounded_display" if display.endswith("K") else "provider_display",
               "provider_difficulty": difficulty, "provider_intent": provider_intent, "seed": capture["seed"],
               "measurement_window_end": "", "observation_kind": "public_keyword_magic_suggestion"}
        if cid.startswith("exclude_"):
            excluded.append({**row, "reason": cid})
            continue
        c = clusters[cid]
        item = next((k for k in study["keywords"] if key(k["query"]) == key(query) and k["game"] == capture["game"]), None)
        if item is None:
            scope = "legitimate_commands" if cid.endswith("-commands") else c.get("scope", "third_party_software")
            if any(t in query for t in (" bot", " gold", " money")):
                scope = "ambiguous_command_or_software"
            item = {"query": query, "game": capture["game"], "language": "en", "cluster_id": cid,
                    "scope": scope, "intent": c.get("intent", "mixed"), "sources": []}
            study["keywords"].append(item)
        item.update(discovery="observed", discovery_note="Visible US Keyword Magic suggestion; reader intent still needs its own SERP validation")
        item["sources"] = sorted(set(item.get("sources", []) + [raw["source_url"]]))
        if any(brand in query for brand in ("midnight", "fatality", "pellix", "orbit")):
            item.update(intent="navigational_commercial", article_target_policy="comparison_research_only_until_brand_serp_validated")
        if "anti cheat" in query or "frog cheater" in query or "cheating problem" in query:
            item.update(intent="informational_game_policy_or_news", article_target_policy="separate_official_source_and_currentness_check_before_article")
        if item["scope"] == "ambiguous_command_or_software":
            item["article_target_policy"] = "validate_intent_first_do_not_assume_third_party_software"
        rows.append(row)
study["metric_policy"]["provider_order"] = ["semrush_public_keyword_checker", "semrush_public_keyword_magic"]
save_json(directory / "study.json", study)
dedup = {(r["query"], r.get("provider", "semrush_public_keyword_checker")): r for r in excluded}
save_json(directory / "excluded-provider-suggestions.json", list(dedup.values()))
path = directory / "semrush-keyword-magic-metrics.csv"
with path.open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(import_metrics(directory, path))
