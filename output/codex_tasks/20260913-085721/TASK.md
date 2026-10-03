# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write 70 unique English Tier-2 SEO/GEO articles: seven separate batches of 10, one batch for each host activosblog.com, pages10.com, blogminds.com, blogocial.com, full-design.com, pointblog.net, and bloggazza.com. In every batch create exactly one article linking to each of these targets: https://cluster.center/en with anchor cheats; https://cluster.center/en/cs2 with anchor cs2 cheats; https://cluster.center/en/deadlock with anchor deadlock cheats; https://cheatsgaming.com/; https://cheatsgaming.com/games/cs2/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52; https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924; https://cheatsgaming.com/games/cs2/top-cheats-for-cs2-the-best-hack-cfab8351f70b; https://cheatsgaming.com/games/cs2/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364; https://cheatsgaming.com/games/deadlock/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e; https://cheatsgaming.com/games/cs2/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710. Vary every CheatsGaming anchor while ensuring it contains cheat or hack. Do not repeat angles from previously published articles. Each article must be at least 600 words, include SEO front matter, one source-page image, image alt text, answer-first opening, three or more H2 sections, and FAQ. Keep content high-level, educational, risk-aware, and never provide anti-cheat bypass or evasion instructions. Product mapping: CS2 and Deadlock use cluster.center.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260913-085721`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260913-085721.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. CS2 Aimbot Settings Explained: FOV, Smooth and Hitboxes

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\01-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`

### 2. CS2 Aimbot Settings Explained: FOV, Smooth and Hitboxes

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\02-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\02-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\02-cs2-aimbot-settings-explained-fov-smooth-and-hitboxes.md`

### 3. CS2 ESP Explained: Boxes, Chams, Skeleton and Status Icons

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\03-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\03-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\03-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`

### 4. CS2 ESP Explained: Boxes, Chams, Skeleton and Status Icons

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\04-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\04-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\04-cs2-esp-explained-boxes-chams-skeleton-and-status-icons.md`

### 5. CS2 TriggerBot Settings Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\05-cs2-triggerbot-settings-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\05-cs2-triggerbot-settings-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\05-cs2-triggerbot-settings-explained.md`

### 6. CS2 TriggerBot Settings Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\06-cs2-triggerbot-settings-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\06-cs2-triggerbot-settings-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\06-cs2-triggerbot-settings-explained.md`

### 7. CS2 Hack vs Assistive Tools: What Players Search For

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\07-cs2-hack-vs-assistive-tools-what-players-search-for.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\07-cs2-hack-vs-assistive-tools-what-players-search-for.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\07-cs2-hack-vs-assistive-tools-what-players-search-for.md`

### 8. CS2 Hack vs Assistive Tools: What Players Search For

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\08-cs2-hack-vs-assistive-tools-what-players-search-for.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\08-cs2-hack-vs-assistive-tools-what-players-search-for.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\08-cs2-hack-vs-assistive-tools-what-players-search-for.md`

### 9. CS2 External Cheat Feature Glossary

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\09-cs2-external-cheat-feature-glossary.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\09-cs2-external-cheat-feature-glossary.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\09-cs2-external-cheat-feature-glossary.md`

### 10. CS2 External Cheat Feature Glossary

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\10-cs2-external-cheat-feature-glossary.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\10-cs2-external-cheat-feature-glossary.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\10-cs2-external-cheat-feature-glossary.md`

### 11. CS2 Bomb Timer, Spectator List and Keybinds Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\11-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\11-cs2-bomb-timer-spectator-list-and-keybinds-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\11-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`

### 12. CS2 Bomb Timer, Spectator List and Keybinds Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\12-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\12-cs2-bomb-timer-spectator-list-and-keybinds-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\12-cs2-bomb-timer-spectator-list-and-keybinds-explained.md`

### 13. CS2 Cheat Features Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\13-cs2-cheat-features-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\13-cs2-cheat-features-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\13-cs2-cheat-features-explained.md`

