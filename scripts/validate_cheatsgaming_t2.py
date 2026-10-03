from __future__ import annotations

import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "output" / "briefs" / "CHEATSGAMING-T2-57-20260908"
BRIEF_FILES = [
    PACK / "01-HOME-CS2-BRIEFS.md",
    PACK / "02-DEADLOCK-BRIEFS.md",
    PACK / "03-DOTA2-BRIEFS-HOLD.md",
]
PROMPT_FILE = PACK / "04-VISUAL-PROMPTS.md"


def field(block: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}: `(.*?)`\s*$", block, re.MULTILINE)
    return match.group(1).strip() if match else ""


errors: list[str] = []
briefs: list[dict[str, object]] = []
target_counts: Counter[str] = Counter()

for path in BRIEF_FILES:
    text = path.read_text(encoding="utf-8")
    target = ""
    matches = list(re.finditer(r"^### CG-(\d{3}) — .*?$", text, re.MULTILINE))
    cursor = 0
    target_markers = list(
        re.finditer(r"^Target(?: on hold)?: (https://\S+)\s*$", text, re.MULTILINE)
    )
    for index, match in enumerate(matches):
        start = match.start()
        while cursor < len(target_markers) and target_markers[cursor].start() < start:
            target = target_markers[cursor].group(1)
            cursor += 1
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        brief_id = int(match.group(1))
        h1 = field(block, "H1")
        slug = field(block, "Slug")
        primary = field(block, "Primary keyword")
        description = field(block, "Description")
        if not all([target, h1, slug, primary, description]):
            errors.append(f"CG-{brief_id:03d}: missing target/H1/slug/primary/description")
        if primary.lower() not in h1.lower():
            errors.append(f"CG-{brief_id:03d}: primary keyword absent from H1")
        if primary.lower() not in description.lower():
            errors.append(f"CG-{brief_id:03d}: primary keyword absent from description")
        if len(description) > 160:
            errors.append(f"CG-{brief_id:03d}: description is {len(description)} chars")
        if target and target not in block:
            errors.append(f"CG-{brief_id:03d}: exact target URL absent from backlink block")
        for required in [
            "Status / type",
            "SEO title",
            "Secondary phrases",
            "Intent and thesis",
            "Required scene / counterexample",
            "Evidence",
            "FAQ",
            "Visuals",
            "Do not",
        ]:
            if f"- {required}:" not in block:
                errors.append(f"CG-{brief_id:03d}: missing field {required}")
        target_counts[target] += 1
        briefs.append(
            {
                "id": brief_id,
                "target": target,
                "h1": h1,
                "slug": slug,
                "primary": primary,
                "description_length": len(description),
            }
        )

ids = [int(item["id"]) for item in briefs]
if ids != list(range(1, 58)):
    errors.append(f"Brief IDs are not exactly 001-057: {ids}")
if len(target_counts) != 19:
    errors.append(f"Expected 19 targets, found {len(target_counts)}")
for target, count in target_counts.items():
    if count != 3:
        errors.append(f"Target {target} has {count} briefs instead of 3")
