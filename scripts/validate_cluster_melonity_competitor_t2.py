from __future__ import annotations

import json
import re
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "output" / "briefs" / "CLUSTER-MELONITY-COMPETITOR-T2-20-20260908"
BRIEF_FILES = [
    PACKAGE / "01-CLUSTER-CS2.md",
    PACKAGE / "02-CLUSTER-DEADLOCK.md",
    PACKAGE / "03-CLUSTER-HOME.md",
    PACKAGE / "04-MELONITY-DOTA2.md",
    PACKAGE / "05-MELONITY-DEADLOCK.md",
]

EXPECTED = {
    "01-CLUSTER-CS2.md": ("https://cluster.center/en/cs2", "buy cheats cs2"),
    "02-CLUSTER-DEADLOCK.md": ("https://cluster.center/en/deadlock", "deadlock cheat"),
    "03-CLUSTER-HOME.md": ("https://cluster.center/en", "cheats"),
    "04-MELONITY-DOTA2.md": ("https://melonity.gg/en", "dota 2 cheats"),
    "05-MELONITY-DEADLOCK.md": ("https://melonity.gg/en/deadlock", "deadlock hacks"),
}


def norm(value: str) -> str:
    value = value.lower().replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def field(block: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}:\s*(.+?)\s*$", block, re.MULTILINE)
    return match.group(1).strip() if match else ""


errors: list[str] = []
records: list[dict[str, str]] = []
file_counts: dict[str, int] = {}

for path in BRIEF_FILES:
    if not path.exists():
        errors.append(f"missing brief file: {path.name}")
        continue

    text = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^## (CM-\d{3})\s+—\s+(.+)$", text, re.MULTILINE))
    file_counts[path.name] = len(headings)
    if len(headings) != 4:
        errors.append(f"{path.name}: expected 4 briefs, found {len(headings)}")

    expected_url, expected_anchor = EXPECTED[path.name]
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[match.start():end]
        rec = {
            "id": match.group(1),
            "file": path.name,
            "h1": field(block, "H1"),
            "seo_title": field(block, "SEO title"),
            "slug": field(block, "Slug"),
            "primary_keyword": field(block, "Primary keyword"),
            "description": field(block, "Description"),
            "target_url": expected_url,
            "anchor": expected_anchor,
        }
        records.append(rec)

        for key in ("h1", "seo_title", "slug", "primary_keyword", "description"):
            if not rec[key]:
                errors.append(f"{rec['id']}: missing {key}")

        if len(rec["seo_title"]) > 60:
            errors.append(f"{rec['id']}: SEO title is {len(rec['seo_title'])} chars")
        if len(rec["h1"]) > 70:
            errors.append(f"{rec['id']}: H1 is {len(rec['h1'])} chars")
        if len(rec["description"]) > 160:
            errors.append(f"{rec['id']}: description is {len(rec['description'])} chars")
        if norm(rec["primary_keyword"]) not in norm(rec["description"]):
            errors.append(f"{rec['id']}: primary keyword missing from description")

        link = f"[{expected_anchor}]({expected_url})"
        if block.count(link) != 1:
            errors.append(
                f"{rec['id']}: expected one exact anchor link {link!r}, found {block.count(link)}"
            )
        if "### FAQ questions" not in block:
            errors.append(f"{rec['id']}: FAQ questions missing")
        if "### Original-value requirement" not in block:
            errors.append(f"{rec['id']}: original-value requirement missing")
        if "### E-E-A-T and style" not in block:
            errors.append(f"{rec['id']}: E-E-A-T section missing")
        if "### Do not write" not in block:
            errors.append(f"{rec['id']}: safety boundary missing")

all_text = "\n".join(path.read_text(encoding="utf-8") for path in BRIEF_FILES if path.exists())
if re.search(r"^\s*\|.*\|\s*$", all_text, re.MULTILINE):
    errors.append("markdown table syntax found in brief files")

ids = [rec["id"] for rec in records]
expected_ids = [f"CM-{i:03d}" for i in range(1, 21)]
if ids != expected_ids:
    errors.append(f"IDs are not consecutive CM-001..CM-020: {ids}")

for key in ("h1", "slug", "primary_keyword"):
    values = [norm(rec[key]) for rec in records]
    if len(values) != len(set(values)):
        errors.append(f"duplicate {key} values found")

prior_titles: list[tuple[str, str]] = []
brief_root = ROOT / "output" / "briefs"
for path in brief_root.rglob("*.md"):
    if PACKAGE in path.parents:
        continue
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        continue
    for pattern in (
        r"^- H1:\s*(.+)$",
        r"^\*\*EN article title:\*\*\s*(.+?)\s*$",
        r"^# (?!#)(.+)$",
    ):
        for title in re.findall(pattern, text, re.MULTILINE):
            cleaned = title.strip().strip(chr(96))
            if 12 <= len(cleaned) <= 140:
                prior_titles.append((cleaned, str(path.relative_to(ROOT))))

max_prior_similarity = 0.0
nearest: list[dict[str, object]] = []
for rec in records:
    current = norm(rec["h1"])
    best_score = 0.0
    best_title = ""
    best_path = ""
    for prior_title, prior_path in prior_titles:
        score = SequenceMatcher(None, current, norm(prior_title)).ratio()
        if score > best_score:
            best_score = score
            best_title = prior_title
            best_path = prior_path
    max_prior_similarity = max(max_prior_similarity, best_score)
    if best_score >= 0.80:
        nearest.append(
            {
                "id": rec["id"],
                "score": round(best_score, 3),
                "prior_title": best_title,
                "prior_path": best_path,
            }
        )

if nearest:
    errors.append("one or more H1 titles are >= 0.80 similar to prior brief titles")

report = {
    "status": "PASS" if not errors else "FAIL",
    "briefs": len(records),
    "targets": len(EXPECTED),
    "briefs_per_target": sorted(file_counts.values()),
    "unique_h1": len({norm(rec["h1"]) for rec in records}),
    "unique_slugs": len({norm(rec["slug"]) for rec in records}),
    "unique_primary_keywords": len({norm(rec["primary_keyword"]) for rec in records}),
    "max_seo_title_length": max((len(rec["seo_title"]) for rec in records), default=0),
    "max_description_length": max((len(rec["description"]) for rec in records), default=0),
    "max_prior_title_similarity": round(max_prior_similarity, 3),
    "nearest_prior_over_0_80": nearest,
    "errors": errors,
}

print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(0 if not errors else 1)

