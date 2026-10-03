"""Readable editorial decisions and measured-demand overview for an existing study."""
import csv
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.service import read_json, save_json

directory = Path(sys.argv[1])
core = read_json(directory / "core.json")
lines = ["# Editorial plan: CS2, Dota 2, Deadlock", "", f"Primary market: US / Google; English. These are {len(core['clusters'])} editorial groups, not fully validated SERP clusters.",
         "Each outline is a brief, not a claim that every feature works as described. Research and publication gates remain in force.", "",
         "Known volumes below are Semrush estimates observed September 21, 2026: rolling monthly averages, with no measurement-window end disclosed. Do not add close variants to estimate unique demand."]
for c in core["clusters"]:
    measured = [k for k in c["keywords"] if k["volume"] is not None]
    lines += ["", f"## {c['title']}", "", f"- ID: {c['id']}", f"- Query family: `{c['primary_query']}`",
              f"- Action: {c['publication_action']}; intended site: {c.get('primary_site', 'pending')}",
              f"- Reader job: {c['reader_job']}", f"- Original contribution: {c['original_value']}"]
    if c.get("existing_url"):
        lines.append(f"- Existing URL to update: {c['existing_url']}")
    if c.get("section_parent_id"):
        lines.append(f"- Include as a section of: {c['section_parent_id']}; no separate page is scheduled.")
    if c.get("supporting_sections"):
        lines.append("- Include distinct supporting sections: " + "; ".join(section["id"] for section in c["supporting_sections"]))
    target = c["article_target"]
    lines.append(f"- Article target: `{target['query']}`; its own volume: {target['volume'] if target['volume'] is not None else 'unknown'}.")
    for subset in c.get("validated_query_subsets", []):
        lines.append("- Validated subset only (not the entire group): " + "; ".join(subset["queries"]))
    if measured:
        lines += [f"- Measured US query: `{k['query']}` — {k['volume']} / month ({k['frequency_band']}, provider estimate)." for k in measured]
    else:
        lines.append("- Search volume: unknown. Specific wording is not proof of low frequency.")
    lines += ["- Article/section candidate phrases: " + "; ".join(k["query"] for k in c["keywords"] if k["query"] != c["primary_query"] and k.get("query_role", "article_candidate") == "article_candidate"),
              "- Separate access/navigation/research phrases (not article keyword requirements): " + "; ".join(k["query"] for k in c["keywords"] if k.get("query_role", "article_candidate") != "article_candidate"),
              "- Editorial concepts: " + "; ".join(c.get("semantic_terms", [])),
              "- Reviewed vocabulary: " + "; ".join(t['term'] for t in c.get('reviewed_related_terms', [])), "", "Proposed structure:", ""]
    lines += [f"{i}. {heading}" for i, heading in enumerate(c["outline"], 1)]
    if c.get("serp_mismatch"):
        lines += ["", "Intent gate: " + c["serp_mismatch"]]
    if c.get("publication_gate"):
        lines += ["", "Publication gate: " + c["publication_gate"]]
    if c.get("reference_urls"):
        lines += ["", "Reference leads to verify before drafting:", ""]
        lines += ["- " + url for url in c["reference_urls"]]
(directory / "EDITORIAL_PLAN.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

vocabulary = ['# Reviewed semantic vocabulary', '',
    'English vocabulary selected for each reader job. The CSV retains source URLs and occurrence counts.',
    'This is the usable editorial list; raw corpus co-occurrences remain a separate research input.',
    'Observations cover the selected main text, not title/metadata. They are not proof of search volume or product capabilities. Unobserved concepts remain explicitly labeled. No term is a writing quota.',
    '', '[Source-by-source CSV](reviewed-semantic-terms.csv)']
for c in core['clusters']:
    vocabulary += ['', '## ' + c['title'], '', 'Group: `' + c['id'] + '`', '']
    for t in c.get('reviewed_related_terms', []):
        count = t['document_frequency']
        label = f"Observed in the selected text of {count} sampled {'page' if count == 1 else 'pages'}" if count else 'Editorial concept; exact phrase not observed in the selected main text'
        vocabulary.append(f"- **{t['term']}** — {t['usage_note']} {label}.")
(directory / 'SEMANTIC_VOCABULARY.md').write_text('\n'.join(vocabulary) + '\n', encoding='utf-8')

rows = core.get("backlink_sample") or []
summary = {"scope": "Selected provider sample; not a full profile or an acquisition target",
           "checked_at": max((r.get("checked_at", "") for r in rows), default=None), "links": len(rows),
           "target_hosts": sorted({urlsplit(r["target_url"]).netloc for r in rows}),
           "source_hosts": len({urlsplit(r["source_url"]).netloc for r in rows}),
           "provider_anchor_counts": dict(Counter(r["anchor_kind"] for r in rows)),
           "verification_counts": dict(Counter(r.get("verification", {}).get("status", "not_checked") for r in rows)),
           "verified_exact_text_counts": dict(Counter(r["anchor_kind"] for r in rows if r.get("verification", {}).get("status") == "target_and_anchor_found")),
           "limitations": ["Top rows are selection-biased; repeated domains do not imply independent recommendations.",
                           "Page Authority Scores and vendor safety claims are not independently validated.",
                           "A missing link in parsed HTML is not proof that the provider invented it or that it never existed.",
                           "Link ownership, payment and editorial independence are unknown.",
                           "A branded anchor can also contain a target phrase; the exclusive classifier gives the brand priority.",
                           "Naked URL refers to visible URL-shaped anchor text, which may differ from the target URL."]}
save_json(directory / "backlink-anchor-summary.json", summary)
with (directory / "backlink-anchor-analysis.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    fields = ["source_url", "target_url", "anchor", "anchor_kind", "rel", "provider", "checked_at", "verification_status"]
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    for r in rows:
        writer.writerow({f: r.get("verification", {}).get("status") if f == "verification_status" else r.get(f) for f in fields})
print({"editorial_groups": len(core["clusters"]), "measured_us_queries": core["coverage"]["keywords_with_volume"], "backlinks": summary})
