from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable


SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS sources (
    id INTEGER PRIMARY KEY,
    path TEXT NOT NULL UNIQUE,
    kind TEXT NOT NULL,
    sha256 TEXT NOT NULL,
    title TEXT,
    meta_json TEXT NOT NULL DEFAULT '{}',
    ingested_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    heading TEXT,
    slug TEXT NOT NULL,
    body TEXT NOT NULL,
    token_hint INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS semantic_clusters (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    game TEXT NOT NULL,
    cluster TEXT NOT NULL,
    category TEXT,
    tier TEXT,
    main_query TEXT,
    frequency REAL NOT NULL DEFAULT 0,
    exact_frequency REAL NOT NULL DEFAULT 0,
    difficulty REAL,
    promotion_type TEXT,
    keywords TEXT NOT NULL DEFAULT '[]',
    notes TEXT,
    raw_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS topic_ideas (
    id INTEGER PRIMARY KEY,
    game TEXT NOT NULL,
    language TEXT NOT NULL DEFAULT 'en',
    title TEXT NOT NULL,
    source_kind TEXT NOT NULL,
    source_ref TEXT,
    cluster TEXT,
    main_query TEXT,
    score REAL NOT NULL DEFAULT 0,
    volume_words TEXT,
    outline_json TEXT NOT NULL DEFAULT '[]',
    ad_integration TEXT,
    evidence_json TEXT NOT NULL DEFAULT '[]',
    risk_level TEXT NOT NULL DEFAULT 'normal',
    status TEXT NOT NULL DEFAULT 'new',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(game, language, title)
);

CREATE TABLE IF NOT EXISTS published_articles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    slug TEXT,
    game TEXT,
    language TEXT,
    url TEXT,
    published_at TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS topic_exclusions (
    id INTEGER PRIMARY KEY,
    pattern TEXT NOT NULL UNIQUE,
    note TEXT
);

CREATE TABLE IF NOT EXISTS article_runs (
    id INTEGER PRIMARY KEY,
    spec TEXT NOT NULL,
    options_json TEXT NOT NULL DEFAULT '{}',
    manifest_path TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


FTS_SCHEMA = """
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts
USING fts5(heading, body, source_path UNINDEXED);

CREATE VIRTUAL TABLE IF NOT EXISTS clusters_fts
USING fts5(cluster, main_query, keywords, notes, game UNINDEXED);
"""


class KnowledgeDb:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.fts_available = True

    def close(self) -> None:
        self.conn.close()

    def remove_source(self, source_id: int) -> None:
        """Remove obsolete derived index entries, not the source file or publication memory."""
        for table, fts in (("chunks", "chunks_fts"), ("semantic_clusters", "clusters_fts")):
            for row in self.conn.execute(f"SELECT id FROM {table} WHERE source_id=?", (source_id,)).fetchall():
                try:
                    self.conn.execute(f"DELETE FROM {fts} WHERE rowid=?", (row["id"],))
                except sqlite3.OperationalError:
                    self.fts_available = False
        self.conn.execute("DELETE FROM sources WHERE id=?", (source_id,))

    def init(self) -> None:
        self.conn.executescript(SCHEMA)
        self._migrate()
        try:
            self.conn.executescript(FTS_SCHEMA)
        except sqlite3.OperationalError:
            self.fts_available = False
        self.conn.commit()

    def _migrate(self) -> None:
        columns = {
            row["name"]
            for row in self.conn.execute("PRAGMA table_info(topic_ideas)").fetchall()
        }
        if "risk_level" not in columns:
            self.conn.execute("ALTER TABLE topic_ideas ADD COLUMN risk_level TEXT NOT NULL DEFAULT 'normal'")

    def reset(self) -> None:
        for table in (
            "chunks_fts",
            "clusters_fts",
            "article_runs",
            "topic_ideas",
            "semantic_clusters",
            "chunks",
            "sources",
        ):
            try:
                self.conn.execute(f"DROP TABLE IF EXISTS {table}")
            except sqlite3.OperationalError:
                pass
        self.conn.commit()
        self.init()

    def upsert_source(
        self,
        *,
        path: str,
        kind: str,
        sha256: str,
        title: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> int:
        self.conn.execute(
            """
            INSERT INTO sources(path, kind, sha256, title, meta_json)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                kind=excluded.kind,
                sha256=excluded.sha256,
                title=excluded.title,
                meta_json=excluded.meta_json,
                ingested_at=CURRENT_TIMESTAMP
            """,
            (path, kind, sha256, title, json.dumps(meta or {}, ensure_ascii=False)),
        )
        row = self.conn.execute("SELECT id FROM sources WHERE path=?", (path,)).fetchone()
        assert row is not None
        source_id = int(row["id"])
        old_chunk_ids = [
            int(item["id"])
            for item in self.conn.execute("SELECT id FROM chunks WHERE source_id=?", (source_id,)).fetchall()
        ]
        old_cluster_ids = [
            int(item["id"])
            for item in self.conn.execute("SELECT id FROM semantic_clusters WHERE source_id=?", (source_id,)).fetchall()
        ]
        for chunk_id in old_chunk_ids:
            try:
                self.conn.execute("DELETE FROM chunks_fts WHERE rowid=?", (chunk_id,))
            except sqlite3.OperationalError:
                self.fts_available = False
        for cluster_id in old_cluster_ids:
            try:
                self.conn.execute("DELETE FROM clusters_fts WHERE rowid=?", (cluster_id,))
            except sqlite3.OperationalError:
                self.fts_available = False
        self.conn.execute("DELETE FROM chunks WHERE source_id=?", (source_id,))
        self.conn.execute("DELETE FROM semantic_clusters WHERE source_id=?", (source_id,))
        return source_id

    def add_chunk(self, source_id: int, source_path: str, heading: str, slug: str, body: str) -> int:
        token_hint = max(1, len(body.split()))
        cur = self.conn.execute(
            """
            INSERT INTO chunks(source_id, heading, slug, body, token_hint)
            VALUES (?, ?, ?, ?, ?)
            """,
            (source_id, heading, slug, body, token_hint),
        )
        chunk_id = int(cur.lastrowid)
        try:
            self.conn.execute(
                "INSERT INTO chunks_fts(rowid, heading, body, source_path) VALUES (?, ?, ?, ?)",
                (chunk_id, heading, body, source_path),
            )
        except sqlite3.OperationalError:
            self.fts_available = False
        return chunk_id

    def add_semantic_cluster(self, **kwargs: Any) -> int:
        keywords = kwargs.pop("keywords", [])
        raw = kwargs.pop("raw", {})
        source_id = int(kwargs["source_id"])
        cur = self.conn.execute(
            """
            INSERT INTO semantic_clusters(
                source_id, game, cluster, category, tier, main_query, frequency,
                exact_frequency, difficulty, promotion_type, keywords, notes, raw_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                source_id,
                kwargs.get("game"),
                kwargs.get("cluster"),
                kwargs.get("category"),
                kwargs.get("tier"),
                kwargs.get("main_query"),
                float(kwargs.get("frequency") or 0),
                float(kwargs.get("exact_frequency") or 0),
                kwargs.get("difficulty"),
                kwargs.get("promotion_type"),
                json.dumps(keywords, ensure_ascii=False),
                kwargs.get("notes"),
                json.dumps(raw, ensure_ascii=False),
            ),
        )
        cluster_id = int(cur.lastrowid)
        try:
            self.conn.execute(
                """
                INSERT INTO clusters_fts(rowid, cluster, main_query, keywords, notes, game)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    cluster_id,
                    kwargs.get("cluster") or "",
                    kwargs.get("main_query") or "",
                    " ".join(keywords),
                    kwargs.get("notes") or "",
                    kwargs.get("game") or "",
                ),
            )
        except sqlite3.OperationalError:
            self.fts_available = False
        return cluster_id

    def upsert_topic_idea(self, **kwargs: Any) -> int:
        outline = kwargs.pop("outline", [])
        evidence = kwargs.pop("evidence", [])
        self.conn.execute(
            """
            INSERT INTO topic_ideas(
                game, language, title, source_kind, source_ref, cluster, main_query,
                score, volume_words, outline_json, ad_integration, evidence_json, risk_level, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(game, language, title) DO UPDATE SET
                source_kind=excluded.source_kind,
                source_ref=excluded.source_ref,
                cluster=excluded.cluster,
                main_query=excluded.main_query,
                score=excluded.score,
                volume_words=excluded.volume_words,
                outline_json=excluded.outline_json,
                ad_integration=excluded.ad_integration,
                evidence_json=excluded.evidence_json,
                risk_level=excluded.risk_level,
                status=CASE WHEN topic_ideas.status='retired' THEN excluded.status ELSE topic_ideas.status END
            """,
            (
                kwargs.get("game"),
                kwargs.get("language", "en"),
                kwargs.get("title"),
                kwargs.get("source_kind"),
                kwargs.get("source_ref"),
                kwargs.get("cluster"),
                kwargs.get("main_query"),
                float(kwargs.get("score") or 0),
                kwargs.get("volume_words"),
                json.dumps(outline, ensure_ascii=False),
                kwargs.get("ad_integration"),
                json.dumps(evidence, ensure_ascii=False),
                kwargs.get("risk_level", "normal"),
                kwargs.get("status", "new"),
            ),
        )
        row = self.conn.execute(
            "SELECT id FROM topic_ideas WHERE game=? AND language=? AND title=?",
            (kwargs.get("game"), kwargs.get("language", "en"), kwargs.get("title")),
        ).fetchone()
        assert row is not None
        return int(row["id"])

    def search_chunks(self, query: str, limit: int = 8) -> list[sqlite3.Row]:
        if query.strip():
            try:
                rows = self.conn.execute(
                    """
                    SELECT c.*, s.path AS source_path, bm25(chunks_fts) AS rank
                    FROM chunks_fts
                    JOIN chunks c ON c.id = chunks_fts.rowid
                    JOIN sources s ON s.id = c.source_id
                    WHERE chunks_fts MATCH ?
                    ORDER BY rank
                    LIMIT ?
                    """,
                    (query, limit),
                ).fetchall()
                if rows:
                    return rows
            except sqlite3.OperationalError:
                self.fts_available = False
        like = f"%{query[:80]}%" if query.strip() else "%"
        return self.conn.execute(
            """
            SELECT c.*, s.path AS source_path, 0 AS rank
            FROM chunks c
            JOIN sources s ON s.id = c.source_id
            WHERE c.heading LIKE ? OR c.body LIKE ?
            ORDER BY c.token_hint DESC
            LIMIT ?
            """,
            (like, like, limit),
        ).fetchall()

    def search_clusters(self, query: str, game: str | None = None, limit: int = 20) -> list[sqlite3.Row]:
        params: list[Any] = []
        game_clause = ""
        if game and game != "all":
            game_clause = " AND sc.game=?"
            params.append(game)
        if query.strip():
            try:
                rows = self.conn.execute(
                    f"""
                    SELECT sc.*, bm25(clusters_fts) AS rank
                    FROM clusters_fts
                    JOIN semantic_clusters sc ON sc.id = clusters_fts.rowid
                    WHERE clusters_fts MATCH ?{game_clause}
                    ORDER BY rank
                    LIMIT ?
                    """,
                    [query, *params, limit],
                ).fetchall()
                if rows:
                    return rows
            except sqlite3.OperationalError:
                self.fts_available = False
        like = f"%{query[:80]}%" if query.strip() else "%"
        return self.conn.execute(
            f"""
            SELECT sc.*, 0 AS rank
            FROM semantic_clusters sc
            WHERE (sc.cluster LIKE ? OR sc.main_query LIKE ? OR sc.keywords LIKE ?){game_clause}
            ORDER BY sc.frequency DESC, sc.exact_frequency DESC
            LIMIT ?
            """,
            [like, like, like, *params, limit],
        ).fetchall()

    def list_topics(
        self,
        game: str = "all",
        language: str = "en",
        limit: int = 10,
        include_restricted: bool = False,
    ) -> list[sqlite3.Row]:
        params: list[Any] = []
        where = [
            "status NOT IN ('used', 'retired')",
            """
            NOT EXISTS (
                SELECT 1
                FROM published_articles pa
                WHERE lower(pa.title) = lower(topic_ideas.title)
                   OR (pa.slug IS NOT NULL AND pa.slug != '' AND lower(pa.slug) = lower(topic_ideas.title))
            )
            """,
            """
            NOT EXISTS (
                SELECT 1
                FROM topic_exclusions te
                WHERE instr(lower(topic_ideas.title), lower(te.pattern)) > 0
                   OR instr(lower(coalesce(topic_ideas.cluster, '')), lower(te.pattern)) > 0
                   OR instr(lower(coalesce(topic_ideas.main_query, '')), lower(te.pattern)) > 0
            )
            """,
        ]
        if not include_restricted:
            where.append("risk_level != 'restricted'")
        if game != "all":
            where.append("game=?")
            params.append(game)
        if language != "all":
            where.append("language=?")
            params.append(language)
        return self.conn.execute(
            f"""
            SELECT *
            FROM topic_ideas
            WHERE {" AND ".join(where)}
            ORDER BY score DESC, id ASC
            LIMIT ?
            """,
            [*params, limit],
        ).fetchall()

    def upsert_published_article(
        self,
        *,
        title: str,
        slug: str | None = None,
        game: str | None = None,
        language: str | None = None,
        url: str | None = None,
        published_at: str | None = None,
        notes: str | None = None,
    ) -> int:
        self.conn.execute(
            """
            INSERT INTO published_articles(title, slug, game, language, url, published_at, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(title) DO UPDATE SET
                slug=excluded.slug,
                game=excluded.game,
                language=excluded.language,
                url=excluded.url,
                published_at=excluded.published_at,
                notes=excluded.notes
            """,
            (title, slug, game, language, url, published_at, notes),
        )
        row = self.conn.execute("SELECT id FROM published_articles WHERE title=?", (title,)).fetchone()
        assert row is not None
        return int(row["id"])

    def upsert_topic_exclusion(self, pattern: str, note: str | None = None) -> int:
        self.conn.execute(
            """
            INSERT INTO topic_exclusions(pattern, note)
            VALUES (?, ?)
            ON CONFLICT(pattern) DO UPDATE SET note=excluded.note
            """,
            (pattern, note),
        )
        row = self.conn.execute("SELECT id FROM topic_exclusions WHERE pattern=?", (pattern,)).fetchone()
        assert row is not None
        return int(row["id"])

    def mark_topics_used(self, ids: Iterable[int]) -> None:
        self.conn.executemany("UPDATE topic_ideas SET status='used' WHERE id=?", [(int(i),) for i in ids])
        self.conn.commit()

    def record_run(self, spec: str, options: dict[str, Any], manifest_path: str | None) -> int:
        cur = self.conn.execute(
            "INSERT INTO article_runs(spec, options_json, manifest_path) VALUES (?, ?, ?)",
            (spec, json.dumps(options, ensure_ascii=False), manifest_path),
        )
        self.conn.commit()
        return int(cur.lastrowid)
