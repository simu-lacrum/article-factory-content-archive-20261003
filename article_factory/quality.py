from __future__ import annotations

import json
import re
import itertools
import yaml
from dataclasses import dataclass
from pathlib import Path

from .io_utils import read_text, write_text
from .products import product_for_game


RISK_PATTERNS = [
    (r"\b100%\s+(?:undetected|safe|безопасн|не\s*бан)", "Unsupported absolute safety guarantee"),
    (r"\b(?:bypass|evade|обход|обойти)\b.{0,40}\b(?:anti-?cheat|vac|античит)", "Operational anti-cheat evasion wording"),
    (r"\b(?:first|then|step\s*\d|you should|you need to)\b.{0,70}\b(?:inject|patch the driver|disable the anti.?cheat)\b", "Operational implementation instruction"),
]

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\[insert\b",
    r"\{\{[^}]+\}\}",
    r"<[^>]+>",
]

IMAGE_SLOT_PATTERN = re.compile(r"<!--\s*IMAGE_SLOT_(\d+)(.*?)-->", flags=re.I | re.S)


@dataclass
class ReviewFinding:
    severity: str
    message: str
    excerpt: str | None = None


def word_count(text: str) -> int:
    return len(re.findall(r"[\wа-яёА-ЯЁ'-]+", public_body(text)))


