from __future__ import annotations

import hashlib
import re
from datetime import date
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

GAMES = {"cs2", "dota2", "deadlock"}
QUERY_ROLES = {"article_candidate", "product_access", "community_research", "implementation_research", "ambiguous_research"}
TRACKING = {"gclid", "fbclid", "ref", "referrer"}


def key(value: str) -> str:
    return " ".join(re.findall(r"[\w]+", value.casefold()))


def identity(*values: str) -> str:
    return hashlib.sha256("\0".join(values).encode()).hexdigest()[:20]


def canonical_url(value: str) -> str:
    parts = urlsplit(value)
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise ValueError(f"Expected a public HTTP URL: {value}")
    host = parts.hostname.lower().removeprefix("www.")
    port = parts.port
    if port and port not in {80, 443}:
        host += f":{port}"
    query = sorted((k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
                   if not k.lower().startswith("utm_") and k.lower() not in TRACKING)
    return urlunsplit(("https", host, parts.path.rstrip("/") or "/", urlencode(query), ""))


def scope_for(query: str) -> str:
    text = key(query)
    if "planetary conquest" in text:
        return "unrelated_game"
    if re.search(r"\b(console|sv cheats|cheat codes|cheat commands|lobby commands|console commands|practice commands)\b", text):
        return "legitimate_commands"
    if re.search(r"\b(bypass|evade|spoofer|injector|source code|cheat tutorial)\b", text):
        return "restricted_operational"
    return "third_party_software"


def validate_extraction_rule(rule: dict) -> None:
    if not isinstance(rule, dict) or not isinstance(rule.get("content_selector"), str) or not rule["content_selector"].strip():
        raise ValueError("Extraction rule requires a nonempty content_selector")
    count = rule.get("expected_matches", 1)
    if type(count) is not int or count < 1:
        raise ValueError("Extraction expected_matches must be a positive integer")


def validate_study(study: dict) -> None:
    if study.get("schema_version") != 1:
        raise ValueError("Unsupported research schema_version; expected 1")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,79}", study.get("id", "")):
        raise ValueError("Study id must be a lowercase slug")
    date.fromisoformat(study["captured_at"][:10])
    market = study.get("market", {})
    if not re.fullmatch(r"[A-Z]{2}", market.get("country", "")) or not market.get("engine"):
        raise ValueError("Study market requires a two-letter country and engine")
    cluster_ids = [c["id"] for c in study.get("clusters", [])]
    if len(cluster_ids) != len(set(cluster_ids)):
        raise ValueError("Duplicate cluster ids")
    seen = set()
    for item in study.get("keywords", []):
        if item.get("game") not in GAMES or not item.get("language") or not item.get("query"):
            raise ValueError("Keyword requires game, language and query")
        token = (item["game"], item["language"], key(item["query"]))
        if token in seen:
            raise ValueError(f"Duplicate keyword: {token}")
        seen.add(token)
        if item.get("query_role", "article_candidate") not in QUERY_ROLES:
            raise ValueError("Unknown query_role")
        if item.get("discovery") not in {"observed", "editorial_expansion"}:
            raise ValueError("Label keyword discovery as observed or editorial_expansion")
        if item["discovery"] == "observed" and not item.get("sources"):
            raise ValueError("Observed keywords require source references")
        if item.get("cluster_id") not in cluster_ids:
            raise ValueError(f"Keyword refers to missing cluster: {item.get('cluster_id')}")
        for source in item.get("sources", []):
            canonical_url(source)
    for snapshot in study.get("serps", []):
        for required in ("query", "game", "language", "engine", "captured_at", "method"):
            if not snapshot.get(required):
                raise ValueError(f"SERP requires {required}")
        date.fromisoformat(snapshot["captured_at"][:10])
        for result in snapshot.get("results", []):
            canonical_url(result["url"])
            rank = result.get("rank")
            if rank is not None and (isinstance(rank, bool) or not isinstance(rank, int) or rank < 1):
                raise ValueError("Rank must be a positive integer or null")
            if rank is not None and snapshot["method"] == "web_search_unspecified":
                raise ValueError("Web search tool result order is not a Google organic rank")
    for cluster in study.get("clusters", []):
        reviewed = cluster.get("reviewed_semantic_terms", [])
        if not isinstance(reviewed, list) or any(not isinstance(t, dict) or not isinstance(t.get("term"), str)
            or not key(t["term"]) or not isinstance(t.get("usage_note"), str) or not t["usage_note"].strip() for t in reviewed):
            raise ValueError("reviewed_semantic_terms requires term and usage_note for each entry")
        if len({key(t["term"]) for t in reviewed}) != len(reviewed):
            raise ValueError("Duplicate reviewed semantic term")
        for term in reviewed:
            if not isinstance(term.get('source_urls', []), list):
                raise ValueError('Reviewed term source_urls must be a list')
            for url in term.get('source_urls', []):
                canonical_url(url)
        if not isinstance(cluster.get("evidence_terms", []), list) or any(not isinstance(t, str) or not t.strip() for t in cluster.get("evidence_terms", [])):
            raise ValueError("evidence_terms must be a list of nonempty reviewed phrases")
        target_query = key(cluster.get("article_target_query", cluster.get("primary_query", "")))
        target = next((k for k in study.get("keywords", []) if k["cluster_id"] == cluster["id"] and key(k["query"]) == target_query), None)
        if cluster.get("publication_action") in {"write_article", "update_article"} and target and target.get("query_role", "article_candidate") != "article_candidate":
            raise ValueError("An article target must be an article_candidate; keep acquisition/navigation/implementation research separate")
        if cluster.get("publication_action") == "update_article" and not cluster.get("existing_url"):
            raise ValueError("update_article requires an existing_url")
        if cluster.get("existing_url"):
            canonical_url(cluster["existing_url"])
        parent_id = cluster.get("section_parent_id")
        if cluster.get("publication_action") == "include_as_section" or parent_id:
            parent = next((c for c in study.get("clusters", []) if c["id"] == parent_id), None)
            if (not parent or parent["id"] == cluster["id"] or parent.get("section_parent_id")
                or parent["game"] != cluster["game"] or parent.get("language", "en") != cluster.get("language", "en")
                or parent.get("publication_action") not in {"write_article", "update_article", "update_hub"}
                or cluster.get("publication_action") != "include_as_section"):
                raise ValueError("A section must name a standalone parent in the same game and language")
        if cluster.get("article_target_query") and not any(
            k["cluster_id"] == cluster["id"] and k["game"] == cluster["game"]
            and k["language"] == cluster.get("language", "en")
            and key(k["query"]) == key(cluster["article_target_query"]) for k in study.get("keywords", [])
        ):
            raise ValueError("article_target_query must be an explicit member of its editorial group")
    for url in study.get("source_policies", {}):
        canonical_url(url)
    for url, rule in study.get("extraction_rules", {}).items():
        canonical_url(url)
        validate_extraction_rule(rule)


