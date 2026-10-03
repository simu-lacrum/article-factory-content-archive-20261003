from __future__ import annotations

import csv
import io
import json
import math
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

from .db import KnowledgeDb
from .io_utils import file_sha256, read_text, relpath, slugify, text_sha256, write_text


DEFAULT_IGNORES = {
    "research",
    "tests",
    "docs",
    ".seo-cache",
    "memory/graph",
    ".article-factory",
    "article_factory",
    "config",
    "CURRENT_CODEX_TASK.md",
    "output",
    "outputs",
    "knowledge/wiki",
    "knowledge/link_sources",
    "memory/ai-memory-export",
    "published",
    "prompts",
    "__pycache__",
}

TEXT_EXTENSIONS = {".md", ".txt", ".html", ".htm"}
CSV_EXTENSIONS = {".csv", ".tsv"}
PDF_EXTENSIONS = {".pdf"}
LINK_SOURCE_DIRS = ("knowledge/link_sources",)
MATERIALIZED_LINK_ROOT = Path("knowledge") / "agent_memory" / "sources"


@dataclass
class IngestStats:
    sources: int = 0
    chunks: int = 0
    clusters: int = 0
    wiki_pages: int = 0
    warnings: list[str] | None = None

    def add_warning(self, message: str) -> None:
        if self.warnings is None:
            self.warnings = []
        self.warnings.append(message)


@dataclass
class LinkMaterializeStats:
    files: int = 0
    fetched: int = 0
    skipped: int = 0
    warnings: list[str] | None = None
    outputs: list[str] | None = None

    def add_warning(self, message: str) -> None:
        if self.warnings is None:
            self.warnings = []
        self.warnings.append(message)

    def add_output(self, path: Path, root: Path) -> None:
        if self.outputs is None:
            self.outputs = []
        self.outputs.append(relpath(path, root))


def parse_markdown_sections(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_heading = "Document"
    current_body: list[str] = []
    heading_re = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
    for line in lines:
        match = heading_re.match(line)
        if match:
            if current_body:
                sections.append((current_heading, current_body))
            current_heading = match.group(2).strip()
            current_body = [line]
        else:
            current_body.append(line)
    if current_body:
        sections.append((current_heading, current_body))
    clean: list[tuple[str, str]] = []
    for heading, body_lines in sections:
        body = "\n".join(body_lines).strip()
        if body:
            clean.append((heading, body))
    return clean


def sniff_csv(text: str) -> csv.Dialect:
    sample = text[:4096]
    try:
        return csv.Sniffer().sniff(sample, delimiters=";,|\t,")
    except csv.Error:
        dialect = csv.excel()
        dialect.delimiter = ";"
        return dialect


def number(value: str | int | float | None) -> float:
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).replace("\xa0", "").replace(" ", "").replace(",", ".")
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return float(match.group(0)) if match else 0.0


def difficulty(value: str | int | float | None) -> float | None:
    if value is None or value == "":
        return None
    return number(value)


def split_keywords(value: str | None, fallback: str | None = None) -> list[str]:
    if not value:
        return [fallback] if fallback else []
    parts = re.split(r"\s*\|\s*|\s*;\s*", value)
    items = [p.strip() for p in parts if p.strip()]
    if fallback and fallback not in items:
        items.insert(0, fallback)
    return items[:80]


def detect_game(path: Path, headers: list[str]) -> str:
    low = path.name.lower()
    if "cs2" in low or "кс" in low:
        return "cs2"
    if "dota" in low or "дота" in low:
        return "dota2"
    header_blob = " ".join(headers).lower()
    if "counter" in header_blob or "cs2" in header_blob:
        return "cs2"
    return "general"


def ingest_markdown(db: KnowledgeDb, path: Path, root: Path, wiki_root: Path) -> IngestStats:
    stats = IngestStats()
    text = read_text(path)
    source_path = relpath(path, root)
    source_id = db.upsert_source(
        path=source_path,
        kind="markdown",
        sha256=file_sha256(path),
        title=path.stem,
        meta={"format": "markdown"},
    )
    sections = parse_markdown_sections(text)
    for heading, body in sections:
        slug = slugify(heading)
        db.add_chunk(source_id, source_path, heading, slug, body)
        stats.chunks += 1
        wiki_path = wiki_root / slugify(path.stem) / f"{slug}.md"
        write_text(
            wiki_path,
            f"---\nsource: {source_path}\nheading: {json.dumps(heading, ensure_ascii=False)}\n---\n\n{body}\n",
        )
        stats.wiki_pages += 1
    db.conn.commit()
    stats.sources += 1
    return stats


