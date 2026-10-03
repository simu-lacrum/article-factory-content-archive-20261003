"""Apply the reviewed free/download and feature query expansion, without inventing demand."""
import sys
from pathlib import Path
from urllib.parse import quote_plus

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import key, validate_study
from article_factory.research.service import read_json, save_json, import_serps

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
raw = read_json(directory / "raw/google-acquisition-observations.json")
initial_count = len(study["keywords"])

# These are manually selected research candidates, not a Cartesian-product page generator.
expansions = {
    "deadlock-hub": "deadlock hack|deadlock hacks|deadlock cheat software|deadlock cheat features|deadlock cheat review|best deadlock hack",
    "cs2-hub": "cs2 hacks|cs2 hack|counter strike 2 cheats|counter strike 2 hacks|counter strike 2 cheat|counter strike 2 hack|cs 2 cheats|cs2 cheat software|cs2 cheat features",
    "dota2-hub": "dota2 cheats|dota2 hacks|dota 2 hack|dota 2 hacks|dota 2 cheat software|dota 2 cheat features",
    "dota2-comparison": "free vs paid dota 2 cheats|dota 2 cheats free trial|dota 2 script free trial|dota 2 free cheat vs trial|dota 2 cheat subscription|dota 2 cheat free version limitations",
    "deadlock-auto-parry": "deadlock auto parry cheats|deadlock auto parry hack|deadlock auto parry script|deadlock autoparry cheat|deadlock auto parry cheat free|free deadlock auto parry|deadlock auto parry download|deadlock auto parry mod|deadlock auto block cheat|deadlock melee parry cheat|deadlock parry hack|deadlock auto parry light melee|deadlock auto parry vs auto block",
    "deadlock-souls": "deadlock soul aimbot cheat|deadlock soul aimbot free|deadlock soul aimbot download|deadlock soul triggerbot free|deadlock auto soul secure|deadlock auto deny cheat|deadlock soul orb aimbot|deadlock soul esp cheat|deadlock soul triggerbot vs aimbot|deadlock auto last hit cheat",
    "deadlock-esp": "deadlock wallhack|deadlock wallhack cheat|deadlock wallhack free|deadlock esp hack|deadlock esp free|free deadlock esp|deadlock esp download|deadlock radar hack|deadlock player esp|deadlock item esp|deadlock health esp|deadlock radar vs esp",
    "deadlock-aimbot": "deadlock aimbot cheat|deadlock aimbot free|free deadlock aimbot|deadlock aimbot download|deadlock silent aim|deadlock silent aim cheat|deadlock aim assist cheat|deadlock aimbot vs aim assist|deadlock aimbot prediction|deadlock triggerbot|deadlock triggerbot cheat|deadlock triggerbot free",
    "deadlock-combos": "deadlock combo script|deadlock auto combo|deadlock auto combo cheat|deadlock hero scripts|deadlock ability automation|deadlock combo script free",
    "deadlock-dodger": "deadlock auto dodge|deadlock auto dodge cheat|deadlock auto dodge script|deadlock dodger cheat|deadlock auto dodge free|deadlock auto dodge vs parry|deadlock skillshot dodge cheat",
    "deadlock-trial": "deadlock cheats free trial|deadlock free cheat vs trial|deadlock cheat subscription|deadlock cheat trial limitations|deadlock cheat refund policy",
    "cs2-triggerbot": "cs2 triggerbot cheat|cs2 triggerbot free|free cs2 triggerbot|cs2 triggerbot download|cs2 triggerbot hack|triggerbot cs2 free|cs2 triggerbot vs aimbot|cs2 triggerbot limitations",
    "cs2-esp": "cs2 wallhack|cs2 wallhack free|free cs2 wallhack|cs2 wallhack download|cs2 esp free|free cs2 esp|cs2 esp download|cs2 radar hack|cs2 radar hack free|cs2 box esp|cs2 skeleton esp|cs2 health esp|cs2 radar vs wallhack",
    "cs2-aimbot": "cs2 aimbot cheat|cs2 aimbot free|free cs2 aimbot|cs2 aimbot download|cs2 aim assist cheat|cs2 silent aim|cs2 silent aim vs aimbot|cs2 recoil control cheat|cs2 no recoil cheat|cs2 legit aimbot|cs2 aim assist vs aimbot",
    "cs2-skin-changer": "cs2 skin changer free|free cs2 skin changer|cs2 skin changer free download|cs2 skinchanger|cs2 skinchanger free|cs2 inventory changer|cs2 knife changer|cs2 glove changer|cs2 skin changer vs inventory changer|cs2 skin changer server|cs2 skin changer bannable|cs2 skin changer mod",
    "cs2-external": "cs2 external cheat free|free external cs2 cheats|cs2 external esp|cs2 external radar|cs2 external vs internal cheat",
    "cs2-grenade-helper": "cs2 grenade helper cheat|cs2 grenade helper free|cs2 lineup helper|cs2 nade helper|cs2 grenade prediction cheat|cs2 grenade helper vs lineup guide",
    "cs2-free-paid": "cs2 cheats free trial|free cs2 cheats vs paid|cs2 cheat free version limitations|cs2 cheat subscription vs lifetime",
    "dota2-scripts": "dota 2 script|dota2 scripts|dota 2 scripts free|free dota 2 scripts|dota 2 scripts download|dota 2 scripts free download|dota 2 hack scripts|dota 2 script hack|dota 2 script bot|dota 2 combo scripts|dota 2 auto combo script",
    "dota2-invoker": "dota 2 invoker script|dota 2 script invoker|invoker script free|dota 2 invoker script free|invoker combo script|invoker script vs macro",
    "dota2-meepo": "dota 2 meepo script|meepo script free|dota 2 meepo script free|meepo auto poof script|meepo script vs macro",
    "dota2-maphack": "dota 2 map hack|dota2 maphack|dota 2 maphack free|free dota 2 maphack|dota 2 maphack download|dota 2 map hack free download|dota 2 script map hack|dota 2 esp|dota 2 fog of war hack|dota 2 enemy vision cheat|dota 2 maphack vs esp",
    "dota2-ward-tracker": "dota 2 ward esp|dota 2 enemy ward hack|dota 2 ward detection cheat",
    "dota2-roshan": "dota 2 roshan timer hack|dota 2 roshan tracker cheat|dota 2 roshan esp free",
    "dota2-teleport": "dota 2 teleport tracker|dota 2 tp tracker cheat|dota 2 teleport preview cheat|dota 2 teleport esp",
    "dota2-auto-dodge": "dota 2 autododge|dota 2 auto dodge cheat|dota 2 auto dodge script|dota 2 auto dodge free|dota 2 dodger hack|dota 2 auto dodge vs auto block|dota 2 skillshot dodge script|dota 2 auto hex script",
    "dota2-auto-last-hit": "dota 2 last hit script free|dota 2 auto last hit cheat|dota 2 auto deny script|dota 2 last hit hack|dota 2 last hit trainer vs script",
    "dota2-skin-changer": "dota 2 skin changer free|free dota 2 skin changer|dota 2 skin changer download|dota 2 skin changer free download|dota 2 script skin|dota2 skinchanger|dota 2 inventory changer|dota 2 skin changer visible to others",
}

