"""Reviewed decisions from google-feature-intents.json; no wholesale study reset."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.service import read_json, save_json
from article_factory.research.models import validate_study

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
for query, game, cluster_id in (("dota 2 ward tracker cheat", "dota2", "dota2-ward-tracker"), ("deadlock aimbot fov", "deadlock", "deadlock-fov")):
    if not any(k["query"] == query and k["game"] == game for k in study["keywords"]):
        study["keywords"].append({"query": query, "game": game, "language": "en", "cluster_id": cluster_id,
            "intent": "informational", "scope": "third_party_software", "discovery": "editorial_expansion", "sources": [],
            "discovery_note": "Editor-proposed query checked in Google; executing a search does not independently establish user demand. See raw/google-feature-intents.json."})
updates = {
    "deadlock-fov": {
        "publication_action": "include_as_section", "section_parent_id": "deadlock-aimbot", "priority": "P2",
        "article_target_query": "deadlock aimbot fov",
        "serp_mismatch": "Camera FOV query returns settings discussions, mods and video. The aimbot-qualified query has a public Aimed FOV description but also repositories and camera/trainer discussions. Only one shared eligible URL; no validated merge. Explain the terminology inside the aimbot article. Do not promise camera-setting instructions or a standalone page for this unmeasured phrase.",
        "evidence_needed": ["Attribute Aimed FOV description to its publisher", "Do not claim a new camera setting, allowed modification or current limit without first-party evidence", "Revisit standalone demand only with stronger query evidence"],
    },
    "dota2-roshan": {
        "publication_action": "include_as_section", "section_parent_id": "dota2-maphack", "priority": "P2",
        "article_target_query": "dota 2 roshan esp",
        "serp_mismatch": "The timer query returns manual tools and game-mechanics references. The ESP-qualified query also returns general Roshan guides rather than a dedicated feature explainer. Two shared wiki URLs do not meet the three-URL rule. Keep the timer-versus-information distinction as a section of the existing maphack article; do not sell this as validated standalone cheat demand.",
        "evidence_needed": ["Distinguish a manually started timer from claimed object information", "Recheck any game timings against current primary sources before stating them", "Do not inherit product claims from a generic Roshan guide"],
    },
    "dota2-ward-tracker": {
        "publication_action": "include_as_section", "section_parent_id": "dota2-maphack", "priority": "P2",
        "article_target_query": "dota 2 ward tracker cheat",
        "serp_mismatch": "Even the cheat-qualified query mixes three practice-command results, product descriptions, a reseller and a repository. Ward Tracker appears on a vendor feature page, but standalone demand and volume are unconfirmed. Explain information source and display inside the existing maphack article; keep practice-command intent separate.",
        "evidence_needed": ["Treat advertised ward display as a vendor statement, not proven full hidden-map access", "Keep practice commands and third-party information features separate", "Revisit a standalone article only with a distinct reader job and stronger demand evidence"],
    },
}
maphack_url = "https://umbrella-dota.com/en/features/maphack/"
for c in study["clusters"]:
    if c["id"] in updates:
        c.update(updates[c["id"]])
    if c["id"] in {"dota2-roshan", "dota2-ward-tracker", "dota2-maphack"}:
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | {maphack_url})
    if c["id"] == "dota2-roshan":
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | {"https://dotasense.com/guides/roshan-timer", "https://dota2tool.vercel.app/"})
        c["intent_matched_urls"] = []
        c["usage_phrases"] = ["Roshan", "Roshan timer", "respawn window"]
        c["corpus_note"] = "Timer pages match the broad timer query, not the proposed ESP subsection. They belong to the general corpus, not intent_matched_sample. Use them to understand the competing reader job, not as evidence for third-party ESP claims."
    if c["id"] == "dota2-ward-tracker":
        c["intent_matched_urls"] = [maphack_url]
        c["usage_phrases"] = ["ward tracker", "enemy wards", "observer ward", "sentry ward"]
    if c["id"] == "deadlock-fov":
        c["competitor_urls"] = sorted(set(c["competitor_urls"]) | {"https://tsuki.gg/scripts/deadlock/aimed-fov"})
study.setdefault("page_types", {}).update({maphack_url: "product_feature_page", "https://dotasense.com/guides/roshan-timer": "gameplay_guide_with_timer_product", "https://dota2tool.vercel.app/": "manual_timer_tool", "https://tsuki.gg/scripts/deadlock/aimed-fov": "public_script_description"})
study.setdefault("source_policies", {}).update({
    maphack_url: {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True, "reviewed_at": "2026-09-21", "reason": "Page mixes feature labels with unverified hidden-information, safety and evasion claims plus setup instructions. Retain for on-page analysis; do not automatically feed these passages to the writer."},
    "https://dota2tool.vercel.app/": {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True, "reviewed_at": "2026-09-21", "reason": "Useful example of the manual-timer reader job, not an authoritative source for current game timings or third-party ESP functionality."},
    "https://dotasense.com/guides/roshan-timer": {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True, "reviewed_at": "2026-09-21", "reason": "Gameplay/timer page observed in broad timer SERP. It does not substantiate ESP or other third-party information features."},
})
validate_study(study)
save_json(directory / "study.json", study)
print({"updated_groups": list(updates), "keywords": len(study["keywords"])})
