from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from .db import KnowledgeDb
from .io_utils import read_text, relpath
from .products import product_for_game


@dataclass
class TopicSeed:
    game: str
    language: str
    title: str
    source_kind: str
    source_ref: str
    score: float
    cluster: str | None = None
    main_query: str | None = None
    volume_words: str | None = None
    outline: list[str] | None = None
    ad_integration: str | None = None
    evidence: list[str] | None = None
    risk_level: str = "normal"


def classify_risk(*values: str | None) -> str:
    text = " ".join(item or "" for item in values).lower()
    restricted_patterns = [
        r"\bhwid\b",
        r"spoofer|спуфер",
        r"hardware ban|аппаратн",
        r"anti-?cheat|античит|\bvac\b|faceit",
        r"bypass|evade|обход|обойти",
        r"inject|инжект|driver|kernel|драйвер",
        r"wallhack|\bwh\b|\bвх\b",
        r"aimbot|rage|hvh|хвх|рейдж",
    ]
    elevated_patterns = [
        r"cheat|hack|чит|хак",
        r"script|скрипт|macro|макрос|ahk",
        r"skin changer|скинченджер",
        r"cfg|config|конфиг",
    ]
    if any(re.search(pattern, text, flags=re.I) for pattern in restricted_patterns):
        return "restricted"
    if any(re.search(pattern, text, flags=re.I) for pattern in elevated_patterns):
        return "elevated"
    return "normal"


def parse_cluster_map(path: Path, root: Path) -> list[TopicSeed]:
    if not path.exists():
        return []
    text = read_text(path)
    blocks = re.split(r"\n(?=###\s+\d+\.\s+)", text)
    seeds: list[TopicSeed] = []
    for block in blocks:
        head = re.match(r"###\s+\d+\.\s+(.+)", block)
        if not head:
            continue
        heading = head.group(1).strip()
        title_match = re.search(r"\*\*EN article title:\*\*\s*`?([^`\n]+)`?", block)
        volume_match = re.search(r"\*\*Объем:\*\*\s*([^\n]+)", block)
        ad_match = re.search(r"\*\*Рекламная интеграция:\*\*\s*([^\n]+(?:\n(?!\*\*|---|###).+)*)", block)
        why_match = re.search(r"\*\*Почему можно ранжироваться:\*\*\s*([^\n]+)", block)
        outline: list[str] = []
        outline_match = re.search(r"\*\*Оглавление:\*\*\s*\n\n((?:- .+\n?)+)", block)
        if outline_match:
            outline = [line[2:].strip() for line in outline_match.group(1).splitlines() if line.startswith("- ")]
        title = title_match.group(1).strip() if title_match else heading
        score = 100.0
        if "KD 2" in block or "KD 3" in block:
            score += 25
        if "Уже написано" in block:
            score -= 20
        if "long-tail" in block.lower() or "длинный хвост" in block.lower():
            score += 12
        evidence = [heading]
        if why_match:
            evidence.append(why_match.group(1).strip())
        seeds.append(
            TopicSeed(
                game="dota2",
                language="en",
                title=title,
                source_kind="cluster_map",
                source_ref=relpath(path, root),
                score=score,
                cluster=heading,
                main_query=title,
                volume_words=volume_match.group(1).strip() if volume_match else None,
                outline=outline,
                ad_integration=ad_match.group(1).strip() if ad_match else None,
                evidence=evidence,
                risk_level=classify_risk(title, heading, ad_match.group(1) if ad_match else None),
            )
        )
    return seeds


def parse_topic_seed_files(root: Path) -> list[TopicSeed]:
    directory = root / "knowledge" / "topic_seeds"
    if not directory.exists():
        return []
    seeds: list[TopicSeed] = []
    for path in sorted(directory.glob("*.json")):
        try:
            data = json.loads(read_text(path))
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else data.get("topics", [])
        for item in items:
            if not isinstance(item, dict):
                continue
            title = item.get("title")
            if not title:
                continue
            game = item.get("game") or "general"
            main_query = item.get("main_query") or title
            cluster = item.get("cluster") or main_query
            score = float(item.get("score") or 80.0)
            language = item.get("language") or ("ru" if re.search(r"[а-яё]", main_query, flags=re.I) else "en")
            seeds.append(
                TopicSeed(
                    game=game,
                    language=language,
                    title=title,
                    source_kind="curated_topic_seed",
                    source_ref=relpath(path, root),
                    score=score,
                    cluster=cluster,
                    main_query=main_query,
                    volume_words=item.get("volume_words") or ("1,500-2,200 words" if language == "en" else "8,000-12,000 знаков"),
                    outline=item.get("outline") or [],
                    ad_integration=item.get("ad_integration") or f"Native {product_for_game(game)} integration",
                    evidence=item.get("evidence") or [cluster, main_query],
                    risk_level=item.get("risk_level") or classify_risk(title, cluster, main_query),
                )
            )
    return seeds


