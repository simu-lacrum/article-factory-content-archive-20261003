---
source: SEO_ARTICLE_RULES.md
heading: "Final Self-Review"
---

## Final Self-Review

Before finishing, the agent must check:

- Title length is 60 characters or less.
- Description is 160 characters or less and includes the primary keyword.
- FAQ exists at the end.
- Image placement notes exist.
- Graph bootstrap passed with 100% node and edge coverage, and the canonical visual prompt guide was read.
- Every generated-image prompt targets the chosen model explicitly, assigns reference roles, declares typography mode, includes output ratio/size, and scores at least 80/100.
- Generated-image indices alternate B/A across the run, every B asset names two actually attached reference files and passes 4/5 fidelity, and every mapped-product visual uses the exact mapped color with the correct branch role: small accent in A, dominant field replacing yellow/amber in B.
- Published-topic memory was checked.
- Article uses internal evidence or verified facts without exposing "local sources/evidence pack" wording in the body, and does not invent current facts.
- Product mention is native and not overused.
- No markdown tables are present; lists are used instead.
- The style matches the imported Medium source direction: practical, direct, conversational, and free from water, bureaucratic wording, or academic filler.
- The article is saved as markdown in the requested output path.
- `python -m article_factory review output\runs\<run_id>.json` was run when a manifest exists.
