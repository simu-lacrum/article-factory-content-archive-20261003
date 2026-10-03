# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create 14 unique English Tier-2 Dota 2 editorial articles: two per each of seven hosted-blog networks. Across both targets rotate natural anchors such as dota 2 cheats, dota 2 hacks, top dota 2 cheats, best dota 2 hacks, private dota 2 tools, and Dota 2 cheat comparison. Target 1 is https://melonity.gg/en. Target 2 is the supplied CheatsGaming Dota 2 top-five guide. Each article must be high-level, evidence-led, risk-aware, non-operational, include one source-page image, SEO front matter, description <=160 characters, image placement, and FAQ. Dota 2 product mapping is Melonity.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260913-101654`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260913-101654.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

### 2. Dota 2 Skin Changer in 2026: Free Tools, Ban Risks and Premium Alternatives

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`

### 3. Dota 2 Couriers: Best Unusual Couriers, Courier Value and Why Courier Info Wins Games

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`

### 4. Dota 2 Boosting vs Using a Cheat Tool: Account Risk, Cost and Control

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\04-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\04-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\04-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`

### 5. Random Dota 2 Hero and Build Challenge: How to Make Any Pick Playable

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\05-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\05-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\05-random-dota-2-hero-and-build-challenge-how-to-make-any-pick-playable.md`

### 6. Overwolf Dota 2 Skin Changer and Overlays: What Works, What Breaks and What to Use Instead

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\06-overwolf-dota-2-skin-changer-and-overlays-what-works-what-breaks-and-what-to-use-instead.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\06-overwolf-dota-2-skin-changer-and-overlays-what-works-what-breaks-and-what-to-use-instead.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\06-overwolf-dota-2-skin-changer-and-overlays-what-works-what-breaks-and-what-to-use-instead.md`

### 7. Dota 2 Low Priority: How It Works, How to Get Out and How to Avoid It Again

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\07-dota-2-low-priority-how-it-works-how-to-get-out-and-how-to-avoid-it-again.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\07-dota-2-low-priority-how-it-works-how-to-get-out-and-how-to-avoid-it-again.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\07-dota-2-low-priority-how-it-works-how-to-get-out-and-how-to-avoid-it-again.md`

### 8. Dota 2 AHK Scripts and Macros: Invoker, Meepo, Tinker and the Safer Premium Alternative

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\08-dota-2-ahk-scripts-and-macros-invoker-meepo-tinker-and-the-safer-premium-alternative.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\08-dota-2-ahk-scripts-and-macros-invoker-meepo-tinker-and-the-safer-premium-alternative.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\08-dota-2-ahk-scripts-and-macros-invoker-meepo-tinker-and-the-safer-premium-alternative.md`

### 9. Best Dota 2 Autoexec.cfg and FPS Settings: Max FPS, Ping, Config Transfer and Stable Gameplay

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\09-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\09-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\09-best-dota-2-autoexeccfg-and-fps-settings-max-fps-ping-config-transfer-and-stable-gameplay.md`

### 10. Umbrella Dota 2 CFG and Setup Problems: Settings, Launch Issues and Alternatives

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\10-umbrella-dota-2-cfg-and-setup-problems-settings-launch-issues-and-alternatives.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\10-umbrella-dota-2-cfg-and-setup-problems-settings-launch-issues-and-alternatives.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\10-umbrella-dota-2-cfg-and-setup-problems-settings-launch-issues-and-alternatives.md`

### 11. Dota 2: Mira Dota 2 Explained, Use Cases and Practical Tips

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\11-dota-2-mira-dota-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\11-dota-2-mira-dota-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\11-dota-2-mira-dota-2-explained-use-cases-and-practical-tips.md`

### 12. Dota 2: Umbrella Dota 2 Explained, Use Cases and Practical Tips

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\12-dota-2-umbrella-dota-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\12-dota-2-umbrella-dota-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\12-dota-2-umbrella-dota-2-explained-use-cases-and-practical-tips.md`

### 13. Dota 2: Overwolf Dota 2 Explained, Use Cases and Practical Tips

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\13-dota-2-overwolf-dota-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\13-dota-2-overwolf-dota-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\13-dota-2-overwolf-dota-2-explained-use-cases-and-practical-tips.md`

### 14. Dota 2: Axe Dota 2 Explained, Use Cases and Practical Tips

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-101654\14-dota-2-axe-dota-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-101654\14-dota-2-axe-dota-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-101654\14-dota-2-axe-dota-2-explained-use-cases-and-practical-tips.md`