def semantic_topic_seeds(db: KnowledgeDb, game: str = "all") -> list[TopicSeed]:
    rows = db.search_clusters("", game=game, limit=-1)
    seeds: list[TopicSeed] = []
    for row in rows:
        main_query = row["main_query"] or row["cluster"]
        cluster = row["cluster"] or main_query
        kd = row["difficulty"] if row["difficulty"] is not None else 6
        frequency = float(row["frequency"] or row["exact_frequency"] or 0)
        exact = float(row["exact_frequency"] or 0)
        # Legacy CSV numbers lack market/provider/date. They cannot rank new EN opportunities.
        score = 20.0
        promotion = (row["promotion_type"] or "").lower()
        tier = (row["tier"] or "").lower()
        cluster_low = cluster.lower()
        if "прямая реклама" in promotion:
            score *= 0.65
        if "core" in tier or cluster_low.startswith("core:"):
            score *= 0.72
        if "long" in tier or "длин" in cluster_low or "general" in cluster_low:
            score *= 1.2
        if "бренд" in cluster_low or "mel" in cluster_low:
            score *= 1.25
        keywords = json.loads(row["keywords"] or "[]")
        outline = [
            f"What users mean by \"{main_query}\"",
            "Current game context and common misconceptions",
            "Practical checklist and safe expectations",
            f"Where {product_for_game(row['game'])} fits naturally without unsupported promises",
            "FAQ based on long-tail keywords",
        ]
        language = "ru" if re.search(r"[а-яё]", main_query, flags=re.I) else "en"
        title = build_title(row["game"], main_query, language)
        seeds.append(
            TopicSeed(
                game=row["game"],
                language=language,
                title=title,
                source_kind="semantic_csv",
                source_ref=str(row["id"]),
                score=score,
                cluster=cluster,
                main_query=main_query,
                volume_words="1,500-2,200 words" if language == "en" else "8,000-12,000 знаков",
                outline=outline,
                ad_integration=row["promotion_type"],
                evidence=[cluster, main_query, *keywords[:8]],
                risk_level=classify_risk(cluster, main_query, row["promotion_type"], " ".join(keywords[:20])),
            )
        )
    return seeds


def build_title(game: str, query: str, language: str) -> str:
    labels = {"dota2": "Dota 2", "cs2": "CS2", "general": "the topic"}
    game_name = labels.get(game, game.replace("_", " ").title())
    query = query.strip()
    if language == "ru":
        clean = query[:1].upper() + query[1:]
        return f"{clean}: полный разбор для {game_name}"
    return query[:1].upper() + query[1:]


def rebuild_topic_ideas(db_path: Path, root: Path) -> int:
    db = KnowledgeDb(db_path)
    db.init()
    seeds: list[TopicSeed] = []
    seeds.extend(parse_cluster_map(root / "melonity-seo-cluster-map-en.md", root))
    seeds.extend(parse_topic_seed_files(root))
    seeds.extend(semantic_topic_seeds(db, "all"))
    from .research.service import active_core
    core = active_core(root)
    if core:
        for cluster in core["clusters"]:
            if cluster.get("publication_action") not in {"write_article", "update_article"}:
                continue
            seeds.append(TopicSeed(game=cluster["game"], language=cluster.get("language", "en"),
                title=cluster["title"], source_kind="seo_research", source_ref=cluster["id"],
                score=210 if cluster.get("priority") == "P1" else 200,
                cluster=cluster["id"], main_query=cluster.get("article_target_query", cluster["primary_query"]),
                volume_words="Cover the reader job completely; no SEO word-count target",
                outline=cluster.get("outline", []), evidence=[cluster["reader_job"], cluster["original_value"]],
                ad_integration=f"Contextual {product_for_game(cluster['game'])} mention with disclosure when commercial",
                risk_level="restricted" if cluster.get("scope") == "restricted_operational" else "elevated"))
    # Retire disappeared generated topics without erasing publication or used-topic history.
    identities = {(s.game, s.language, s.title) for s in seeds}
    for row in db.conn.execute("SELECT id,game,language,title FROM topic_ideas WHERE status='new'").fetchall():
        if (row['game'], row['language'], row['title']) not in identities:
            db.conn.execute("UPDATE topic_ideas SET status='retired' WHERE id=?", (row['id'],))
    count = 0
    for seed in seeds:
        db.upsert_topic_idea(
            game=seed.game,
            language=seed.language,
            title=seed.title,
            source_kind=seed.source_kind,
            source_ref=seed.source_ref,
            cluster=seed.cluster,
            main_query=seed.main_query,
            score=seed.score,
            volume_words=seed.volume_words,
            outline=seed.outline or [],
            ad_integration=seed.ad_integration,
            evidence=seed.evidence or [],
            risk_level=seed.risk_level,
        )
        count += 1
    db.conn.commit()
    db.close()
    return count