### 14. CS2 Cheat Features Explained

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\14-cs2-cheat-features-explained.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\14-cs2-cheat-features-explained.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\14-cs2-cheat-features-explained.md`

### 15. Сервера awp cs2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\15-сервера-awp-cs2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\15-сервера-awp-cs2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\15-сервера-awp-cs2-полныи-разбор-для-cs2.md`

### 16. Cs2 настройки графики: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\16-cs2-настроики-графики-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\16-cs2-настроики-графики-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\16-cs2-настроики-графики-полныи-разбор-для-cs2.md`

### 17. Фаталити кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\17-фаталити-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\17-фаталити-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\17-фаталити-кс-2-полныи-разбор-для-cs2.md`

### 18. Настройка nvidia для cs 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\18-настроика-nvidia-для-cs-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\18-настроика-nvidia-для-cs-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\18-настроика-nvidia-для-cs-2-полныи-разбор-для-cs2.md`

### 19. Паблик кс 2 1 на 1: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\19-паблик-кс-2-1-на-1-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\19-паблик-кс-2-1-на-1-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\19-паблик-кс-2-1-на-1-полныи-разбор-для-cs2.md`

### 20. Консольные команды cs2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\20-консольные-команды-cs2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\20-консольные-команды-cs2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\20-консольные-команды-cs2-полныи-разбор-для-cs2.md`

### 21. Команды для оптимизации кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\21-команды-для-оптимизации-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\21-команды-для-оптимизации-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\21-команды-для-оптимизации-кс-2-полныи-разбор-для-cs2.md`

### 22. Буст фейсита кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\22-буст-феисита-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\22-буст-феисита-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\22-буст-феисита-кс2-полныи-разбор-для-cs2.md`

### 23. Как скачать карту в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\23-как-скачать-карту-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\23-как-скачать-карту-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\23-как-скачать-карту-в-кс2-полныи-разбор-для-cs2.md`

### 24. Карты для тренировки раскида в кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\24-карты-для-тренировки-раскида-в-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\24-карты-для-тренировки-раскида-в-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\24-карты-для-тренировки-раскида-в-кс-2-полныи-разбор-для-cs2.md`

### 25. Что делать если не сохраняются настройки в кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\25-что-делать-если-не-сохраняются-настроики-в-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\25-что-делать-если-не-сохраняются-настроики-в-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\25-что-делать-если-не-сохраняются-настроики-в-кс-2-полныи-разбор-для-cs2.md`

### 26. Что делать если не открывается консоль в кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\26-что-делать-если-не-открывается-консоль-в-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\26-что-делать-если-не-открывается-консоль-в-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\26-что-делать-если-не-открывается-консоль-в-кс-2-полныи-разбор-для-cs2.md`

### 27. Повтор гранаты кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\27-повтор-гранаты-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\27-повтор-гранаты-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\27-повтор-гранаты-кс2-полныи-разбор-для-cs2.md`

### 28. Нужен ли прайм для фейсит кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\28-нужен-ли-праим-для-феисит-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\28-нужен-ли-праим-для-феисит-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\28-нужен-ли-праим-для-феисит-кс2-полныи-разбор-для-cs2.md`

### 29. Раскид даст 2 в кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\29-раскид-даст-2-в-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\29-раскид-даст-2-в-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\29-раскид-даст-2-в-кс-2-полныи-разбор-для-cs2.md`

### 30. Оптимизация во весь экран кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\30-оптимизация-во-весь-экран-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\30-оптимизация-во-весь-экран-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\30-оптимизация-во-весь-экран-кс-2-полныи-разбор-для-cs2.md`

### 31. Посмотреть статистику в кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\31-посмотреть-статистику-в-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\31-посмотреть-статистику-в-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\31-посмотреть-статистику-в-кс-2-полныи-разбор-для-cs2.md`

