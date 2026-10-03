# SEO Article Rules For Codex Agents

This file is mandatory reading before generating article ideas, briefs, or final SEO articles in this project.

## Core Principle

Codex is the writer. External LLM APIs are optional tooling, not the authoring layer. The agent must build every article from project markdown memory, semantic cores, published-topic memory, graph exports, and evidence packs.

The article must feel useful to a real Dota 2, Deadlock, or CS2 reader, not like a thin SEO rewrite. Do not invent facts. If a fact is not present in project memory or a fresh verified source provided by the user, either omit it or mark it as uncertain.

## Required Files To Read First

Before topic ideation or article writing, run `python -m article_factory graph bootstrap`, require 100% node and edge coverage, read `memory/graph/SESSION_BOOTSTRAP.md`, then read every file it lists. The required set includes:

- `AGENTS.md`
- `SEO_ARTICLE_RULES.md`
- `knowledge/agent_memory/rules/article-visual-prompt-guide.md`
- `knowledge/editorial_memory.md`
- `published/articles.csv`
- `published/avoid_topics.txt`
- `knowledge/agent_memory/products/product-map.md`
- `memory/ai-memory-export/index.md`
- `memory/ai-memory-export/published-and-avoid.md`
- `memory/ai-memory-export/topic-priorities.md`
- `memory/graph/knowledge-graph.json`

The machine-readable receipt `memory/graph/session-bootstrap.json` must account for every graph node and edge. A manual spot-check of the graph is not equivalent to the full traversal.

For a specific article, also read the generated evidence JSON in `output/evidence/<run_id>/` and the matching prompt in `output/prompts/<run_id>/`.

If external URLs were added through `knowledge/link_sources/*.txt`, use the materialized markdown copies in `knowledge/agent_memory/sources/` instead of opening the URLs during writing.

## Published Topic Rule

Do not propose or write direct duplicates of already published articles.

The Medium account `https://medium.com/@mrkhertz` is the author source hub. Its imported articles contain useful product and market knowledge, but their exact topics are already used. Treat them as memory, not as topics to repeat.

Blocked topic angles are defined in `published/avoid_topics.txt`. Adjacent angles are allowed only when the article has a clearly different search intent and does not repackage the same article.

## Article Front Matter

Every final article markdown file must start with front matter:

```yaml
---
title: "SEO title, 50-60 characters maximum"
description: "SEO description, 160 characters maximum, includes primary_keyword"
game: dota2
language: en
primary_keyword: "main keyword from semantic cluster"
secondary_keywords:
  - "keyword 2"
  - "keyword 3"
semantic_cluster: "cluster name"
reader_job: "The concrete question this article resolves"
research_study: "Study id and cluster id from the active research core"
keyword_usage: "Natural usage; no density quota"
sources_used:
  - "knowledge/agent_memory/source.md"
---
```

Rules:

- `title` must be no longer than 60 characters. Prefer 50-60.
- `description` must be no longer than 160 characters and must contain `primary_keyword`.
- `primary_keyword` must come from the semantic core or the generated evidence pack.
- `secondary_keywords` must come from the same cluster or a closely related cluster.
- Do not use a keyword if it does not match the article's real intent.

## Keyword Usage

There is no mandatory keyword density. Inspect actual competitor usage by page type and extraction method; treat counts as descriptive evidence, not a ranking target. Use the active study selected in `config/research.json`. Old CSV frequency and difficulty values without provider, country, language, match type and date are unverified.

Read `docs/SEO_RESEARCH_WORKFLOW.md` for research, SERP cohorts, real volume imports, anchor classification, original-value and editorial acceptance rules. Unknown volume stays unknown; a long query is not automatically low-frequency. Never fabricate US/UK frequency, keyword difficulty, positions or incoming backlink ratios.

Use keywords naturally:

- Make the primary topic clear in the SEO title, description and opening. Use the primary phrase in a heading or FAQ only when the phrasing fits the reader's question naturally.
- Use secondary keywords in subheadings only when they answer a real subtopic.
- Do not stuff exact-match phrases into every paragraph.
- If the exact phrase is awkward, use a natural variant and mention the tradeoff in an editorial note only if needed.

