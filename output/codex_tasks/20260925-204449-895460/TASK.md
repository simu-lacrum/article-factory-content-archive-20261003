# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Rewrite the complete Dota 2 guide corpus published on CheatsGaming at https://cheatsgaming.com/games/dota-2. Use the current articles and URLs as the destination inventory, and use https://dota2cheat.com/ as the source corpus to audit and rewrite. Preserve each destination intent, improve originality, evidence, readability, GEO citability and human voice, and use the CheatsGaming editorial system. Do not copy either site. Keep descriptions exactly 160 characters, include the primary keyword, and omit the final period. Do not create standalone duplicates of blocked published angles; where a destination is a legacy duplicate, reframe it with a materially different reader job or mark it for consolidation. Restricted topics remain high-level and risk-aware with no bypass, evasion or cheat implementation steps.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260925-204449-895460`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260925-204449-895460.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Melonity, Umbrella and Octarine: compare documented features

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260925-204449-895460\01-melonity-umbrella-and-octarine-compare-documented-features.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260925-204449-895460\01-melonity-umbrella-and-octarine-compare-documented-features.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260925-204449-895460\01-melonity-umbrella-and-octarine-compare-documented-features.md`

### 2. Dota 2 auto dodge: a feature name is not a coverage list

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260925-204449-895460\02-dota-2-auto-dodge-a-feature-name-is-not-a-coverage-list.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260925-204449-895460\02-dota-2-auto-dodge-a-feature-name-is-not-a-coverage-list.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260925-204449-895460\02-dota-2-auto-dodge-a-feature-name-is-not-a-coverage-list.md`

### 3. Dota 2 cosmetic changers: appearance, ownership and visibility

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260925-204449-895460\03-dota-2-cosmetic-changers-appearance-ownership-and-visibility.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260925-204449-895460\03-dota-2-cosmetic-changers-appearance-ownership-and-visibility.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260925-204449-895460\03-dota-2-cosmetic-changers-appearance-ownership-and-visibility.md`

### 4. Dota 2 scripts, macros and bots are different things

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260925-204449-895460\04-dota-2-scripts-macros-and-bots-are-different-things.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260925-204449-895460\04-dota-2-scripts-macros-and-bots-are-different-things.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260925-204449-895460\04-dota-2-scripts-macros-and-bots-are-different-things.md`
