# ТЗ: восемь T2-статей для двух CS2-страниц Medium

## Цель кластера

Подготовить восемь самостоятельных англоязычных статей: четыре поддерживают страницу про legit cheats, четыре — страницу про external cheats. Каждая статья закрывает отдельный поисковый интент, дает читателю полноценный ответ до ссылки и содержит один контекстный backlink на назначенную Medium-страницу.

Целевые страницы:

- Legit: https://medium.com/@mrkhertz/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364
- External: https://medium.com/@mrkhertz/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4

Общие требования:

- Язык статей: English.
- Стиль: direct, practical, conversational, lightly gamer-aware; короткие абзацы, без SEO-воды.
- Не делать новый рейтинг, top-5, best-cheat listicle или прямой обзор Cluster: эти интенты уже заняты.
- Не давать инструкции по обходу anti-cheat, evasion, injection, driver/memory access, скрытию поведения или подбору «незаметных» числовых настроек.
- Не обещать безопасность, отсутствие банов, актуальную цену, trial, detection status или конкретную anti-cheat protection.
- `cluster.center` упомянуть один раз в спокойном feature-oriented блоке после основной образовательной части. Прямую продуктовую ссылку в T2 не ставить: главный исходящий CTA — назначенная Medium-страница.
- Один контекстный backlink на целевую страницу, желательно dofollow, в зоне 35–65% текста. Не ставить в первом абзаце, FAQ, author bio или рядом с другим коммерческим URL.
- На каждом отдельном домене использовать только один из восьми анкоров ниже. Не повторять exact-match anchor между публикациями.
- Не использовать Markdown-таблицы. Сравнения оформлять списками.
- Финал каждой статьи: FAQ из 4–6 вопросов и короткий вывод/soft CTA.
- Каждый draft должен иметь YAML front matter, description до 160 символов с primary keyword, 2–5 image placement notes и internal-link suggestions.
- При генерации каждого B-ассета физически загрузить обе перечисленные reference-картинки; строки `Reference A/B` задают их раздельные роли, а не служат только текстовым описанием.

## T2-01 — Legit / терминологический интент

### SEO

- Title: `Legit vs Rage vs Semirage in CS2 Explained`
- Slug: `legit-vs-rage-vs-semirage-cs2`
- Primary keyword: `legit vs rage CS2`
- Secondary keywords: `legit CS2 cheat`, `semirage CS2`, `HvH meaning`, `rage cheat meaning`
- Description: `Legit vs rage CS2 explained: what legit, semirage and HvH terminology means, where the categories overlap, and what they do not prove.`
- Intent: informational terminology; пользователь путает legit, semirage, rage и HvH.
- Volume: 1,300–1,700 words.
- Risk: restricted; только определения, категории и risk-aware expectations.

### Тезис и структура

Тезис: legit/rage/semirage описывают предполагаемый стиль использования и набор функций, но сами по себе не доказывают безопасность или техническую архитектуру продукта.

Структура:

1. `# Legit vs Rage vs Semirage in CS2 Explained`
2. `## Quick answer: the terms in plain English`
3. `## What “legit” means in CS2 cheat discussions`
4. `## What semirage changes`
5. `## Rage and HvH are not the same question as architecture`
6. `## Legit does not automatically mean external or safe`
7. `## A better checklist for reading product claims`
8. `## Where Cluster fits in the terminology`
9. `## FAQ`
10. Conclusion.

Обязательно разобрать ошибку `legit = undetectable` и различие между user-facing label и подтвержденным фактом. Не обсуждать способы маскировки.

### Backlink

- URL: legit target.
- Anchor: `legit CS2 cheats`
- Placement: после раздела `A better checklist for reading product claims`.
- Suggested sentence: `If you want a current market comparison after the terminology, this roundup of [legit CS2 cheats](https://medium.com/@mrkhertz/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364) is the natural next read.`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 1.
- Style branch: B3 symbolic object.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: text-in-image.
- Reference A: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-08.png` — composition only: asymmetrical headline/hero balance and one controlled transformation.
- Reference B: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-05.png` — render/palette/typography only: large headline mass, warm rounded depth, stable lower hero crop.
- Reference fidelity target: at least 4/5 across layout silhouette, light palette, rounded shapes, depth and typography mass.
- Prompt QA score: 93/100.

