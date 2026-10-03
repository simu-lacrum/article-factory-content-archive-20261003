"""Export Article Factory Markdown into Tumblr-ready Markdown and HTML.

The source articles contain publishing metadata and editorial image notes that
should not be pasted into Tumblr.  This module removes those private layers and
converts the remaining, deliberately small Markdown subset to basic HTML.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


FRONT_MATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
INTERNAL_LINK_SECTION_RE = re.compile(
    r"^##\s+Internal-link suggestions\s*$.*?(?=^##\s+|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")


def clean_markdown(source: str) -> str:
    """Return public article copy without metadata or editorial-only notes."""

    text = source.replace("\r\n", "\n").replace("\r", "\n")
    text = FRONT_MATTER_RE.sub("", text, count=1)
    text = HTML_COMMENT_RE.sub("", text)
    text = INTERNAL_LINK_SECTION_RE.sub("", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def _inline_markdown(text: str) -> str:
    """Convert the inline syntax used by the article set to safe HTML."""

    tokens: list[str] = []

    def save_token(value: str) -> str:
        tokens.append(value)
        return f"\x00{len(tokens) - 1}\x00"

    def replace_code(match: re.Match[str]) -> str:
        return save_token(f"<code>{html.escape(match.group(1))}</code>")

    def replace_link(match: re.Match[str]) -> str:
        label = html.escape(match.group(1), quote=False)
        href = html.escape(match.group(2), quote=True)
        return save_token(f'<a href="{href}">{label}</a>')

    text = re.sub(r"`([^`]+)`", replace_code, text)
    text = LINK_RE.sub(replace_link, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    for index, token in enumerate(tokens):
        text = text.replace(f"\x00{index}\x00", token)
    return text


def markdown_to_html(markdown: str) -> str:
    """Convert clean article Markdown to a basic Tumblr-safe HTML fragment."""

    output: list[str] = []
    paragraph: list[str] = []
    list_kind: str | None = None

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{_inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind is not None:
            output.append(f"</{list_kind}>")
            list_kind = None

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line:
            flush_paragraph()
            close_list()
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            output.append(f"<h{level}>{_inline_markdown(heading.group(2))}</h{level}>")
            continue

        unordered = re.match(r"^[-*]\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            wanted_kind = "ul" if unordered else "ol"
            if list_kind != wanted_kind:
                close_list()
                list_kind = wanted_kind
                output.append(f"<{list_kind}>")
            item = (unordered or ordered).group(1)  # type: ignore[union-attr]
            output.append(f"<li>{_inline_markdown(item)}</li>")
            continue

        if line.startswith("> "):
            flush_paragraph()
            close_list()
            output.append(f"<blockquote>{_inline_markdown(line[2:])}</blockquote>")
            continue

        close_list()
        paragraph.append(line)

    flush_paragraph()
    close_list()
    return "\n".join(output).strip() + "\n"


def _title_from_markdown(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def _stats(markdown: str) -> dict[str, int]:
    return {
        "words": len(re.findall(r"\b[\w’'-]+\b", markdown, re.UNICODE)),
        "headings": len(re.findall(r"^#{1,3}\s+", markdown, re.MULTILINE)),
        "unordered_items": len(re.findall(r"^[-*]\s+", markdown, re.MULTILINE)),
        "ordered_items": len(re.findall(r"^\d+\.\s+", markdown, re.MULTILINE)),
        "links": len(LINK_RE.findall(markdown)),
    }


def export_articles(source_dir: Path, output_dir: Path) -> dict[str, object]:
    """Export every Markdown file in *source_dir* into two Tumblr formats."""

    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    markdown_dir = output_dir / "markdown"
    html_dir = output_dir / "html"
    markdown_dir.mkdir(parents=True, exist_ok=True)
    html_dir.mkdir(parents=True, exist_ok=True)

    articles: list[dict[str, object]] = []
    for source_path in sorted(source_dir.glob("*.md")):
        cleaned = clean_markdown(source_path.read_text(encoding="utf-8"))
        converted = markdown_to_html(cleaned)
        markdown_path = markdown_dir / source_path.name
        html_path = html_dir / f"{source_path.stem}.html"
        markdown_path.write_text(cleaned, encoding="utf-8", newline="\n")
        html_path.write_text(converted, encoding="utf-8", newline="\n")
        articles.append(
            {
                "title": _title_from_markdown(cleaned, source_path.stem),
                "source": str(source_path),
                "markdown": str(markdown_path),
                "html": str(html_path),
                **_stats(cleaned),
            }
        )

    manifest: dict[str, object] = {
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "article_count": len(articles),
        "articles": articles,
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    index_lines = ["# Tumblr-ready article exports", ""]
    for article in articles:
        markdown_name = Path(str(article["markdown"])).name
        html_name = Path(str(article["html"])).name
        index_lines.extend(
            [
                f"## {article['title']}",
                "",
                f"- [Markdown](markdown/{markdown_name})",
                f"- [HTML](html/{html_name})",
                "",
            ]
        )
    (output_dir / "INDEX.md").write_text(
        "\n".join(index_lines).rstrip() + "\n", encoding="utf-8", newline="\n"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create clean Markdown and basic HTML copies for Tumblr."
    )
    parser.add_argument("--source", type=Path, required=True, help="Article directory")
    parser.add_argument("--output", type=Path, required=True, help="Export directory")
    args = parser.parse_args()

    if not args.source.is_dir():
        parser.error(f"source directory does not exist: {args.source}")
    manifest = export_articles(args.source, args.output)
    print(json.dumps({"status": "PASS", "article_count": manifest["article_count"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
