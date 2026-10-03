from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .db import KnowledgeDb
from .io_utils import read_text, write_text


def export_ai_memory(db_path: Path, output_dir: Path) -> dict:
    db = KnowledgeDb(db_path)
    db.init()
    output_dir.mkdir(parents=True, exist_ok=True)
    topics = db.conn.execute(
        """
        SELECT game, language, title, cluster, main_query, score, volume_words, ad_integration
        FROM topic_ideas
        WHERE status NOT IN ('used', 'retired')
        ORDER BY score DESC
        LIMIT 80
        """
    ).fetchall()
    sources = db.conn.execute("SELECT path, kind, title, ingested_at FROM sources ORDER BY path").fetchall()
    clusters = db.conn.execute(
        """
        SELECT game, cluster, main_query, frequency, exact_frequency, difficulty, promotion_type
        FROM semantic_clusters
        ORDER BY frequency DESC, exact_frequency DESC
        LIMIT 120
        """
    ).fetchall()
    now = datetime.now().isoformat(timespec="seconds")
    index = [
        "# Article Factory Memory Index",
        "",
        f"Updated: {now}",
        "",
        "Current SEO research: use config/research.json and the selected study's core.json. Legacy CSV frequency/KD values are unverified and must not be presented as current US/UK metrics.",
        "Research priority is editorial judgment, not predicted traffic. Unknown volume is not zero or low frequency.",
        "",
        "## Purpose",
        "Persistent project memory for automated SEO article generation based on local factual sources.",
        "",
        "## Files",
        "- `project-summary.md` - operating model and rules.",
        "- `product-requirements.md` - non-negotiable target state.",
        "- `product-map.md` - product mapping by game: Dota 2 uses Melonity; Deadlock and CS2 use cluster.center.",
        "- `seo-article-rules.md` - mandatory article structure, SEO metadata, FAQ, image notes, and review rules.",
        "- `article-visual-prompt-guide.md` - mandatory Nano Banana Pro visual system with B-first alternation, strict warm-story reference fidelity, and mapped Cluster/Melonity accents.",
        "- `topic-priorities.md` - highest-priority article opportunities.",
        "- `published-and-avoid.md` - published articles and no-duplicate topic patterns.",
        "- `source-inventory.md` - ingested sources.",
        "- `semantic-clusters.md` - top semantic clusters.",
        "- `log.md` - export log.",
    ]
    write_text(output_dir / "index.md", "\n".join(index) + "\n")
    requirements_path = db_path.parent.parent / "PRODUCT_REQUIREMENTS.md"
    if requirements_path.exists():
        write_text(output_dir / "product-requirements.md", read_text(requirements_path))
    seo_rules_path = db_path.parent.parent / "SEO_ARTICLE_RULES.md"
    if seo_rules_path.exists():
        write_text(output_dir / "seo-article-rules.md", read_text(seo_rules_path))
    visual_guide_path = db_path.parent.parent / "knowledge" / "agent_memory" / "rules" / "article-visual-prompt-guide.md"
    if visual_guide_path.exists():
        write_text(output_dir / "article-visual-prompt-guide.md", read_text(visual_guide_path))
    product_map_path = db_path.parent.parent / "knowledge" / "agent_memory" / "products" / "product-map.md"
    if product_map_path.exists():
        write_text(output_dir / "product-map.md", read_text(product_map_path))
    summary = """# Project Summary

The workspace is a local knowledge base for generating SEO articles about Dota 2, Deadlock, and CS2 from factual sources.

Product mapping: Dota 2 articles integrate Melonity. Deadlock and CS2 articles integrate cluster.center.

Core rule: articles must be built from evidence packs retrieved from local markdown, CSV semantic cores, uploaded PDFs/text, and materialized link sources. Persistent URLs are copied into `knowledge/agent_memory/sources/` as markdown before indexing, so future agents read local files instead of opening links. The generator should avoid unsupported current facts and should not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheats.

Public-facing voice rule: final article bodies must not mention "local sources", "local evidence", "evidence pack", "knowledge base", or similar internal-provenance wording. Use the evidence silently and write from an expert editorial perspective: practical, conversational, lightly slangy, gamer-aware, and based on experience.

Visual rule: number generated conceptual assets across each run and alternate odd branch B (warm narrative) with even branch A (tactile industrial), so a one-cover run uses the new reference family. Real screenshots do not consume an index. Every B asset must actually attach two persistent warm-story references and pass 4/5 fidelity. Use Cluster #635FD5 and Melonity #FF1469 by branch: one small 3–8% semantic accent in A; the dominant 35–70% field replacing yellow/amber in B.

Recommended flow:
1. Ingest new CSV/markdown/PDF/link sources.
2. Rebuild topic ideas from semantic clusters.
3. Select topics that balance search demand, lower difficulty, product fit, and non-duplication.
4. Generate evidence pack and article prompt.
5. Use an LLM provider only after evidence is assembled.
6. Review generated articles before publication and mark published topics in `published/articles.csv`.
"""
    write_text(output_dir / "project-summary.md", summary)
    topic_lines = ["# Topic Priorities", ""]
    for row in topics:
        topic_lines.extend(
            [
                f"## {row['title']}",
                f"- Game: {row['game']}",
                f"- Language: {row['language']}",
                f"- Cluster: {row['cluster']}",
                f"- Main query: {row['main_query']}",
                f"- Score: {row['score']:.2f}",
                f"- Volume: {row['volume_words'] or 'auto'}",
                f"- Ad integration: {row['ad_integration'] or 'native'}",
                "",
            ]
        )
    write_text(output_dir / "topic-priorities.md", "\n".join(topic_lines))
    published = db.conn.execute(
        "SELECT title, url, game, language, notes FROM published_articles ORDER BY id"
    ).fetchall()
    exclusions = db.conn.execute("SELECT pattern, note FROM topic_exclusions ORDER BY id").fetchall()
    pa_lines = ["# Published Articles And Topic Exclusions", ""]
    pa_lines.append("## Published Articles")
    pa_lines.append("")
    for row in published:
        pa_lines.append(f"- {row['title']} ({row['game']}/{row['language']}): {row['url']} - {row['notes'] or ''}")
    pa_lines.append("")
    pa_lines.append("## Topic Exclusions")
    pa_lines.append("")
    for row in exclusions:
        pa_lines.append(f"- `{row['pattern']}` - {row['note'] or ''}")
    write_text(output_dir / "published-and-avoid.md", "\n".join(pa_lines) + "\n")
    source_lines = ["# Source Inventory", ""]
    for row in sources:
        source_lines.append(f"- `{row['path']}` ({row['kind']}, ingested {row['ingested_at']})")
    write_text(output_dir / "source-inventory.md", "\n".join(source_lines) + "\n")
    cluster_lines = ["# Legacy Semantic Clusters", "", "Frequency and KD below have no verified provider/market/date. Do not use them as current US/UK metrics; use the active research core.", ""]
    for row in clusters:
        cluster_lines.append(
            f"- {row['game']} | {row['cluster']} | {row['main_query']} | freq={row['frequency']} | exact={row['exact_frequency']} | kd={row['difficulty']} | promo={row['promotion_type']}"
        )
    write_text(output_dir / "semantic-clusters.md", "\n".join(cluster_lines) + "\n")
    write_text(output_dir / "log.md", f"# Log\n\n- {now}: exported article-factory memory snapshot.\n")
    db.close()
    return {"output_dir": str(output_dir), "topics": len(topics), "sources": len(sources), "clusters": len(clusters)}
