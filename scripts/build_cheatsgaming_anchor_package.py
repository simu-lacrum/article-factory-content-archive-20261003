from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "cheatsgaming-anchor-articles-20260909"
DEST = ROOT / "output" / "deliverables" / RUN_ID
EVIDENCE_DIR = ROOT / "output" / "evidence" / RUN_ID
MANIFEST_PATH = ROOT / "output" / "runs" / f"{RUN_ID}.json"

CS2_SOURCE = ROOT / "output" / "packages" / "CHEATSGAMING-T2-57-20260908-HOME-CS2" / "md"
DEADLOCK_SOURCE = ROOT / "output" / "packages" / "CHEATSGAMING-T2-57-20260908-DEADLOCK" / "md"

TARGETS = {
    "cs2-free": "https://cheatsgaming.com/games/cs2/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52",
    "cs2-legit": "https://cheatsgaming.com/games/cs2/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364",
    "cs2-external": "https://cheatsgaming.com/games/cs2/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4",
    "cs2-install": "https://cheatsgaming.com/games/cs2/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710",
    "cs2-best": "https://cheatsgaming.com/games/cs2/top-cheats-for-cs2-the-best-hack-cfab8351f70b",
    "deadlock-parry": "https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924",
    "deadlock-install": "https://cheatsgaming.com/games/deadlock/how-to-install-deadlock-cheats-hacks-for-free-588c4515cbf7",
    "deadlock-best": "https://cheatsgaming.com/games/deadlock/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e",
}

# The order deliberately preserves the source prompts' B/A design language while
# resetting the selected 24-article package to generated sequence index 1.
ITEMS = [
    (CS2_SOURCE / "CG-007-free-cs2-cheat-vs-trial-vs-crack.md", "cs2", "free CS2 cheat overview", "cs2-free", 1),
    (CS2_SOURCE / "CG-008-cost-of-free-cs2-cheats.md", "cs2", "best free CS2 cheats", "cs2-free", 2),
    (CS2_SOURCE / "CG-009-free-cs2-cheat-landing-page-audit.md", "cs2", "free CS2 hacks review", "cs2-free", 3),
    (CS2_SOURCE / "CG-010-legit-vs-semi-rage-vs-rage-cs2.md", "cs2", "legit CS2 cheats comparison", "cs2-legit", 4),
    (CS2_SOURCE / "CG-011-legit-cs2-cheat-safety-claims.md", "cs2", "best legit CS2 hack", "cs2-legit", 5),
    (CS2_SOURCE / "CG-012-cs2-legit-cheat-review-questions.md", "cs2", "top legit CS2 cheats", "cs2-legit", 6),
    (CS2_SOURCE / "CG-013-external-cs2-cheat-review-tests.md", "cs2", "external CS2 cheats ranking", "cs2-external", 7),
    (CS2_SOURCE / "CG-014-external-cs2-cheat-compatibility.md", "cs2", "best external CS2 hack", "cs2-external", 8),
    (CS2_SOURCE / "CG-015-external-cs2-cheat-update-status.md", "cs2", "external CS2 cheat comparison", "cs2-external", 9),
    (CS2_SOURCE / "CG-020-cs2-cheat-launch-problems-random-fixes.md", "cs2", "CS2 cheat setup guide", "cs2-install", 10),
    (CS2_SOURCE / "CG-019-cs2-cheat-download-verification.md", "cs2", "CS2 cheats installation guide", "cs2-install", 11),
    (CS2_SOURCE / "CG-022-best-cs2-cheat-for-playstyle.md", "cs2", "best CS2 hack comparison", "cs2-best", 12),
    (CS2_SOURCE / "CG-021-cs2-cheat-update-loop-diagnosis.md", "cs2", "CS2 cheats download guide", "cs2-install", 13),
    (CS2_SOURCE / "CG-024-cs2-cheat-subscription-workflow.md", "cs2", "CS2 cheat ranking", "cs2-best", 14),
    (CS2_SOURCE / "CG-023-cs2-cheat-trial-30-minute-evaluation.md", "cs2", "top CS2 cheats list", "cs2-best", 15),
    (DEADLOCK_SOURCE / "CG-032-deadlock-auto-parry-limits.md", "deadlock", "Deadlock Auto-Parry", "deadlock-parry", 16),
    (DEADLOCK_SOURCE / "CG-031-deadlock-parry-window-timing-feints.md", "deadlock", "Deadlock Auto-Parry cheat guide", "deadlock-parry", 17),
    (DEADLOCK_SOURCE / "CG-034-deadlock-cheat-download-verification.md", "deadlock", "Deadlock cheats installation guide", "deadlock-install", 18),
    (DEADLOCK_SOURCE / "CG-033-deadlock-auto-parry-review-evidence.md", "deadlock", "Deadlock Auto-Parry cheat", "deadlock-parry", 19),
    (DEADLOCK_SOURCE / "CG-036-outdated-deadlock-cheat-guide-signals.md", "deadlock", "Deadlock cheats download guide", "deadlock-install", 20),
    (DEADLOCK_SOURCE / "CG-035-deadlock-cheat-support-ticket.md", "deadlock", "Deadlock cheat setup article", "deadlock-install", 21),
    (DEADLOCK_SOURCE / "CG-040-deadlock-cheat-comparison-beyond-aimbot.md", "deadlock", "best Deadlock hack", "deadlock-best", 22),
    (DEADLOCK_SOURCE / "CG-041-deadlock-hero-coverage-depth.md", "deadlock", "top Deadlock cheats", "deadlock-best", 23),
    (DEADLOCK_SOURCE / "CG-042-deadlock-cheat-trial-checklist.md", "deadlock", "Deadlock cheat ranking", "deadlock-best", 24),
]


