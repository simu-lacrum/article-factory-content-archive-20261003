# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create eight distinct 500-800 word Tier 2 article briefs, one per supplied target URL. Match the language of each target page, use exactly two organic backlinks per article with the specified Russian anchors for Deadlock, Foxhole and GTA 5 RP and natural English equivalents for English pages, use the Dota video workflow as source truth for the Dota scripting target, keep content high-level and risk-aware, and provide Nano Banana Pro article-editorial-poster-v1 visual prompts.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260805-114024`

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
12. Build every generated-image prompt with `article-editorial-poster-v1`, target Nano Banana Pro by default, assign explicit reference roles, and require a QA score of at least 80/100.
13. After writing all articles, run `python -m article_factory review output\runs\20260805-114024.json`.
14. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Дота 2 интернешнл 2025: полный разбор для Dota 2

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`

### 2. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\02-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\02-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\02-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

### 3. Dota 2 Skin Changer in 2026: Free Tools, Ban Risks and Premium Alternatives

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\03-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\03-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\03-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`

### 4. Dota 2 Couriers: Best Unusual Couriers, Courier Value and Why Courier Info Wins Games

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\04-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\04-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\04-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`

### 5. Dota 2 Boosting vs Using a Cheat Tool: Account Risk, Cost and Control

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\05-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\05-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\05-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`

### 6. Invoker Auto Cast and One-Button Combos: From AHK Macros to Melonity Hero Scripts

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\06-invoker-auto-cast-and-one-button-combos-from-ahk-macros-to-melonity-hero-scripts.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\06-invoker-auto-cast-and-one-button-combos-from-ahk-macros-to-melonity-hero-scripts.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\06-invoker-auto-cast-and-one-button-combos-from-ahk-macros-to-melonity-hero-scripts.md`

### 7. Melonity Dota 2 Setup Guide: Free Trial, CFG, Spoofer and First Safe Launch

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\07-melonity-dota-2-setup-guide-free-trial-cfg-spoofer-and-first-safe-launch.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\07-melonity-dota-2-setup-guide-free-trial-cfg-spoofer-and-first-safe-launch.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\07-melonity-dota-2-setup-guide-free-trial-cfg-spoofer-and-first-safe-launch.md`

### 8. Dota 2 Hidden Pool and Smurf Pool: How to Check Your Account and Get Better Matches

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-114024\08-dota-2-hidden-pool-and-smurf-pool-how-to-check-your-account-and-get-better-matches.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-114024\08-dota-2-hidden-pool-and-smurf-pool-how-to-check-your-account-and-get-better-matches.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-114024\08-dota-2-hidden-pool-and-smurf-pool-how-to-check-your-account-and-get-better-matches.md`
