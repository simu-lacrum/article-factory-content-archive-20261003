# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create eight independent Tier 2 articles exactly as specified in the authoritative brief at C:\Users\User\.codex\attachments\65c6ac2c-ac9b-4a85-bac1-213c623d7aca\pasted-text-1.txt: 1 AI Dota 2 script QA EN; 2 Deadlock comparison criteria RU; 3 Deadlock information triage EN; 4 Deadlock phase profiles RU; 5 Foxhole logistics bottlenecks RU; 6 Foxhole artillery coordination EN; 7 GTA 5 RP platform compatibility EN; 8 GTA 5 RP menu profiles RU. Preserve exact anchors, URLs, section word bands, FAQs, front matter, visual slots, and safety restrictions from the brief.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260805-154106`

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
13. After writing all articles, run `python -m article_factory review output\runs\20260805-154106.json`.
14. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Дота 2 интернешнл 2025: полный разбор для Dota 2

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`

### 2. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\02-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\02-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\02-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

### 3. Dota 2 Skin Changer in 2026: Free Tools, Ban Risks and Premium Alternatives

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\03-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\03-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\03-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`

### 4. Dota 2 Couriers: Best Unusual Couriers, Courier Value and Why Courier Info Wins Games

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\04-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\04-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\04-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`

### 5. Dota 2 Boosting vs Using a Cheat Tool: Account Risk, Cost and Control

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\05-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\05-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\05-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`

### 6. Dota 2 AHK Scripts and Macros: Invoker, Meepo, Tinker and the Safer Premium Alternative

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\06-dota-2-ahk-scripts-and-macros-invoker-meepo-tinker-and-the-safer-premium-alternative.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\06-dota-2-ahk-scripts-and-macros-invoker-meepo-tinker-and-the-safer-premium-alternative.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\06-dota-2-ahk-scripts-and-macros-invoker-meepo-tinker-and-the-safer-premium-alternative.md`

### 7. Random Dota 2 Hero and Build Challenge: How to Make Any Pick Playable

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\07-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\07-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\07-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.md`

### 8. Best Dota 2 Autoexec.cfg and FPS Settings: Max FPS, Ping, Config Transfer and Stable Gameplay

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260805-154106\08-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-154106\08-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-154106\08-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.md`