for key in ["h1", "slug"]:
    values = [str(item[key]).lower() for item in briefs]
    duplicates = [value for value, count in Counter(values).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate {key}: {duplicates}")

prompt_text = PROMPT_FILE.read_text(encoding="utf-8")
prompt_matches = list(re.finditer(r"^## CG-(\d{3}) — .*?$", prompt_text, re.MULTILINE))
prompt_ids: list[int] = []
filenames: list[str] = []
for index, match in enumerate(prompt_matches):
    prompt_id = int(match.group(1))
    prompt_ids.append(prompt_id)
    end = prompt_matches[index + 1].start() if index + 1 < len(prompt_matches) else len(prompt_text)
    block = prompt_text[match.start():end]
    for number in range(1, 17):
        if not re.search(rf"(?:^|\s){number}\. ", block):
            errors.append(f"CG-{prompt_id:03d} prompt: missing block {number}")
    expected_branch = "B" if prompt_id % 2 else "A"
    branch_match = re.search(rf"{prompt_id:03d},\s*(A|B\d)", block)
    if not branch_match or not branch_match.group(1).startswith(expected_branch):
        errors.append(f"CG-{prompt_id:03d} prompt: wrong A/B branch")
    for token in [
        "article-editorial-poster-v1",
        "Nano Banana Pro / `gemini-3-pro-image`",
        "Publisher identity: CheatsGaming editorial system",
        "#2B58FF",
        "#001FD4",
        "#0E0E10",
        "#F2F2F2",
        "#6DB33F",
        "3840×2160",
    ]:
        if token not in block:
            errors.append(f"CG-{prompt_id:03d} prompt: missing {token}")
    mapped = "#635FD5" if prompt_id <= 42 else "#FF1469"
    if mapped not in block:
        errors.append(f"CG-{prompt_id:03d} prompt: missing mapped color {mapped}")
    refs = re.findall(r"reference-\d{2}\.png", block)
    if prompt_id % 2:
        if len(refs) != 2 or len(set(refs)) != 2:
            errors.append(f"CG-{prompt_id:03d} prompt: branch B needs two distinct refs, got {refs}")
        if "replacing yellow/amber" not in block or "fidelity ≥4/5" not in block:
            errors.append(f"CG-{prompt_id:03d} prompt: incomplete B color/fidelity contract")
    elif "References: none." not in block:
        errors.append(f"CG-{prompt_id:03d} prompt: branch A must state References: none")
    qa_match = re.search(r"QA:\s*(\d{2,3})/100", block)
    if not qa_match or int(qa_match.group(1)) < 80:
        errors.append(f"CG-{prompt_id:03d} prompt: QA below 80 or absent")
    file_match = re.search(r"`([a-z0-9-]+\.webp)`", block)
    if not file_match:
        errors.append(f"CG-{prompt_id:03d} prompt: output filename absent")
    else:
        filenames.append(file_match.group(1))

if prompt_ids != list(range(1, 58)):
    errors.append(f"Prompt IDs are not exactly 001-057: {prompt_ids}")
if len(filenames) != len(set(filenames)):
    errors.append("Duplicate visual output filenames")
if "placeholder" in prompt_text.lower():
    errors.append("Placeholder text remains in visual prompt file")


def normalize_title(value: str) -> str:
    value = value.lower().replace("cs 2", "cs2").replace("dota-2", "dota 2")
    value = re.sub(r"^\d+[-_. ]+", "", value)
    value = re.sub(r"[^a-zа-яё0-9]+", " ", value)
    return " ".join(value.split())


prior_titles: set[str] = set()
brief_root = ROOT / "output" / "briefs"
for path in brief_root.rglob("*.md"):
    if PACK in path.parents:
        continue
    prior_titles.add(normalize_title(path.stem))
    old_text = path.read_text(encoding="utf-8", errors="replace")
    for match in re.finditer(r"^- H1: `(.*?)`\s*$", old_text, re.MULTILINE):
        prior_titles.add(normalize_title(match.group(1)))

for memory_path in [ROOT / "published" / "articles.csv", ROOT / "published" / "avoid_topics.txt"]:
    if memory_path.exists():
        for line in memory_path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip():
                prior_titles.add(normalize_title(line))

prior_titles.discard("")
max_prior_similarity = 0.0
nearest_prior: list[dict[str, object]] = []
for item in briefs:
    current = normalize_title(str(item["h1"]))
    best_title = ""
    best_score = 0.0
    for old in prior_titles:
        score = SequenceMatcher(None, current, old).ratio()
        if score > best_score:
            best_score = score
            best_title = old
    max_prior_similarity = max(max_prior_similarity, best_score)
    nearest_prior.append(
        {"id": int(item["id"]), "score": round(best_score, 3), "prior": best_title}
    )
    if best_score >= 0.88:
        errors.append(
            f"CG-{int(item['id']):03d}: H1 is too close to prior topic ({best_score:.3f}): {best_title}"
        )

result = {
    "status": "PASS" if not errors else "FAIL",
    "briefs": len(briefs),
    "targets": len(target_counts),
    "briefs_per_target": sorted(set(target_counts.values())),
    "prompts": len(prompt_ids),
    "unique_h1": len({str(item['h1']).lower() for item in briefs}),
    "unique_slugs": len({str(item['slug']).lower() for item in briefs}),
    "unique_primary_keywords": len({str(item['primary']).lower() for item in briefs}),
    "max_description_length": max(int(item["description_length"]) for item in briefs),
    "max_prior_title_similarity": round(max_prior_similarity, 3),
    "nearest_prior_over_0_80": [item for item in nearest_prior if float(item["score"]) >= 0.80],
    "errors": errors,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if not errors else 1)