## Voice And Style

Use the same editorial direction as the imported Medium articles from `https://medium.com/@mrkhertz`: direct, practical, gamer-aware, and written like a person who has actually looked at the topic instead of summarizing it from a distance.

Style rules:

- Write in a conversational expert voice: calm, confident, practical, and easy to read.
- Write like an expert practitioner, not like a bot summarizing files. The body of the article must never say "local sources", "local evidence", "evidence pack", "knowledge base", or similar internal-provenance wording.
- Product integration must be concrete and attributable. Never invent firsthand experience, tests, quotations or outcomes. Use "we tested" or "from our experience" only when an actual test/experience record supports it. Disclose a commercial relationship where relevant.
- Add a little natural gaming slang and simpler speech where it fits: ranked, pubs, tilt, legit, sketchy, hard-sell, clean setup, player reports, match pressure. Do not overdo slang or make the text sound childish.
- Prefer short paragraphs, clear H2/H3 headings, lists, examples, mistakes, and checklists.
- Start from the reader's real problem: confusion, frustration, comparison, account risk, feature choice, or a specific in-game mechanic.
- Explain terms plainly. Assume the reader is smart, but not always familiar with every cheat, product, or game-specific term.
- A light first-person or second-person tone is allowed when it sounds natural. Do not overuse it.
- Keep the article normal in volume: complete enough to satisfy search intent, but without padding. If the user sets a target volume, follow it; if not, write the shortest complete article that still covers the topic well.
- Remove water, generic AI filler, corporate wording, bureaucratic phrasing, and academic over-explaining.
- Avoid empty phrases like "in today's gaming landscape", "it is important to note", "delve into", "comprehensive overview", or similar filler unless the phrase is truly needed.
- Do not turn the text into a dry encyclopedia entry. The reader should feel the article has judgment, examples, and practical direction.

## Formatting Limits

Do not use markdown tables in article drafts, article briefs, idea lists, or final article files. Use bullet lists, numbered lists, short subsections, or comparison lists instead.

## Mandatory Article Structure

The final article must be a complete markdown article with this structure:

1. Front matter.
2. H1 title.
3. Short opening that answers the reader's question immediately, without a word quota.
4. Quick answer or key takeaway block.
5. Main explanatory sections with clear H2 headings.
6. Practical examples, mistakes, checklist, or comparison list where useful.
7. Native product integration after the educational value is already delivered.
8. Image placement notes.
9. Internal-link suggestions.
10. A short conclusion or contextual CTA only if it adds something useful.
11. FAQ block at the end.

Do not write a generic landing page. The first screen of the article should answer the user's query.

## FAQ Requirement

Every article must end with an FAQ section.

Rules:

- Use `## FAQ` for English articles.
- Use `## Частые вопросы` or `## FAQ` for Russian articles.
- Include 4-7 questions.
- Questions must target long-tail search intent from the same cluster.
- At least one FAQ answer should include the primary keyword naturally.
- FAQ answers must be short, factual, and not promotional by default.

## Image Placement Notes

Every article must include image placement notes directly in the markdown. Do not attach images silently.

Use this exact format:

```markdown
<!-- IMAGE_SLOT_01
Placement: after "## Section Heading"
Type: real screenshot | product UI | gameplay screenshot | generated image | diagram
Purpose: what the image should help the reader understand
Suggested file name: dota-2-example-topic-01.webp
Alt text: concise SEO-friendly alt text
Caption: optional caption for the article
If generated, Nano Banana prompt:
Write the full prompt here. Keep text readable, avoid fake UI labels unless needed.
Generated sequence index: 1, 2, 3...
Style branch: A | B1 | B2 | B3
Mapped product and brand color role: Cluster #635FD5 | Melonity #FF1469 | none; A = small semantic accent, B = dominant field replacing yellow/amber
Model: Nano Banana Pro / gemini-3-pro-image
Aspect ratio and size: 16:9, 2K
Typography mode: art-first | text-in-image
Reference roles: Image A = composition; Image B = material; etc.
Visual style version: article-editorial-poster-v1
Prompt QA score: 0-100
-->
```