for game, label, site in (("deadlock", "Deadlock", "deadlockhacks.com"), ("cs2", "CS2", "counterskrikecheats.com"), ("dota2", "Dota 2", "cheatsgaming.com")):
    stem = label.lower()
    ident = game + "-free-download"
    queries = [f"free {stem} cheats", f"{stem} cheats free", f"{stem} free cheats", f"{stem} cheat free", f"free {stem} hacks", f"{stem} hacks free", f"{stem} hack free", f"{stem} cheats download", f"download {stem} cheats", f"{stem} cheats free download", f"free {stem} cheats download", f"{stem} hack download", f"{stem} hacks free download", f"best free {stem} cheats", f"{stem} free cheat no subscription"]
    expansions[ident] = "|".join(queries)
    if not any(c["id"] == ident for c in study["clusters"]):
        study["clusters"].append({"id": ident, "game": game, "language": "en", "primary_query": queries[0],
            "title": f"{label} free access and downloads: landing-page research", "reader_job": "Find an actually available free offer or clearly identified trial, with stated limitations and a verified official destination.",
            "intent": "transactional", "scope": "third_party_software", "page_type": "product_or_category", "publication_action": "research_landing", "primary_site": site,
            "grouping_basis": "editorial_hypothesis_pending_serp_overlap_validation", "original_value": "A dated offer inventory distinguishing permanent free access, limited trial, paid subscription and unavailable offers.",
            "semantic_terms": ["free version", "trial duration", "feature limits", "subscription", "official website", "availability", "last checked"],
            "competitor_urls": [], "outline": ["State what is actually free and currently verified", "Distinguish trial access from a free tier", "Show limitations and dated official source", "Identify download destination without implementation instructions", "FAQ"],
            "anchor_guidance": ["Use the vendor name for an official destination; use download wording only if it really leads to the stated download", "Link a free-versus-trial explanation where terms need explaining", "Never label a paid affiliate destination as a free download"],
            "evidence_needed": ["Verify access terms, destination ownership and availability from first-party sources", "Inspect existing owned URLs before creating a landing page", "No fake download buttons, binary mirroring, implementation or evasion steps"],
            "priority": "P1" if game != "dota2" else "P2", "priority_basis": "User-requested acquisition coverage; not an estimate of ranking opportunity",
            "serp_mismatch": "The sampled acquisition results include products, catalogs, videos and sometimes commands. An explanatory article does not by itself satisfy download intent. This is a research destination, not a publishable offer.",
            "editorial_status": "requires_verified_offer_before_landing_publication"})