def slugify_anchor(anchor: str) -> str:
    value = anchor.lower().replace("auto-parry", "auto-parry")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value


def front_matter_value(text: str, key: str) -> str:
    match = re.search(rf'^\s*{re.escape(key)}:\s*"?([^"\r\n]+)"?\s*$', text, flags=re.M)
    return match.group(1).strip() if match else ""


def source_branch(text: str) -> str:
    match = re.search(
        r"(?:Index/branch/model|Generated sequence index, branch, model):\s*0*\d+,\s*(A|B[123]?)",
        text,
        flags=re.I,
    )
    if match:
        branch = match.group(1).upper()
        return "B2" if branch == "B" else branch
    match = re.search(r"^Style branch:\s*(A|B[123]?)\s*$", text, flags=re.I | re.M)
    if not match:
        raise ValueError("No visual branch found")
    branch = match.group(1).upper()
    return "B2" if branch == "B" else branch


def transform_article(text: str, anchor: str, index: int, expected_url: str) -> str:
    old_target = front_matter_value(text, "target_url")
    if old_target != expected_url:
        raise ValueError(f"Target mismatch: expected {expected_url}, got {old_target}")

    link_pattern = re.compile(rf"\[([^\]]+)\]\({re.escape(expected_url)}\)")
    anchors = [m.group(1) for m in link_pattern.finditer(text)]
    if anchor not in anchors:
        raise ValueError(f"Expected exact anchor {anchor!r}; found {anchors!r}")

    branch = source_branch(text)
    expected_family = "B" if index % 2 else "A"
    if not branch.startswith(expected_family):
        raise ValueError(f"Sequence {index} needs {expected_family}, source prompt is {branch}")

    text = re.sub(r'^(target_url:\s*"[^"]+"\s*)$', rf'\1\ntarget_anchor: "{anchor}"\nproduct: "cluster.center"', text, count=1, flags=re.M)
    text = re.sub(r'^published:\s*"[^"]+"$', 'published: "2026-09-09"', text, flags=re.M)
    text = re.sub(r'^updated:\s*"[^"]+"$', 'updated: "2026-09-09"', text, flags=re.M)
    text = text.replace("September 8, 2026", "September 9, 2026")

    text = re.sub(
        r"((?:Index/branch/model|Generated sequence index, branch, model):\s*)0*\d+",
        rf"\g<1>{index:03d}",
        text,
        flags=re.I,
    )
    text = re.sub(r"^Generated sequence index:\s*\d+\s*$", f"Generated sequence index: {index}", text, flags=re.M)
    text = re.sub(r"^Style branch:\s*(?:A|B|B1|B2|B3)\s*$", f"Style branch: {branch}", text, flags=re.I | re.M)
    text = re.sub(r"^Prompt QA score:\s*(\d+)(?:/100)?\s*$", r"Prompt QA score: \1", text, flags=re.M)

    if branch.startswith("B") and not re.search(r"Reference fidelity[^\n]*4/5|4/5[^\n]*fidelity", text, flags=re.I):
        text = text.replace(
            "Visual style version:",
            "Reference fidelity: 4/5 minimum across layout silhouette, palette, shape language, depth treatment, and typography mass\nVisual style version:",
            1,
        )

    # Normalize reference paths so the files named in every B prompt exist in the archive.
    text = re.sub(
        r"(?<!article-editorial-warm-story-v1/)references/article-editorial-warm-story-v1/",
        "references/article-editorial-warm-story-v1/",
        text,
    )
    return text