### 32. Конфиги про игроков кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\32-конфиги-про-игроков-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\32-конфиги-про-игроков-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\32-конфиги-про-игроков-кс2-полныи-разбор-для-cs2.md`

### 33. Как сделать 4 3 в кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\33-как-сделать-4-3-в-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\33-как-сделать-4-3-в-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\33-как-сделать-4-3-в-кс-2-полныи-разбор-для-cs2.md`

### 34. Тренировка аим кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\34-тренировка-аим-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\34-тренировка-аим-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\34-тренировка-аим-кс2-полныи-разбор-для-cs2.md`

### 35. Карты для аима в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\35-карты-для-аима-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\35-карты-для-аима-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\35-карты-для-аима-в-кс2-полныи-разбор-для-cs2.md`

### 36. CS2: Xone Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\36-cs2-xone-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\36-cs2-xone-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\36-cs2-xone-cs2-explained-use-cases-and-practical-tips.md`

### 37. CS2: Xone Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\37-cs2-xone-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\37-cs2-xone-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\37-cs2-xone-cs2-explained-use-cases-and-practical-tips.md`

### 38. Смок окно мираж кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\38-смок-окно-мираж-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\38-смок-окно-мираж-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\38-смок-окно-мираж-кс-2-полныи-разбор-для-cs2.md`

### 39. Расширение для фейсита кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\39-расширение-для-феисита-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\39-расширение-для-феисита-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\39-расширение-для-феисита-кс-2-полныи-разбор-для-cs2.md`

### 40. Бинд колесико мыши кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\40-бинд-колесико-мыши-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\40-бинд-колесико-мыши-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\40-бинд-колесико-мыши-кс-2-полныи-разбор-для-cs2.md`

### 41. При запуске кс 2 черный экран но звук есть: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\41-при-запуске-кс-2-черныи-экран-но-звук-есть-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\41-при-запуске-кс-2-черныи-экран-но-звук-есть-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\41-при-запуске-кс-2-черныи-экран-но-звук-есть-полныи-разбор-для-cs2.md`

### 42. CS2: Dust 2 Cs 2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\42-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\42-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\42-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.md`

### 43. CS2: Dust 2 Cs 2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\43-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\43-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\43-cs2-dust-2-cs-2-explained-use-cases-and-practical-tips.md`

### 44. Как поменять руки в кс 2 в настройках: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\44-как-поменять-руки-в-кс-2-в-настроиках-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\44-как-поменять-руки-в-кс-2-в-настроиках-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\44-как-поменять-руки-в-кс-2-в-настроиках-полныи-разбор-для-cs2.md`

### 45. Как оптимизировать кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\45-как-оптимизировать-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\45-как-оптимизировать-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\45-как-оптимизировать-кс2-полныи-разбор-для-cs2.md`

### 46. Карты для раскидок в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\46-карты-для-раскидок-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\46-карты-для-раскидок-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\46-карты-для-раскидок-в-кс2-полныи-разбор-для-cs2.md`

### 47. Как растянуть экран кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\47-как-растянуть-экран-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\47-как-растянуть-экран-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\47-как-растянуть-экран-кс-2-полныи-разбор-для-cs2.md`

### 48. CS2: Dm Server Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\48-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\48-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\48-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.md`

### 49. CS2: Dm Server Cs2 Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\49-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\49-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\49-cs2-dm-server-cs2-explained-use-cases-and-practical-tips.md`

### 50. Как поставить конфиг в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\50-как-поставить-конфиг-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\50-как-поставить-конфиг-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\50-как-поставить-конфиг-в-кс2-полныи-разбор-для-cs2.md`

### 51. Раскидка на мираже кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\51-раскидка-на-мираже-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\51-раскидка-на-мираже-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\51-раскидка-на-мираже-кс-2-полныи-разбор-для-cs2.md`

### 52. Команды для банихопа в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\52-команды-для-банихопа-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\52-команды-для-банихопа-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\52-команды-для-банихопа-в-кс2-полныи-разбор-для-cs2.md`