Final prompt:

> Create a hero cover for an editorial article titled “Legit vs Rage vs Semirage in CS2 Explained.” This is generated asset #1, branch B3 — warm narrative symbolic object. Editorial thesis: the three labels describe different usage categories but do not prove safety or architecture. Represent the idea as one oversized rounded three-position selector dial with three distinct detents, physically believable and softly toy-like; the selector is the only hero and the action is choosing a label. Canvas: 16:9 landscape, 2K master, 6% crop-safe margins. Put the headline in the left 36% and the dial in the lower-right 52%, with one small neutral indicator. Background must be exact Cluster violet `#635FD5` as the dominant 55–65% field, replacing all yellow/amber background; keep warm cream and coral only on the dial. Use matte soft-touch plastic and painted metal, eye-level three-quarter camera, 55 mm feel, soft upper-left daylight, rounded contact shadow and mild foreground depth. Render exactly “LEGIT, RAGE, OR SEMIRAGE?” in English uppercase, three lines, bold condensed geometric sans-serif, upper-left; no other text. Image A `reference-08.png` is composition-only; Image B `reference-05.png` is render/palette/typography-only. Do not copy their objects, words, logos or exact layout. Require 4/5 branch fidelity. No CS2 logo, weapons, characters, menus, code, shields, padlocks, fake statistics, neon, cyberpunk or extra labels. If constraints conflict, prioritize thesis, headline accuracy, one-hero hierarchy, exact violet field, physical plausibility, then detail.

`IMAGE_SLOT_02` — manual editorial diagram after the quick answer: three labeled cards `Legit`, `Semirage`, `Rage/HvH`, with one sentence each. This is a typeset diagram, not generated art; cite no technical safety claims.

## T2-02 — Legit / aimbot settings explainer

### SEO

- Title: `CS2 Aimbot Settings: FOV, Smooth and Hitboxes`
- Slug: `cs2-aimbot-settings-fov-smooth-hitboxes`
- Primary keyword: `cs2 aimbot settings`
- Secondary keywords: `CS2 FOV`, `aim smoothing`, `CS2 hitboxes`, `weapon profiles`
- Description: `CS2 aimbot settings explained at a high level: FOV, Smooth, target priority, hitboxes, checks and weapon profiles without stealth recipes.`
- Intent: feature meaning, not ready-made configuration.
- Volume: 1,600–2,100 words.
- Risk: restricted; no recommended values or evasion advice.

### Тезис и структура

Тезис: хороший explainer должен показать, какую проблему решает каждый control и как controls interact, не превращаясь в «legit config» recipe.

Структура:

1. `# CS2 Aimbot Settings: FOV, Smooth and Hitboxes`
2. `## Quick answer: what each control changes`
3. `## FOV is the capture area, not a quality score`
4. `## Smooth changes movement character`
5. `## Crosshair priority vs hit-chance priority`
6. `## Hitboxes: head, neck, spine, hips, arms and legs`
7. `## Visible, Team and Flash checks`
8. `## Why weapon profiles exist`
9. `## How Cluster groups these controls`
10. `## FAQ`

Не давать числовые пресеты, советы «как выглядеть естественно» или привязку настроек к обходу VAC/VACLive.

### Backlink

- URL: legit target.
- Anchor: `legit CS2 cheat comparison`
- Placement: в переходе между weapon profiles и Cluster block.
- Suggested sentence: `For a broader product-level shortlist beyond individual controls, see this [legit CS2 cheat comparison](https://medium.com/@mrkhertz/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364).`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 2.
- Style branch: A tactile industrial product poster.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: art-first.
- Reference roles: no uploaded image references; use the canonical branch-A text specification only.
- Prompt QA score: 92/100.

Final prompt:

