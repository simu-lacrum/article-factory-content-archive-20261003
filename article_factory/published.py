from __future__ import annotations

import csv
import io
from pathlib import Path

from .db import KnowledgeDb
from .io_utils import read_text, slugify, write_text


PUBLISHED_HEADER = "title,slug,game,language,url,published_at,notes\n"
AVOID_TOPICS_HEADER = "# One pattern per line. Format: pattern | note\n"


def ensure_published_file(path: Path) -> None:
    if not path.exists():
        write_text(path, PUBLISHED_HEADER)


def load_published_csv(db: KnowledgeDb, path: Path) -> int:
    ensure_published_file(path)
    text = read_text(path)
    reader = csv.DictReader(io.StringIO(text))
    count = 0
    for row in reader:
        title = (row.get("title") or "").strip()
        if not title:
            continue
        db.upsert_published_article(
            title=title,
            slug=(row.get("slug") or slugify(title)).strip(),
            game=(row.get("game") or "").strip() or None,
            language=(row.get("language") or "").strip() or None,
            url=(row.get("url") or "").strip() or None,
            published_at=(row.get("published_at") or "").strip() or None,
            notes=(row.get("notes") or "").strip() or None,
        )
        count += 1
    db.conn.commit()
    return count


def ensure_avoid_topics_file(path: Path) -> None:
    if not path.exists():
        write_text(path, AVOID_TOPICS_HEADER)


def load_topic_exclusions(db: KnowledgeDb, path: Path) -> int:
    ensure_avoid_topics_file(path)
    count = 0
    for line in read_text(path).splitlines():
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if "|" in text:
            pattern, note = [part.strip() for part in text.split("|", 1)]
        else:
            pattern, note = text, None
        if not pattern:
            continue
        db.upsert_topic_exclusion(pattern, note)
        count += 1
    db.conn.commit()
    return count


def append_published_csv(
    path: Path,
    *,
    title: str,
    slug: str | None = None,
    game: str | None = None,
    language: str | None = None,
    url: str | None = None,
    published_at: str | None = None,
    notes: str | None = None,
) -> None:
    ensure_published_file(path)
    needs_newline = path.read_text(encoding="utf-8").endswith("\n")
    with path.open("a", encoding="utf-8", newline="") as f:
        if not needs_newline:
            f.write("\n")
        writer = csv.writer(f)
        writer.writerow([title, slug or slugify(title), game or "", language or "", url or "", published_at or "", notes or ""])
