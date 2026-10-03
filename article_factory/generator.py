from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .db import KnowledgeDb
from .io_utils import clamp_words, slugify, write_text
from .llm import LlmResult, call_llm
from .products import product_for_game


RESTRICTED_EVIDENCE_PATTERNS = [
    r"\bhwid\b",
    r"spoofer|спуфер",
    r"anti-?cheat|античит|\bvac\b|faceit",
    r"bypass|evade|обход|обойти",
    r"inject|инжект|driver|kernel|драйвер",
    r"100%\s+(?:undetected|safe|guarantee|безопасн|гарант)",
    r"undetected|не\s*детект",
    r"cheats?\s+are\s+the\s+fastest",
    r"solve\s+this\s+in\s+one\s+click",
    r"developer\s+1|dota_game_account_debug",
    r"all-hero\s+scripts|hero\s+scripts|auto-?combo",
]

SYSTEM_EVIDENCE_SOURCES = {
    "README.md",
    "AGENTS.md",
    "SEO_ARTICLE_RULES.md",
    "CURRENT_CODEX_TASK.md",
    "SYSTEM_ARCHITECTURE.md",
    "PRODUCT_REQUIREMENTS.md",
    "AI_MEMORY_INTEGRATION.md",
    "knowledge/schema.md",
}


@dataclass
class ArticleSpec:
    raw: str
    count: int = 10
    language: str = "en"
    game: str = "all"
    style: str = "Medium-style, direct, practical, conversational, lightly slangy, gamer-aware, expert voice, no filler"
    volume: str | None = None
    ad_mode: str = "native"


def parse_spec(text: str, *, count: int | None = None, game: str | None = None, language: str | None = None) -> ArticleSpec:
    spec = ArticleSpec(raw=text)
    count_match = re.search(r"(\d{1,2})\s*(?:seo\s*)?(?:стат|article)", text, flags=re.I)
    if count_match:
        spec.count = int(count_match.group(1))
    if count is not None:
        spec.count = count
    if game:
        spec.game = game
    else:
        games = [name for name, pattern in {"cs2": r"\bcs2\b|кс\s*2|counter", "dota2": r"\bdota\b|дота", "deadlock": r"deadlock|дедлок"}.items() if re.search(pattern, text, flags=re.I)]
        spec.game = games[0] if len(games) == 1 else "all"
    if spec.count < 1:
        raise ValueError("Article count must be positive")
    if language:
        spec.language = language
    elif re.search(r"\b(en|english|англ)", text, flags=re.I):
        spec.language = "en"
    elif re.search(r"\b(ru|рус|русск)", text, flags=re.I):
        spec.language = "ru"
    volume_match = re.search(r"(\d[\d\s]{2,})\s*(слов|words|знаков|символ)", text, flags=re.I)
    if volume_match:
        spec.volume = f"{volume_match.group(1).strip()} {volume_match.group(2)}"
    style_match = re.search(r"в стиле[:\s]+(.+?)(?:,|\.|$)", text, flags=re.I)
    if style_match:
        spec.style = style_match.group(1).strip()
    return spec


def make_fts_query(text: str) -> str:
    terms = re.findall(r"[\wа-яёА-ЯЁ]{3,}", text)
    seen: list[str] = []
    for term in terms:
        low = term.lower()
        if low not in seen:
            seen.append(low)
    return " OR ".join(seen[:8])


SPEC_STOPWORDS = {
    "generate",
    "write",
    "article",
    "articles",
    "about",
    "with",
    "integrate",
    "integration",
    "native",
    "seo",
    "words",
    "style",
    "game",
    "deadlock",
    "dota",
    "cs2",
    "cluster",
    "center",
    "melonity",
}


def spec_terms(text: str) -> list[str]:
    terms: list[str] = []
    for term in re.findall(r"[a-zA-Z0-9а-яА-ЯёЁ]{3,}", text.lower()):
        if term in SPEC_STOPWORDS or term in terms:
            continue
        terms.append(term)
    return terms[:12]