def evidence_for(item: dict[str, object]) -> dict[str, object]:
    game = str(item["game"])
    target_key = str(item["target_key"])
    target_url = str(item["target_url"])
    anchor = str(item["anchor"])
    product_source = (
        "knowledge/agent_memory/products/cs2-cluster-center-external.md"
        if game == "cs2"
        else "knowledge/agent_memory/products/deadlock-cluster-center-internal.md"
    )
    target_slug = target_url.rsplit("/", 1)[-1]
    return {
        "topic": {
            "id": f"ANCHOR-{int(item['sequence']):02d}",
            "title": str(item["title"]),
            "game": game,
            "language": "en",
            "risk_level": "restricted-safe",
            "target_anchor": anchor,
            "target_url": target_url,
        },
        "evidence": [
            {
                "source": f"knowledge/agent_memory/sources/target-urls/{target_slug}.md",
                "heading": "Target page and link context",
                "excerpt": "The target page establishes the page topic and the commercial phrase family used for contextual anchor selection.",
            },
            {
                "source": product_source,
                "heading": "Mapped cluster.center product memory",
                "excerpt": "Product descriptions are limited to high-level, attributed feature categories and exclude safety guarantees or operational implementation.",
            },
            {
                "source": "output/briefs/CHEATSGAMING-T2-57-20260908/01-HOME-CS2-BRIEFS.md" if game == "cs2" else "output/briefs/CHEATSGAMING-T2-57-20260908/02-DEADLOCK-BRIEFS.md",
                "heading": f"Brief for {target_key}",
                "excerpt": "The brief defines a distinct adjacent search intent, counterexample, factual boundary, and exact contextual backlink sentence.",
            },
            {
                "source": "output/deliverables/cheatsgaming-anchor-articles-20260909/SERP-AND-ANCHOR-ANALYSIS.md",
                "heading": "SERP lexical consensus and anchor diversification",
                "excerpt": "The anchor is drawn from repeated live SERP wording while varying comparison, ranking, overview, guide, and review formulations across the three placements.",
            },
        ],
        "strict_rules": [
            "No operational installation, injection, bypass, evasion, or detection-avoidance guidance.",
            "No current safety, price, trial, or availability guarantee unless freshly verified and attributed.",
            "Keep the exact target anchor natural and use it once in the contextual backlink.",
        ],
    }


