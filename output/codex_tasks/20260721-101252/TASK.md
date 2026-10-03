# Codex Article Task — Exact Tier-2 Campaign

Write the nine exact articles from the user's pasted brief. Codex is the writer; no external LLM provider is used.

## Campaign Constraints

- 500–800 words each, target 620–720 excluding front matter and image comments.
- Articles 5 and 6 are Russian; all others are English.
- Exactly two links per article to the supplied Medium target, with the supplied distinct anchors and at least 120 words between links.
- First link after substantive value; second in the conclusion or next step; no links in FAQ.
- One H1, 3–5 substantive H2 sections plus FAQ, two image-placement notes, exactly four FAQ questions.
- Dota 2 uses Melonity; CS2 and Deadlock use cluster.center.
- No direct ranking duplication, unsupported current claims, safety guarantees, prices, technical implementation, or protection-avoidance guidance.
- No markdown tables.

## Files

Use the matching prompt and evidence files in:

- `C:\Users\User\Desktop\articles\output\prompts\20260721-101252`
- `C:\Users\User\Desktop\articles\output\evidence\20260721-101252`

Write final documents to:

- `C:\Users\User\Desktop\articles\output\articles\20260721-101252`

Review with:

`python -m article_factory review output\runs\20260721-101252.json`
