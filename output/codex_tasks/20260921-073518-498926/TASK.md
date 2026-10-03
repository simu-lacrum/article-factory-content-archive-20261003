# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write three English articles: CS2 triggerbot vs aimbot; Dota 2 scripts vs macros vs bots; Deadlock souls aimbot. Use current research and concise prose.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260921-073518-498926`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260921-073518-498926.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. CS2 triggerbot vs aimbot: what changes?

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260921-073518-498926\01-cs2-triggerbot-vs-aimbot-what-changes.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260921-073518-498926\01-cs2-triggerbot-vs-aimbot-what-changes.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260921-073518-498926\01-cs2-triggerbot-vs-aimbot-what-changes.md`

### 2. Dota 2 scripts, macros and bots are different things

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260921-073518-498926\02-dota-2-scripts-macros-and-bots-are-different-things.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260921-073518-498926\02-dota-2-scripts-macros-and-bots-are-different-things.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260921-073518-498926\02-dota-2-scripts-macros-and-bots-are-different-things.md`

### 3. Deadlock souls aimbot: what the feature targets

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260921-073518-498926\03-deadlock-souls-aimbot-what-the-feature-targets.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260921-073518-498926\03-deadlock-souls-aimbot-what-the-feature-targets.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260921-073518-498926\03-deadlock-souls-aimbot-what-the-feature-targets.md`