def analysis_report() -> str:
    return """# SERP and Anchor Analysis

Checked: 9 September 2026 (Europe/Moscow). Scope: English-language web results for eight commercial-intent query clusters. No paid keyword-volume provider was available, so this is a lexical and intent analysis of visible organic titles/snippets, not a volume forecast. Rankings can vary by location and personalization.

## Method

- Queried each page theme with its game, feature/category, and `best`, `free`, `review`, `download`, `install`, or `comparison` modifier.
- Compared repeated wording in competitor titles, H1s, snippets, and community results.
- Selected one direct category anchor, one commercial near-match, and one contextual editorial variation for each target.
- Avoided repeating the same exact-match anchor three times. This follows the programmatic SEO rule to vary descriptive anchors and prevents the package from looking like a mechanical link set.
- Treated vendor status, pricing, detection, and safety language as claims. No “undetected,” “no ban,” or similar promise is used as an anchor.

## Deadlock: installation target

Target: https://cheatsgaming.com/games/deadlock/how-to-install-deadlock-cheats-hacks-for-free-588c4515cbf7

Visible competitors included Avalanche’s “How to Install and Use Deadlock Cheats,” NUXD’s “Deadlock Cheat Tool Download, Hack Setup Guide & Status,” and multiple Deadlock mod installation guides. The recurring lexical core is `Deadlock + cheat + install/setup/download + guide`.

Selected anchors:

- `Deadlock cheats installation guide`
- `Deadlock cheat setup article`
- `Deadlock cheats download guide`

Why: the set covers install, setup, and download intent without claiming the destination hosts a current executable or that following a guide is safe.

Competitor references:

- https://avalan.cc/guides/how-to-use-deadlock-cheats
- https://nuxd.net/games/deadlock/index.html
- https://docs.deadlockmods.app/using-mod-manager/installation

## Deadlock: Auto-Parry target

Target: https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924

The results combine mechanic explainers with community accusation/review language. Repeated wording includes `Deadlock Auto-Parry`, `auto-parry cheat`, `parry timing`, and `how it works`. This mixed SERP makes an exact feature phrase useful, but the surrounding article must distinguish ordinary timing evidence from a product claim.

Selected anchors:

- `Deadlock Auto-Parry`
- `Deadlock Auto-Parry cheat guide`
- `Deadlock Auto-Parry cheat`

Why: the exact entity remains stable across all three, while `guide` and the unmodified feature name diversify context.

Competitor references:

- https://deadlock.io/en/articles/mechanics/parry
- https://forums.playdeadlock.com/threads/auto-parry-cheat-or-normal-gameplay.49573/
- https://steamcommunity.com/app/1422450/discussions/0/802345853100546534/

## Deadlock: best-cheats target

Target: https://cheatsgaming.com/games/deadlock/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e

Competitor titles strongly repeat `Best Deadlock Cheat`, `Best Deadlock Cheats`, `2026`, `review`, and `comparison`. The year is omitted from anchors because it becomes stale and does not belong in evergreen link text.

Selected anchors:

- `best Deadlock hack`
- `top Deadlock cheats`
- `Deadlock cheat ranking`

Why: these cover the same commercial comparison cluster while distributing exact-match pressure across `best`, `top`, and `ranking` language.

Competitor references:

- https://cheatstore.net/blog/best-deadlock-cheat-in-2026
- https://ivsofte.biz/en/blog/best-deadlock-cheats/
- https://madchad.net/best-deadlock-cheats-2026/

## CS2: best-free target

Target: https://cheatsgaming.com/games/cs2/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52

Results repeatedly use `Free CS2 Cheats`, `Free CS2 Cheat`, `Free CS2 Hack`, `download`, and feature-list language. The articles deliberately shift value toward provenance, support, and total friction because free-download SERPs often over-index on unsupported status promises.

Selected anchors:

- `free CS2 cheat overview`
- `best free CS2 cheats`
- `free CS2 hacks review`

Why: one exact category phrase is paired with editorial `overview` and `review` variants.

Competitor references:

- https://cs2hacks.net/free-cs2-cheats
- https://icheat.io/free-cs2-cheats/
- https://project-infinity.cloud/free-cs2-cheats/

## CS2: legit target

Target: https://cheatsgaming.com/games/cs2/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364

The SERP uses `best legit CS2 cheat`, `legit-focused`, `review`, and product-specific evaluations. It also blurs play-style labels with safety claims, so the supporting articles explain terminology and review quality rather than publishing “safe settings.”

Selected anchors:

- `legit CS2 cheats comparison`
- `best legit CS2 hack`
- `top legit CS2 cheats`

Why: all three match commercial comparison intent while sounding natural in three different editorial sentences.

Competitor references:

- https://vredux.com/articles/best-cs2-legit-cheats
- https://cheatsupply.com/guides/serotonin-cs2-review
- https://cheatsupply.com/guides/pellix-review

## CS2: external target

Target: https://cheatsgaming.com/games/cs2/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4

The lexical core is unusually clean: `external CS2 cheat(s)`, `best external`, `review`, and `comparison`. Competitors frequently turn architecture into a safety shortcut; the articles here keep architecture, compatibility, stability, maintenance, and safety as separate questions.

Selected anchors:

- `external CS2 cheats ranking`
- `best external CS2 hack`
- `external CS2 cheat comparison`

Why: each phrase reflects a recurring SERP modifier, with no unsupported architectural guarantee.

Competitor references:

- https://cs2hacks.net/cs2-external-cheat
- https://cheatsupply.com/guides/predator-cs2-review
- https://cheatsupply.com/guides/pellix-review

## CS2: installation target

Target: https://cheatsgaming.com/games/cs2/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710

The visible query pattern is `how to install CS2 cheats`, `CS2 cheat download`, and `setup guide`. Because the operational version of this intent would cross the project’s safety boundary, these donor articles focus on provenance, symptom classification, stale-build diagnosis, and escalation to accountable support.

Selected anchors:

- `CS2 cheat setup guide`
- `CS2 cheats installation guide`
- `CS2 cheats download guide`

Why: the wording matches the SERP without implying that the donor article provides loader or anti-cheat instructions.

Competitor references:

- https://undetek.app/
- https://icheat.io/free-cs2-cheats/
- https://cs2hacks.net/free-cs2-cheats

## CS2: best-cheats target

Target: https://cheatsgaming.com/games/cs2/top-cheats-for-cs2-the-best-hack-cfab8351f70b

Competitors repeat `Best CS2 Cheats`, `Best CS2 Hack`, `compare`, `features`, `prices`, and `tested`. The package avoids a second universal ranking; its articles turn the target into a candidate pool and explain how to compare playstyle fit, trial evidence, maintenance, and subscription friction.

Selected anchors:

- `best CS2 hack comparison`
- `CS2 cheat ranking`
- `top CS2 cheats list`

Why: the three phrases preserve the dominant comparison intent while allowing natural surrounding prose and avoiding one repeated exact anchor.

Competitor references:

- https://cs2hacks.net/compare-cs2-cheats
- https://clustercheats.substack.com/p/top-5-cs2-cheats-in-2026-the-best
- https://peerlist.io/060121131/articles/best-cs2-cheats

## GEO and programmatic decisions

- Every article opens with an answer-first block that can stand alone in an AI citation.
- Question-led FAQ headings target long-tail follow-ups without adding FAQPage schema to a commercial site.
- Observed facts, publisher claims, dates, limitations, and unknowns remain separate.
- The 24 pages use 24 distinct primary intents and counterexamples. They are not a city/product-name swap template.
- One contextual target link appears in each article, using the exact anchor named in its filename and front matter.
- Generated covers alternate B/A globally. Cluster `#635FD5` is a 35–70% field replacing yellow/amber in B and a 3–8% semantic accent in A. CheatsGaming publisher blue remains structural and secondary.
"""