> Create a 16:9 2K hero cover for an editorial explainer about CS2 aimbot settings. This is generated asset #2, branch A — tactile industrial product poster. Editorial thesis: FOV, Smooth and hitboxes are separate controls in one system, not a single “strength” slider. Represent the system as one compact optical calibration instrument with a circular capture ring, one damped motion track and one simplified six-zone mannequin token inside the device; the instrument is the only hero and the action is calibrating. Reserve x=6–42%, y=9–50% as a completely empty headline safe zone. Place the device in the right 56%, occupying about 58% of the frame. Background off-white `#EFEFEA`; hero matte charcoal and frosted glass; exact Cluster violet `#635FD5` only on one active calibration ring covering 4–6% of the frame. Do not use violet as a wash or light. Camera high three-quarter, 50 mm feel, moderate depth, large upper-left studio source, clean contact shadow. Art-first: no letters, numbers, pseudo-UI, logos or labels. No game art, weapon, character, target silhouette, code, neon, crosshair glamour, fake values or extra machines. Reference roles: none attached. Prioritize editorial meaning, one-hero hierarchy, safe zone, exact small violet accent, physical contacts, then surface detail.

`IMAGE_SLOT_02` — verified real product UI screenshot of the Aimbot tab after `Why weapon profiles exist`; crop only, hide account data, do not edit values or fabricate controls. If rights are unavailable, replace with a manually drawn neutral control map.

## T2-03 — Legit / Aimbot vs TriggerBot

### SEO

- Title: `CS2 Aimbot vs TriggerBot: What Changes?`
- Slug: `cs2-aimbot-vs-triggerbot`
- Primary keyword: `aimbot vs triggerbot CS2`
- Secondary keywords: `CS2 triggerbot`, `aim assistance`, `shot timing`, `holding angles`
- Description: `Aimbot vs triggerbot CS2 explained: one changes aim assistance, the other changes shot timing, with a clear feature-by-feature breakdown.`
- Intent: comparison of two feature categories.
- Volume: 1,300–1,800 words.
- Risk: restricted; functional comparison only.

### Тезис и структура

1. `# CS2 Aimbot vs TriggerBot: What Changes?`
2. `## Quick answer: aim movement vs shot timing`
3. `## What Aimbot controls`
4. `## What TriggerBot controls`
5. `## Shared concepts: hitboxes, checks and profiles`
6. `## Why the features should not be treated as interchangeable`
7. `## Reading product feature lists without hype`
8. `## Where Cluster fits`
9. `## FAQ`

Сравнивать задачи controls, не давать operational setup и не объяснять, как снизить подозрительность.

### Backlink

- URL: legit target.
- Anchor: `Mark Hertz’s legit CS2 roundup`
- Placement: после `Reading product feature lists without hype`.
- Suggested sentence: `Once the difference between aiming and timing is clear, [Mark Hertz’s legit CS2 roundup](https://medium.com/@mrkhertz/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364) shows how complete products package those features.`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 3.
- Style branch: B2 modular message card.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: text-in-image.
- Reference A: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-06.png` — composition only: split scene/message modules and thick rounded gutter.
- Reference B: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-04.png` — render/palette/typography only: warm rounded 3D, simple central hero, large clean headline.
- Fidelity: minimum 4/5.
- Prompt QA score: 92/100.

Final prompt:

> Create a 16:9 2K editorial cover for “CS2 Aimbot vs TriggerBot: What Changes?” This is generated asset #3, branch B2 warm narrative modular card. Editorial thesis: aim assistance changes movement toward a target, while TriggerBot changes the timing of a shot. Use one rounded dual-purpose training device as the single hero: its left physical motion track guides a pointer, while its right mechanical timer releases one neutral signal token. The action is comparing movement and timing. Split the frame into a left headline module (36%) and right scene module (58%) with a thick off-white rounded gutter. Use exact Cluster violet `#635FD5` as the dominant 50–60% field replacing yellow/amber; warm cream, coral and muted teal may appear only on the device. Camera slightly elevated, 55 mm feel, two depth planes, soft upper-left daylight, rounded shadows, light grain. Render exactly “AIM OR TIMING?” in English uppercase, two lines, bold condensed geometric sans-serif in the left module; no other text. Image A `reference-06.png` supplies layout only. Image B `reference-04.png` supplies rounded rendering and typography mass only. Do not copy people, animals, wording or exact layouts. Require 4/5 fidelity. No guns, targets shaped like people, CS2 logos, gameplay, menus, code, fake values, neon or multiple devices. Priority: distinction between movement and timing, exact headline, modular hierarchy, exact violet field, physical clarity, detail.