# Keep access comparisons as article jobs; broad free/download queries get their own destination.
for c in study["clusters"]:
    if c["id"] in {"cs2-free-paid", "deadlock-trial"}:
        c["primary_query"] = c["article_target_query"] = "free vs paid " + ("cs2" if c["game"] == "cs2" else "deadlock") + " cheats"
        c["serp_mismatch"] = "Broad free/download searches show access pages and catalogs. This comparison targets access terms, not a downloadable offer; do not use the broad head query's volume as its own demand."

clusters = {c["id"]: c for c in study["clusters"]}
keywords = {(k["game"], key(k["query"])): k for k in study["keywords"]}

def put(query, cluster_id, role="product_access", discovery="editorial_expansion", source=None, note=None):
    c = clusters[cluster_id]
    token = (c["game"], key(query))
    row = keywords.get(token)
    if row is None:
        row = {"query": query, "game": c["game"], "language": "en", "cluster_id": cluster_id,
               "intent": "transactional" if role == "product_access" else "informational", "scope": "third_party_software",
               "discovery": "editorial_expansion", "sources": [], "discovery_note": "Manually proposed variant; demand and synonym grouping remain unverified."}
        study["keywords"].append(row)
        keywords[token] = row
    elif not cluster_id.endswith("-free-download") and discovery != "observed":
        return row  # Preserve reviewed roles and grouping of pre-existing non-acquisition phrases.
    if cluster_id.endswith("-free-download"):
        row["cluster_id"] = cluster_id
    row["query_role"] = role
    row["recommended_page_type"] = {"product_access": "verified_product_or_category", "community_research": "discussion_or_navigation", "implementation_research": "research_only_no_operational_article", "ambiguous_research": "intent_review", "article_candidate": "article_or_section"}[role]
    if role == "product_access":
        row["intent"] = "transactional"
    if discovery == "observed":
        row["discovery"] = discovery
        row["sources"] = sorted(set(row.get("sources", [])) | {source})
        row["discovery_note"] = note
    return row

for cluster_id, phrases in expansions.items():
    for phrase in phrases.split("|"):
        role = "article_candidate" if any(x in phrase for x in (" vs ", "limitations", "visible to others", "bannable", "refund policy")) else "product_access"
        put(phrase, cluster_id, role)

autocomplete_routes = {
    "deadlock": "deadlock-auto-parry", "cs2": "cs2-skin-changer", "dota2": "dota2-scripts"
}
for batch in raw["autocomplete"]:
    for query in batch["queries"]:
        cluster_id = autocomplete_routes[batch["game"]]
        if query == "dota 2 script map hack": cluster_id = "dota2-maphack"
        if query == "dota 2 script skin": cluster_id = "dota2-skin-changer"
        if query == "dota 2 script invoker": cluster_id = "dota2-invoker"
        role = "community_research" if any(x in query for x in ("reddit", "github", "unknowncheats")) else "implementation_research" if any(x in query for x in (" source", "lua", "ahk")) else "ambiguous_research" if any(x in query for x in ("server", "plugin", "bot", "light melee")) else "article_candidate" if "bannable" in query else "product_access"
        row = put(query, cluster_id, role, "observed", "https://www.google.com/search?q=" + quote_plus(batch["seed"]) + "&hl=en&gl=us&pws=0",
                  "Visible non-history autocomplete label; signed-in session, location unknown. No volume inferred. See raw/google-acquisition-observations.json.")
        if role == "implementation_research": row["scope"] = "restricted_operational"

