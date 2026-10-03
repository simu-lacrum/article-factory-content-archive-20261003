# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create exactly 20 distinct English Tier-2 competitor-focused article briefs: four for each of five target URLs. Use comparison, alternatives, decision and evidence-checking intents. Competitors include Undetek, Octarine, Umbrella, Predator, Iniuria and other currently verifiable options. Exact anchors by target: cluster.center/en/cs2 = buy cheats cs2; cluster.center/en/deadlock = deadlock cheat; cluster.center/en = cheats; melonity.gg/en = dota 2 cheats; melonity.gg/en/deadlock = deadlock hacks. Do not duplicate published topics, do not claim guaranteed safety, and do not include operational anti-cheat bypass instructions.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260908-174145`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260908-174145.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. CS2 Aimbot Settings Explained: FOV, Smooth and Hitboxes

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`

### 2. CS2 ESP Explained: Boxes, Chams, Skeleton and Status Icons

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\02-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\02-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\02-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`

### 3. CS2 TriggerBot Settings Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\03-cs2-triggerbot-settings-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\03-cs2-triggerbot-settings-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\03-cs2-triggerbot-settings-explained.md`

### 4. CS2 Hack vs Assistive Tools: What Players Search For

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\04-cs2-hack-vs-assistive-tools-what-players-search-for.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\04-cs2-hack-vs-assistive-tools-what-players-search-for.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\04-cs2-hack-vs-assistive-tools-what-players-search-for.md`

### 5. CS2 External Cheat Feature Glossary

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\05-cs2-external-cheat-feature-glossary.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\05-cs2-external-cheat-feature-glossary.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\05-cs2-external-cheat-feature-glossary.md`

### 6. CS2 Bomb Timer, Spectator List and Keybinds Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\06-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\06-cs2-bomb-timer-spectator-list-and-keybinds-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\06-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`

### 7. CS2 Cheat Features Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\07-cs2-cheat-features-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\07-cs2-cheat-features-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\07-cs2-cheat-features-explained.md`

### 8. CS2: Dust 2 Cs 2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\08-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\08-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\08-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.md`

### 9. CS2: Dm Server Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\09-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\09-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\09-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.md`

### 10. CS2: Aim Cs2 Map Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\10-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\10-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\10-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.md`

### 11. CS2: Bind Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\11-cs2-bind-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\11-cs2-bind-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\11-cs2-bind-cs2-explained-use-cases-and-practical-tips.md`

### 12. CS2: Rage Midnight Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\12-cs2-rage-midnight-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\12-cs2-rage-midnight-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\12-cs2-rage-midnight-cs2-explained-use-cases-and-practical-tips.md`

### 13. CS2: Cs 2 Cheat Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\13-cs2-cs-2-cheat-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\13-cs2-cs-2-cheat-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\13-cs2-cs-2-cheat-explained-use-cases-and-practical-tips.md`

### 14. CS2: Cs 2 Setting Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\14-cs2-cs-2-setting-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\14-cs2-cs-2-setting-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\14-cs2-cs-2-setting-explained-use-cases-and-practical-tips.md`

### 15. CS2: Nixware Cfg Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\15-cs2-nixware-cfg-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\15-cs2-nixware-cfg-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\15-cs2-nixware-cfg-cs2-explained-use-cases-and-practical-tips.md`

### 16. CS2: Fatality Win Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\16-cs2-fatality-win-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\16-cs2-fatality-win-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\16-cs2-fatality-win-cs2-explained-use-cases-and-practical-tips.md`

### 17. CS2: Cs2 Workshop Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\17-cs2-cs2-workshop-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\17-cs2-cs2-workshop-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\17-cs2-cs2-workshop-explained-use-cases-and-practical-tips.md`

### 18. CS2: Faceit Finder Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\18-cs2-faceit-finder-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\18-cs2-faceit-finder-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\18-cs2-faceit-finder-cs2-explained-use-cases-and-practical-tips.md`

### 19. CS2: Aim Map Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\19-cs2-aim-map-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\19-cs2-aim-map-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\19-cs2-aim-map-cs2-explained-use-cases-and-practical-tips.md`

### 20. CS2: Midnight Cs 2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-174145\20-cs2-midnight-cs-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-174145\20-cs2-midnight-cs-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-174145\20-cs2-midnight-cs-2-explained-use-cases-and-practical-tips.md`
