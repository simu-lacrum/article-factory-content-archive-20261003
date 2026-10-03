from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from article_factory.tumblr_export import clean_markdown, markdown_to_html

PACKAGE = Path(__file__).resolve().parents[1]
MD_DIR = PACKAGE / "md"
HTML_DIR = PACKAGE / "html"
REF_SOURCE = ROOT / "knowledge/agent_memory/references/article-editorial-warm-story-v1"
REF_DEST = PACKAGE / "references/article-editorial-warm-story-v1"

FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
IMAGE = re.compile(r"<!--\s*IMAGE_SLOT_(\d+)\s*\n(.*?)-->", re.S)


def field(front: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$", front)
    return match.group(1).strip().strip('"\'') if match else ""


def wrapper(title: str, description: str, article_html: str, slots: list[tuple[str, str]]) -> str:
    slot_html = "\n".join(
        f'<details{" open" if i == 0 else ""}><summary>Image slot {html.escape(num)}</summary>'
        f'<pre>{html.escape(content.strip())}</pre></details>'
        for i, (num, content) in enumerate(slots)
    )
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<style>
:root{{--blue:#2B58FF;--deep:#001FD4;--ink:#0E0E10;--paper:#F2F2F2;--green:#6DB33F;--violet:#635FD5}}
*{{box-sizing:border-box}}body{{margin:0;background:#e8e8ea;color:var(--ink);font-family:Inter,Arial,sans-serif;line-height:1.62}}
.toolbar{{position:sticky;top:0;z-index:9;display:flex;gap:12px;align-items:center;padding:12px 18px;background:var(--ink);color:white}}
.toolbar button{{border:0;border-radius:9px;background:var(--blue);color:white;font-weight:800;padding:11px 16px;cursor:pointer}}.toolbar button:hover{{background:var(--deep)}}
.status{{font:600 12px/1.2 ui-monospace,Consolas,monospace;text-transform:uppercase;letter-spacing:.05em}}
.shell{{max-width:980px;margin:28px auto;padding:0 18px}}article{{background:white;border-radius:20px;padding:clamp(24px,5vw,64px);box-shadow:0 12px 36px #0002}}
h1,h2,h3{{line-height:1.16}}h1{{font-size:clamp(34px,5vw,58px);margin-top:0}}h2{{margin-top:2.2em;border-top:4px solid var(--blue);padding-top:.6em}}h3{{margin-top:1.5em}}
blockquote{{margin:28px 0;padding:18px 22px;border-left:6px solid var(--violet);background:var(--paper);border-radius:0 14px 14px 0}}a{{color:var(--deep);font-weight:700}}li{{margin:.45em 0}}
.production{{margin-top:28px;background:var(--ink);color:white;border-radius:20px;padding:24px}}.production h2{{border:0;margin-top:0}}details{{margin:12px 0;background:#1c1c22;border-radius:14px;padding:12px}}summary{{cursor:pointer;font-weight:800}}pre{{white-space:pre-wrap;word-break:break-word;font-size:12px;line-height:1.45;color:#f7f7f7}}
@media(max-width:600px){{.toolbar{{align-items:flex-start;flex-direction:column}}article{{border-radius:14px;padding:24px}}}}
</style>
</head>
<body>
<div class="toolbar"><button id="copy-button" type="button">Copy formatted article</button><span class="status" id="copy-status">Ready for JustPaste</span></div>
<main class="shell">
<article id="article" aria-label="{html.escape(title, quote=True)}">
{article_html.rstrip()}
</article>
<section class="production"><h2>Image production brief</h2><p>These notes are not included when the article button is used.</p>{slot_html}</section>
</main>
<script>
const button=document.getElementById('copy-button');const status=document.getElementById('copy-status');const article=document.getElementById('article');
function fallbackCopy(){{const selection=window.getSelection();selection.removeAllRanges();const range=document.createRange();range.selectNodeContents(article);selection.addRange(range);const ok=document.execCommand('copy');selection.removeAllRanges();if(!ok)throw new Error('copy command failed')}}
button.addEventListener('click',async()=>{{try{{const rich=article.innerHTML;const plain=article.innerText;if(navigator.clipboard&&window.ClipboardItem&&window.isSecureContext){{await navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([rich],{{type:'text/html'}}),'text/plain':new Blob([plain],{{type:'text/plain'}})}})])}}else{{fallbackCopy()}}status.textContent='Copied — paste into JustPaste';button.textContent='Copied'}}catch(error){{try{{fallbackCopy();status.textContent='Copied — paste into JustPaste';button.textContent='Copied'}}catch(fallbackError){{status.textContent='Copy blocked — select the article manually'}}}}setTimeout(()=>{{button.textContent='Copy formatted article'}},2200)}});
</script>
</body>
</html>
'''


def build() -> None:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    REF_DEST.mkdir(parents=True, exist_ok=True)
    for name in ["reference-03.png", "reference-04.png", "reference-05.png", "reference-06.png", "reference-07.png", "reference-08.png"]:
        shutil.copy2(REF_SOURCE / name, REF_DEST / name)
    shutil.copy2(REF_SOURCE / "README.md", REF_DEST / "README.md")

    records = []
    for path in sorted(MD_DIR.glob("CG-*.md")):
        raw = path.read_text(encoding="utf-8")
        fm = FRONT.search(raw)
        front = fm.group(1) if fm else ""
        title = field(front, "title") or path.stem
        description = field(front, "description")
        public_md = clean_markdown(raw)
        public_html = markdown_to_html(public_md)
        slots = IMAGE.findall(raw)
        out = HTML_DIR / f"{path.stem}.html"
        out.write_text(wrapper(title, description, public_html, slots), encoding="utf-8", newline="\n")
        words = len(re.findall(r"\b[A-Za-z][A-Za-z’'-]*\b", public_md))
        records.append({
            "id": path.stem.split("-", 2)[0] + "-" + path.stem.split("-", 2)[1],
            "title": title,
            "description": description,
            "slug": path.stem.split("-", 2)[2],
            "markdown": f"md/{path.name}",
            "html": f"html/{out.name}",
            "words": words,
            "image_slots": len(slots),
        })

    manifest = {
        "package": "CHEATSGAMING-T2-57-20260908-DEADLOCK",
        "generated": "2026-09-08",
        "language": "en",
        "game": "Deadlock",
        "article_count": len(records),
        "articles": records,
    }
    (PACKAGE / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    cards = []
    for rec in records:
        cards.append(f'''<li><strong>{html.escape(rec["id"])} — {html.escape(rec["title"])}</strong><span>{rec["words"]} words · {rec["image_slots"]} image slots</span><a href="{html.escape(rec["html"])}">Open copy-ready HTML</a><a href="{html.escape(rec["markdown"])}">Markdown source</a></li>''')
    index = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Deadlock article package</title><style>:root{{--b:#2B58FF;--v:#635FD5;--i:#0E0E10;--p:#F2F2F2}}*{{box-sizing:border-box}}body{{margin:0;background:var(--p);color:var(--i);font-family:Inter,Arial,sans-serif}}main{{max-width:1050px;margin:auto;padding:48px 20px}}h1{{font-size:clamp(36px,6vw,68px);line-height:1}}p{{max-width:760px;line-height:1.6}}ul{{list-style:none;padding:0;display:grid;gap:14px}}li{{background:white;border-left:8px solid var(--v);border-radius:14px;padding:18px;display:grid;gap:8px}}li span{{color:#555}}a{{color:#001FD4;font-weight:800}}</style></head><body><main><h1>Deadlock article package</h1><p>15 SEO/GEO-ready articles. Open any HTML file and use the sticky <b>Copy formatted article</b> button. Image briefs remain visible below the article and are excluded from the copied body.</p><ul>{''.join(cards)}</ul></main></body></html>'''
    (PACKAGE / "index.html").write_text(index, encoding="utf-8", newline="\n")

    # Article Factory's visual-sequence review continues from the preceding
    # HOME/CS2 package, which owns indices 001-027.
    review_items = []
    evidence_dir = ROOT / "output/evidence/CHEATSGAMING-T2-57-20260908-DEADLOCK"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    shared_evidence = [
        {"source": "output/briefs/CHEATSGAMING-T2-57-20260908/02-DEADLOCK-BRIEFS.md", "role": "article brief and query intent"},
        {"source": "output/briefs/CHEATSGAMING-T2-57-20260908/04-VISUAL-PROMPTS.md", "role": "visual sequence and art direction"},
        {"source": "knowledge/agent_memory/products/deadlock-cluster-center-internal.md", "role": "documented Deadlock product taxonomy"},
        {"source": "knowledge/agent_memory/rules/article-visual-prompt-guide.md", "role": "canonical prompt contract"},
    ]
    for article_path in sorted(MD_DIR.glob("CG-*.md")):
        article_raw = article_path.read_text(encoding="utf-8")
        article_fm = FRONT.search(article_raw)
        article_front = article_fm.group(1) if article_fm else ""
        evidence_path = evidence_dir / f"{article_path.stem}.json"
        evidence_path.write_text(json.dumps({"evidence": shared_evidence}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        review_items.append({
            "topic_id": article_path.stem.split("-", 2)[1],
            "title": field(article_front, "title") or article_path.stem,
            "game": field(article_front, "game"),
            "language": field(article_front, "language") or "en",
            "status": "article",
            "output": str(article_path.resolve()),
            "evidence": str(evidence_path.resolve()),
        })
    review_manifest = {
        "created_at": "CHEATSGAMING-T2-57-20260908-DEADLOCK",
        "spec": {"raw": "Review the completed T2 run through Deadlock CG-042."},
        "llm_provider": "codex",
        "model": "codex",
        "visual_sequence_start": 28,
        "items": review_items,
    }
    review_path = ROOT / "output/runs/CHEATSGAMING-T2-57-20260908-DEADLOCK.json"
    review_path.write_text(json.dumps(review_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    checksums = []
    for file in sorted(p for p in PACKAGE.rglob("*") if p.is_file() and p.name not in {"SHA256SUMS.txt", "build_package.py"}):
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        checksums.append(f"{digest}  {file.relative_to(PACKAGE).as_posix()}")
    (PACKAGE / "SHA256SUMS.txt").write_text("\n".join(checksums) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    build()