snapshots = []
for capture in raw["searches"]:
    snapshots.append({k: capture[k] for k in ("query", "game", "captured_at")})
    snapshots[-1].update(language="en", engine="google", country_requested="US", country_observed=None, method="browser_dom", session_cohort="codex-iab-signed-in",
        source_file="raw/google-acquisition-observations.json", personalization_note="Results are not personalized", location_note="Unknown - Can't determine location; US requested only",
        result_scope="Public linked h3 headings; no organic rank asserted; not a guaranteed full top ten", visible_questions=capture["questions"],
        results=[{"title": title, "url": url, "type": kind, "page_type": kind + "_provisional", "rank": None, "observed_heading_order": i} for i, (title, url, kind) in enumerate(capture["results"], 1)])
    # Deliberately do not promote a query we typed to observed keyword discovery.

urls = {
    "deadlock-free-download": ["https://uc.zone/en/deadlock", "https://cheater.fun/deadlock_cheats/", "https://en.exloader.net/tree/games/deadlock/", "https://octarine.fun/en/deadlock/"],
    "cs2-free-download": ["https://undetek.com/", "https://anyx.gg/", "https://cheater.fun/cs2-hacks/"],
    "dota2-free-download": ["https://uc.zone/en/dota2", "https://cheater.fun/cheats_for_dota2_download_hacks_free/"],
    "cs2-skin-changer": ["https://en.exloader.net/tree/modifications/sdk2changer/"],
    "dota2-maphack": ["https://en.exloader.net/tree/modifications/d2jsr/"]
}
for ident, sources in urls.items():
    clusters[ident]["competitor_urls"] = sorted(set(clusters[ident]["competitor_urls"]) | set(sources))
    for url in sources:
        if "cheater.fun" in url or "exloader.net" in url or "octarine.fun/en/deadlock" in url:
            study.setdefault("page_types", {})[url] = "software_catalog" if "cheater.fun" in url or "/games/" in url else "software_access_landing"
            study.setdefault("source_policies", {})[url] = {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True, "reviewed_at": "2026-09-21", "reason": "Acquisition-intent and copy analysis only. Downloads, ownership, current access terms, safety and efficacy not verified. No automatic adoption of catalog claims."}

for url in ["https://cheater.fun/deadlock_cheats/", "https://cheater.fun/cs2-hacks/", "https://cheater.fun/cheats_for_dota2_download_hacks_free/"]:
    study.setdefault("extraction_rules", {})[url] = {"content_selector": ".col-lg.small_display_margin", "expected_matches": 1, "reviewed_at": "2026-09-21", "reason": "Category heading, introduction and all visible catalog cards. Default article extraction selected only the first card. Exclude the side navigation and news widget."}
study.setdefault("extraction_rules", {})["https://en.exloader.net/tree/games/deadlock/"] = {"content_selector": ".games-inside-wrapper > .title, .games-inside-wrapper > .game-description-seo, .games-inside-wrapper > .mod-cards, .games-inside-wrapper > .game-seo", "expected_matches": 4, "reviewed_at": "2026-09-21", "reason": "Category title, description, cards and category FAQ; exclude languages, navigation and company footer."}
for url in ["https://en.exloader.net/tree/modifications/sdk2changer/", "https://en.exloader.net/tree/modifications/d2jsr/"]:
    study.setdefault("extraction_rules", {})[url] = {"content_selector": ".games-inside-wrapper > .title-block, .games-inside-wrapper > .rate-info-block, .games-inside-wrapper > .download-info, .games-inside-wrapper > .basic-info-block, .games-inside-wrapper > .main-content", "expected_matches": 5, "reviewed_at": "2026-09-21", "reason": "Vendor description and metadata; exclude user reviews, related products, navigation and footer. Setup text retained only for on-page counting; source excluded from article fact evidence."}

# Lexical facets describe the words, not verified intent or an available offer.
for row in study["keywords"]:
    text = " " + key(row["query"]) + " "
    row["search_facets"] = [word for word in ("free", "download", "trial", "paid", "best", "vs", "reddit", "github") if f" {word} " in text]
    row.setdefault("query_role", "article_candidate")
    row.setdefault("recommended_page_type", "article_or_section")

validate_study(study)
save_json(directory / "study.json", study)
save_json(directory / "raw/google-acquisition-intents.json", {"method_note": raw["method_note"], "snapshots": snapshots})
result = import_serps(directory, directory / "raw/google-acquisition-intents.json")
print({"added_keywords": len(study["keywords"]) - initial_count, "keywords": len(study["keywords"]), "groups": len(study["clusters"]), "serps": result["stored_snapshots"]})