def public_body(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return text


def has_markdown_table(text: str) -> bool:
    separator = re.compile(r"\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?")
    lines = text.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if "|" not in stripped:
            continue
        if separator.fullmatch(stripped):
            previous_line = lines[index - 1].strip() if index else ""
            next_line = lines[index + 1].strip() if index + 1 < len(lines) else ""
            if "|" in previous_line or "|" in next_line:
                return True
        if stripped.startswith("|") and stripped.endswith("|") and index + 1 < len(lines):
            if separator.fullmatch(lines[index + 1].strip()):
                return True
    return False


def strip_front_matter(text: str) -> tuple[dict[str, str], str]:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip()
    body = text[end + 4 :].strip()
    try:
        parsed = yaml.safe_load(raw)
    except yaml.YAMLError:
        return {}, body
    if not isinstance(parsed, dict):
        return {}, body
    return {str(k): "" if v is None else str(v) for k, v in parsed.items()}, body


def generated_image_slots(text: str) -> list[dict[str, str | int | None]]:
    slots: list[dict[str, str | int | None]] = []
    for match in IMAGE_SLOT_PATTERN.finditer(text):
        body = match.group(2)
        if not re.search(r"^\s*Type:\s*generated image\s*$", body, flags=re.I | re.M):
            continue
        index_match = re.search(r"^\s*Generated sequence index:\s*(\d+)\s*$", body, flags=re.I | re.M)
        branch_match = re.search(r"^\s*Style branch:\s*(A|B1|B2|B3)\s*$", body, flags=re.I | re.M)
        qa_match = re.search(r"^\s*Prompt QA score:\s*(\d{1,3})\s*$", body, flags=re.I | re.M)
        slots.append(
            {
                "slot_id": int(match.group(1)),
                "sequence_index": int(index_match.group(1)) if index_match else None,
                "style_branch": branch_match.group(1).upper() if branch_match else None,
                "qa_score": int(qa_match.group(1)) if qa_match else None,
                "body": body,
            }
        )
    return slots


def review_article(article_path: Path, evidence_path: Path | None = None) -> dict:
    if not article_path.exists():
        return {
            "article": str(article_path),
            "status": "fail",
            "word_count": 0,
            "h2_count": 0,
            "evidence_sources": 0,
            "findings": [{"severity": "error", "message": "Article file does not exist"}],
        }
    text = read_text(article_path)
    meta, body = strip_front_matter(text)
    findings: list[ReviewFinding] = []
    if not meta:
        findings.append(ReviewFinding("error", "Missing front matter"))
    for key in ("title", "description", "game", "language", "primary_keyword"):
        if key not in meta:
            findings.append(ReviewFinding("error", f"Missing front matter key: {key}"))
    title = meta.get("title", "").strip()
    seo_title = meta.get("seo_title", "").strip() or title
    description = meta.get("description", "").strip()
    primary_keyword = meta.get("primary_keyword", "").strip()
    if seo_title and len(seo_title) > 60:
        findings.append(ReviewFinding("warning", f"SEO title is longer than 60 characters: {len(seo_title)}"))
    if description and len(description) > 160:
        findings.append(ReviewFinding("warning", f"SEO description is longer than 160 characters: {len(description)}"))
    if primary_keyword and description and primary_keyword.lower() not in description.lower():
        findings.append(ReviewFinding("warning", "SEO description does not contain primary_keyword"))
    wc = word_count(body)
    if wc == 0:
        findings.append(ReviewFinding("error", "Article has no reader-visible content"))
    h2_count = len(re.findall(r"^##\s+", body, flags=re.M))
    if has_markdown_table(body):
        findings.append(ReviewFinding("error", "Markdown tables are not allowed; use lists instead"))
    sections = re.findall(r"^##\s+(.+)$", public_body(body), flags=re.M)
    if not sections or not re.search(r"^(?:FAQ|frequently asked questions|частые вопросы|часто задаваемые вопросы|вопросы и ответы)\b", sections[-1], flags=re.I):
        findings.append(ReviewFinding("warning", "No FAQ section detected"))
    visuals_opt_out = meta.get("visuals", "").strip().lower() in {"none", "no", "false", "omitted"}
    if not visuals_opt_out and not re.search(r"!\[[^\]]*\]\(|(?:image|screenshot)[_\s]+slot|image\s+placement|photo\s+placement|фото|изображени", body, flags=re.I):
        findings.append(ReviewFinding("warning", "No image placement notes detected"))
    product = meta.get("product", "").strip() or product_for_game(meta.get("game"))
    generated_slots = generated_image_slots(body)
    expected_accent = None
    if product == "Melonity":
        expected_accent = "#FF1469"
    elif product == "cluster.center":
        expected_accent = "#635FD5"
    for slot in generated_slots:
        slot_id = slot["slot_id"]
        sequence_index = slot["sequence_index"]
        style_branch = slot["style_branch"]
        qa_score = slot["qa_score"]
        slot_body = str(slot["body"])
        if sequence_index is None:
            findings.append(ReviewFinding("error", f"IMAGE_SLOT_{slot_id:02d} is missing a numeric Generated sequence index"))
        if style_branch is None:
            findings.append(ReviewFinding("error", f"IMAGE_SLOT_{slot_id:02d} is missing Style branch A/B1/B2/B3"))
        if sequence_index is not None and style_branch is not None:
            expected_branch = "B" if sequence_index % 2 else "A"
            if not style_branch.startswith(expected_branch):
                findings.append(
                    ReviewFinding(
                        "error",
                        f"IMAGE_SLOT_{slot_id:02d} breaks visual alternation: index {sequence_index} requires branch {expected_branch}",
                    )
                )
        if style_branch is not None and style_branch.startswith("B"):
            reference_files = set(
                re.findall(
                    r"article-editorial-warm-story-v1[/\\]reference-\d{2}\.png",
                    slot_body,
                    flags=re.I,
                )
            )
            if len(reference_files) < 2:
                findings.append(
                    ReviewFinding(
                        "error",
                        f"IMAGE_SLOT_{slot_id:02d} branch B must name two actual warm-story reference files",
                    )
                )
            if re.search(r"Reference roles:\s*none", slot_body, flags=re.I):
                findings.append(ReviewFinding("error", f"IMAGE_SLOT_{slot_id:02d} branch B cannot use Reference roles: none"))
            if not re.search(r"(?:Reference fidelity[^\n]*4/5|4/5[^\n]*fidelity)", slot_body, flags=re.I):
                findings.append(
                    ReviewFinding(
                        "error",
                        f"IMAGE_SLOT_{slot_id:02d} branch B is missing the 4/5 reference-fidelity target",
                    )
                )
            if expected_accent and not re.search(
                r"(?:dominant(?:\s+brand)?\s+field|field[^\n.]*replac(?:e|es|ing)[^\n.]*yellow|replac(?:e|es|ing)[^\n.]*yellow[^\n.]*field|доминирующ\w*\s+пол\w*|замен\w*[^\n.]*желт\w*[^\n.]*фон)",
                slot_body,
                flags=re.I,
            ):
                findings.append(
                    ReviewFinding(
                        "error",
                        f"IMAGE_SLOT_{slot_id:02d} branch B must use mapped brand color {expected_accent} as the dominant field replacing yellow/amber",
                    )
                )
        if expected_accent and expected_accent.lower() not in slot_body.lower():
            findings.append(
                ReviewFinding(
                    "error",
                    f"IMAGE_SLOT_{slot_id:02d} is missing mapped brand color {expected_accent} for {product}",
                )
            )
        if "gemini-3-pro-image" not in slot_body or "Nano Banana Pro" not in slot_body:
            findings.append(ReviewFinding("error", f"IMAGE_SLOT_{slot_id:02d} does not name Nano Banana Pro / gemini-3-pro-image"))
        if qa_score is None or qa_score < 80:
            findings.append(ReviewFinding("error", f"IMAGE_SLOT_{slot_id:02d} has no passing Prompt QA score (minimum 80)"))
    if product != "the mapped product" and not re.search(re.escape(product), body, flags=re.I):
        findings.append(ReviewFinding("warning", f"No {product} integration detected"))
    repeated = repeated_paragraphs(body)
    for paragraph, count in repeated[:3]:
        findings.append(
            ReviewFinding(
                "warning" if count < 5 else "error",
                f"Repeated paragraph detected {count} times",
                excerpt=paragraph[:220],
            )
        )
    reader_body = public_body(body)
    for sentence in re.split(r"(?<=[.!?])\s+|\n", reader_body):
        for pattern, message in RISK_PATTERNS:
            match = re.search(pattern, sentence, flags=re.I)
            if match and not re.search(r"\b(?:no|not|never|cannot|can't|do not|don't|doesn't)\b", sentence[:match.end()], flags=re.I):
                findings.append(ReviewFinding("error", message, excerpt=sentence[:240]))
    slop = re.findall(r"\b(?:in (?:the|today's) (?:ever-evolving|fast-paced|dynamic) (?:world|landscape)|delve into|unlock your (?:full )?potential|take your (?:gameplay|game) to the next level|it is (?:important|worth) (?:to note|noting)|in conclusion)\b", reader_body, flags=re.I)
    if slop:
        findings.append(ReviewFinding("warning", "Generic filler language: rewrite in specific reader language", excerpt="; ".join(slop)))
    # Editorial comments (image briefs and internal-link notes) are intentionally
    # stripped by the public exporters, so they are not publishable placeholders.
    placeholder_body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    for pattern in PLACEHOLDER_PATTERNS:
        match = re.search(pattern, placeholder_body, flags=re.I)
        if match:
            findings.append(ReviewFinding("error", "Placeholder text detected", excerpt=match.group(0)))
    evidence_sources = 0
    if evidence_path and evidence_path.exists():
        evidence = json.loads(read_text(evidence_path))
        evidence_sources = len({item.get("source") for item in evidence.get("evidence", []) if item.get("source")})
        if evidence_sources == 0:
            findings.append(ReviewFinding("warning", "No attributable factual sources supplied"))
    else:
        findings.append(ReviewFinding("warning", "No evidence pack found for this article"))
    status = "pass"
    if any(item.severity == "error" for item in findings):
        status = "fail"
    elif any(item.severity == "warning" for item in findings):
        status = "needs_review"
    return {
        "article": str(article_path),
        "status": status,
        "word_count": wc,
        "h2_count": h2_count,
        "evidence_sources": evidence_sources,
        "findings": [item.__dict__ for item in findings],
        "editorial_review_required": True,
        "review_scope": "Automated formatting and risk indicators; not proof of accuracy, helpfulness or E-E-A-T",
    }


def repeated_paragraphs(text: str) -> list[tuple[str, int]]:
    paragraphs = [
        re.sub(r"\s+", " ", item).strip()
        for item in re.split(r"\n\s*\n", text)
        if len(re.sub(r"\s+", " ", item).strip()) > 80
    ]
    counts: dict[str, int] = {}
    for paragraph in paragraphs:
        counts[paragraph] = counts.get(paragraph, 0) + 1
    return sorted(((p, c) for p, c in counts.items() if c >= 2), key=lambda item: item[1], reverse=True)


def review_manifest(manifest_path: Path, output_path: Path | None = None) -> dict:
    manifest = json.loads(read_text(manifest_path))
    results = []
    for item in manifest.get("items", []):
        if item.get("status") != "article":
            results.append(
                {
                    "article": item.get("output"),
                    "status": "not_generated",
                    "findings": [{"severity": "info", "message": "Only a brief/prompt was generated"}],
                }
            )
            continue
        results.append(review_article(Path(item["output"]), Path(item["evidence"]) if item.get("evidence") else None))
    generated_sequence: list[tuple[dict, dict[str, str | int | None]]] = []
    for item, result in zip(manifest.get("items", []), results):
        article_path = Path(item.get("output", ""))
        if item.get("status") == "article" and article_path.exists():
            for slot in generated_image_slots(read_text(article_path)):
                generated_sequence.append((result, slot))
    sequence_start = int(manifest.get("visual_sequence_start", 1))
    for expected_index, (result, slot) in enumerate(generated_sequence, start=sequence_start):
        if slot["sequence_index"] == expected_index:
            continue
        result.setdefault("findings", []).append(
            {
                "severity": "error",
                "message": (
                    f"Generated visual sequence must be global and contiguous: "
                    f"IMAGE_SLOT_{int(slot['slot_id']):02d} has index {slot['sequence_index']}, expected {expected_index}"
                ),
                "excerpt": None,
            }
        )
        result["status"] = "fail"
    summary = {
        "manifest": str(manifest_path),
        "total": len(results),
        "pass": sum(1 for item in results if item.get("status") == "pass"),
        "needs_review": sum(1 for item in results if item.get("status") == "needs_review"),
        "fail": sum(1 for item in results if item.get("status") == "fail"),
        "not_generated": sum(1 for item in results if item.get("status") == "not_generated"),
        "results": results,
        "editorial_review_required": True,
    }
    for left, right in itertools.combinations(results, 2):
        paths = [Path(item.get("article") or "") for item in (left, right)]
        if not all(path.is_file() for path in paths):
            continue
        shingles = []
        for path in paths:
            _, content = strip_front_matter(read_text(path))
            tokens = re.findall(r"\w+", public_body(content).lower())
            shingles.append({tuple(tokens[i:i + 8]) for i in range(len(tokens) - 7)})
        small = min(map(len, shingles))
        overlap = len(shingles[0] & shingles[1]) / small if small >= 80 else 0
        if overlap >= 0.55:
            for result, other in ((left, right), (right, left)):
                result["findings"].append({"severity": "error", "message": "Substantial cross-article text duplication", "excerpt": other["article"]})
                result["status"] = "fail"
    for status in ("pass", "needs_review", "fail", "not_generated"):
        summary[status] = sum(item.get("status") == status for item in results)
    if output_path:
        write_text(output_path, json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    return summary