`IMAGE_SLOT_02` — manual two-column diagram after the quick answer: `Aimbot = aim movement` and `TriggerBot = shot timing`; no numeric examples.

## T2-04 — Legit / target priority and profiles

### SEO

- Title: `CS2 Target Priority and Weapon Profiles Explained`
- Slug: `cs2-target-priority-weapon-profiles`
- Primary keyword: `cs2 target priority`
- Secondary keywords: `crosshair priority`, `hit chance priority`, `weapon profiles`, `CS2 hitboxes`
- Description: `CS2 target priority explained with crosshair and hit-chance concepts, weapon profiles, hitboxes and checks at a safe high level.`
- Intent: narrow feature explainer.
- Volume: 1,200–1,600 words.
- Risk: restricted; no best profile or weapon-specific stealth recipe.

### Тезис и структура

1. `# CS2 Target Priority and Weapon Profiles Explained`
2. `## Quick answer`
3. `## What target priority decides`
4. `## Crosshair priority in plain English`
5. `## Hit-chance priority as a product concept`
6. `## Why separate weapon profiles exist`
7. `## Hitboxes and checks are separate decisions`
8. `## Where Cluster fits`
9. `## FAQ`

### Backlink

- URL: legit target.
- Anchor: `how legit CS2 tools compare`
- Placement: immediately before the Cluster block.
- Suggested sentence: `For the wider choice context, continue with [how legit CS2 tools compare](https://medium.com/@mrkhertz/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364) after you understand the individual controls.`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 4.
- Style branch: A.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: art-first.
- Reference roles: none attached.
- Prompt QA score: 91/100.

Final prompt:

> Create a 16:9 2K hero cover for an editorial article about target priority and weapon profiles in CS2 assistance tools. Generated asset #4, branch A tactile industrial product poster. Editorial thesis: priority rules choose among available targets, while weapon profiles store different control groups; they are related but not the same setting. Represent this as one tabletop selector console with a rotating profile carousel feeding one highlighted decision slot. The console is the only hero and the action is selecting. Reserve the upper-left 40% as a clean headline safe zone. Place the console right and low, occupying 55–62% of frame. Use warm off-white background, matte charcoal body, translucent neutral profile cartridges and exact Cluster violet `#635FD5` on one active decision slot only, 4–5% of frame. Materials: soft-touch plastic and frosted acrylic. Camera high three-quarter, 45 mm equivalent, deep enough focus to read the mechanism, clean upper-left studio light and one long soft shadow. Art-first: no text, letters, numbers, logos or fake UI. No weapons, player models, crosshair, code, neon, multiple consoles or statistics. No references attached. Priority: clear selection metaphor, one hero, empty safe zone, small violet accent, physical plausibility, minor detail.

`IMAGE_SLOT_02` — verified Aimbot settings screenshot showing only the target-priority/profile region; crop without changing UI. Caption must call it an example interface, not a universal CS2 standard.

## T2-05 — External / architecture terminology

### SEO

- Title: `External vs Internal CS2 Cheats: Key Differences`
- Slug: `external-vs-internal-cs2-cheats`
- Primary keyword: `external vs internal CS2 cheats`
- Secondary keywords: `external cheat CS2`, `internal cheat meaning`, `CS2 overlay`, `feature tradeoffs`
- Description: `External vs internal CS2 cheats explained at a high level: terminology, interface and feature tradeoffs, plus claims readers should treat cautiously.`
- Intent: architecture terminology and marketing-claim literacy.
- Volume: 1,500–2,000 words.
- Risk: restricted; no implementation mechanics, memory access, driver or bypass discussion.

### Тезис и структура

1. `# External vs Internal CS2 Cheats: Key Differences`
2. `## Quick answer without the marketing spin`
3. `## What “external” usually means in product language`
4. `## What “internal” usually means`
5. `## Interface and feature tradeoffs`
6. `## Why architecture alone does not prove safety`
7. `## Questions to ask before trusting a claim`
8. `## Where Cluster fits`
9. `## FAQ`

Не подтверждать техническое описание конкретного продукта, если оно дано только маркетингом. Не писать, что external «не взаимодействует» с игрой как установленный факт.

### Backlink