def readme() -> str:
    return """# CheatsGaming Anchor Article Package

This package contains 24 English Markdown articles: 15 for CS2 and 9 for Deadlock, exactly three for each of the eight requested target pages.

## Folder layout

- `cs2/`: 15 articles, an article index, and a consolidated image-prompt file.
- `deadlock/`: 9 articles, an article index, and a consolidated image-prompt file.
- `references/article-editorial-warm-story-v1/`: the eight persistent references named by branch-B prompts.
- `SERP-AND-ANCHOR-ANALYSIS.md`: competitor-title patterns, selected anchors, rationale, and limitations.
- `QUALITY-REPORT.md`: generated after validation.

Each article filename is the hyphenated exact anchor used for its contextual link. The original phrase is also stored as `target_anchor` in front matter.

The image prompts target Nano Banana Pro / `gemini-3-pro-image` and follow `article-editorial-poster-v1` plus the CheatsGaming publisher layer. Generated sequence indices run from 1 through 24 and alternate B/A. Branch-B prompts name two files from the packaged reference directory and require at least 4/5 reference fidelity.

Restricted-topic boundary: the articles do not provide injection, anti-cheat bypass, evasion, low-level implementation, direct loader, or warning-suppression instructions. Current prices, trials, product status, and account-safety guarantees are intentionally not asserted.
"""


