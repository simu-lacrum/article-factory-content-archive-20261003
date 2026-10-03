"""Merge reviewed cosmetic/radar/soul decisions; preserve unrelated study edits."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.service import read_json, save_json
from article_factory.research.models import validate_study

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
query = "deadlock soul triggerbot"
if not any(k["query"] == query and k["game"] == "deadlock" for k in study["keywords"]):
    study["keywords"].append({"query": query, "game": "deadlock", "language": "en", "cluster_id": "deadlock-souls",
        "intent": "informational", "scope": "third_party_software", "discovery": "editorial_expansion", "sources": [],
        "discovery_note": "Editor-proposed query checked in Google; searching it does not establish measured demand. A product feature label is not a volume estimate."})
skin_urls = ["https://xplay.gg/blog/cs2-skinchanger-how-it-works-and-how-to-access-it-on-our-servers/",
             "https://www.hotspawn.com/counter-strike/guide/are-cs2-skin-changers-bannable",
             "https://sellyourskins.com/blog/is-skin-changer-bannable/"]
radar_urls = ["https://chamscheats.com/counter-strike-2-aimbot-esp-wallhack-undetected/",
              "https://www.gamer.ru/en/p/radar-khak-v-cs2-nevidimaya-ugroza-BEWc3dHWwnc0Z"]
soul_url = "https://cheatstore.net/deadlock/triggerbot"
for c in study["clusters"]:
    if c["id"] == "cs2-skin-changer":
        c.update(
            serp_mismatch="The broad query mixes product selection, a server-cosmetic guide, a trading tool, risk discussions and software/video results. The visibility question returns three discussions and three guides plus a repository issue. Only the Xplay URL overlaps. Keep these as distinct reader questions within the existing comparison update, not a validated synonym cluster or an automatic new URL.",
            update_scope="Preserve the existing comparison's purchasing job. Add a concise visibility/ownership section and distinguish client tools, server cosmetics and actual item trading. Re-audit current product claims before changing any ranking or recommendation.",
            outline=["What the reader wants to change: appearance, server cosmetics or owned items", "Can other players see the change? State the specific context and evidence", "Compare documented functions using the same criteria", "Inventory ownership and trading are separate questions", "What is confirmed, vendor-stated or unknown", "FAQ"],
            intent_matched_urls=[], usage_phrases=["skin changer", "skin changers", "client", "inventory"],
            corpus_note="Risk guides were found for the narrower visibility question. They are supplementary observations, not the broad query's comparison-page norm. Xplay was blocked by ordinary HTTP; its snippet does not supply body counts.",
            evidence_needed=["Inspect the live comparison before editing and preserve its reader job", "Verify current visibility claims with first-party product/server documentation; older forum labels may refer to CS:GO", "Do not infer inventory ownership or universal invisibility from a cosmetic feature name", "Obtain volume before prioritizing by measured demand"])
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | set(skin_urls))
    elif c["id"] == "cs2-esp":
        c.update(article_target_query="cs2 radar vs esp", intent_matched_urls=radar_urls,
            usage_phrases=["radar", "ESP", "wallhack"],
            serp_mismatch="The broad cs2 esp sample has three repository results, three release/download/showcase results, two videos and one demo discussion. The radar comparison has two articles, three discussions, a release and social results. No shared eligible URL. Aim the planned explainer at the narrower comparison; its demand remains unmeasured. Do not turn the broad download/implementation intent into an instructional article.",
            corpus_note="Chams is a commercial feature explainer. Gamer.ru labels its page auto-translated and mixes unsupported efficacy/evasion claims with an implausible cosmetic-performance promotion. Both are on-page observations only; neither establishes technical truth or a word-count target.",
            evidence_needed=["Use dated first-party descriptions for each displayed-information claim", "Separate native minimap settings, demo spectator views, on-screen overlays and third-party radar", "No anti-cheat evasion, configuration or implementation steps", "Obtain comparison-query volume before demand-based scheduling"])
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | set(radar_urls))
    elif c["id"] == "deadlock-souls":
        c.update(
            serp_mismatch="The singular soul aimbot sample contains three product pages, two repositories, two forum results and video. Soul triggerbot mixes two products with gameplay discussions, wiki/commands, a repository and video. Only Tsuki is shared. Keep one supporting feature explainer; do not split aim/fire/display into new pages or claim the terms are SERP-validated synonyms. Existing plural target has its own earlier observation; volume is unknown for all these variants.",
            publication_role="Supporting explanation linked from the feature hub; the article does not substitute for a product-access page.",
            intent_matched_urls=["https://tsuki.gg/products/deadlock/features"], usage_phrases=["soul aimbot", "soul triggerbot", "soul ESP"],
            corpus_note="Tsuki is observed for both new singular variants. Broader product descriptions remain a mixed-format corpus; Cluster is owned and excluded from competitor usage statistics.")
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | {soul_url})
study.setdefault("page_types", {}).update({
    skin_urls[0]: "server_cosmetic_feature_guide", skin_urls[1]: "risk_guide", skin_urls[2]: "risk_guide",
    radar_urls[0]: "commercial_feature_explainer", radar_urls[1]: "auto_translated_editorial_post",
    soul_url: "product_feature_landing"})
for url in [*skin_urls, *radar_urls, soul_url]:
    study.setdefault("source_policies", {})[url] = {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True,
        "reviewed_at": "2026-09-21", "reason": "Search-intent and on-page evidence only. Current efficacy, safety, ownership, detection and mechanics claims were not independently verified; do not feed them automatically into article facts."}
study.setdefault("extraction_rules", {}).update({
    skin_urls[1]: {"content_selector": "h1, #post-desc", "expected_matches": 2, "reviewed_at": "2026-09-21", "reason": "Exclude tournament/newsletter/related-story widgets from the article body."},
    skin_urls[2]: {"content_selector": "h1, .entry-content", "expected_matches": 2, "reviewed_at": "2026-09-21", "reason": "Exclude sidebar, related articles, author metadata and comments."},
    radar_urls[0]: {"content_selector": "#elCmsPageWrap", "expected_matches": 1, "reviewed_at": "2026-09-21", "reason": "Article including its FAQ and closing section; exclude preceding shop product cards."},
    radar_urls[1]: {"content_selector": ".postinnercontent", "expected_matches": 1, "reviewed_at": "2026-09-21", "reason": "Post title and body, excluding the site language controls and comments heading."}
})
validate_study(study)
save_json(directory / "study.json", study)
print({"updated_groups": ["cs2-skin-changer", "cs2-esp", "deadlock-souls"], "keywords": len(study["keywords"])})