- URL: external target.
- Anchor: `external cheats for CS2`
- Placement: после `Questions to ask before trusting a claim`.
- Suggested sentence: `If you want to see which products the author groups into this category, read the current [external cheats for CS2](https://medium.com/@mrkhertz/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4) roundup.`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 5.
- Style branch: B2.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: text-in-image.
- Reference A: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-07.png` — composition only: macro device crop and information outside the device.
- Reference B: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-06.png` — render/palette/typography only: rounded modules, clean gutter, editorial message mass.
- Fidelity: minimum 4/5.
- Prompt QA score: 94/100.

Final prompt:

> Create a 16:9 2K cover for “External vs Internal CS2 Cheats: Key Differences.” Generated asset #5, branch B2 warm narrative modular message card. Editorial thesis: external and internal are architecture labels with tradeoffs, not automatic safety ratings. Use one oversized rounded enclosure as the single hero, shown in two physical states within the same object: one readable outer layer and one sealed inner module. The action is revealing a boundary, not showing implementation. Put the headline in a large left module occupying 38% and the hero in the right 56%, with a thick cream gutter. Exact Cluster violet `#635FD5` must replace the yellow/amber reference field and cover 55–65% of the frame. Secondary colors: warm cream, coral and muted teal on the object only. Soft rounded 3D, eye-level macro camera, 60 mm feel, two depth planes, upper-left daylight, clean contact shadow and restrained bloom. Render exactly “EXTERNAL VS INTERNAL” in English uppercase, three lines, bold condensed geometric sans-serif; no other text. Image A `reference-07.png` supplies macro crop only. Image B `reference-06.png` supplies modular rendering and typography mass only. Do not copy their phone, people, wording, branding or exact layout. Require 4/5 fidelity. No diagrams of code, drivers, memory, injection, bypass, anti-cheat, locks, shields, hackers, game logos or fake performance claims. Priority: factual boundary metaphor, headline, one-object hierarchy, exact violet field, warm depth, detail.

`IMAGE_SLOT_02` — manually typeset comparison list after `Interface and feature tradeoffs`; label all points as general tendencies, not universal facts.

## T2-06 — External / ESP visual taxonomy

### SEO

- Title: `CS2 ESP Explained: Boxes, Chams and Skeletons`
- Slug: `cs2-esp-boxes-chams-skeletons`
- Primary keyword: `cs2 esp`
- Secondary keywords: `CS2 chams`, `CS2 skeleton ESP`, `health bar ESP`, `status indicators`
- Description: `CS2 ESP explained: boxes, chams, skeletons, health and ammo bars, status icons, world indicators and the problem of visual clutter.`
- Intent: visual feature glossary and readability.
- Volume: 1,600–2,100 words.
- Risk: restricted; describe display categories, not tactical exploitation.

### Тезис и структура

1. `# CS2 ESP Explained: Boxes, Chams and Skeletons`
2. `## Quick answer: ESP is a visual-information layer`
3. `## Boxes, names and skeletons`
4. `## Chams vs outlines`
5. `## Health, ammo and weapon information`
6. `## Blind, zoom and reload indicators`
7. `## Bomb, defuse and other world indicators`
8. `## Readability beats a screen full of noise`
9. `## Where Cluster fits`
10. `## FAQ`

### Backlink

- URL: external target.
- Anchor: `CS2 external cheat overview`
- Placement: после раздела о readability.
- Suggested sentence: `For a broader shortlist after the visual-feature breakdown, see this [CS2 external cheat overview](https://medium.com/@mrkhertz/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4).`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 6.
- Style branch: A.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: art-first.
- Reference roles: none attached.
- Prompt QA score: 92/100.

Final prompt:

> Create a 16:9 2K editorial cover for a high-level article explaining CS2 ESP layers. Generated asset #6, branch A tactile industrial product poster. Editorial thesis: ESP is a stack of visual-information layers, and too many layers create clutter. Represent the concept as one transparent inspection panel with three physically separated overlays — outer box frame, skeletal line layer and status-token layer — mounted in a single frosted-glass instrument. The panel is the only hero and the action is layering. Reserve x=6–43%, y=8–48% as an empty off-white headline zone. Place the instrument right, occupying 55% of frame. Palette: off-white `#EFEFEA`, cool gray glass, charcoal frame; exact Cluster violet `#635FD5` on one active layer tab only, 4–6% of frame, never as background or glow. Materials: frosted glass and matte aluminum. Camera frontal three-quarter, 65 mm feel, shallow-to-moderate depth, clean diffuse upper-left light. Art-first: no text, labels, numbers, logos or pseudo-UI. No player likeness, weapons, maps, wallhack gameplay, game logo, neon, HUD clutter, fake values or extra panels. No references attached. Priority: layer concept, one hero, safe zone, exact small violet accent, optical plausibility, detail.