def build_indexes(records: list[dict[str, object]]) -> None:
    for game in ("cs2", "deadlock"):
        subset = [r for r in records if r["game"] == game]
        lines = [f"# {game.upper()} Article Index", ""]
        prompts = [f"# {game.upper()} Image Prompts", "", "Each prompt is also embedded in its article. Sequence numbering is global across both game folders.", ""]
        for record in sorted(subset, key=lambda r: str(r["anchor"]).lower()):
            lines.extend(
                [
                    f"## {record['anchor']}",
                    "",
                    f"- File: `{record['file_name']}`",
                    f"- Article: {record['title']}",
                    f"- Target: {record['target_url']}",
                    f"- Generated cover: #{record['sequence']} / {record['branch']}",
                    "",
                ]
            )
            prompt_match = re.search(r"<!--\s*IMAGE_SLOT_01.*?-->", str(record["text"]), flags=re.S | re.I)
            if prompt_match:
                prompts.extend(
                    [
                        f"## {record['anchor']} — sequence #{record['sequence']} / {record['branch']}",
                        "",
                        prompt_match.group(0),
                        "",
                    ]
                )
        (DEST / game / "ARTICLE-INDEX.md").write_text("\n".join(lines), encoding="utf-8")
        (DEST / game / "IMAGE-PROMPTS.md").write_text("\n".join(prompts), encoding="utf-8")


def main() -> None:
    expected_parent = (ROOT / "output" / "deliverables").resolve()
    if DEST.resolve().parent != expected_parent:
        raise RuntimeError(f"Refusing to write outside {expected_parent}")

    for folder in (DEST / "cs2", DEST / "deadlock", EVIDENCE_DIR, MANIFEST_PATH.parent):
        folder.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, object]] = []
    manifest_items: list[dict[str, object]] = []
    for source, game, anchor, target_key, sequence in ITEMS:
        if not source.is_file():
            raise FileNotFoundError(source)
        raw = source.read_text(encoding="utf-8")
        transformed = transform_article(raw, anchor, sequence, TARGETS[target_key])
        branch = source_branch(transformed)
        file_name = f"{slugify_anchor(anchor)}.md"
        destination = DEST / game / file_name
        destination.write_text(transformed, encoding="utf-8", newline="\n")
        title = front_matter_value(transformed, "title")
        record = {
            "source": str(source.relative_to(ROOT)),
            "game": game,
            "anchor": anchor,
            "target_key": target_key,
            "target_url": TARGETS[target_key],
            "sequence": sequence,
            "branch": branch,
            "file_name": file_name,
            "output": str(destination),
            "title": title,
            "text": transformed,
        }
        records.append(record)
        evidence_path = EVIDENCE_DIR / f"{game}-{file_name[:-3]}.json"
        evidence_path.write_text(json.dumps(evidence_for(record), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        manifest_items.append(
            {
                "topic_id": f"ANCHOR-{sequence:02d}",
                "title": title,
                "game": game,
                "language": "en",
                "status": "article",
                "output": str(destination),
                "evidence": str(evidence_path),
            }
        )

    build_indexes(records)
    (DEST / "README.md").write_text(readme(), encoding="utf-8", newline="\n")
    (DEST / "SERP-AND-ANCHOR-ANALYSIS.md").write_text(analysis_report(), encoding="utf-8", newline="\n")

    reference_src = ROOT / "knowledge" / "agent_memory" / "references" / "article-editorial-warm-story-v1"
    reference_dest = DEST / "references" / "article-editorial-warm-story-v1"
    reference_dest.mkdir(parents=True, exist_ok=True)
    for number in range(1, 9):
        name = f"reference-{number:02d}.png"
        shutil.copy2(reference_src / name, reference_dest / name)

    manifest = {
        "created_at": "2026-09-09T10:41:43+03:00",
        "run_id": RUN_ID,
        "spec": {"raw": "24 English contextual-link articles: three for each of eight CheatsGaming CS2/Deadlock target pages."},
        "llm_provider": "codex",
        "model": "codex",
        "visual_sequence_start": 1,
        "items": manifest_items,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    public_manifest = {
        "run_id": RUN_ID,
        "article_count": len(records),
        "games": {"cs2": 15, "deadlock": 9},
        "targets": TARGETS,
        "articles": [
            {
                key: record[key]
                for key in ("game", "file_name", "title", "anchor", "target_url", "sequence", "branch")
            }
            for record in records
        ],
    }
    (DEST / "manifest.json").write_text(json.dumps(public_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"destination": str(DEST), "manifest": str(MANIFEST_PATH), "articles": len(records)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
