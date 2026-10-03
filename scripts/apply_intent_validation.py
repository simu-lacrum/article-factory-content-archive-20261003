"""Apply reviewed decisions from the retained 2026-09-21 Google samples.

This merges only named fields; it does not replace imported metrics or SERPs.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.service import read_json, save_json
from article_factory.research.models import validate_study

directory = Path(sys.argv[1])
study = read_json(directory / "study.json")
articles = ["https://cswatch.gg/blog/cs2-cheat-types-explained", "https://steamreport.net/blog/cs2-cheating-types-explained"]
changes = {
    "cs2-triggerbot": {
        "article_target_query": "triggerbot vs aimbot cs2",
        "intent_matched_urls": articles,
        "usage_phrases": ["triggerbot", "aimbot", "triggerbot vs aimbot"],
        "serp_mismatch": "The broad cs2 triggerbot sample is dominated by releases, repositories and video. The comparison query returned two explainers and two discussions plus video. Its search volume is unknown; do not transfer the broad query's 20 estimate. Four eligible results are insufficient for automatic overlap validation.",
        "evidence_needed": ["Confirm the CS2 publication domain", "Obtain volume for the comparison query itself", "Recheck attributed feature claims before publication"],
    },
    "dota2-scripts": {
        "article_target_query": "dota 2 scripts vs macros",
        "serp_mismatch": "Broad scripts results are primarily commercial catalogs/product pages. The comparison query includes discussions, an implementation thread, a macro catalog, videos and one unrelated-game result. Use a plain-language distinction in the existing article; do not claim that the comparison query has the broad query's 20 monthly searches. Forum opinions and AI Overview statements do not establish Valve policy.",
        "evidence_needed": ["Obtain volume for the comparison query itself", "Keep community-bot evidence explicitly historical", "Update the existing URL rather than making a duplicate generic scripts guide"],
    },
    "deadlock-auto-parry": {
        "article_target_query": "is there a parry cheat in deadlock",
        "serp_mismatch": "The parry question and deadlock auto parry cheat share three eligible URLs in the same browser cohort. This validates that two-query subset only. Update the existing CheatsGaming article with a direct answer and limits; one clip is not evidence of a particular player's software.",
        "evidence_needed": ["Verify any current vendor feature claim", "Do not present player allegations as established facts", "Check remaining modifiers individually before creating more pages"],
    },
}
for cluster in study["clusters"]:
    if cluster["id"] in changes:
        cluster.update(changes[cluster["id"]])
    if cluster["id"] == "cs2-triggerbot":
        cluster["competitor_urls"] = sorted(set(cluster["competitor_urls"]) | set(articles))
study.setdefault("source_policies", {}).update({
    articles[0]: {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True,
                  "reason": "Contains unsupported anti-cheat effectiveness/safety claims and overconfident behavioral detection statements. Analyze layout and wording, not product truth.", "reviewed_at": "2026-09-21"},
    articles[1]: {"role": "competitor_onpage_analysis_only", "exclude_from_fact_evidence": True,
                  "reason": "Commercial reporting-service article makes unsupported report-priority and ban-effectiveness claims. Analyze layout and wording, not product truth.", "reviewed_at": "2026-09-21"},
})
for url in articles:
    study.setdefault("page_types", {})[url] = "guide_or_article"
validate_study(study)
save_json(directory / "study.json", study)
print({"updated_groups": list(changes), "onpage_only_sources": articles})