`IMAGE_SLOT_02` — verified ESP UI screenshot after the taxonomy sections; preserve every pixel except privacy redaction and crop. If unavailable, use a neutral manually drawn layer diagram rather than generated fake UI.

## T2-07 — External / TriggerBot settings

### SEO

- Title: `CS2 TriggerBot Settings Explained`
- Slug: `cs2-triggerbot-settings-explained`
- Primary keyword: `cs2 triggerbot settings`
- Secondary keywords: `reaction time`, `between-shots delay`, `hit chance`, `minimum damage`, `multipoint scale`
- Description: `CS2 triggerbot settings explained at a high level: reaction time, delays, hitboxes, checks, hit chance and multipoint concepts.`
- Intent: feature meaning and taxonomy.
- Volume: 1,500–2,000 words.
- Risk: restricted; no numeric presets, angle-holding recipe or evasion advice.

### Тезис и структура

1. `# CS2 TriggerBot Settings Explained`
2. `## Quick answer: TriggerBot is about shot timing`
3. `## Reaction time and between-shots delay`
4. `## Hitboxes and checks`
5. `## Minimum damage and hit chance as thresholds`
6. `## Multipoint scale and visualization`
7. `## What settings cannot guarantee`
8. `## Where Cluster fits`
9. `## FAQ`

### Backlink

- URL: external target.
- Anchor: `external CS2 comparison`
- Placement: после `What settings cannot guarantee`.
- Suggested sentence: `To place TriggerBot in the context of complete products, continue with Mark Hertz’s [external CS2 comparison](https://medium.com/@mrkhertz/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4).`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 7.
- Style branch: B3.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: text-in-image.
- Reference A: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-08.png` — composition only: one diagonal symbolic hero balanced against a large left headline.
- Reference B: `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-05.png` — render/palette/typography only: bold headline mass, warm rounded light and lower hero crop.
- Fidelity: minimum 4/5.
- Prompt QA score: 93/100.

Final prompt:

> Create a 16:9 2K editorial cover for “CS2 TriggerBot Settings Explained.” Generated asset #7, branch B3 warm narrative symbolic object. Editorial thesis: TriggerBot controls the timing conditions around a shot, not aim movement. Use one oversized rounded mechanical stopwatch with a single neutral signal token paused just before a release gate; the stopwatch is the only hero and the action is waiting for a condition. Place the exact headline in the left 38% and the hero diagonally in the lower-right 54%. Exact Cluster violet `#635FD5` replaces yellow/amber and forms the dominant 55–65% field. Use warm cream, coral and muted teal only on the stopwatch and token. Soft toy-like but premium 3D, matte plastic and painted metal, 60 mm three-quarter camera, two depth planes, upper-left daylight, rounded contact shadow, mild bloom. Render exactly “SHOT TIMING, EXPLAINED” in English uppercase, three lines, bold condensed geometric sans-serif; no other text. Image A `reference-08.png` supplies diagonal composition only. Image B `reference-05.png` supplies rendering and typography mass only. Do not copy objects, words, logos or exact layouts. Require 4/5 fidelity. No guns, player targets, crosshairs, code, anti-cheat symbols, numeric values, menus, neon or extra clocks. Priority: timing thesis, exact headline, one-hero silhouette, exact violet field, physical plausibility, detail.

`IMAGE_SLOT_02` — verified TriggerBot UI crop showing the named controls, with values left untouched. Caption: `Example grouping of TriggerBot controls; available options can change.`

## T2-08 — External / Hub utilities

### SEO