def ingest_text_file(db: KnowledgeDb, path: Path, root: Path, wiki_root: Path) -> IngestStats:
    if path.suffix.lower() == ".md":
        return ingest_markdown(db, path, root, wiki_root)
    stats = IngestStats()
    text = read_text(path)
    if path.suffix.lower() in {".html", ".htm"}:
        text = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", text)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
    source_path = relpath(path, root)
    source_id = db.upsert_source(
        path=source_path,
        kind=path.suffix.lower().lstrip(".") or "text",
        sha256=file_sha256(path),
        title=path.stem,
        meta={"format": path.suffix.lower().lstrip(".") or "text"},
    )
    chunk_size = 4200
    for index, start in enumerate(range(0, len(text), chunk_size), start=1):
        body = text[start : start + chunk_size].strip()
        if not body:
            continue
        heading = f"{path.stem} part {index}"
        db.add_chunk(source_id, source_path, heading, slugify(heading), body)
        stats.chunks += 1
        wiki_path = wiki_root / slugify(path.stem) / f"{slugify(heading)}.md"
        write_text(
            wiki_path,
            f"---\nsource: {source_path}\nheading: {json.dumps(heading, ensure_ascii=False)}\n---\n\n{body}\n",
        )
        stats.wiki_pages += 1
    db.conn.commit()
    stats.sources += 1
    return stats


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError as exc:
        raise RuntimeError("PDF support requires free package `pypdf`. Install with: python -m pip install pypdf") from exc
    reader = PdfReader(str(path))
    pages: list[str] = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"# Page {i}\n\n{text.strip()}")
    return "\n\n".join(pages).strip()


def ingest_pdf(db: KnowledgeDb, path: Path, root: Path, wiki_root: Path) -> IngestStats:
    stats = IngestStats()
    try:
        text = extract_pdf_text(path)
    except RuntimeError as exc:
        stats.add_warning(f"{relpath(path, root)} skipped: {exc}")
        return stats
    source_path = relpath(path, root)
    source_id = db.upsert_source(
        path=source_path,
        kind="pdf",
        sha256=file_sha256(path),
        title=path.stem,
        meta={"format": "pdf"},
    )
    if not text:
        stats.add_warning(f"{source_path} had no extractable text")
        return stats
    sections = parse_markdown_sections(text)
    for heading, body in sections:
        slug = slugify(f"{path.stem}-{heading}")
        db.add_chunk(source_id, source_path, heading, slug, body)
        stats.chunks += 1
        wiki_path = wiki_root / slugify(path.stem) / f"{slug}.md"
        write_text(
            wiki_path,
            f"---\nsource: {source_path}\nheading: {json.dumps(heading, ensure_ascii=False)}\n---\n\n{body}\n",
        )
        stats.wiki_pages += 1
    db.conn.commit()
    stats.sources += 1
    return stats


def ingest_csv(db: KnowledgeDb, path: Path, root: Path) -> IngestStats:
    stats = IngestStats()
    text = read_text(path)
    dialect = sniff_csv(text)
    reader = csv.DictReader(io.StringIO(text), dialect=dialect)
    headers = reader.fieldnames or []
    game = detect_game(path, headers)
    source_path = relpath(path, root)
    source_id = db.upsert_source(
        path=source_path,
        kind="semantic_csv",
        sha256=file_sha256(path),
        title=path.stem,
        meta={"headers": headers, "game": game},
    )
    rows = list(reader)
    if "Ключевое слово" in headers and "Кластер" in headers:
        grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            grouped[row.get("Кластер", "Без кластера")].append(row)
        for cluster, group in grouped.items():
            keywords = [r.get("Ключевое слово", "").strip() for r in group if r.get("Ключевое слово")]
            exact_sum = sum(number(r.get("Точная частотность")) for r in group)
            world_sum = sum(number(r.get("Частотность Весь мир")) for r in group)
            kd_values = [number(r.get("KD ТОП-5")) for r in group if r.get("KD ТОП-5")]
            avg_kd = sum(kd_values) / len(kd_values) if kd_values else None
            first = group[0]
            db.add_semantic_cluster(
                source_id=source_id,
                game=game,
                cluster=cluster,
                category=cluster.split(":")[0] if ":" in cluster else None,
                tier=first.get("Tier"),
                main_query=keywords[0] if keywords else cluster,
                frequency=world_sum,
                exact_frequency=exact_sum,
                difficulty=avg_kd,
                promotion_type=first.get("Тип продвижения melonity.gg"),
                keywords=keywords[:120],
                notes=first.get("Комментарий"),
                raw={"rows": group[:20], "row_count": len(group)},
            )
            stats.clusters += 1
    else:
        for row in rows:
            main_query = (
                row.get("Главный запрос кластера")
                or row.get("Ключевое слово")
                or row.get("query")
                or row.get("Keyword")
                or ""
            ).strip()
            cluster = (
                row.get("Категория")
                or row.get("Кластер")
                or row.get("Cluster")
                or main_query
                or "Без кластера"
            ).strip()
            db.add_semantic_cluster(
                source_id=source_id,
                game=game,
                cluster=cluster,
                category=row.get("Категория"),
                tier=row.get("Тип запросов") or row.get("Tier"),
                main_query=main_query,
                frequency=number(row.get("Суммарная частотность кластера") or row.get("Частотность Весь мир")),
                exact_frequency=number(row.get("Суммарная точная частотность") or row.get("Точная частотность")),
                difficulty=difficulty(row.get("Сложность ТОП-5") or row.get("KD ТОП-5")),
                promotion_type=row.get("Тип продвижения melonity.gg"),
                keywords=split_keywords(row.get("Все запросы кластера"), main_query),
                notes=row.get("Комментарий") or row.get("Тип запросов"),
                raw=row,
            )
            stats.clusters += 1
    db.conn.commit()
    stats.sources += 1
    return stats


