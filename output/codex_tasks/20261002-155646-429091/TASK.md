# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Prepare two distinct English SEO articles for Dota 2. First: Dota 2 cheats: evaluate private product pages by feature scope, hero coverage, update notes and evidence, without setup or evasion instructions; map Melonity natively. Second: Skinchanger Dota 2 and CS2: explain cosmetic previews, visibility, inventory ownership and source quality, with MetaSkins as contextual cosmetic reference. Avoid existing generic 2026 and preview/inventory duplicates; include fresh checklists, LSI, FAQs and real image placement guidance.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20261002-155646-429091`

## Required Workflow

1. Run `python -m article_factory graph bootstrap`; require PASS and 100% node/edge coverage.
2. Read `memory/graph/SESSION_BOOTSTRAP.md` and every required file it lists, including `SEO_ARTICLE_RULES.md` and the full visual prompt guide.
3. Read `knowledge/agent_memory/products/product-map.md`.
4. For each item below, read the `prompt` and `evidence` files.
5. Write a complete article to the target output path.
6. Use only facts supported by the evidence pack or mark uncertainty explicitly.
7. Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body. Use those inputs silently and write from an expert editorial voice.
8. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
9. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
10. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
11. Match the imported Medium style: direct, practical, conversational, lightly slangy, gamer-aware, no water, no bureaucratic wording, no academic filler.
12. Number generated assets across the run and alternate style branches: odd = B warm narrative, even = A tactile industrial; real screenshots do not consume an index.
13. Build every generated-image prompt with `article-editorial-poster-v1`, target Nano Banana Pro by default, and use the exact mapped color (Cluster #635FD5; Melonity #FF1469) with the correct branch role: small 3–8% accent in A, dominant 35–70% field replacing yellow/amber in B. Require a QA score of at least 80/100. Every B asset must actually attach two persistent warm-story reference files with explicit composition and render/palette/typography roles and pass 4/5 reference fidelity.
14. After writing all articles, run `python -m article_factory review output\runs\20261002-155646-429091.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Melonity, Umbrella and Octarine: compare documented features

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20261002-155646-429091\01-melonity-umbrella-and-octarine-compare-documented-features.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20261002-155646-429091\01-melonity-umbrella-and-octarine-compare-documented-features.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20261002-155646-429091\01-melonity-umbrella-and-octarine-compare-documented-features.md`

### 2. Dota 2 scripts, macros and bots are different things

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20261002-155646-429091\02-dota-2-scripts-macros-and-bots-are-different-things.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20261002-155646-429091\02-dota-2-scripts-macros-and-bots-are-different-things.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20261002-155646-429091\02-dota-2-scripts-macros-and-bots-are-different-things.md`
