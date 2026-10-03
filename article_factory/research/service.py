from __future__ import annotations

import csv
import io
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from .analysis import anchor_profile, page_type_evidence, related_terms, reviewed_term_profile, serp_groups, term_profile
from .models import canonical_url, frequency_band, identity, key, scope_for, validate_metric, validate_study
from .pages import anchor_kind
from .pages import phrase_count


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save_json(path: Path, value: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def import_metrics(directory: Path, source: Path) -> dict:
    with source.open(encoding="utf-8-sig", newline="") as stream:
        rows = [validate_metric(dict(row)) for row in csv.DictReader(stream)]
    if not rows:
        raise ValueError("Metrics export is empty")
    save_json(directory / "metric-imports" / (identity(source.read_text(encoding="utf-8-sig")) + ".json"), rows)
    path = directory / "metrics.json"
    existing = read_json(path) if path.exists() else []
    def metric_id(row):
        return identity(*(str(row.get(k, "")) for k in ("query", "game", "language", "country", "engine", "provider", "period", "match_type")), row.get("period_basis", "provider_report_month"))
    ids = {metric_id(row): row for row in existing}
    for row in rows:
        row["imported_at"] = datetime.now(timezone.utc).isoformat()
        row["source_file"] = source.name
        ids[metric_id(row)] = row
    save_json(path, list(ids.values()))
    return {"imported": len(rows), "stored": len(ids), "path": str(path)}


def import_backlinks(directory: Path, source: Path) -> dict:
    study = read_json(directory / "study.json")
    with source.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    validated = {}
    for row in rows:
        if not all(row.get(field) for field in ("source_url", "target_url", "provider", "checked_at")):
            raise ValueError("Backlinks require source_url, target_url, provider and checked_at")
        from datetime import date
        date.fromisoformat(row["checked_at"][:10])
        source_url, target_url = canonical_url(row["source_url"]), canonical_url(row["target_url"])
        if urlsplit(source_url).netloc == urlsplit(target_url).netloc:
            continue  # Internal links do not become backlinks by importing them.
        text = row.get("anchor", "")
        row.update(source_url=source_url, target_url=target_url,
                   anchor_kind=anchor_kind(text, target_url, row.get("target_keyword", ""), study.get("brands", [])),
                   evidence_type="provider_export_not_independently_verified")
        validated[identity(source_url, target_url, text)] = row
    if not validated:
        raise ValueError("No external backlinks in export")
    save_json(directory / "backlink-imports" / (identity(source.read_text(encoding="utf-8-sig")) + ".json"), list(validated.values()))
    # The current file is one explicitly selected provider snapshot, never a guessed full web profile.
    save_json(directory / "backlinks.json", list(validated.values()))
    return {"backlinks": len(validated), "referring_domains": len({urlsplit(r["source_url"]).netloc for r in validated.values()}), "scope": "imported_provider_sample"}


def import_serps(directory: Path, source: Path) -> dict:
    payload = read_json(source)
    snapshots = payload.get("snapshots") if isinstance(payload, dict) else payload
    if not isinstance(snapshots, list) or not snapshots:
        raise ValueError("SERP import requires a nonempty snapshot list")
    study = read_json(directory / "study.json")
    merged = {}
    for snapshot in [*study.get("serps", []), *snapshots]:
        token = identity(*(str(snapshot.get(k, "")) for k in ("query", "game", "language", "engine", "country_requested", "country_observed", "method", "session_cohort", "captured_at")))
        merged[token] = snapshot
    updated = {**study, "serps": list(merged.values())}
    validate_study(updated)  # Validate all rows before writing either artifact.
    save_json(directory / "serp-imports" / (identity(source.read_text(encoding="utf-8-sig")) + ".json"), snapshots)
    save_json(directory / "study.json", updated)
    return {"imported": len(snapshots), "stored_snapshots": len(merged), "path": str(directory / "study.json")}


def choose_metric(keyword: dict, metrics: list[dict], study: dict) -> tuple[dict | None, list[dict]]:
    matching = [m for m in metrics if key(m["query"]) == key(keyword["query"])
                and m["game"] == keyword["game"] and m["language"] == keyword["language"]
                and m["country"] == study["market"]["country"] and m["engine"] == study["market"]["engine"]]
    policy = study.get("metric_policy", {})
    providers = policy.get("provider_order") or [policy.get("provider")]
    # An explicit source order can fill gaps; never average sources or blend periods.
    for provider in providers:
        eligible = [m for m in matching if m["provider"] == provider
                    and m["match_type"] == policy.get("match_type") and m["period"] == policy.get("period")
                    and m.get("period_basis", "provider_report_month") == policy.get("period_basis", "provider_report_month")]
        if eligible:
            return (eligible[0] if len(eligible) == 1 else None), matching
    return None, matching


def build_study(directory: Path) -> dict:
    study = read_json(directory / "study.json")
    validate_study(study)
    metrics = read_json(directory / "metrics.json") if (directory / "metrics.json").exists() else []
    metrics = [validate_metric(m) for m in metrics]
    pages = [read_json(p) for p in sorted((directory / "pages").glob("*.json"))]
    valid_pages = [p for p in pages if p.get("text", "").strip() and p.get("http_status") == 200 and p.get("words", 0) > 0]
    excluded_onpage_urls = {canonical_url(u) for u, policy in study.get("source_policies", {}).items()
                           if policy.get("exclude_from_onpage_analysis")}
    analyzable_pages = [p for p in valid_pages if not any(
        canonical_url(p.get(field) or p["url"]) in excluded_onpage_urls
        for field in ("url", "requested_url", "canonical"))]
    by_url = {}
    for page in analyzable_pages:
        path = urlsplit(page["url"]).path
        page["page_type"] = study.get("page_types", {}).get(page["url"],
            "guide_or_article" if "/blog/" in path or "/articles/" in path or "/mechanics/" in path else
            "comparison_overview" if "/information/" in path else
            "command_reference" if "Console_commands" in path or path == "/commands" else
            "guide_index" if path.rstrip("/") == "/guides" else "commercial_page_provisional")
        # Preserve redirect aliases, deduplicate actual pages inside each analysis.
        for url in (page["url"], page.get("requested_url", page["url"]), page.get("canonical", page["url"])):
            by_url[canonical_url(url)] = page
    low, mid = study.get("frequency_thresholds", {}).get("low_max", 100), study.get("frequency_thresholds", {}).get("mid_max", 1000)
    keywords = []
    for item in study["keywords"]:
        metric, candidates = choose_metric(item, metrics, study)
        snapshots = [s for s in study.get("serps", []) if key(s["query"]) == key(item["query"]) and s["game"] == item["game"] and s["language"] == item["language"]
                     and s["engine"] == study["market"]["engine"] and s.get("country_requested") == study["market"]["country"]
                     and s.get("country_observed") in {None, study["market"]["country"]}]
        keywords.append({**item, "id": identity(item["game"], item["language"], key(item["query"])),
                         "scope": item.get("scope", scope_for(item["query"])),
                         "volume": metric["volume"] if metric else None, "metric": metric,
                         "metric_candidates": candidates, "frequency_band": frequency_band(metric["volume"] if metric else None, low, mid),
                         "specificity": "long_tail_phrase" if len(key(item["query"]).split()) >= 4 else "head_or_mid_tail_phrase",
                         "serp_samples": len(snapshots), "page_type_evidence": page_type_evidence(snapshots)})
    groups = serp_groups(study.get("serps", []))
    clusters = []
    for cluster in study.get("clusters", []):
        members = [k for k in keywords if k.get("cluster_id") == cluster["id"] and k["game"] == cluster["game"]]
        refs = set(cluster.get("competitor_urls", [])) | {u for k in members for u in k.get("sources", [])}
        selected = {canonical_url(by_url[canonical_url(u)]["url"]): by_url[canonical_url(u)] for u in sorted(refs) if canonical_url(u) in by_url}
        corpus = [p for p in selected.values() if p.get("language", "en") == cluster.get("language", "en")
                  and urlsplit(canonical_url(p["url"])).netloc not in study.get("owned_domains", [])]
        matched_urls = {canonical_url(u) for u in cluster.get("intent_matched_urls", [])}
        matched_corpus = [p for p in corpus if any(canonical_url(p.get(field, p["url"])) in matched_urls
                                                 for field in ("url", "requested_url", "canonical"))]
        target_query = cluster.get("article_target_query", cluster["primary_query"])
        target = next((k for k in members if key(k["query"]) == key(target_query)), None)
        member_queries = {key(k["query"]) for k in members}
        validated_subsets = [{**g, "queries": [q for q in g["queries"] if key(q) in member_queries]}
                             for g in groups if g["status"] == "serp_validated" and g["game"] == cluster["game"]
                             and g["cohort"][1] == cluster.get("language", "en")
                             and g["cohort"][2] == study["market"]["engine"]
                             and g["cohort"][4] == study["market"]["country"]
                             and g["cohort"][3] in {None, study["market"]["country"]}
                             and len({key(q) for q in g["queries"]} & member_queries) >= 2]
        measured = sum(k["volume"] is not None for k in members)
        usage_phrases = list(dict.fromkeys([cluster["primary_query"], target_query, *cluster.get("usage_phrases", [])]))
        clusters.append({**cluster, "keywords": members, "grouping_basis": cluster.get("grouping_basis", "editorial_hypothesis"),
                         "measured_query_count": measured,
                         "research_state": "partial_serp_validation" if validated_subsets else "partial_provider_metrics_serp_grouping_still_unvalidated" if measured else "unvalidated",
                         "validated_query_subsets": validated_subsets,
                         "article_target": {"query": target_query, "volume": target["volume"] if target else None,
                                            "metric": target["metric"] if target else None,
                                            "frequency_band": target["frequency_band"] if target else "unknown",
                                            "page_type_evidence": target["page_type_evidence"] if target else None},
                         "sampled_pages": len(corpus), "term_usage": term_profile(cluster["primary_query"], corpus),
                         "intent_matched_term_usage": [term_profile(q, matched_corpus) for q in usage_phrases],
                         "reviewed_related_terms": reviewed_term_profile(cluster.get("reviewed_semantic_terms", []), corpus),
                         "corpus_related_terms": related_terms(corpus), "anchors": anchor_profile(corpus, cluster["primary_query"], study.get("brands", [])),
                         "publication_gate": cluster.get("publication_gate", "requires_original_content_and_editorial_review")})
    for cluster in clusters:
        cluster["supporting_sections"] = [{k: child.get(k) for k in (
            "id", "title", "reader_job", "original_value", "article_target", "outline", "semantic_terms", "reviewed_related_terms", "evidence_terms", "competitor_urls", "serp_mismatch"
        )} for child in clusters if child.get("section_parent_id") == cluster["id"]]
    result = {"schema_version": 1, "study_id": study["id"], "captured_at": study["captured_at"],
              "market": study["market"], "metric_policy": study.get("metric_policy", {}),
              "frequency_thresholds": {"low_max": low, "mid_max": mid, "status": "project_convention_not_industry_standard"},
              "keywords": keywords, "clusters": clusters, "serp_groups": groups,
              "source_policies": study.get("source_policies", {}),
              "serp_cohorts": [{k: s.get(k) for k in ("query", "game", "engine", "method", "country_requested", "country_observed", "source_file")} for s in study.get("serps", [])],
              "coverage": {"keywords": len(keywords), "observed_keywords": sum(k["discovery"] == "observed" for k in keywords),
                           "keywords_with_volume": sum(k["volume"] is not None for k in keywords), "serp_snapshots": len(study.get("serps", [])),
                           "pages_fetched": len(valid_pages), "page_failures": len(pages) - len(valid_pages), "clusters": len(clusters)},
              "limitations": study.get("limitations", [])}
    result["coverage"]["unique_fetched_pages"] = len({canonical_url(p["url"]) for p in valid_pages})
    result["coverage"]["short_captures_requiring_context_review"] = sum(p["words"] < 80 for p in valid_pages)
    result["coverage"]["pages_excluded_from_onpage_analysis"] = len(valid_pages) - len(analyzable_pages)
    result["coverage"]["english_competitor_pages"] = len({canonical_url(p["url"]) for p in analyzable_pages if p.get("language") == "en" and urlsplit(canonical_url(p["url"])).netloc not in study.get("owned_domains", [])})
    result["backlink_sample"] = read_json(directory / "backlinks.json") if (directory / "backlinks.json").exists() else None
    # Keep selected public-page observations separate from a provider's index sample.
    result["public_backlink_sample"] = read_json(directory / "public-backlink-sample.json") if (directory / "public-backlink-sample.json").exists() else None
    result["public_backlink_summary"] = read_json(directory / "public-backlink-summary.json") if (directory / "public-backlink-summary.json").exists() else None
    result["coverage"]["missing_volume_by_country"] = export_metric_requests(directory, study, metrics)
    save_json(directory / "core.json", result)
    export_files(directory, result)
    return result


def safe_cell(value: object) -> object:
    return "'" + value if isinstance(value, str) and value.startswith(("=", "+", "-", "@")) else value


def export_metric_requests(directory: Path, study: dict, metrics: list[dict]) -> dict:
    """Provider-ready query lists, kept separate from importable metric evidence."""
    countries = list(dict.fromkeys(filter(None, [study["market"]["country"], study["market"].get("secondary_market")])))
    clusters = {c["id"]: c for c in study.get("clusters", [])}
    rows, counts = [], {}
    lists = directory / "keyword-lists"
    lists.mkdir(exist_ok=True)
    for country in countries:
        market_study = {**study, "market": {**study["market"], "country": country}}
        missing = [k for k in study["keywords"] if (choose_metric(k, metrics, market_study)[0] or {}).get("volume") is None]
        counts[country] = len(missing)
        for game in ("cs2", "dota2", "deadlock"):
            queries = [k["query"] for k in missing if k["game"] == game]
            (lists / f"{game}-{country.lower()}-missing-volume.txt").write_text("\n".join(queries) + ("\n" if queries else ""), encoding="utf-8")
        for keyword in missing:
            cluster = clusters[keyword["cluster_id"]]
            rows.append({"country": country, "engine": study["market"]["engine"], "language": keyword["language"],
                         "game": keyword["game"], "query": keyword["query"], "cluster_id": keyword["cluster_id"],
                         "publication_action": cluster.get("publication_action"), "section_parent_id": cluster.get("section_parent_id"),
                         "is_article_target": key(keyword["query"]) == key(cluster.get("article_target_query", cluster["primary_query"])),
                         "reason": "No numeric volume in the explicitly selected provider/period/match cohort"})
    fields = ["country", "engine", "language", "game", "query", "cluster_id", "publication_action", "section_parent_id", "is_article_target", "reason"]
    with (directory / "metric-requests.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: safe_cell(v) for k, v in row.items()} for row in rows)
    return counts


def export_files(directory: Path, core: dict) -> None:
    for game in ("cs2", "dota2", "deadlock"):
        rows = [k for k in core["keywords"] if k["game"] == game]
        stream = io.StringIO(newline="")
        fields = ["query", "language", "cluster_id", "intent", "query_role", "recommended_page_type", "search_facets", "scope", "discovery", "discovery_note", "volume", "frequency_band",
                  "country", "engine", "provider", "period", "period_basis", "match_type", "volume_basis", "metric_source_url",
                  "specificity", "serp_samples", "sources"]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            metric = row.get("metric") or {}
            exported = {**row, **{field: metric.get(field) for field in ("provider", "period", "period_basis", "match_type", "volume_basis")},
                        "country": core["market"]["country"], "engine": core["market"]["engine"],
                        "metric_source_url": metric.get("source_url")}
            writer.writerow({field: safe_cell(" | ".join(exported[field]) if isinstance(exported.get(field), list) else exported.get(field)) for field in fields})
        (directory / f"{game}-core.csv").write_text(stream.getvalue(), encoding="utf-8-sig")
        save_json(directory / f"{game}-core.json", {"market": core["market"], "keywords": rows,
                                                    "clusters": [c for c in core["clusters"] if c["game"] == game]})
    for name, fields, rows in (
        ("query-routing.csv", ["game", "query", "cluster_id", "query_role", "recommended_page_type", "search_facets", "discovery", "discovery_note", "sources"],
         [{**k, "search_facets": " | ".join(k.get("search_facets", [])), "sources": " | ".join(k.get("sources", []))} for k in core["keywords"]]),
        ("anchor-examples.csv", ["cluster_id", "source_url", "url", "text", "kind", "placement", "relationship"],
         [{"cluster_id": c["id"], **r} for c in core["clusters"] for r in c["anchors"]["examples"]]),
        ("semantic-terms.csv", ["cluster_id", "term", "origin", "document_frequency", "sources"],
         [{"cluster_id": c["id"], "term": t, "origin": "editorial_entity_or_concept", "document_frequency": None, "sources": ""} for c in core["clusters"] for t in c.get("semantic_terms", [])]
         + [{"cluster_id": c["id"], **t, "origin": "observed_corpus_cooccurrence", "sources": " | ".join(t["sources"])} for c in core["clusters"] for t in c["corpus_related_terms"]]),
        ("reviewed-semantic-terms.csv", ["cluster_id", "term", "usage_note", "origin", "document_frequency", "sources", "evidence_scope"],
         [{"cluster_id": c["id"], **t, "sources": " | ".join(t["sources"])} for c in core["clusters"] for t in c["reviewed_related_terms"]]),
        ("keyword-usage.csv", ["cluster_id", "corpus", "query", "url", "page_type", "words", "body_exact", "title_exact", "description_exact", "h1_exact", "h2_h3_exact", "intro_100_words_exact", "extraction"],
         [{"cluster_id": c["id"], "corpus": corpus, "query": profile["query"], **page}
          for c in core["clusters"] for corpus, profiles in (("general_competitor_sample", [c["term_usage"]]), ("intent_matched_sample", c["intent_matched_term_usage"]))
          for profile in profiles for page in profile["pages"]]),
    ):
        with (directory / name).open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows({k: safe_cell(v) for k, v in row.items()} for row in rows)
    lines = ["# SEO research evidence", "", f"Study: {core['study_id']}; captured: {core['captured_at']}", "",
             "## Coverage", ""] + [f"- {k}: {v}" for k, v in core["coverage"].items()]
    lines += ["", "## Limits", "", "- Missing volume is unknown, not zero; phrase length does not establish low frequency.",
              "- Term counts describe the sampled pages. They do not establish ideal keyword density.",
              "- Page links are not an incoming backlink profile. Do not infer anchor ratios for link acquisition.",
              "- Related terms are corpus co-occurrences, not a Google LSI keyword list."]
    lines += [f"- {note}" for note in core["limitations"]]
    for cluster in core["clusters"]:
        lines += ["", f"## {cluster['game']}: {cluster['title']}", "", f"- Primary query: {cluster['primary_query']}",
                  f"- Publication action: {cluster.get('publication_action', 'manual_review')}; section parent: {cluster.get('section_parent_id') or 'none'}",
                  f"- Article/section target: {cluster['article_target']['query']}; own volume: {cluster['article_target']['volume'] if cluster['article_target']['volume'] is not None else 'unknown'}",
                  f"- Grouping: {cluster['grouping_basis']}", f"- Reader job: {cluster.get('reader_job', '')}",
                  f"- Page type: {cluster.get('page_type', 'manual_review')}", f"- Original value: {cluster.get('original_value', '')}",
                  f"- Sampled competitor pages: {cluster['sampled_pages']}",
                  "- Article candidate queries: " + "; ".join(k["query"] for k in cluster["keywords"] if k.get("query_role", "article_candidate") == "article_candidate"),
                  "- Separate access/navigation/research queries: " + "; ".join(k["query"] for k in cluster["keywords"] if k.get("query_role", "article_candidate") != "article_candidate"),
                  "- Editorial semantic terms: " + "; ".join(cluster.get("semantic_terms", [])),
                  "- Reviewed relevant vocabulary: " + "; ".join(t["term"] for t in cluster["reviewed_related_terms"]),
                  "- Corpus terms (review before use): " + "; ".join(t["term"] for t in cluster["corpus_related_terms"][:15]),
                  "- Links: " + "; ".join(cluster.get("anchor_guidance", []))]
        lines += ["", "Observed primary-keyphrase use:", ""]
        for page in cluster["term_usage"]["pages"]:
            lines.append(f"- {page['url']}: {page['words']} words; exact phrase body {page['body_exact']}, title {page['title_exact']}, H1 {page['h1_exact']}, H2/H3 {page['h2_h3_exact']}. Extraction: {page['extraction']}.")
    (directory / "RESEARCH.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def active_core(root: Path) -> dict | None:
    config_path = root / "config" / "research.json"
    if not config_path.exists():
        return None
    config = read_json(config_path)
    study_path = (root / config["active_study"]).resolve()
    if not study_path.is_relative_to(root.resolve()):
        raise ValueError("active_study must be inside the workspace")
    return read_json(study_path / "core.json")


def writing_contract(root: Path, topic: dict) -> dict | None:
    if topic.get("source_kind") != "seo_research":
        return None
    core = active_core(root)
    if not core:
        raise ValueError("Research topic selected but active research is unavailable")
    cluster = next((c for c in core["clusters"] if c["id"] == topic["source_ref"]), None)
    if not cluster:
        raise ValueError("Research topic no longer exists in the active study; rebuild topics")
    # Exclude bulky raw link inventories from the prompt, preserve them in the study.
    return {"study_id": core["study_id"], "captured_at": core["captured_at"], "market": core["market"],
            "source_policies": core.get("source_policies", {}),
            **{k: v for k, v in cluster.items() if k not in {"anchors", "corpus_related_terms"}},
            "keywords": [k for k in cluster["keywords"] if k.get("query_role", "article_candidate") == "article_candidate"],
            "non_article_queries": [k for k in cluster["keywords"] if k.get("query_role", "article_candidate") != "article_candidate"],
            "related_terms": cluster.get("reviewed_related_terms", []),
            "anchor_summary": cluster["anchors"]["groups"],
            "rules": ["Answer the reader job before background. Match the page type.",
                      "Use short concrete examples and explain tradeoffs. Remove repeated conclusions and filler.",
                      "No invented testing, quotations, user experiences, rankings, prices or safety promises.",
                      "Exact phrase use is descriptive evidence, never a density target. Use variants when natural.",
                      "Related terms are reviewed vocabulary with usage notes and observed-source labels. Unobserved concepts are not competitor evidence; no term is mandatory. Raw co-occurrence output is not a writing checklist.",
                      "Original value must be delivered, not merely promised. Do not clone a rival outline.",
                      "Supporting sections belong inside this page; do not duplicate their entire outline or FAQ as separate articles.",
                      "non_article_queries are routing context, not phrases to insert into this article. A download/free access request needs an actual verified offer; do not relabel a paid offer as free.",
                      "Vendor comparisons need a dated source for each cell/claim and a visible commercial disclosure.",
                      "For third-party cheat topics, use high-level terminology and evaluation only; no operational evasion or cheat implementation. Legitimate practice/custom-lobby references may include verified built-in command syntax within the stated supported context.",
                      "A direct answer should stand alone and identify entities clearly; no mandatory chunk size or llms.txt."]}


def research_evidence(root: Path, topic: dict, limit: int = 8) -> list[dict]:
    contract = writing_contract(root, topic)
    if contract is None:
        return []
    config = read_json(root / "config" / "research.json")
    directory = root / config["active_study"]
    target_urls = {canonical_url(u) for u in contract.get("competitor_urls", [])}
    target_urls.update(canonical_url(u) for section in contract.get("supporting_sections", []) for u in section.get("competitor_urls", []))
    excluded_urls = {canonical_url(u) for u, policy in contract.get("source_policies", {}).items()
                     if policy.get("exclude_from_fact_evidence")}
    product = "melonity.gg" if topic["game"] == "dota2" else "cluster.center"
    focus = re.sub(r"\b(?:cs2|dota 2|deadlock)\b", "", contract["primary_query"], flags=re.I).strip()
    focus_terms = [focus, *contract.get("evidence_terms", [])]
    if "souls" in focus:
        focus_terms += [focus.replace("souls", "soul"), "soul triggerbot", "soul orb"]
    candidates = []
    for folder in ("pages", "owned-pages"):
        for path in sorted((directory / folder).glob("*.json")):
            page = read_json(path)
            if page.get("http_status") != 200 or page.get("language", "en") != topic["language"]:
                continue
            requested = canonical_url(page.get("requested_url", page["url"]))
            if any(canonical_url(page.get(field, page["url"])) in excluded_urls for field in ("url", "requested_url", "canonical")):
                continue
            is_product = urlsplit(requested).netloc == product
            page_aliases = {canonical_url(page.get(field, page["url"])) for field in ("url", "requested_url", "canonical")}
            if not page_aliases & target_urls and not is_product:
                continue
            if is_product and topic["game"] == "cs2" and "deadlock" in requested:
                continue
            section_terms = [term for section in contract.get("supporting_sections", [])
                             if page_aliases & {canonical_url(u) for u in section.get("competitor_urls", [])}
                             for term in (section.get("evidence_terms") or [])]
            page_focus_terms = list(dict.fromkeys([*focus_terms, *section_terms]))
            terms = contract.get("semantic_terms", [])
            focus_score = sum(phrase_count(page["text"], term) for term in page_focus_terms)
            score = 10 * focus_score + sum(phrase_count(page["text"], term) for term in terms)
            if not focus_score and not is_product:
                continue
            words = page["text"].split()
            # HTML often has no sentence punctuation between cards: select windows around
            # the actual feature, rather than returning the first 220 words of a huge block.
            windows, used = [], set()
            for index in range(len(words)):
                if any(phrase_count(" ".join(words[index:index + len(term.split()) + 1]), term) for term in page_focus_terms):
                    start, end = max(0, index - 15), min(len(words), index + 55)
                    if not any(i in used for i in range(start, end)):
                        windows.append(" ".join(words[start:end]))
                        used.update(range(start, end))
                    if len(windows) == 3:
                        break
            excerpt = " […] ".join(windows) if windows else " ".join(words[:120])
            candidates.append((score + (100 if is_product else 0), {"source": page["url"], "heading": page["title"],
                "excerpt": excerpt, "captured_at": page["captured_at"], "capture_file": str(path.relative_to(root)),
                "evidence_type": "publisher_statement_not_independent_test", "extraction": page["extraction"]}))
    seen, selected = set(), []
    for _, item in sorted(candidates, key=lambda pair: pair[0], reverse=True):
        url = canonical_url(item["source"])
        if url not in seen:
            selected.append(item)
            seen.add(url)
        if len(selected) >= limit:
            break
    supplement = directory / "supplemental-evidence.json"
    if supplement.exists():
        selected.extend({k: v for k, v in item.items() if k != "cluster_ids"} for item in read_json(supplement)
                        if topic["source_ref"] in item.get("cluster_ids", []) and canonical_url(item["source"]) not in seen | excluded_urls)
    return selected