def rank_topics_for_spec(topics: list[dict], spec: ArticleSpec) -> list[dict]:
    terms = spec_terms(spec.raw)
    if not terms:
        return topics
    ranked: list[tuple[float, dict]] = []
    for topic in topics:
        evidence = " ".join(json.loads(topic.get("evidence_json") or "[]"))
        haystack = " ".join(
            str(topic.get(field) or "")
            for field in ("title", "cluster", "main_query", "ad_integration")
        )
        haystack = f"{haystack} {evidence}".lower()
        matches = sum(1 for term in terms if term in haystack)
        exact_bonus = 0
        for term in terms:
            if term and term in str(topic.get("main_query") or "").lower():
                exact_bonus += 4
            elif term and term in str(topic.get("title") or "").lower():
                exact_bonus += 3
        ranked.append((float(topic.get("score") or 0) + matches * 12 + exact_bonus, topic))
    return [topic for _, topic in sorted(ranked, key=lambda item: item[0], reverse=True)]


def build_evidence_pack(db: KnowledgeDb, topic: dict, language: str, limit: int = 10) -> list[dict]:
    product = product_for_game(topic.get("game"))
    queries = [
        topic.get("title") or "",
        topic.get("main_query") or "",
        topic.get("cluster") or "",
        f"Tone of Voice SEO article content pattern {product}",
        f"product features {product} TOV SEO article",
        "product map cluster.center Melonity",
    ]
    rows = []
    seen = set()
    for query in queries:
        fts_query = make_fts_query(query)
        for row in db.search_chunks(fts_query or query, limit=limit):
            if row["source_path"] in SYSTEM_EVIDENCE_SOURCES or row["source_path"].replace("\\", "/").startswith(("knowledge/agent_memory/rules/", "memory/graph/", "research/")):
                continue
            if is_irrelevant_product_evidence(topic, row):
                continue
            key = re.sub(r"\s+", " ", row["body"]).strip().casefold()
            if key in seen:
                continue
            body = row["body"]
            if topic.get("risk_level") == "normal" and is_restricted_evidence(row["heading"], body):
                continue
            seen.add(key)
            rows.append(
                {
                    "source": row["source_path"],
                    "heading": row["heading"],
                    "excerpt": clamp_words(body, 180),
                }
            )
            if len(rows) >= limit:
                return rows
    return rows


def is_irrelevant_product_evidence(topic: dict, row: dict) -> bool:
    game = (topic.get("game") or "").lower()
    text = f"{row['source_path']}\n{row['heading']}\n{row['body']}".lower()
    if game == "dota2":
        return any(marker in text for marker in ("cluster.center", "deadlock", "counter-strike", "cs2")) and not any(marker in text for marker in ("dota", "melonity", "product-map"))
    if game not in {"deadlock", "cs2"}:
        return False
    allowed_markers = ["cluster.center", "cluster center", "product-map", "deadlock-cs2-cluster-center"]
    if game == "deadlock":
        allowed_markers.extend(["deadlock", "deadlock-cluster-center"])
    if game == "cs2":
        allowed_markers.extend(["cs2", "counter-strike", "counter strike", "semantic_core_cs2"])
    if any(marker in text for marker in allowed_markers):
        return False
    wrong_markers = ["melonity", "dota 2", "dota2", "melonity-knowledge-base", "melonity-seo-cluster-map"]
    return any(marker in text for marker in wrong_markers)


def is_restricted_evidence(heading: str, body: str) -> bool:
    text = f"{heading}\n{body}"
    return any(re.search(pattern, text, flags=re.I | re.S) for pattern in RESTRICTED_EVIDENCE_PATTERNS)


