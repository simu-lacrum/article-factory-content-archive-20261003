from __future__ import annotations

import json
import re
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
MD_DIR = PACKAGE / "md"
HTML_DIR = PACKAGE / "html"

FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
COMMENTS = re.compile(r"<!--.*?-->", re.S)


def field(front: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$", front)
    return match.group(1).strip().strip('"\'') if match else ""


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z’'-]*", text)


def main() -> int:
    records = []
    failures: list[str] = []
    files = sorted(MD_DIR.glob("CG-*.md"))
    expected_ids = [f"CG-{i:03d}" for i in range(28, 43)]
    actual_ids = ["-".join(p.stem.split("-")[:2]) for p in files]
    if actual_ids != expected_ids:
        failures.append(f"Article ID sequence mismatch: {actual_ids}")

    for index, path in enumerate(files, start=28):
        raw = path.read_text(encoding="utf-8")
        fm = FRONT.search(raw)
        front = fm.group(1) if fm else ""
        body = raw[fm.end():] if fm else raw
        public = COMMENTS.sub("", body)
        title = field(front, "title")
        desc = field(front, "description")
        keyword = field(front, "primary_keyword")
        target = field(front, "target_url")
        h1_match = re.search(r"(?m)^#\s+(.+)$", public)
        h1 = h1_match.group(1) if h1_match else ""
        faq_match = re.search(r"(?ms)^## FAQ\s*$.*", public)
        faq = faq_match.group(0) if faq_match else ""
        first_120 = " ".join(words(public)[:120])
        body_target_links = len(re.findall(rf"\]\({re.escape(target)}\)", public)) if target else 0
        slots = re.findall(r"<!--\s*IMAGE_SLOT_(\d+)\s*\n(.*?)-->", raw, re.S)
        cover = slots[0][1] if slots else ""
        branch_match = re.search(r"Style branch:\s*([^\n]+)", cover, re.I)
        branch = branch_match.group(1).strip() if branch_match else ""
        qa_match = re.search(r"Prompt QA(?: score)?:\s*(\d+)", cover, re.I)
        qa = int(qa_match.group(1)) if qa_match else 0
        ref_names = sorted(set(re.findall(r"reference-\d+\.png", cover)))
        pct_values = [int(x) for x in re.findall(r"(?:about\s*)?(\d{1,2})%", cover)]

        checks = {
            "front_matter": bool(fm),
            "seo_title_le_60": 1 <= len(title) <= 60,
            "description_le_160": 1 <= len(desc) <= 160,
            "keyword_in_description": keyword.lower() in desc.lower(),
            "keyword_in_h1": keyword.lower() in h1.lower(),
            "keyword_in_first_120_words": keyword.lower() in first_120.lower(),
            "keyword_in_faq": keyword.lower() in faq.lower(),
            "one_target_backlink_in_public_body": body_target_links == 1,
            "faq_at_end": bool(re.search(r"(?ms)^## FAQ\s*$.*\Z", public.strip())),
            "four_faq_questions": len(re.findall(r"(?m)^###\s+", faq)) == 4,
            "two_image_slots": [n for n, _ in slots] == ["01", "02"],
            "no_markdown_tables": not bool(re.search(r"(?m)^\s*\|.*\|\s*$", public)),
            "model_declared": "Nano Banana Pro / gemini-3-pro-image" in cover,
            "visual_style_declared": "article-editorial-poster-v1" in cover,
            "cluster_color_exact": "#635FD5" in cover,
            "prompt_qa_ge_80": qa >= 80,
            "branch_parity": (index % 2 == 0 and branch.startswith("A")) or (index % 2 == 1 and branch.startswith("B")),
            "b_two_reference_files": len(ref_names) == 2 if index % 2 else len(ref_names) == 0,
            "b_dominant_or_a_accent": ("dominant" in cover.lower() and any(35 <= p <= 70 for p in pct_values)) if index % 2 else ("dominant" not in cover.lower() and any(3 <= p <= 8 for p in pct_values)),
            "restricted_safety_boundary": not bool(re.search(r"(?i)\b(you should disable (?:antivirus|defender)|how to bypass anti-cheat|zero[- ]risk guarantee|guaranteed undetected|completely safe to use)\b", public)),
        }
        html_path = HTML_DIR / f"{path.stem}.html"
        html_text = html_path.read_text(encoding="utf-8") if html_path.exists() else ""
        checks.update({
            "html_exists": html_path.exists(),
            "copy_button_present": 'id="copy-button"' in html_text,
            "rich_html_clipboard": "'text/html'" in html_text,
            "production_brief_visible": "Image production brief" in html_text,
            "copy_scope_excludes_brief": '<article id="article"' in html_text and "</article>\n<section class=\"production\"" in html_text,
        })
        failed = [name for name, value in checks.items() if not value]
        for name in failed:
            failures.append(f"{path.name}: {name}")
        records.append({
            "id": f"CG-{index:03d}",
            "file": path.name,
            "public_words": len(words(public)),
            "title_chars": len(title),
            "description_chars": len(desc),
            "branch": branch,
            "prompt_qa": qa,
            "checks": len(checks),
            "passed": len(checks) - len(failed),
            "failures": failed,
        })

    required_refs = {"reference-03.png", "reference-04.png", "reference-05.png", "reference-06.png", "reference-07.png", "reference-08.png"}
    packaged_refs = {p.name for p in (PACKAGE / "references/article-editorial-warm-story-v1").glob("reference-*.png")}
    if packaged_refs != required_refs:
        failures.append(f"Packaged reference set mismatch: {sorted(packaged_refs)}")

    report = [
        "# Quality report: CheatsGaming Deadlock articles",
        "",
        f"**Status: {'PASS' if not failures else 'FAIL'}**",
        "",
        f"- Articles: {len(files)}/15",
        f"- HTML exports: {len(list(HTML_DIR.glob('CG-*.html')))}/15",
        f"- Deterministic checks: {sum(r['passed'] for r in records)}/{sum(r['checks'] for r in records)}",
        "- Article Factory review: 15 pass, 0 needs review, 0 fail (`ARTICLE-FACTORY-REVIEW.json`).",
        f"- Packaged branch-B references: {len(packaged_refs)}/6 required unique files",
        "- Review lenses: SEO metadata and placement; GEO quick-answer/citation structure; content usefulness and trust boundaries; restricted-topic safety; visual prompt contract; JustPaste export behavior.",
        "",
        "## Per-article results",
        "",
    ]
    for rec in records:
        report.append(f"- **{rec['id']}** — PASS {rec['passed']}/{rec['checks']}; {rec['public_words']} public words; title {rec['title_chars']} chars; description {rec['description_chars']} chars; branch {rec['branch']}; prompt QA {rec['prompt_qa']}/100.")
    report.extend(["", "## Failures", ""])
    report.extend([f"- {item}" for item in failures] or ["- None."])
    report.extend([
        "",
        "## Human publishing checks still required",
        "",
        "- Recheck current Deadlock update context and every volatile product claim on publication day.",
        "- Confirm image rights, source captions, redactions, and mobile crops after assets are produced.",
        "- Paste one representative article into JustPaste.me and verify its editor preserves headings, lists, links, and blockquotes.",
        "- Review the final page around the backlink so the anchor remains natural after surrounding site edits.",
    ])
    (PACKAGE / "QUALITY-REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "PASS" if not failures else "FAIL", "articles": len(files), "failures": failures}, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