Rules:

- Use 2-5 image slots for normal articles.
- At least one image should support the main explanation, not just decorate the page.
- If an image should be a real screenshot, say exactly what screen/state/action it should show.
- If the image can be generated, include a ready-to-send Nano Banana prompt.
- Do not invent product screenshots that could misrepresent the UI. Use generated conceptual images only when a real screenshot is not required.
- Treat Nano Banana Pro / `gemini-3-pro-image` as the default generator unless the user explicitly selects a different model.
- Number generated conceptual images globally across the current article batch. Odd generated indices use branch B (`warm narrative editorial ad`, submode B1/B2/B3); even generated indices use branch A (`tactile industrial product poster`). This B-first order ensures that a one-cover article actually uses the new reference family. Real screenshots and verified product/game UI do not consume an index. Adjacent generated images may not repeat a branch.
- Compile every generated-image prompt through `knowledge/agent_memory/rules/article-visual-prompt-guide.md`. It must define the generated sequence index, style branch, asset role, factual article thesis, one physical visual metaphor, one hero, aspect ratio, composition, palette roles, mapped brand color role, materials, camera, lighting, typography mode, reference roles, constraints, priority order, and output size.
- Apply the exact mapped brand color by branch: Cluster / `cluster.center` uses `#635FD5` for Deadlock and CS2; Melonity uses `#FF1469` for Dota 2. In branch A keep it as one 3–8% semantic accent and never as a global wash. In branch B use it as the dominant 35–70% field that replaces the warm-story reference's yellow/amber background; do not leave yellow dominant or reduce the mapped color to a small token.
- Assign one explicit function to every attached reference (composition, material, palette, subject identity, lighting, or camera). Do not give the model an undifferentiated pile of references.
- For every branch-B asset, actually attach two files from `knowledge/agent_memory/references/article-editorial-warm-story-v1/`: one composition reference and one render/palette/typography reference. `Reference roles: none` is an automatic failure. Require at least 4/5 fidelity across layout silhouette, warm/light palette, rounded shape language, depth treatment, and typography mass.
- Prefer `art-first` for article covers: reserve a clean headline safe zone and prohibit letters, pseudo-text, labels, and logos. Use `text-in-image` only with exact quoted copy, language, case, line count, position, and a ban on all other text.
- Use 2K as the normal master size; use 4K for final hero assets, typography-heavy posters, print, or substantial downstream crops. Write the size with an uppercase `K`.
- Score every final prompt with the guide's 100-point rubric. A score below 80, or any automatic rejection condition, requires a rewrite before generation.
- Do not ask for a named brand's or living artist's style. Describe the abstract editorial product-poster properties instead.

## Product Integration

Mandatory product mapping:

- Dota 2 articles integrate `Melonity`.
- Deadlock articles integrate `cluster.center`.
- CS2 articles integrate `cluster.center`.

Do not swap products between games unless the user explicitly asks for a comparison.

Product mentions must be native and grounded.

Good pattern:

- Explain the game mechanic, player problem, or SEO topic first.
- Add one concise section for the mapped product where it naturally fits.
- Mention only product facts supported by project memory, imported sources, user-provided specs, or freshly verified sources.
- Use a calm, practical CTA.

Avoid:

- Unsupported safety guarantees.
- Claims about current ban waves, anti-cheat status, patch state, prices, or feature availability unless present in current project sources or freshly verified sources.
- Repeating the product name in every section.
- Turning an educational article into a hard-sell ad.

## Safety And Factual Limits

Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.

Allowed:

- High-level educational explanation.
- Risk-aware framing.
- Product-positioning language grounded in project evidence or verified facts, written in a public expert voice.
- Discussion of user intent, terminology, historical context, and common mistakes.

Not allowed:

- Step-by-step evasion or bypass instructions.
- Low-level injection, driver, kernel, exploit, or detection-avoidance details.
- Absolute claims like "100% safe", "undetected forever", or guaranteed no bans.

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
