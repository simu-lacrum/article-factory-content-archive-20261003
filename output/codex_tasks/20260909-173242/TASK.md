# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create exactly five Substack-ready editorial articles, one per target URL: https://cluster.center/ru in Russian using anchor приватные читы для многопользовательских игр; https://cluster.center/en in English using anchor private cheats for multiplayer games; https://cluster.center/ru/cs2 in Russian using anchor приватный чит для CS2; https://cluster.center/ru/deadlock in Russian using anchor чит для Deadlock; https://cluster.center/en/cs2 in English using anchor private CS2 cheats. Each article must have a genuinely distinct search intent and structure, an evidence-led comparison or evaluation angle, one contextual target link with the exact anchor, answer-first GEO sections, short paragraphs, image/GIF placement notes using existing Substack assets, FAQ, and non-operational risk-aware language. Do not create a new article for https://cluster.center/en/deadlock because it is already covered.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260909-173242`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260909-173242.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. CS2 Aimbot Settings Explained: FOV, Smooth and Hitboxes

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260909-173242\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260909-173242\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260909-173242\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`

### 2. CS2 ESP Explained: Boxes, Chams, Skeleton and Status Icons

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260909-173242\02-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260909-173242\02-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260909-173242\02-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`

### 3. CS2 TriggerBot Settings Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260909-173242\03-cs2-triggerbot-settings-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260909-173242\03-cs2-triggerbot-settings-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260909-173242\03-cs2-triggerbot-settings-explained.md`

### 4. CS2 External Cheat Feature Glossary

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260909-173242\04-cs2-external-cheat-feature-glossary.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260909-173242\04-cs2-external-cheat-feature-glossary.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260909-173242\04-cs2-external-cheat-feature-glossary.md`

### 5. CS2 Bomb Timer, Spectator List and Keybinds Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260909-173242\05-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260909-173242\05-cs2-bomb-timer-spectator-list-and-keybinds-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260909-173242\05-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`