def build_prompt(spec: ArticleSpec, topic: dict, evidence: list[dict]) -> str:
    outline = json.loads(topic.get("outline_json") or "[]")
    topic_evidence = json.loads(topic.get("evidence_json") or "[]")
    lang_name = "Russian" if spec.language == "ru" else "English"
    volume = spec.volume or topic.get("volume_words") or "Cover the reader's question completely, without a fixed SEO word count"
    product = product_for_game(topic.get("game") or spec.game)
    source_notes = "\n\n".join(
        f"### Source: {item['source']} / {item['heading']}\n{item['excerpt']}" for item in evidence
    )
    outline_text = "\n".join(f"- {item}" for item in outline) if outline else "- Build the best SEO structure for the topic."
    topic_evidence_text = "\n".join(f"- {item}" for item in topic_evidence)
    return f"""You are an expert SEO editor and game-content researcher.

Write a useful, non-generic SEO article in {lang_name}.

USER SPEC:
{spec.raw}

ARTICLE TARGET:
- Title: {topic.get('title')}
- Game: {topic.get('game')}
- Main query: {topic.get('main_query')}
- Cluster: {topic.get('cluster')}
- Risk level: {topic.get('risk_level', 'normal')}
- Target volume: {volume}
- Style: {spec.style}
- Advertising mode: {spec.ad_mode}
- Product to integrate: {product}

SEO / TOPIC EVIDENCE:
{topic_evidence_text}

SUGGESTED OUTLINE:
{outline_text}

BACKGROUND NOTES FOR THE WRITER (do not name these in the article):
{source_notes}

STRICT RULES:
- Use the background notes and verified facts internally; do not mention "local sources", "local evidence", "evidence pack", or "knowledge base" in the final article body.
- Write in a direct editorial voice. Never invent personal testing or experience; use "we tested" only with a real test record.
- Use only supported facts or mark uncertainty explicitly.
- Do not invent current patch, price, ban-wave, anti-cheat, or product-status facts.
- Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheats.
- If risk level is `restricted`, write only a high-level educational/risk-aware article and refuse operational steps.
- You may mention {product} as a product/brand in a native ad block, but do not make unsupported safety guarantees.
- Respect product mapping: Dota 2 uses Melonity; Deadlock and CS2 use cluster.center.
- Deliver the reader's answer first. Include only examples, explanations and checklists that help this specific intent.
- Match the imported Medium source style: direct, practical, conversational, lightly slangy, gamer-aware, and free from water, corporate wording, bureaucratic phrasing, or academic over-explaining.
- Keep the target volume useful but tight: cover the intent completely, without padding.
- Do not use markdown tables. Use bullet lists, numbered lists, and comparison lists instead.
- Return Markdown with front matter: title, description, game, language, primary_keyword, secondary_keywords.
- End with a useful FAQ block and include image placement notes. Follow the project's visual prompt guide.
- Use related entities and natural variants where relevant. There is no mandatory keyword density or ideal anchor ratio.
- Do not add empty introductions, repeated takeaways, fake quotes, or a fixed paragraph template to reach a word count.
"""


def estimate_target_words(spec: ArticleSpec, topic: dict) -> int:
    text = spec.volume or topic.get("volume_words") or ""
    nums = [int(match) for match in re.findall(r"\d{3,5}", text.replace(",", ""))]
    if nums:
        return max(nums)
    return 1600 if spec.language == "en" else 1200


def keyword_list(topic: dict) -> list[str]:
    values: list[str] = []
    for field in ("main_query", "cluster", "title"):
        value = topic.get(field)
        if value and value not in values:
            values.append(str(value))
    try:
        evidence = json.loads(topic.get("evidence_json") or "[]")
        for item in evidence:
            if isinstance(item, str) and len(item) <= 90 and item not in values:
                values.append(item)
    except json.JSONDecodeError:
        pass
    return values[:12]