- Title: `CS2 Bomb Timer, Spectator List and Keybinds`
- Slug: `cs2-bomb-timer-spectator-list-keybinds`
- Primary keyword: `cs2 bomb timer`
- Secondary keywords: `CS2 spectator list`, `CS2 keybinds overlay`, `CS2 HUD utilities`, `bomb timer overlay`
- Description: `CS2 bomb timer, spectator list and keybinds explained as HUD utilities: what each shows, why clarity matters and what claims to avoid.`
- Intent: niche utility feature explainer.
- Volume: 1,300–1,700 words.
- Risk: elevated; Spectator List is observer awareness only, never an evasion signal.

### Тезис и структура

1. `# CS2 Bomb Timer, Spectator List and Keybinds`
2. `## Quick answer: small utilities, different jobs`
3. `## Bomb timer and round-state information`
4. `## Spectator List means observer awareness`
5. `## Keybinds show assigned and active controls`
6. `## Why utility overlays become cluttered`
7. `## What these features do not guarantee`
8. `## Where Cluster fits`
9. `## FAQ`

Не писать, что Spectator List нужно использовать для изменения поведения под наблюдением. Не обещать millisecond accuracy без актуальной проверки.

### Backlink

- URL: external target.
- Anchor: `external CS2 cheat roundup`
- Placement: после `What these features do not guarantee`.
- Suggested sentence: `For the broader market context behind these utility features, read the [external CS2 cheat roundup](https://medium.com/@mrkhertz/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4).`

### Визуалы

`IMAGE_SLOT_01` — generated cover.

- Generated sequence index: 8.
- Style branch: A.
- Model: Nano Banana Pro / `gemini-3-pro-image`.
- Aspect ratio and size: 16:9, 2K.
- Typography mode: art-first.
- Reference roles: none attached.
- Prompt QA score: 91/100.

Final prompt:

> Create a 16:9 2K editorial cover for an article about CS2 Bomb Timer, Spectator List and Keybinds. Generated asset #8, branch A tactile industrial product poster. Editorial thesis: three small HUD utilities answer three different questions — time remaining, who is observing and which controls are active. Represent them as one compact desk console with three large physical modules integrated into a single chassis: a countdown ring without numbers, one observer lens icon and one raised bind switch. The console is the only hero and the action is monitoring. Reserve the upper-left 40% as a completely clean headline safe zone. Place the console in the right/lower 58%. Palette: off-white background, matte charcoal chassis, frosted clear modules, exact Cluster violet `#635FD5` only on the currently active switch, 3–5% of frame. Materials: soft-touch plastic, frosted acrylic and a little brushed steel. Camera high three-quarter, 50 mm feel, clean upper-left studio light, one controlled shadow, no neon. Art-first: no text, digits, labels, fake UI, logos or pseudo-glyphs. No weapons, maps, characters, code, cyberpunk, surveillance eyes, anti-cheat imagery, statistics or extra consoles. No references attached. Priority: three-jobs/one-console thesis, one hero, safe zone, small violet accent, physical clarity, detail.

`IMAGE_SLOT_02` — verified Hub/HUD screenshot showing Bomb Timer, Spectator List and Keybinds if all three are present in one current interface. Otherwise use three separate verified crops in one manually typeset figure; do not invent missing UI.

## Финальная редакционная проверка пакета

- Восемь статей имеют разные primary intents и не повторяют две target listicles.
- Legit-страница получает четыре ссылки; External-страница получает четыре ссылки.
- Анкоры не повторяются и распределены между partial-match, natural и author-branded формулировками.
- В каждой статье ровно один money-page backlink.
- Все продуктовые утверждения ограничены подтвержденными high-level feature categories.
- Ни одна статья не содержит numeric stealth settings, bypass/evasion, implementation details или гарантий безопасности.
- Generated sequence непрерывна и чередуется B/A: 1 B, 2 A, 3 B, 4 A, 5 B, 6 A, 7 B, 8 A.
- Каждый B prompt прикладывает два named warm-story reference files, задает роли и требует fidelity 4/5.
- Cluster `#635FD5` используется в B как доминирующее поле 35–70%, в A как один акцент 3–8%.
- Каждый prompt содержит asset role, thesis, metaphor, one hero, ratio/size, composition, palette, materials, camera, light, typography, references, constraints and priority order, и набирает не менее 80/100.
