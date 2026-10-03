"""Combine retained public observations with clearly labeled editorial hypotheses."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import canonical_url, key
from article_factory.research.pages import phrase_count
from article_factory.research.service import read_json, save_json

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")

def classify(url):
    if "battlestar" in url or "planetary" in url:
        return "unrelated", "unrelated_game"
    if "youtube.com" in url or "tiktok.com" in url:
        return "video", "video"
    if "github.com" in url:
        return "code_reference", "repository"
    if any(part in url for part in ("reddit.com", "/forum", "steamcommunity.com", "hackvshack.net", "stackexchange.com")):
        return "forum", "discussion"
    if any(part in url.lower() for part in ("console_commands", "gamefaqs.", "liveabout.", "fandom.com/wiki/cheats", "totalcsgo.com/commands")):
        return "article", "command_reference"
    if any(part in url for part in ("/guides/", "/blog/", "/information/", "/articles/", "buttondown.com", "/archive/", "/guides-")):
        return "article", "guide_or_article"
    if "apps.apple.com" in url or "stratz.com" in url:
        return "product", "legitimate_analytics"
    return "organic", "commercial_page_provisional"

snapshots = []
for file in sorted((directory / "raw").glob("google-observed*.json")):
    data = read_json(file)
    for sample in data["samples"]:
        game = "dota2" if "dota" in sample["query"] else "deadlock" if "deadlock" in sample["query"] else "cs2"
        snapshots.append({"query": sample["query"], "game": game, "language": "en", "engine": "google",
                          "country_requested": data["country_requested"], "country_observed": None,
                          "captured_at": data["captured_at"], "method": "browser_dom", "session_cohort": "codex-iab-signed-in",
                          "sample_scope": data["result_scope"], "questions": sample.get("questions", []),
                          "source_file": str(file.relative_to(directory)),
                          "results": [{"url": u, "rank": None, "observed_heading_order": i,
                                       "type": classify(u)[0], "page_type": classify(u)[1]} for i, u in enumerate(sample["urls"], 1)]})
for file in sorted((directory / "raw").glob("*.json")):
    data = read_json(file)
    if not isinstance(data, dict) or data.get("engine") != "web_search_unspecified" or not data.get("query"):
        continue
    query = data["query"]
    results = []
    for title, url in re.findall(r"^([^\n]+) \((https?://[^\s)]+)\)\s*\n", data.get("raw", ""), flags=re.M):
        results.append({"url": url, "title": title, "rank": None, "type": classify(url)[0], "page_type": classify(url)[1]})
    if results:
        snapshots.append({"query": query, "game": "dota2" if "dota" in query else "deadlock" if "deadlock" in query else "cs2",
                          "language": "en", "engine": "unspecified", "country_requested": None, "country_observed": None,
                          "captured_at": data["captured_at"], "method": "web_search_unspecified", "results": results,
                          "source_file": str(file.relative_to(directory))})
study["serps"] = snapshots

for game, query, site in (("cs2", "cs2 cheats", "cheatsgaming.com"), ("dota2", "dota 2 cheats", "cheatsgaming.com"), ("deadlock", "deadlock cheats", "deadlockhacks.com")):
    cid = game + "-hub"
    if not any(c["id"] == cid for c in study["clusters"]):
        study["clusters"].append({"id": cid, "game": game, "language": "en", "primary_query": query,
            "title": query.upper() if game == "cs2" else query.title(), "reader_job": "Choose between feature explanations, product comparisons and legitimate console-command references",
            "intent": "mixed_commercial_and_informational", "scope": "mixed", "page_type": "category_hub",
            "publication_action": "update_hub", "primary_site": site, "grouping_basis": "editorial_hypothesis_pending_serp_overlap_validation",
            "original_value": "An explicit intent split with links to useful feature articles and dated commercial information",
            "semantic_terms": ["features", "comparison", "console commands", "scripts"], "competitor_urls": [],
            "anchor_guidance": ["Link each distinct reader job with a descriptive anchor; do not repeat an exact-match anchor across every card"], "outline": []})
        study["keywords"].append({"query": query, "game": game, "language": "en", "cluster_id": cid, "intent": "mixed", "scope": "mixed", "discovery": "editorial_expansion", "sources": []})

cluster_map = {c["id"]: c for c in study["clusters"]}
extra = {"deadlock-auto-parry": ["https://tsuki.gg/products/deadlock/features"],
         "deadlock-souls": ["https://avalan.cc/features", "https://tsuki.gg/products/deadlock/features"],
         "cs2-triggerbot": ["https://insanitycheats.com/product-tag/triggerbot/", "https://undetek.com/free-cs2-cheats-download/"]}
for cid, urls in extra.items():
    cluster_map[cid]["competitor_urls"] = sorted(set(cluster_map[cid]["competitor_urls"] + urls))
for game in ("cs2", "dota2", "deadlock"):
    head = next(s for s in snapshots if s["method"] == "browser_dom" and s["query"] == {"cs2": "cs2 cheats", "dota2": "dota 2 cheats", "deadlock": "deadlock cheats"}[game])
    cluster_map[game + "-hub"]["competitor_urls"] = [r["url"] for r in head["results"] if r["page_type"] == "commercial_page_provisional"]
for cid in ("cs2-external", "cs2-comparison", "cs2-triggerbot", "cs2-esp", "cs2-aimbot", "cs2-skin-changer"):
    cluster_map[cid]["competitor_urls"] = sorted(set(cluster_map[cid]["competitor_urls"] + ["https://cs2-cheats.com/", "https://en.exloader.net/"]))

inventory = read_json(directory / "owned-inventory.json")["links"]
mapping = {"dota2-scripts": "dota-2-cheats-scripts-explained", "dota2-maphack": "maphack-for-dota-2",
           "dota2-skin-changer": "dota-2-skin-changer-2026", "dota2-comparison": "melonity-vs-umbrella",
           "dota2-commands": "complete-guide-to-cheat-commands", "cs2-external": "top-5-external",
           "cs2-free-paid": "best-free-cheats", "cs2-comparison": "top-cheats-for-cs2",
           "cs2-skin-changer": "top-skinchangers-for-cs2", "deadlock-auto-parry": "deadlock-auto-parry-cheat",
           "deadlock-comparison": "top-cheats-for-deadlock"}
for cid, token in mapping.items():
    match = next((x for x in inventory if token in x["url"]), None)
    if match:
        cluster_map[cid].update(existing_url=match["url"], publication_action="update_article", primary_site="cheatsgaming.com",
                                cannibalization_note="Existing live URL matches the subject. Improve or differentiate it; do not publish a second generic guide.")

priorities = ["cs2-triggerbot", "deadlock-souls", "deadlock-fov", "dota2-ward-tracker", "dota2-roshan", "cs2-esp", "deadlock-auto-parry", "dota2-teleport", "cs2-skin-changer", "dota2-scripts", "deadlock-comparison", "cs2-external"]
for c in study["clusters"]:
    c["priority"] = "P1" if c["id"] in priorities else "P2"
    c["priority_basis"] = "Editorial usefulness, feature specificity and existing coverage; NOT search volume or ranking difficulty"
    c["research_state"] = "needs_dedicated_serp_and_volume"
    matching = [s for s in snapshots if s["method"] == "browser_dom" and key(s["query"]) == key(c["primary_query"])]
    if matching:
        c["research_state"] = "serp_sampled_volume_unknown"
    if c["id"] == "dota2-ward-tracker":
        c["serp_mismatch"] = "Broad ward tracker query surfaced warding guides, analytics and apps. Do not assume third-party cheat intent. Validate the qualified variant before a standalone article."
        c["recommended_target_query"] = "dota 2 ward tracker cheat"
        c["publication_action"] = "validate_intent_first"
    c["suggested_questions"] = list(dict.fromkeys(q for s in matching for q in s.get("questions", [])))
    # Every B/A visual contract still comes from the canonical guide, not this research module.

pages = [read_json(p) for p in (directory / "pages").glob("*.json")]
for keyword in study["keywords"]:
    if keyword.get("discovery_note", "").startswith("Observed People Also Ask"):
        continue
    matches = [p["url"] for p in pages if p.get("language") == keyword["language"] and p.get("text")
               and p.get("requested_url", p["url"]) in cluster_map[keyword["cluster_id"]]["competitor_urls"]
               and phrase_count(p["title"] + " " + p["text"], keyword["query"])]
    keyword["discovery"] = "observed" if matches else "editorial_expansion"
    keyword["sources"] = matches if matches else keyword["sources"]
    keyword["discovery_note"] = "Exact phrase found in sampled publisher text; does not prove search volume" if matches else "Writer-proposed search phrase based on the topic; demand unverified"
questions = {"cs2-triggerbot": ["What is a triggerbot in CS2?", "Is triggerbot cheating?", "What's the difference between aimbot and triggerbot?"],
             "cs2-external": ["Does CS2 detect external cheats?"],
             "dota2-scripts": ["Is scripting allowed in Dota 2?", "Is scripting in a game cheating?"],
             "deadlock-auto-parry": ["Is there auto parry in Deadlock?", "How does parry work in Deadlock?", "Does Unstoppable stop parry Deadlock?", "How to train parry Deadlock?"]}
for cid, phrases in questions.items():
    for phrase in phrases:
        c = cluster_map[cid]
        existing = next((k for k in study["keywords"] if key(k["query"]) == key(phrase) and k["game"] == c["game"]), None)
        if existing:
            existing.update(discovery="observed", sources=["https://www.google.com/search?q=" + c["primary_query"].replace(" ", "+") + "&hl=en&gl=us&pws=0"],
                            discovery_note="Observed People Also Ask question in the saved Google sample. Question wording does not establish exact search volume.")
            continue
        study["keywords"].append({"query": phrase, "game": c["game"], "language": "en", "cluster_id": cid,
            "intent": "informational", "scope": "legitimate_mechanic" if phrase in {"How does parry work in Deadlock?", "Does Unstoppable stop parry Deadlock?", "How to train parry Deadlock?"} else c["scope"],
            "discovery": "observed", "sources": ["https://www.google.com/search?q=" + c["primary_query"].replace(" ", "+") + "&hl=en&gl=us&pws=0"],
            "discovery_note": "Observed People Also Ask question in the saved Google sample. Question wording does not establish exact search volume."})
save_json(directory / "study.json", study)
print(json.dumps({"serps": len(snapshots), "observed_terms": sum(k["discovery"] == "observed" for k in study["keywords"]), "clusters": len(study["clusters"])}))