def fallback_brief(spec: ArticleSpec, topic: dict, evidence: list[dict], prompt_path: str) -> str:
    product = product_for_game(topic.get("game") or spec.game)
    outline = json.loads(topic.get("outline_json") or "[]")
    topic_evidence = json.loads(topic.get("evidence_json") or "[]")
    lines = [
        "---",
        f"title: {json.dumps(topic.get('title'), ensure_ascii=False)}",
        f"game: {topic.get('game')}",
        f"language: {spec.language}",
        "status: needs_codex",
        f"prompt: {prompt_path}",
        "---",
        "",
        f"# {topic.get('title')}",
        "",
        "This file is an article brief. Codex should write the final article manually from this prompt and evidence; do not require an external LLM API.",
        "",
        "## Target",
        f"- Main query: {topic.get('main_query')}",
        f"- Cluster: {topic.get('cluster')}",
        f"- Volume: {spec.volume or topic.get('volume_words') or 'auto'}",
        f"- Style: {spec.style}",
        "- Formatting: no markdown tables; use lists only.",
        "",
        "## Evidence",
    ]
    lines.extend(f"- {item}" for item in topic_evidence[:20])
    lines.append("")
    lines.append("## Suggested Structure")
    if outline:
        lines.extend(f"- {item}" for item in outline)
    else:
        lines.extend(
            [
                "- Search intent and quick answer",
                "- Main explanation",
                "- Practical examples",
                f"- {product} native integration",
                "- FAQ",
            ]
        )
    lines.append("")
    lines.append("## Source Pack")
    for item in evidence:
        lines.append(f"### {item['heading']}")
        lines.append(f"Source: `{item['source']}`")
        lines.append("")
        lines.append(item["excerpt"])
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def generate_articles(
    db_path: Path,
    output_root: Path,
    spec_text: str,
    *,
    count: int | None = None,
    game: str | None = None,
    language: str | None = None,
    llm_provider: str = "none",
    model: str | None = None,
    mark_used: bool = False,
    include_restricted: bool = False,
) -> dict:
    db = KnowledgeDb(db_path)
    db.init()
    spec = parse_spec(spec_text, count=count, game=game, language=language)
    from .research.service import active_core, writing_contract, research_evidence
    core = active_core(output_root.parent)
    candidate_count = max(spec.count * 8, 50)
    topics = [dict(row) for row in db.list_topics(spec.game, spec.language, candidate_count, include_restricted=include_restricted)]
    if core:
        topics = [dict(row) for row in db.list_topics(spec.game, spec.language, -1, include_restricted=include_restricted)
                  if row["source_kind"] == "seo_research"]
    topics = rank_topics_for_spec(topics, spec)
    if core and spec.game == "all":
        pools = {g: [t for t in topics if t["game"] == g] for g in ("cs2", "dota2", "deadlock")}
        topics = []
        while any(pools.values()):
            for pool in pools.values():
                if pool:
                    topics.append(pool.pop(0))
    run_stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    article_dir = output_root / "articles" / run_stamp
    prompt_dir = output_root / "prompts" / run_stamp
    brief_dir = output_root / "briefs" / run_stamp
    evidence_dir = output_root / "evidence" / run_stamp
    manifest = {
        "created_at": run_stamp,
        "spec": spec.__dict__,
        "llm_provider": llm_provider,
        "model": model,
        "items": [],
    }
    used_ids: list[int] = []
    for idx, topic in enumerate(topics[: spec.count], start=1):
        evidence = research_evidence(output_root.parent, topic) if topic.get("source_kind") == "seo_research" else build_evidence_pack(db, topic, spec.language)
        contract = writing_contract(output_root.parent, topic)
        prompt = build_prompt(spec, topic, evidence)
        if contract:
            prompt += "\nRESEARCH AND READER CONTRACT (editorial input, not article text):\n" + json.dumps(contract, ensure_ascii=False, indent=2) + "\n"
        slug = f"{idx:02d}-{slugify(topic['title'])}"
        prompt_path = prompt_dir / f"{slug}.md"
        evidence_path = evidence_dir / f"{slug}.json"
        write_text(prompt_path, prompt)
        write_text(
            evidence_path,
            json.dumps(
                {
                    "topic": topic,
                    "research_contract": contract,
                    "evidence": evidence,
                    "strict_rules": [
                        "Use only supported facts or mark uncertainty explicitly.",
                        "Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body; write from an expert editorial voice.",
                        "Do not invent current patch, price, ban-wave, anti-cheat, or product-status facts.",
                        "Do not provide operational anti-cheat evasion, exploit, or cheat-implementation instructions.",
                        "Do not use markdown tables; use lists instead.",
                        "Match the imported Medium style: direct, practical, conversational, lightly slangy, and no filler.",
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )
        if llm_provider == "template":
            result = LlmResult(text="", provider="none", model=None,
                               error="Template articles retired: Codex must write the final article from the brief.")
        else:
            result = call_llm(llm_provider, prompt, model)
        if result.text.strip():
            article_path = article_dir / f"{slug}.md"
            write_text(article_path, result.text.strip() + "\n")
            status = "article"
            output_path = article_path
        else:
            brief_path = brief_dir / f"{slug}.md"
            brief = fallback_brief(spec, topic, evidence, str(prompt_path))
            write_text(brief_path, brief)
            status = "brief"
            output_path = brief_path
        manifest["items"].append(
            {
                "topic_id": topic["id"],
                "title": topic["title"],
                "game": topic["game"],
                "language": topic["language"],
                "status": status,
                "output": str(output_path),
                "prompt": str(prompt_path),
                "evidence": str(evidence_path),
                "llm_error": result.error,
            }
        )
        if status == "article":
            used_ids.append(int(topic["id"]))
    manifest_path = output_root / "runs" / f"{run_stamp}.json"
    write_text(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2))
    db.record_run(spec_text, {"count": count, "game": game, "language": language, "llm": llm_provider, "model": model}, str(manifest_path))
    if mark_used:
        db.mark_topics_used(used_ids)
    db.close()
    return manifest
