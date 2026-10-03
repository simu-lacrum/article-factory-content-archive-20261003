# CheatsGaming Anchor Article Package

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