def fetch_url(url: str, timeout: int = 25, *, use_reader_fallback: bool = True) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 article-factory/0.1"})
    with urlopen(req, timeout=timeout) as response:
        content_type = response.headers.get("content-type", "")
        data = response.read()
    encoding = "utf-8"
    match = re.search(r"charset=([^;\s]+)", content_type, flags=re.I)
    if match:
        encoding = match.group(1)
    text = data.decode(encoding, errors="replace")
    text = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_url_with_fallback(url: str, timeout: int = 35) -> str:
    try:
        return fetch_url(url, timeout=timeout, use_reader_fallback=False)
    except HTTPError as exc:
        if exc.code not in {401, 403, 406, 429}:
            raise
    reader_url = f"https://r.jina.ai/{url}"
    req = Request(reader_url, headers={"User-Agent": "Mozilla/5.0 article-factory/0.1"})
    with urlopen(req, timeout=timeout) as response:
        data = response.read()
    return data.decode("utf-8", errors="replace").strip()


def fetch_url_as_markdown(url: str, timeout: int = 35) -> tuple[str, str]:
    reader_url = f"https://r.jina.ai/{url}"
    req = Request(reader_url, headers={"User-Agent": "Mozilla/5.0 article-factory/0.1"})
    try:
        with urlopen(req, timeout=timeout) as response:
            data = response.read()
        text = data.decode("utf-8", errors="replace").strip()
        if text:
            return text, "jina_reader"
    except (HTTPError, URLError, TimeoutError):
        pass
    return fetch_url_with_fallback(url, timeout=timeout), "plain_text"


def title_from_materialized_text(text: str, url: str) -> str:
    for pattern in (r"(?im)^Title:\s*(.+?)\s*$", r"(?im)^#\s+(.+?)\s*$"):
        match = re.search(pattern, text)
        if match:
            title = match.group(1).strip()
            if title:
                return title
    parsed = urlparse(url)
    leaf = unquote(parsed.path.strip("/").split("/")[-1] or parsed.netloc)
    return leaf.replace("-", " ").strip() or url


def link_slug(url: str) -> str:
    parsed = urlparse(url)
    leaf = unquote(parsed.path.strip("/").split("/")[-1] or parsed.netloc)
    if not leaf or leaf.startswith("@"):
        leaf = parsed.netloc + "-" + leaf.strip("@")
    return slugify(leaf, max_len=120)


