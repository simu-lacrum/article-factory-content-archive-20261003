"""Export Article Factory Markdown into JustPaste.it-ready HTML fragments.

The exporter keeps the public article body, converts its small Markdown subset
to conservative HTML, and inserts image URL placeholders from the production
prompts stored in the editorial specification.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from .tumblr_export import clean_markdown, markdown_to_html


IMAGE_BLOCK_RE = re.compile(
    r"^### Изображение (?P<index>\d+) — (?P<role>cover|inline)\s*\n\s*"
    r"- Placement: (?P<placement>.*?)\n"
    r"- Alt: (?P<alt>.*?)\n"
    r"- Prompt: (?P<prompt>.*?)(?=\n(?:---|###))",
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class ImageSlot:
    index: int
    role: str
    placement: str
    alt: str
    prompt: str
    filename: str = ""
    prompt_file: str = ""
    url_token: str = ""


def parse_image_slots(spec_text: str) -> list[ImageSlot]:
    normalized = spec_text.replace("\r\n", "\n").replace("\r", "\n")
    slots: list[ImageSlot] = []
    for match in IMAGE_BLOCK_RE.finditer(normalized):
        slots.append(
            ImageSlot(
                index=int(match.group("index")),
                role=match.group("role").strip(),
                placement=match.group("placement").strip(),
                alt=match.group("alt").strip(),
                prompt=match.group("prompt").strip(),
            )
        )
    return slots


def _public_stem(source_path: Path) -> str:
    return re.sub(r"^\d+-", "", source_path.stem)


def _with_output_names(slot: ImageSlot, source_path: Path) -> ImageSlot:
    stem = _public_stem(source_path)
    filename = f"image-{slot.index:02d}-{stem}-{slot.role}.png"
    prompt_file = f"image-{slot.index:02d}-{stem}-{slot.role}-prompt.txt"
    return ImageSlot(
        index=slot.index,
        role=slot.role,
        placement=slot.placement,
        alt=slot.alt,
        prompt=slot.prompt,
        filename=filename,
        prompt_file=prompt_file,
        url_token=f"IMAGE_{slot.index:02d}_URL",
    )


def _figure_html(slot: ImageSlot) -> str:
    alt = html.escape(slot.alt, quote=True)
    comment = html.escape(
        f"Upload {slot.filename}, then replace {slot.url_token} with its JustPaste image URL",
        quote=False,
    )
    return (
        f"<!-- {comment} -->\n"
        f'<figure><img src="{slot.url_token}" alt="{alt}" /></figure>'
    )


def _inline_heading(placement: str) -> str:
    marker = re.search(r"H2\s+(.+?)\.?$", placement.strip())
    if not marker:
        raise ValueError(f"cannot extract H2 placement from: {placement}")
    return marker.group(1).rstrip(".").strip().strip("`")


def insert_image_slots(article_html: str, slots: list[ImageSlot]) -> str:
    cover = next((slot for slot in slots if slot.role == "cover"), None)
    inline = next((slot for slot in slots if slot.role == "inline"), None)
    if cover is None or inline is None:
        raise ValueError("each article requires one cover and one inline image slot")

    cover_figure = _figure_html(cover)
    article_html, cover_count = re.subn(
        r"(</h1>)",
        rf"\1\n{cover_figure}",
        article_html,
        count=1,
    )
    if cover_count != 1:
        raise ValueError("cover placement failed: article H1 not found")

    heading = _inline_heading(inline.placement)
    heading_html = f"<h2>{html.escape(heading, quote=False)}</h2>"
    if heading_html not in article_html:
        raise ValueError(f"inline placement heading not found: {heading}")
    article_html = article_html.replace(
        heading_html,
        f"{heading_html}\n{_figure_html(inline)}",
        1,
    )
    return article_html.rstrip() + "\n"


def _title_from_html(article_html: str, fallback: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", article_html, re.DOTALL)
    return html.unescape(match.group(1)).strip() if match else fallback


def export_justpaste(source_dir: Path, spec_path: Path, output_dir: Path) -> dict[str, object]:
    source_dir = source_dir.resolve()
    spec_path = spec_path.resolve()
    output_dir = output_dir.resolve()
    html_dir = output_dir / "html"
    prompt_dir = output_dir / "image-prompts"
    html_dir.mkdir(parents=True, exist_ok=True)
    prompt_dir.mkdir(parents=True, exist_ok=True)

    source_files = sorted(source_dir.glob("*.md"))
    parsed_slots = parse_image_slots(spec_path.read_text(encoding="utf-8"))
    if not source_files:
        raise ValueError("no source articles found")
    expected_prompt_count = len(source_files) * 2
    if len(parsed_slots) != expected_prompt_count:
        raise ValueError(
            f"expected {expected_prompt_count} image prompts for {len(source_files)} "
            f"articles, found {len(parsed_slots)}"
        )

    articles: list[dict[str, object]] = []
    for article_index, source_path in enumerate(source_files):
        raw_markdown = source_path.read_text(encoding="utf-8")
        public_markdown = clean_markdown(raw_markdown)
        base_html = markdown_to_html(public_markdown)
        article_slots = [
            _with_output_names(slot, source_path)
            for slot in parsed_slots[article_index * 2 : article_index * 2 + 2]
        ]
        final_html = insert_image_slots(base_html, article_slots)
        html_path = html_dir / f"{source_path.stem}.html"
        html_path.write_text(final_html, encoding="utf-8", newline="\n")

        for slot in article_slots:
            prompt_text = "\n".join(
                [
                    f"Image ID: {slot.index:02d}",
                    f"Article: {source_path.name}",
                    f"Role: {slot.role}",
                    f"Placement: {slot.placement}",
                    f"Alt: {slot.alt}",
                    f"Suggested output filename: {slot.filename}",
                    "",
                    "Prompt:",
                    slot.prompt,
                    "",
                ]
            )
            (prompt_dir / slot.prompt_file).write_text(
                prompt_text, encoding="utf-8", newline="\n"
            )

        articles.append(
            {
                "title": _title_from_html(final_html, source_path.stem),
                "source": str(source_path),
                "html": str(html_path),
                "image_slots": [asdict(slot) for slot in article_slots],
            }
        )

    manifest: dict[str, object] = {
        "format": "justpaste-html-fragment",
        "source_dir": str(source_dir),
        "spec_path": str(spec_path),
        "output_dir": str(output_dir),
        "article_count": len(articles),
        "image_prompt_count": len(parsed_slots),
        "articles": articles,
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    index_lines = [
        "# JustPaste.it HTML package",
        "",
        "Each HTML file is a body fragment for the JustPaste.it HTML editor.",
        "Generate or upload each named image, then replace its IMAGE_XX_URL token with the hosted image URL.",
        "",
    ]
    for article in articles:
        html_name = Path(str(article["html"])).name
        index_lines.extend([f"## {article['title']}", "", f"- [HTML](html/{html_name})"])
        for slot_data in article["image_slots"]:  # type: ignore[union-attr]
            slot = ImageSlot(**slot_data)
            index_lines.append(
                f"- Image {slot.index:02d} ({slot.role}): "
                f"[prompt](image-prompts/{slot.prompt_file}) — token `{slot.url_token}`"
            )
        index_lines.append("")
    (output_dir / "INDEX.md").write_text(
        "\n".join(index_lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create JustPaste.it HTML fragments with image prompt slots."
    )
    parser.add_argument("--source", type=Path, required=True, help="Article directory")
    parser.add_argument("--spec", type=Path, required=True, help="Editorial specification")
    parser.add_argument("--output", type=Path, required=True, help="Export directory")
    args = parser.parse_args()

    if not args.source.is_dir():
        parser.error(f"source directory does not exist: {args.source}")
    if not args.spec.is_file():
        parser.error(f"spec file does not exist: {args.spec}")
    manifest = export_justpaste(args.source, args.spec, args.output)
    print(
        json.dumps(
            {
                "status": "PASS",
                "article_count": manifest["article_count"],
                "image_prompt_count": manifest["image_prompt_count"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
