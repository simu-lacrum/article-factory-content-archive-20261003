from __future__ import annotations

import itertools
import statistics
from collections import Counter
from urllib.parse import urlsplit

from .models import canonical_url, key, scope_for
from .pages import phrase_count, anchor_kind

STOP = set("a an the and or of to for in on at by with is are be as this that your you our we it its from not can will how what which when best free cheat cheats dota cs2 deadlock game games more all new use read click here com http https www".split())


def cohort(snapshot: dict) -> tuple:
    # Requested gl=US is not proof of an observed US search location.
    return tuple(snapshot.get(k) for k in ("game", "language", "engine", "country_observed", "country_requested", "method", "session_cohort")) + (snapshot["captured_at"][:10],)


def urls(snapshot: dict) -> set[str]:
    return {canonical_url(r["url"]) for r in snapshot.get("results", [])
            if r.get("type") in {"organic", "forum", "product", "article", "category", "comparison"}}


def serp_groups(snapshots: list[dict], minimum_overlap: int = 3) -> list[dict]:
    """Keep every qualifying pair; do not force a partition or merge through bridges."""
    groups: list[list[dict]] = []
    latest = {}
    for snapshot in sorted(snapshots, key=lambda s: s["captured_at"]):
        latest[(cohort(snapshot), key(snapshot["query"]))] = snapshot
    eligible = [(s, urls(s)) for s in sorted(latest.values(), key=lambda s: (s["game"], s["query"]))
                if s.get("grouping_eligible") is not False and s.get("method") != "web_search_unspecified"]
    eligible = [(s, u) for s, u in eligible if len(u) >= 5]
    paired = set()
    for (a, a_urls), (b, b_urls) in itertools.combinations(eligible, 2):
        if (cohort(a) == cohort(b) and scope_for(a["query"]) == scope_for(b["query"])
                and len(a_urls & b_urls) >= minimum_overlap):
            groups.append([a, b])
            paired.update((id(a), id(b)))
    groups.extend([s] for s, _ in eligible if id(s) not in paired)
    return [{"queries": [s["query"] for s in group], "game": group[0]["game"],
             "status": "serp_validated" if len(group) > 1 else "single_query_sample",
             "grouping_method": "pairwise_complete_link_no_forced_partition",
             "validation_scope": "shared_URL_threshold_only_not_intent_equivalence_or_publication_approval",
             "minimum_shared_urls": minimum_overlap, "cohort": list(cohort(group[0])),
             "pair_overlap": [{"a": a["query"], "b": b["query"], "shared": sorted(urls(a) & urls(b))}
                              for a, b in itertools.combinations(group, 2)]} for group in groups]


def distribution(values: list[int | float]) -> dict:
    if not values:
        return {"n": 0, "min": None, "median": None, "max": None, "q1": None, "q3": None}
    quartiles = statistics.quantiles(values, n=4, method="inclusive") if len(values) >= 4 else [None] * 3
    return {"n": len(values), "min": min(values), "median": statistics.median(values), "max": max(values),
            "q1": quartiles[0], "q3": quartiles[2]}


def term_profile(query: str, pages: list[dict]) -> dict:
    rows = []
    for page in pages:
        words = page["words"]
        count = phrase_count(page["text"], query)
        rows.append({"url": page["url"], "words": words, "body_exact": count,
                     "page_type": page.get("page_type", "unclassified"),
                     "exact_per_1000_words": round(count * 1000 / words, 3) if words else None,
                     "title_exact": phrase_count(page["title"], query),
                     "description_exact": phrase_count(page["description"], query),
                     "h1_exact": sum(phrase_count(h, query) for h in page.get("document_h1", [h["text"] for h in page["headings"] if h["level"] == 1])),
                     "h2_h3_exact": sum(phrase_count(h["text"], query) for h in page["headings"] if h["level"] in {2, 3}),
                     "intro_100_words_exact": phrase_count(" ".join(page["text"].split()[:100]), query),
                     "capture_notes": (["Short capture: verify whether this is a complete feature/card description or an incomplete page; length alone is not failure."] if words < 80 else []),
                     "extraction": page["extraction"]})
    return {"query": query, "pages": rows,
            "by_page_type": {kind: {"body_exact": distribution([r["body_exact"] for r in rows if r["page_type"] == kind]),
                                     "words": distribution([r["words"] for r in rows if r["page_type"] == kind])} for kind in sorted({r["page_type"] for r in rows})},
            "body_exact_distribution": distribution([r["body_exact"] for r in rows]),
            "words_distribution": distribution([r["words"] for r in rows]),
            "interpretation": "Observed usage in this sampled corpus, not a ranking factor or writing quota. Use by_page_type; the overall distribution may mix page types."}