def is_published_article_url(url: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if "medium.com" not in parsed.netloc.lower():
        return False
    return bool(path and path.lower() != "@mrkhertz")


def materialized_markdown(url: str, text: str, source_list: Path, root: Path, method: str) -> str:
    title = title_from_materialized_text(text, url)
    tags = ["external_source", "local_agent_memory"]
    parsed = urlparse(url)
    if "medium.com" in parsed.netloc.lower():
        tags.append("medium")
        medium_path = parsed.path.strip("/").lower()
        if medium_path.startswith("@mrkhertz"):
            tags.append("mrkhertz")
        elif medium_path.startswith("@aurelivoines"):
            tags.append("aurelivoines")
    if is_published_article_url(url):
        tags.extend(["published_article", "do_not_duplicate_topic"])
    tag_lines = "\n".join(f"  - {json.dumps(tag, ensure_ascii=False)}" for tag in tags)
    return f"""---
memory_type: "external_source"
source_url: {json.dumps(url, ensure_ascii=False)}
source_list: {json.dumps(relpath(source_list, root), ensure_ascii=False)}
imported_at: {json.dumps(datetime.now().isoformat(timespec="seconds"), ensure_ascii=False)}
fetch_method: {json.dumps(method, ensure_ascii=False)}
do_not_duplicate_topic: {"true" if is_published_article_url(url) else "false"}
tags:
{tag_lines}
---

# {title}

> This page is a local markdown copy for agent memory. Future Codex agents should read this file instead of fetching the source URL during article work.

Source URL: {url}

{text.strip()}
"""


def materialize_link_sources(
    root: Path,
    *,
    links_file: Path | None = None,
    output_root: Path | None = None,
    force: bool = False,
) -> LinkMaterializeStats:
    stats = LinkMaterializeStats(warnings=[], outputs=[])
    target_root = output_root or (root / MATERIALIZED_LINK_ROOT)
    for link_file in iter_link_source_files(root, links_file):
        urls = parse_links_file(link_file)
        if not urls:
            continue
        stats.files += 1
        group_dir = target_root / slugify(link_file.stem)
        for url in urls:
            output_path = group_dir / f"{link_slug(url)}.md"
            if output_path.exists() and not force:
                stats.skipped += 1
                stats.add_output(output_path, root)
                continue
            try:
                text, method = fetch_url_as_markdown(url)
            except (HTTPError, URLError, TimeoutError, RuntimeError) as exc:
                stats.add_warning(f"Could not materialize {url}: {exc}")
                continue
            write_text(output_path, materialized_markdown(url, text, link_file, root, method))
            stats.fetched += 1
            stats.add_output(output_path, root)
    return stats


def iter_link_source_files(root: Path, explicit_links_file: Path | None = None) -> list[Path]:
    files: list[Path] = []
    for rel_dir in LINK_SOURCE_DIRS:
        directory = root / rel_dir
        if directory.exists():
            files.extend(sorted(path for path in directory.rglob("*.txt") if path.is_file()))
    if explicit_links_file and explicit_links_file.exists():
        files.append(explicit_links_file)
    deduped: list[Path] = []
    seen = set()
    for path in files:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        deduped.append(path)
    return deduped


def parse_links_file(path: Path) -> list[str]:
    urls: list[str] = []
    for line in read_text(path).splitlines():
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if "|" in text:
            text = text.split("|", 1)[0].strip()
        if text.startswith("http://") or text.startswith("https://"):
            urls.append(text)
    return urls


def ingest_url(db: KnowledgeDb, url: str) -> IngestStats:
    stats = IngestStats()
    try:
        text = fetch_url_with_fallback(url)
    except URLError as exc:
        stats.add_warning(f"Could not fetch {url}: {exc}")
        return stats
    source_id = db.upsert_source(
        path=url,
        kind="url",
        sha256=text_sha256(text),
        title=url,
        meta={"url": url},
    )
    for i in range(0, len(text), 4500):
        body = text[i : i + 4500]
        heading = f"{url} part {math.floor(i / 4500) + 1}"
        db.add_chunk(source_id, url, heading, slugify(heading), body)
        stats.chunks += 1
    db.conn.commit()
    stats.sources += 1
    return stats


def should_ignore(path: Path, root: Path) -> bool:
    rel = relpath(path, root)
    if any(part.startswith(".") and part != ".article-factory" for part in Path(rel).parts):
        return True
    return any(rel == item or rel.startswith(item.rstrip("/") + "/") for item in DEFAULT_IGNORES)


def ingest_workspace(
    db_path: Path,
    root: Path,
    *,
    rebuild: bool = False,
    links_file: Path | None = None,
) -> IngestStats:
    db = KnowledgeDb(db_path)
    if rebuild:
        db.reset()
    else:
        db.init()
    wiki_root = root / "knowledge" / "wiki"
    total = IngestStats(warnings=[])
    for source in db.conn.execute("SELECT id,path FROM sources").fetchall():
        if source["path"].startswith(("http://", "https://")):
            continue
        source_path = root / source["path"]
        if not source_path.is_file() or should_ignore(source_path, root):
            db.remove_source(source["id"])
    db.conn.commit()
    materialized = materialize_link_sources(root, links_file=links_file)
    if materialized.warnings:
        total.warnings.extend(materialized.warnings)
    for path in sorted(root.rglob("*")):
        if should_ignore(path, root) or not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in TEXT_EXTENSIONS:
            stats = ingest_text_file(db, path, root, wiki_root)
        elif suffix in CSV_EXTENSIONS:
            stats = ingest_csv(db, path, root)
        elif suffix in PDF_EXTENSIONS:
            stats = ingest_pdf(db, path, root, wiki_root)
        else:
            continue
        total.sources += stats.sources
        total.chunks += stats.chunks
        total.clusters += stats.clusters
        total.wiki_pages += stats.wiki_pages
    db.close()
    return total
