# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create 10 fully unique English Tier-2 articles for DioWebHost, one article per URL in knowledge/link_sources/diowebhost-t2-20260913.txt. Use adjacent user-intent topics, never copy the existing target page topic or another published article. Required dofollow anchors for Cluster are exactly: cheats -> https://cluster.center/en, cs2 cheats -> https://cluster.center/en/cs2, deadlock cheats -> https://cluster.center/en/deadlock. For every CheatsGaming target, choose one natural anchor containing the word cheat or hack and link to the exact assigned URL. Each article needs SEO front matter, meta description under 160 characters with the primary keyword, concise answer-first opening, scannable H2/H3 structure, at least one compliant generated-image placement, FAQ, and a non-operational risk-aware editorial angle. Product mapping: cluster.center for CS2 and Deadlock. Publishing destination: diowebhost.com/new-post.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260913-075123`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260913-075123.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

### 2. Dota 2 Skin Changer in 2026: Free Tools, Ban Risks and Premium Alternatives

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`

### 3. Dota 2 Couriers: Best Unusual Couriers, Courier Value and Why Courier Info Wins Games

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`

### 4. Dota 2 Boosting vs Using a Cheat Tool: Account Risk, Cost and Control

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\04-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\04-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\04-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`

### 5. Invoker Auto Cast and One-Button Combos: From AHK Macros to Melonity Hero Scripts

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\05-invoker-auto-cast-and-one-button-combos-from-ahk-macros-to-melonity-hero-scripts.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\05-invoker-auto-cast-and-one-button-combos-from-ahk-macros-to-melonity-hero-scripts.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\05-invoker-auto-cast-and-one-button-combos-from-ahk-macros-to-melonity-hero-scripts.md`

### 6. Melonity Dota 2 Setup Guide: Free Trial, CFG, Spoofer and First Safe Launch

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\06-melonity-dota-2-setup-guide-free-trial-cfg-spoofer-and-first-safe-launch.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\06-melonity-dota-2-setup-guide-free-trial-cfg-spoofer-and-first-safe-launch.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\06-melonity-dota-2-setup-guide-free-trial-cfg-spoofer-and-first-safe-launch.md`

### 7. Dota 2 Hidden Pool and Smurf Pool: How to Check Your Account and Get Better Matches

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\07-dota-2-hidden-pool-and-smurf-pool-how-to-check-your-account-and-get-better-matches.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\07-dota-2-hidden-pool-and-smurf-pool-how-to-check-your-account-and-get-better-matches.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\07-dota-2-hidden-pool-and-smurf-pool-how-to-check-your-account-and-get-better-matches.md`

### 8. Random Dota 2 Hero and Build Challenge: How to Make Any Pick Playable

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\08-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\08-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\08-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.md`

### 9. Best Dota 2 Autoexec.cfg and FPS Settings: Max FPS, Ping, Config Transfer and Stable Gameplay

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\09-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\09-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\09-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.md`

### 10. Deadlock Aimbot Settings Explained

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-075123\10-deadlock-aimbot-settings-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-075123\10-deadlock-aimbot-settings-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-075123\10-deadlock-aimbot-settings-explained.md`
