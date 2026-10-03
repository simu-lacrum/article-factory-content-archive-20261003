"""Reviewed intent routing and public-page phrase discovery for the September study."""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import identity, key, validate_study
from article_factory.research.pages import phrase_count
from article_factory.research.service import read_json, save_json

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
clusters = {c["id"]: c for c in study["clusters"]}
matched = {
    "deadlock-free-download": ["https://uc.zone/en/deadlock", "https://cheater.fun/deadlock_cheats/", "https://en.exloader.net/tree/games/deadlock/"],
    "cs2-free-download": ["https://anyx.gg/", "https://undetek.com/", "https://cheater.fun/cs2-hacks/"],
    "dota2-free-download": ["https://uc.zone/en/dota2", "https://cheater.fun/cheats_for_dota2_download_hacks_free/"]
}
for ident, urls in matched.items():
    c = clusters[ident]
    c["intent_matched_urls"] = urls
    game = "dota 2" if c["game"] == "dota2" else c["game"]
    c["usage_phrases"] = [f"free {game} cheats", f"{game} cheats", "free download", "free trial", "download"]
    c["corpus_note"] = "Product/access catalog pages from sampled acquisition results. Keyword counts describe publisher copy and cards; they do not verify a free working offer or establish density targets."

for row in study["keywords"]:
    c = clusters[row["cluster_id"]]
    text = key(row["query"])
    article_target = key(c.get("article_target_query", c["primary_query"]))
    if row.get("query_role", "article_candidate") == "article_candidate" and (
        c.get("publication_action") in {"update_hub", "research_landing"}
        or (text != article_target and ("download" in text.split() or ("free" in text.split() and "vs" not in text.split() and "limitations" not in text.split())))
    ):
        row.update(query_role="product_access", recommended_page_type="verified_product_or_category", intent="transactional")
    if c["id"] in {"cs2-triggerbot", "cs2-esp", "deadlock-auto-parry", "dota2-scripts"} and text == key(c["primary_query"]) and text != article_target:
        row.update(query_role="ambiguous_research", recommended_page_type="intent_review")
    if c.get("publication_action") == "include_as_section" and row.get("query_role") == "article_candidate":
        row["recommended_page_type"] = "section_of_" + c["section_parent_id"]

# Finding a phrase in rival copy is independent from asking Google for that phrase.
# Record only exact normalized phrase matches and keep autocomplete/provider evidence intact.
discovery_pages = [
    "https://cheater.fun/deadlock_cheats/", "https://cheater.fun/cs2-hacks/", "https://cheater.fun/cheats_for_dota2_download_hacks_free/",
    "https://octarine.fun/en/deadlock/", "https://en.exloader.net/tree/games/deadlock/",
    "https://en.exloader.net/tree/modifications/sdk2changer/", "https://en.exloader.net/tree/modifications/d2jsr/"
]
observations = []
for url in discovery_pages:
    page = read_json(directory / "pages" / (identity(url) + ".json"))
    if page.get("http_status") != 200:
        continue
    for row in study["keywords"]:
        if row["discovery"] != "editorial_expansion":
            continue
        fields = {name: phrase_count(page[name], row["query"]) for name in ("title", "description", "text")}
        if not any(fields.values()):
            continue
        row.update(discovery="observed", discovery_note="Exact normalized phrase found in captured publisher title, description or selected body; publisher wording is not demand, accuracy or availability evidence.")
        row["sources"] = sorted(set(row.get("sources", [])) | {url})
        observations.append({"query": row["query"], "game": row["game"], "url": url, "counts": fields, "captured_at": page["captured_at"], "raw_file": page.get("raw_file")})
validate_study(study)
save_json(directory / "study.json", study)
path = directory / "acquisition-phrase-observations.json"
old = read_json(path) if path.exists() else []
combined = {(x["game"], key(x["query"]), x["url"]): x for x in [*old, *observations]}
save_json(path, list(combined.values()))
print({"new_publisher_phrases": len(observations), "query_roles": dict(Counter(k["query_role"] for k in study["keywords"])), "by_game": dict(Counter(k["game"] for k in study["keywords"])), "observed": sum(k["discovery"] == "observed" for k in study["keywords"])})