def related_terms(pages: list[dict], limit: int = 45) -> list[dict]:
    sources: dict[str, list[str]] = {}
    for page in pages:
        tokens = key(page["text"]).split()
        phrases = set()
        for size in (1, 2, 3):
            for i in range(len(tokens) - size + 1):
                words = tokens[i:i + size]
                if words[0] in STOP or words[-1] in STOP or any(w.isdigit() or len(w) < 2 for w in words):
                    continue
                phrases.add(" ".join(words))
        for phrase in phrases:
            sources.setdefault(phrase, []).append(page["url"])
    return [{"term": term, "document_frequency": len(refs), "sources": refs,
             "status": "corpus_cooccurrence_requires_editorial_selection"}
            for term, refs in sorted(sources.items(), key=lambda item: (-len(item[1]), -len(item[0].split()), item[0]))
            if len(refs) >= 2][:limit]


def reviewed_term_profile(entries: list[dict], pages: list[dict]) -> list[dict]:
    """Check a human-selected vocabulary list; occurrence is not demand or truth."""
    result = []
    for entry in entries:
        allowed = {canonical_url(u) for u in entry.get('source_urls', [])}
        relevant_pages = [p for p in pages if not allowed or any(
            canonical_url(p.get(field) or p['url']) in allowed for field in ('url', 'requested_url', 'canonical'))]
        observations = [{"url": p["url"], "body_exact": phrase_count(p["text"], entry["term"]),
                         "page_type": p.get("page_type", "unclassified")}
                        for p in relevant_pages if phrase_count(p["text"], entry["term"]) > 0]
        result.append({**entry, "sources": [p["url"] for p in observations],
                       "document_frequency": len(observations), "observations": observations,
                       "origin": "reviewed_vocabulary_observed_in_sample" if observations else "editorial_concept_not_observed_in_sample",
                       "evidence_scope": "Occurrence in selected main text only; not search volume, a required phrase or a verified product capability. An optional reviewed source list limits ambiguous terms to the relevant context."})
    return result


def anchor_profile(pages: list[dict], query: str | None = None, brands: list[str] | None = None) -> dict:
    rows = [{"source_url": page["url"], **link} for page in pages for link in page["links"]]
    if query is not None:
        for row in rows:
            row["kind"] = anchor_kind(row["text"], row["url"], query, brands or [])
    groups = {}
    for placement in ("editorial", "navigation", "other"):
        for relationship in ("internal", "outbound"):
            matching = [r for r in rows if r["placement"] == placement and r["relationship"] == relationship]
            groups[f"{placement}_{relationship}"] = {"n": len(matching), "counts": dict(Counter(r["kind"] for r in matching))}
    return {"groups": groups, "examples": rows, "inbound_backlinks": None,
            "interpretation": "These are links ON sampled pages. Incoming backlink anchors need a backlink export. No optimal ratio is inferred."}


def page_type_evidence(snapshots: list[dict]) -> dict:
    samples = []
    for snapshot in snapshots:
        unique = {canonical_url(r["url"]): r for r in snapshot.get("results", []) if r.get("type") != "video"}
        counts = Counter(r.get("page_type", "unclassified") for r in unique.values())
        samples.append({"method": snapshot["method"], "captured_at": snapshot["captured_at"],
                        "country_requested": snapshot.get("country_requested"), "source_file": snapshot.get("source_file"),
                        "counts": dict(counts), "unique_nonvideo_results": len(unique)})
    types = Counter()
    for sample in samples:
        types.update(sample["counts"])
    return {"counts": dict(types), "sample_results": sum(types.values()),
            "samples": samples,
            "decision": "manual_review" if not types or "unclassified" in types else "observed_mix",
            "note": "Read each sample separately: the overall counts may repeat URLs across dates and providers. Mixed intents may require separate pages; a product SERP is not automatically an article target."}
