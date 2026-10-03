"""Reviewed Dota automation intent decisions; keep hypotheses distinct from demand."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.service import read_json, save_json
from article_factory.research.models import validate_study

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
invoker = "https://umbrella-dota.com/en/scripts/invoker/"
meepo = "https://umbrella-dota.com/en/scripts/meepo/"
dodger = "https://umbrella-dota.com/en/features/dodger/"
ciro = "https://www.ciroscript.com/dota"
updates = {
    "dota2-invoker": {
        "publication_action": "include_as_section", "section_parent_id": "dota2-scripts", "priority": "P2",
        "article_target_query": "invoker scripts vs hotkeys",
        "serp_mismatch": "Broad Invoker scripts results largely concern code, macros and software. The hotkey comparison also returns ordinary control discussions and legacy guides. Only one URL overlaps (a script tutorial excluded from editorial grouping). Use Invoker as a concrete boundary example in the existing scripts article; this is an editorial consolidation, not a validated synonym merge.",
        "outline": ["Keyboard layout is not an automation specification", "Separate repeating inputs from selecting actions", "Unknown performance and current feature coverage stay unknown"],
        "intent_matched_urls": [], "usage_phrases": ["Invoker", "scripts", "hotkeys"],
        "corpus_note": "Umbrella's hero page is a result for the broad query, not the narrower comparison. Its six-section hero template and numerical claims are not independent evidence of demand or accuracy."
    },
    "dota2-meepo": {
        "publication_action": "include_as_section", "section_parent_id": "dota2-scripts", "priority": "P2",
        "article_target_query": "meepo scripts vs control groups",
        "serp_mismatch": "The broad query mixes a code file, macro download, vendor hero page, community guide, discussion and video. The comparison query mostly concerns ordinary unit control. There are no shared URLs. Keep a short example explaining selection versus automated action in the existing scripts article; do not promise a full Meepo micro guide.",
        "outline": ["Which units receive an input?", "Selecting units and choosing their actions are different jobs", "Do not infer scripting from fast-looking play"],
        "intent_matched_urls": [], "usage_phrases": ["Meepo", "scripts", "control groups"],
        "corpus_note": "The fetched vendor hero page belongs to the broad software query, not the ordinary control-guide comparison corpus. No current in-game timing or combo instruction is inferred."
    },
    "dota2-auto-last-hit": {
        "publication_action": "include_as_section", "section_parent_id": "dota2-scripts", "priority": "P2",
        "article_target_query": "dota 2 last hit script",
        "title": "Last-hit trainers, macros and automation: different jobs",
        "reader_job": "Distinguish practising attack timing from repeating inputs or claiming to automate it.",
        "original_value": "Compare what the player still decides in a practice tool, fixed-input macro and advertised automation feature.",
        "serp_mismatch": "Auto last hit mostly returns manual practice guides and discussions. Adding script brings a code file, macro-help thread, script catalog and product alongside training tools. Only a Dotafire guide discussion and Hake product discussion overlap: two URLs, below the merge threshold. Explain the distinctions as a section of the existing scripts article; standalone demand is unknown.",
        "outline": ["A trainer measures or practises the player's timing", "A macro repeats inputs", "Automation claims need a stated decision and evidence"],
        "intent_matched_urls": ["https://umbrella-dota.com/en/scripts/", "https://uc.zone/en/dota2"],
        "usage_phrases": ["last hit", "last hitting", "auto deny"],
        "corpus_note": "The intent-matched subset contains broad catalog/product pages, not dedicated editorial last-hit explanations. Read page types before comparing usage."
    },
    "dota2-auto-dodge": {
        "publication_role": "Supporting feature explanation linked to the Dota product/feature hub; no download or implementation tutorial.",
        "serp_mismatch": "The auto dodge sample contains three product/feature pages, one discussion and five videos. This supports the automation topic, but does not establish informational demand or a validated group of all dodge variants. Keep the planned explainer focused on how to read a coverage claim, and treat media demonstrations as claims rather than independent efficacy tests.",
        "intent_matched_urls": [dodger, "https://uc.zone/en/dota2", ciro],
        "usage_phrases": ["auto dodge", "dodger", "skillshot"],
        "corpus_note": "Feature page, product landing and reseller catalog are different formats. Their word counts and keyword frequencies are observations, not a target for the explainer."
    }
}
for c in study["clusters"]:
    if c["id"] in updates:
        c.update(updates[c["id"]])
    extra = {"dota2-invoker": [invoker], "dota2-meepo": [meepo], "dota2-auto-dodge": [dodger, ciro]}.get(c["id"], [])
    c["competitor_urls"] = sorted(set(c["competitor_urls"]) | set(extra))
    if c["id"] in updates:
        c["evidence_needed"] = ["Use first-party descriptions for any concrete current capability; vendor publication is not independent verification", "Keep ordinary game controls, training tools and third-party automation distinct", "No code, implementation, anti-cheat evasion or cheat configuration steps", "Obtain real keyword metrics before labeling the query low-frequency or scheduling by demand"]
    if c["id"] == "dota2-scripts":
        heading = "Three concrete cases: Invoker hotkeys, Meepo control groups and last-hit trainers"
        if heading not in c["outline"]:
            c["outline"].insert(-1, heading)
study.setdefault("page_types", {}).update({invoker: "hero_product_guide", meepo: "hero_product_guide", dodger: "product_feature_page", ciro: "reseller_product_catalog"})
for url in [invoker, meepo, dodger, ciro]:
    study.setdefault("source_policies", {})[url] = {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True,
        "reviewed_at": "2026-09-21", "reason": "Retain for search intent and keyword usage only. Hero pages reuse a template and include unverified numerical game statistics; the feature page includes unverified reaction/effectiveness/safety claims and setup instructions. Do not import these as article facts."}
validate_study(study)
save_json(directory / "study.json", study)
supplement = read_json(directory / "supplemental-evidence.json")
source = "https://steamcommunity.com/sharedfiles/filedetails/?id=531587903"
if not any(x["source"] == source for x in supplement):
    supplement.append({"cluster_ids": ["dota2-scripts", "dota2-auto-last-hit"], "source": source,
        "heading": "Last Hit Exercises: author's Workshop description", "excerpt": "The Workshop listing labels Last Hit Exercises a custom game. The author describes practising last hitting and tracking missed hits in a controlled environment. This is an example of a training task, not a product claim that it plays for the user.",
        "captured_at": "2026-09-21", "collection_method": "web_tool_page_open", "evidence_type": "historical_first_party_workshop_description",
        "limitation": "The listing shows a 2017 update date. Current compatibility, availability and operation were not tested. Generic hidden Steam notices in parsed HTML were not treated as a verified removed-item state."})
save_json(directory / "supplemental-evidence.json", supplement)
print({"updated_groups": list(updates), "sections_added": 3, "keyword_count_unchanged": len(study["keywords"])})
