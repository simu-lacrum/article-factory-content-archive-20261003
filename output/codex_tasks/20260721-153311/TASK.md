# Codex Article Task — Six Localized Tier-2 Site Links

Write the six exact articles defined by the matching prompt and evidence files. Codex is the writer; no external LLM provider is used.

## Campaign Constraints

- 1000–1200 words per article, excluding front matter and image comments.
- One article per requested localized product URL.
- Exactly two target links per article, distinct anchors, first after substantive value, second in the conclusion/next step, and 120+ words between links.
- SEO front matter, one H1, focused H2 sections, three image-placement notes, internal-link suggestions, and exactly five FAQs.
- Dota 2 uses Melonity; CS2 and Deadlock use cluster.center.
- No direct ranking duplication, unsupported current claims, prices, safety guarantees, concealment guidance, or low-level implementation.
- No markdown tables.

## Files

- Prompts: `C:\Users\User\Desktop\articles\output\prompts\20260721-153311`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260721-153311`
- Articles: `C:\Users\User\Desktop\articles\output\articles\20260721-153311`

Review with `python -m article_factory review output\runs\20260721-153311.json` and fix every finding.
