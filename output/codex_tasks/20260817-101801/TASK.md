# Codex task — four Melonity T2 articles

Status: complete.

The user-supplied editorial brief is the controlling specification. It overrides the default Deadlock product mapping for this run and explicitly assigns the two Deadlock articles to Melonity targets.

## Delivery contract

- Two US English and two Russian standalone T2 articles.
- Exact H1, slug, description, primary keyword, outline, backlink anchor and target from the brief.
- Exact word ranges: 1,350–1,650; 1,400–1,750; 1,350–1,650; 1,400–1,700.
- One commercial backlink per body and no other URLs.
- Restricted or restricted-adjacent treatment only; no implementation, hidden-data access, detection-evasion or configuration instructions.
- FAQ is the final H2, with five questions and 2–4 sentences per answer.
- No Markdown tables.
- Preserve eight supplied production prompts exactly. Do not generate images.
- Export four standalone HTML body fragments for JustPaste.it with two image URL tokens per article.

## Outputs

See [ARTICLE_INDEX.md](ARTICLE_INDEX.md).

## Verification

- Article Factory review: 4/4 PASS.
- Word counts: 1,597; 1,703; 1,350; 1,400.
- H2 count: 9 in every article.
- Commercial links: exactly one in every article, with the assigned anchor and target.
- HTML: four fragments, one H1 and nine H2 elements each, eight figures total.
- Prompt extraction: indices 01–08 and exact text equality with the supplied brief.
- Raster assets: 0.
- Local 8-word overlap audit: no matches within the set and no matches against the existing `output/articles` archive.

The English Deadlock page and its current feature labels, plus the Dota 2 `Teleport Preview` label, were checked on 2026-08-17. The locale-less Deadlock URL should still be resolved in the intended Russian publication session because the web crawler follows locale redirects.