### 53. Как перенести конфиг в кс 2 на другой аккаунт: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\53-как-перенести-конфиг-в-кс-2-на-другои-аккаунт-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\53-как-перенести-конфиг-в-кс-2-на-другои-аккаунт-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\53-как-перенести-конфиг-в-кс-2-на-другои-аккаунт-полныи-разбор-для-cs2.md`

### 54. Не появляются карты из мастерской кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\54-не-появляются-карты-из-мастерскои-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\54-не-появляются-карты-из-мастерскои-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\54-не-появляются-карты-из-мастерскои-кс-2-полныи-разбор-для-cs2.md`

### 55. Как убрать лаги кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\55-как-убрать-лаги-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\55-как-убрать-лаги-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\55-как-убрать-лаги-кс-2-полныи-разбор-для-cs2.md`

### 56. Айпи серверов кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\56-аипи-серверов-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\56-аипи-серверов-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\56-аипи-серверов-кс2-полныи-разбор-для-cs2.md`

### 57. Смоки мираж кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\57-смоки-мираж-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\57-смоки-мираж-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\57-смоки-мираж-кс2-полныи-разбор-для-cs2.md`

### 58. Как создать сервер в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\58-как-создать-сервер-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\58-как-создать-сервер-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\58-как-создать-сервер-в-кс2-полныи-разбор-для-cs2.md`

### 59. Как сделать бинд в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\59-как-сделать-бинд-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\59-как-сделать-бинд-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\59-как-сделать-бинд-в-кс2-полныи-разбор-для-cs2.md`

### 60. Паблик кс2 мираж: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\60-паблик-кс2-мираж-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\60-паблик-кс2-мираж-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\60-паблик-кс2-мираж-полныи-разбор-для-cs2.md`

### 61. Как открыть премьер в кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\61-как-открыть-премьер-в-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\61-как-открыть-премьер-в-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\61-как-открыть-премьер-в-кс2-полныи-разбор-для-cs2.md`

### 62. Карты с прицелами кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\62-карты-с-прицелами-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\62-карты-с-прицелами-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\62-карты-с-прицелами-кс-2-полныи-разбор-для-cs2.md`

### 63. Как забиндить ноуклип кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\63-как-забиндить-ноуклип-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\63-как-забиндить-ноуклип-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\63-как-забиндить-ноуклип-кс2-полныи-разбор-для-cs2.md`

### 64. Бинды для кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\64-бинды-для-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\64-бинды-для-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\64-бинды-для-кс2-полныи-разбор-для-cs2.md`

### 65. Оптимизация для кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\65-оптимизация-для-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\65-оптимизация-для-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\65-оптимизация-для-кс2-полныи-разбор-для-cs2.md`

### 66. Разрешение в параметрах запуска кс2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\66-разрешение-в-параметрах-запуска-кс2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\66-разрешение-в-параметрах-запуска-кс2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\66-разрешение-в-параметрах-запуска-кс2-полныи-разбор-для-cs2.md`

### 67. Что с серверами кс 2: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\67-что-с-серверами-кс-2-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\67-что-с-серверами-кс-2-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\67-что-с-серверами-кс-2-полныи-разбор-для-cs2.md`

### 68. Аим карты в кс 2 с ботами: полный разбор для CS2

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\68-аим-карты-в-кс-2-с-ботами-полныи-разбор-для-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\68-аим-карты-в-кс-2-с-ботами-полныи-разбор-для-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\68-аим-карты-в-кс-2-с-ботами-полныи-разбор-для-cs2.md`

### 69. CS2: Aim Cs2 Map Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\69-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\69-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\69-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.md`

### 70. CS2: Aim Cs2 Map Explained, Use Cases and Practical Tips

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260913-085721\70-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260913-085721\70-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260913-085721\70-cs2-aim-cs2-map-explained-use-cases-and-practical-tips.md`