def validate_metric(row: dict) -> dict:
    """Provider exports must state a market, month and match semantics."""
    required = ("query", "game", "language", "country", "engine", "provider", "period", "match_type")
    if any(not str(row.get(field, "")).strip() for field in required):
        raise ValueError("Metric requires " + ", ".join(required))
    if row["game"] not in GAMES or not re.fullmatch(r"\d{4}-\d{2}", row["period"]):
        raise ValueError("Invalid metric game or period (YYYY-MM)")
    date.fromisoformat(row["period"] + "-01")
    if row["match_type"] not in {"exact", "phrase", "broad", "provider_grouped", "provider_unspecified"}:
        raise ValueError("Unknown match_type")
    if row.get("period_basis", "provider_report_month") not in {"provider_report_month", "capture_month"}:
        raise ValueError("Unknown period_basis")
    if row.get("period_basis") == "capture_month" and not row.get("captured_at"):
        raise ValueError("A capture-month cohort requires captured_at; it is not a measurement month")
    if row.get("captured_at"):
        date.fromisoformat(row["captured_at"][:10])
    if not re.fullmatch(r"[A-Za-z]{2}", row["country"]):
        raise ValueError("Metric country must be a two-letter code, such as US or GB")
    raw = row.get("volume")
    volume = None if raw is None or str(raw).strip() == "" else float(raw)
    if volume is not None and (not 0 <= volume < float("inf") or not volume.is_integer()):
        raise ValueError("Volume must be a finite nonnegative integer or empty")
    return {**row, "volume": int(volume) if volume is not None else None,
            "country": row["country"].upper()}


def frequency_band(volume: int | None, low_max: int, mid_max: int) -> str:
    if low_max < 0 or mid_max <= low_max:
        raise ValueError("Require 0 <= low_max < mid_max")
    if volume is None:
        return "unknown"
    if volume == 0:
        return "reported_zero"
    return "low" if volume <= low_max else "medium" if volume <= mid_max else "high"
