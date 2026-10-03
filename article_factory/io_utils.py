from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import Path


TEXT_ENCODINGS = ("utf-8-sig", "utf-8", "cp1251", "windows-1251", "latin-1")


def read_text(path: Path) -> str:
    data = path.read_bytes()
    last_error: Exception | None = None
    for encoding in TEXT_ENCODINGS:
        try:
            return data.decode(encoding)
        except UnicodeDecodeError as exc:
            last_error = exc
    if last_error:
        raise last_error
    return data.decode("utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slugify(value: str, max_len: int = 96) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.lower().replace("ё", "е")
    value = re.sub(r"[^\w\s-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_]+", "-", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value).strip("-")
    if not value:
        value = "item"
    return value[:max_len].strip("-") or "item"


def relpath(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def clamp_words(text: str, max_words: int) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text.strip()
    return " ".join(words[:max_words]).strip() + "..."
