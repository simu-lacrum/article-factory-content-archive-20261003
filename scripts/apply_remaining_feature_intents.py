"""Reviewed page decisions from remaining CS2/Deadlock target-query samples."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import key, validate_study
from article_factory.research.service import read_json, save_json, import_serps

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
raw = read_json(directory / "raw/google-remaining-feature-observations.json")
snapshots = []
for capture in raw["searches"]:
    row = {k: capture[k] for k in ("query", "game", "captured_at")}
    row.update(language="en", engine="google", country_requested="US", country_observed=None, method="browser_dom", session_cohort="codex-iab-signed-in",
        source_file="raw/google-remaining-feature-observations.json", personalization_note="Results are not personalized", location_note="Unknown - Can't determine location; requested US only",
        result_scope="Public linked h3 headings; not a guaranteed full top ten and no organic ranks asserted", visible_questions=capture["questions"],
        results=[{"title": title, "url": url, "type": kind, "page_type": kind + "_provisional", "rank": None, "observed_heading_order": i} for i, (title, url, kind) in enumerate(capture["results"], 1)])
    if capture.get("visible_media_note"):
        row["visible_media_note"] = capture["visible_media_note"]
    snapshots.append(row)

updates = {
    "cs2-aimbot": {"publication_action": "include_as_section", "section_parent_id": "cs2-triggerbot", "article_target_query": "cs2 aim assist vs aimbot",
        "serp_mismatch": "The broad aimbot sample mixes product pages, discussions, repositories, video, a software release and a player's config page. The proposed naming/aim-versus-fire explanation substantially overlaps the existing triggerbot-versus-aimbot article. Add a short naming section there; no validated equivalence or standalone demand is claimed.",
        "outline": ["An aiming label needs an action and target", "Aim assist, aimbot and legitbot are publisher vocabulary, not comparable specifications", "Link to the separate product-access destination when needed"]},
    "cs2-status": {"publication_action": "include_as_section", "section_parent_id": "cs2-comparison", "article_target_query": "cs2 cheat detected status meaning",
        "serp_mismatch": "The exact planned head query returns player trackers, reputation/reporting tools and anti-cheat discussion, not vendor product-status documentation. Preserve status-label interpretation as a comparison criterion, not a standalone article targeting this ambiguous head query.",
        "outline": ["Record the status source and timestamp", "A publisher's label is not an independently verified safety result", "State unavailable or conflicting information explicitly"]},
    "cs2-grenade-helper": {"article_target_query": "cs2 grenade helper vs lineups",
        "serp_mismatch": "The broad sample includes a prediction tool, lineup library, product page, community practice discussion, feature requests, code and video. Adding cheat removes the tool/library from the recorded headings; the two samples share only two eligible URLs. Keep a comparison of reader jobs, with its own unmeasured query. Do not promise to be a lineup library or a downloadable assistance feature.",
        "intent_matched_urls": [], "usage_phrases": ["grenade helper", "lineups", "grenade predictor"],
        "corpus_note": "SCOPE and CSNADES were observed for the broad query. They are first-party examples of tool/library formats, not an intent-matched corpus for the proposed untested comparison wording."},
    "cs2-free-paid": {"serp_mismatch": "The access comparison sample mixes vendor pages, a ranking discussion and videos with a separate free-game-versus-Prime question. Keep the existing comparison update focused on software access terms, and explicitly exclude the game's Prime purchase from this comparison. Dedicated comparison demand is still unknown."},
    "cs2-comparison": {"serp_mismatch": "The best-cheats sample has three product pages, one ranking discussion and four videos. An existing comparison can serve a purchasing research job if claims are dated and comparable. Result titles and videos are not independent tests or a basis for an invented winner."},
    "deadlock-aimbot": {"publication_action": "include_as_section", "section_parent_id": "deadlock-souls", "article_target_query": "deadlock player aimbot vs soul aimbot",
        "serp_mismatch": "The broad aimbot sample mixes repositories, vendor pages, community reports and a trading category. Its proposed article already repeats the player-versus-soul distinction in the soul-feature article. Consolidate that explanation there; the broad acquisition query stays available for product routing.",
        "outline": ["Player and soul-orb targets are different objects", "Projectile prediction is a separate publisher claim", "Name the target before comparing an aiming feature"]},
    "deadlock-fov": {"section_parent_id": "deadlock-souls",
        "evidence_terms": ["FOV for aimbot"],
        "publication_role": "A short aiming-FOV versus camera-FOV distinction in the consolidated target/action article; not a camera-setting tutorial."},
    "deadlock-esp": {"article_target_query": "deadlock radar vs esp",
        "serp_mismatch": "The broad ESP sample has software repositories, products/catalogs, a forum and video. Preserve the planned display-location comparison as a supporting informational job with unmeasured demand. It does not replace the product page sought by an access query.",
        "publication_role": "Supporting feature explanation linked from the product/category hub; article query remains an editorial hypothesis.",
        "intent_matched_urls": [], "usage_phrases": ["ESP", "radar", "wallhack"]},
    "deadlock-combos": {"publication_action": "include_as_section", "section_parent_id": "deadlock-hub", "article_target_query": "deadlock auto combo meaning",
        "serp_mismatch": "Hero combos cheat also returns ordinary cheat sheets, hero guides and console commands. Auto combo cheat still mixes parry/dispel discussion, commands and software. Shared software-release or command results do not validate an editorial cluster. Put a concise automation-scope explanation in the hub; a separate hero-by-hero article series is not justified.",
        "outline": ["A hero synergy guide is not an automation specification", "Separate a sequence of actions from target choice and conditions", "Link to verified feature descriptions without implementation steps"]},
    "deadlock-dodger": {"publication_action": "include_as_section", "section_parent_id": "deadlock-hub", "primary_query": "deadlock auto dodge cheat", "article_target_query": "deadlock auto dodge cheat meaning",
        "title": "Deadlock auto dodge: read the advertised scope",
        "serp_mismatch": "Deadlock dodger is heavily contaminated by a player nickname, hero concept, tracker, match avoidance, sports and Valorant. Auto dodge cheat instead returns product-feature pages, a release and video. Keep a feature-scope section in the hub and do not target the ambiguous nickname query with a standalone article.",
        "outline": ["Which event is claimed to trigger a response?", "Which response and named abilities are actually documented?", "Unknown coverage stays unknown"]},
    "deadlock-trial": {"publication_action": "include_as_section", "section_parent_id": "deadlock-comparison",
        "serp_mismatch": "Free-versus-paid results predominantly show vendor/category pages, plus discussion and video. The general comparison query does return multiple comparative articles. Access terms are a natural criterion in the existing comparison: consolidate this editorial job there, while keeping the separate free/download landing research.",
        "outline": ["Permanent free access, limited trial and paid subscription", "Verify duration, limitations and renewal terms", "Link to a dated official offer, not a disguised paid download"]},
    "deadlock-comparison": {"serp_mismatch": "The exact comparison sample includes several review/comparison pages, a discussion and a product page. This supports updating the existing comparison format. Commercial affiliation, method and dated claim evidence still need to be explicit; a ranking article's promise of testing is not proof of testing.",
        "intent_matched_urls": ["https://ivsofte.biz/en/blog/best-deadlock-cheats/", "https://deadlockcheats.net/blog"],
        "usage_phrases": ["best deadlock cheats", "deadlock cheats", "deadlock cheat", "comparison"],
        "corpus_note": "Two commercial comparison pages captured from the tested comparison query. Their publisher claims are on-page observations only; neither is an independently verified product test."}
}
new_sources = {
    "cs2-grenade-helper": ["https://scope.gg/grenade-predictor/", "https://csnades.gg/"],
    "deadlock-comparison": ["https://ivsofte.biz/en/blog/best-deadlock-cheats/", "https://madchad.net/best-deadlock-cheats-2026/", "https://deadlockcheats.net/blog"]
}
for c in study["clusters"]:
    if c["id"] in updates:
        c.update(updates[c["id"]])
    if c["id"] in new_sources:
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | set(new_sources[c["id"]]))
    if c["id"] == "cs2-triggerbot" and "Aiming names: aim assist, aimbot and legitbot" not in c["outline"]:
        c["outline"].insert(-1, "Aiming names: aim assist, aimbot and legitbot")
    if c["id"] == "deadlock-souls" and "Aiming FOV is not camera FOV" not in c["outline"]:
        c["outline"].insert(-1, "Aiming FOV is not camera FOV")
    if c["id"] == "deadlock-hub":
        c["outline"] = ["Choose the reader job: feature definition, documented comparison or access terms", "Soul targets, parry and displayed information", "Combo and auto-dodge claims: actions and limits", "Link ordinary controls and console commands separately"]

ambiguous_heads = {("cs2", "cs2 aimbot"), ("cs2", "cs2 cheat status"), ("cs2", "cs2 grenade helper"), ("deadlock", "deadlock aimbot"), ("deadlock", "deadlock esp"), ("deadlock", "deadlock hero combos cheat"), ("deadlock", "deadlock dodger")}
clusters = {c["id"]: c for c in study["clusters"]}
for row in study["keywords"]:
    if (row["game"], key(row["query"])) in ambiguous_heads:
        row.update(query_role="ambiguous_research", recommended_page_type="intent_review", intent_note="See the group's reviewed SERP mismatch; broad wording is not the article's target.")
    c = clusters[row["cluster_id"]]
    if row.get("query_role") == "article_candidate" and c.get("section_parent_id"):
        row["recommended_page_type"] = "section_of_" + c["section_parent_id"]

for ident, urls in new_sources.items():
    for url in urls:
        study.setdefault("page_types", {})[url] = "commercial_comparison" if ident == "deadlock-comparison" else "browser_tool" if "scope.gg" in url else "lineup_reference_library"
        study.setdefault("source_policies", {})[url] = {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True, "reviewed_at": "2026-09-21", "reason": "Retain for format and phrase analysis. Check first-party scope separately before using product/tool details; performance, safety, testing and rankings are unverified."}
study.setdefault("extraction_rules", {})["https://csnades.gg/"] = {"content_selector": "div[class~='max-w-[1700px]']", "expected_matches": 2, "reviewed_at": "2026-09-21", "reason": "Two disjoint homepage content wrappers: map/category index and guide/nade cards. The HTML main tag covers only the map list, omitting introduction, guides and cards."}
study["source_policies"]["https://scope.gg/grenade-predictor/"]["reason"] += " The page includes legacy-looking tickrate/map wording; do not assume every detail describes the current CS2 version."
study["source_policies"]["https://deadlockcheats.net/blog"]["reason"] += " The comparison uses an own-product column and unnamed generic rivals, with no inspected test protocol."
study["source_policies"]["https://ivsofte.biz/en/blog/best-deadlock-cheats/"]["reason"] += " Reseller recommendations and anti-cheat/evasion assertions are not independent factual evidence."
validate_study(study)
save_json(directory / "study.json", study)
save_json(directory / "raw/google-remaining-feature-intents.json", {"method_note": raw["method_note"], "snapshots": snapshots})
print(import_serps(directory, directory / "raw/google-remaining-feature-intents.json"))
print({"sections": [(c["id"],c["section_parent_id"]) for c in study["clusters"] if c.get("section_parent_id")]})
