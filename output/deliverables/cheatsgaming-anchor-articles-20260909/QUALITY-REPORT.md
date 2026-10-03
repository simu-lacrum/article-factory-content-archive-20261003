# Quality Report

Checked: 9 September 2026.

## Article Factory review

- Articles reviewed: 24
- Passed: 24
- Needs review: 0
- Failed: 0
- Evidence entries per article: 4
- Generated cover prompts: 24
- Generated sequence: 1–24, strict B/A alternation
- Prompt QA scores: all at least 93/100
- Markdown tables in article bodies: none
- FAQ blocks: present in every article
- Image placement notes: present in every article
- Product mapping: `cluster.center` for every CS2 and Deadlock article

Machine-readable result: `output/runs/cheatsgaming-anchor-articles-20260909.review.json` in the project workspace.

## Anchor integrity

- Every article contains exactly one link to its assigned target URL.
- Every target link uses the exact `target_anchor` phrase stored in front matter.
- Every filename is the lowercase, hyphenated version of that exact anchor.
- Each of the eight requested URLs receives exactly three articles and three diversified anchors.

## Programmatic uniqueness gate

The article bodies were compared with five-word shingle Jaccard similarity after removing image-production comments.

- Highest pairwise similarity: 0.2435
- Most similar pair: `external-cs2-cheat-comparison.md` and `external-cs2-cheats-ranking.md`
- No pair approaches the 0.80 near-duplicate warning threshold.
- Body-only word counts range from 936 to 1,439 words; average 1,238.2 words.

This indicates that the package is not a “swap the keyword” template. Pages within the same target cluster share necessary vocabulary, but their thesis, structure, counterexample, and decision framework remain distinct.

## Restricted-topic gate

- No operational installation, injection, driver, kernel, memory-access, exploit, anti-cheat bypass, or evasion instructions.
- No direct loader or third-party mirror links.
- No absolute “undetected,” “100% safe,” or no-ban guarantees.
- Installation-intent articles focus on provenance, stale documentation, symptom classification, and accountable support.
- Comparison articles treat rankings as candidate pools and keep current prices/status claims out unless publication-day verification is available.

## Visual prompt gate

- Model target is Nano Banana Pro / `gemini-3-pro-image`.
- Visual system is `article-editorial-poster-v1` plus the CheatsGaming publisher layer.
- All B prompts name two packaged warm-story reference files, assign separate roles, and require at least 4/5 fidelity.
- Cluster violet `#635FD5` replaces the yellow/amber dominant field in B and occupies roughly 35–70% of the frame.
- In A, `#635FD5` remains a small 3–8% semantic accent.
- CheatsGaming electric/deep blue, charcoal, off-white, and tiny status green retain their publisher roles.

Actual generated images were not requested and are not included. The archive contains production-ready prompts and their required B-branch reference files.
