from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "publish" / "20260910-t2-27"


def parse_article(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    metadata: dict[str, str] = {}
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    if match:
        for line in match.group(1).splitlines():
            field = re.match(r"^([a-zA-Z_][\w-]*):\s*(.*)$", line)
            if not field:
                continue
            value = field.group(2).strip().strip('"').strip("'")
            metadata[field.group(1)] = value
        text = text[match.end() :]
    text = re.sub(r"<!--\s*IMAGE_PLACEMENT_NOTES.*?-->", "", text, flags=re.S)
    text = re.sub(r"<!--\s*IMAGE_SLOT_\d+.*?-->", "", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return metadata, text


def inline_markup(value: str) -> str:
    images: list[str] = []

    def store_image(match: re.Match[str]) -> str:
        alt = html.escape(match.group(1), quote=True)
        url = html.escape(match.group(2), quote=True)
        images.append(f'<figure><img src="{url}" alt="{alt}"></figure>')
        return f"\x00IMG{len(images) - 1}\x00"

    value = re.sub(r"!\[([^\]]*)\]\((https?://[^)]+)\)", store_image, value)
    value = html.escape(value, quote=False)
    value = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        value,
    )
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    for index, item in enumerate(images):
        value = value.replace(f"\x00IMG{index}\x00", item)
    return value


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_type: str | None = None

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(f"<p>{inline_markup(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items, list_type
        if list_items:
            tag = list_type or "ul"
            blocks.append(f"<{tag}>" + "".join(f"<li>{inline_markup(item)}</li>" for item in list_items) + f"</{tag}>")
            list_items = []
            list_type = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_list()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        bullet = re.match(r"^-\s+(.+)$", stripped)
        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        image_only = re.fullmatch(r"!\[[^\]]*\]\(https?://[^)]+\)", stripped)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{inline_markup(heading.group(2))}</h{level}>")
        elif image_only:
            flush_paragraph()
            flush_list()
            blocks.append(inline_markup(stripped))
        elif bullet:
            flush_paragraph()
            if list_type not in (None, "ul"):
                flush_list()
            list_type = "ul"
            list_items.append(bullet.group(1))
        elif ordered:
            flush_paragraph()
            if list_type not in (None, "ol"):
                flush_list()
            list_type = "ol"
            list_items.append(ordered.group(1))
        else:
            flush_list()
            paragraph.append(stripped)
    flush_paragraph()
    flush_list()
    return "\n".join(blocks) + "\n"


def read_manifest(run_id: str) -> list[dict]:
    path = ROOT / "output" / "runs" / f"{run_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))["items"]


def main() -> None:
    english = read_manifest("20260910-082336")
    russian = read_manifest("20260910-084742")
    allocations = {
        "substack": english[0:2] + russian[0:3],
        "notion": english[2:4] + russian[3:6],
        "gitbook": english[4:6] + russian[6:9],
        "github": english[6:8] + russian[9:12],
        "justpasteme": english[8:10] + russian[12:15],
        "rentry": english[10:12],
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    publish_manifest = {"created_at": "2026-09-10", "total": 27, "platforms": {}}
    for platform, items in allocations.items():
        platform_dir = OUTPUT / platform
        platform_dir.mkdir(parents=True, exist_ok=True)
        records = []
        for sequence, item in enumerate(items, start=1):
            source_path = Path(item["output"])
            metadata, markdown = parse_article(source_path)
            stem = metadata.get("slug") or source_path.stem
            markdown_path = platform_dir / f"{sequence:02d}-{stem}.md"
            html_path = platform_dir / f"{sequence:02d}-{stem}.html"
            markdown_path.write_text(markdown, encoding="utf-8")
            html_path.write_text(markdown_to_html(markdown), encoding="utf-8")
            records.append(
                {
                    "source": str(source_path),
                    "markdown": str(markdown_path),
                    "html": str(html_path),
                    "title": metadata.get("title", item["title"]),
                    "seo_title": metadata.get("seo_title", metadata.get("title", item["title"])),
                    "description": metadata.get("description", ""),
                    "slug": stem,
                    "language": metadata.get("language", item.get("language", "")),
                    "game": metadata.get("game", item.get("game", "")),
                    "target_url": metadata.get("target_url", ""),
                    "target_anchor": metadata.get("target_anchor", ""),
                    "status": "ready",
                }
            )
        publish_manifest["platforms"][platform] = records
    (OUTPUT / "manifest.json").write_text(
        json.dumps(publish_manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"output": str(OUTPUT), "counts": {k: len(v) for k, v in allocations.items()}, "total": 27}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
