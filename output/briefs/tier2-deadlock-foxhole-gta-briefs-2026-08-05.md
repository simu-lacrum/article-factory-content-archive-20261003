# ТЗ на 8 Tier 2 статей для Deadlock, Foxhole и GTA 5 RP

Дата: 5 августа 2026 года  
Формат: восемь самостоятельных статей, по одной на каждую целевую страницу  
Объем каждой статьи: 500–800 слов, рекомендуемый коридор 650–750 слов с учетом FAQ  
Ссылок в каждой статье: ровно 2, обе ведут на закрепленную за статьей целевую страницу  
Модель для generated visuals: Nano Banana Pro / `gemini-3-pro-image`

## Общая редакционная рамка

Каждая Tier 2 статья должна полностью закрывать собственный информационный интент. Ссылка появляется как полезное продолжение уже раскрытой мысли, а не как причина существования текста. Нельзя переписывать целевой лендинг, делать еще один рейтинг «лучших читов» или строить материал из рекламных обещаний.

Обязательные правила для всей серии:

- Язык статьи совпадает с языком целевой страницы: четыре материала на английском и четыре на русском.
- Объем основного текста вместе с FAQ — 500–800 слов. SEO front matter, подписи к изображениям и служебные заметки в объем не входят.
- Ровно две ссылки на целевой URL. Первую ставить после того, как читатель получил практическую ценность, ориентировочно на 35–50% текста. Вторую — на 70–85%, в выводе или последнем смысловом блоке.
- Между ссылками должно быть не менее двух полноценных разделов. Не ставить ссылку в H1, SEO title, description, первом абзаце, FAQ или подписи к изображению.
- Анкоры использовать в точной форме, указанной в соответствующем ТЗ. Не склонять, не менять порядок слов и не добавлять слова внутрь анкора.
- Не добавлять третью ссылку на тот же домен и не дублировать один анкор дважды.
- Тон прямой, практичный, разговорный и gamer-aware. Без канцелярита, академической воды, фальшивых историй от первого лица и агрессивного CTA.
- Не использовать markdown-таблицы. Сравнения, этапы и чек-листы оформлять списками.
- Не фиксировать в тексте цены, число функций, длительность trial, актуальный статус продукта или совместимость как вечные факты. Если без этого нельзя, ставить дату проверки и предлагать перепроверить целевую страницу.
- Не повторять утверждения о «100% безопасности», undetected-статусе, обходе VAC/EAC, драйверном внедрении, cleaner, spoofer, humanizer, скрытии от записи или проверок администратора.
- Не давать инструкции по инжекту, обходу античита, маскировке, эксплуатации уязвимостей, настройке эксплойтов или имитации человеческого поведения.
- Допустимо на высоком уровне обсуждать категории функций, удобство интерфейса, информационную иерархию, совместимость, контролируемость, тестирование и риски.
- В конце обязателен FAQ из четырех коротких вопросов и ответов. FAQ должен расширять материал, а не повторять основной текст.

Каждая готовая статья получает front matter:

```yaml
---
title: "Финальный H1 на языке статьи"
description: "До 160 символов, с primary keyword"
primary_keyword: "Основной поисковый ключ"
game: "Deadlock | Foxhole | GTA 5 RP"
language: "en | ru"
word_count_target: "650-750"
image_model: "Nano Banana Pro / gemini-3-pro-image"
---
```

## Визуальная система серии

Для каждого материала предусмотрены два визуальных слота:

1. Generated cover — полный prompt в стиле `article-editorial-poster-v1`, 16:9, 2K.
2. Один фактический inline-скриншот из указанного источника или с целевой страницы. Скриншот не генерировать: Nano Banana Pro не должен придумывать интерфейс, надписи, показатели или функции продукта.

Промпты специально адаптированы под Nano Banana Pro: один доминирующий объект, не более трех уровней визуальной иерархии, физически понятная метафора, явная safe zone, точные материалы и свет. В каждом prompt запрещены текст, псевдотекст, логотипы, HUD, персонажи и generic cyberpunk. Если редактор добавляет заголовок после генерации, он делает это вручную в предусмотренной safe zone.

---

# ТЗ №1. Deadlock Cheat Features Explained: What Each Category Actually Changes

## Целевая страница и ссылочная схема

- Язык статьи: English.
- Целевая страница: https://medium.com/@aurelivoines/top-4-cheats-for-deadlock-comparison-of-features-prices-and-the-best-software-choice-0f737d360121
- Ссылка №1: анкор `Deadlock cheats`.
- Ссылка №2: анкор `cheats for Deadlock`.
- Обе ссылки ведут на один URL выше.

Рекомендуемый контекст первой ссылки, после объяснения основных категорий: `A current comparison of Deadlock cheats can then show how specific products combine these categories instead of treating every long feature list as equivalent.`

Рекомендуемый контекст второй ссылки, в выводе: `Use the broader comparison of cheats for Deadlock as a market snapshot, then verify the current product pages, support scope and compatibility before making any decision.`

## SEO и позиционирование

- H1: `Deadlock Cheat Features Explained: What Each Category Actually Changes`
- Альтернативный H1: `Aim, Souls, Visuals and Automation: A Deadlock Feature Guide`
- SEO title: `Deadlock Cheat Features Explained: Aim, Visuals and Scripts`
- Meta description: `Learn how Deadlock cheat features differ across aim, Souls, visual awareness, parry and hero automation before reading product comparisons.`
- Primary keyword: `Deadlock cheat features`
- Secondary keywords: `Deadlock aim features`, `Deadlock Souls assistance`, `Deadlock visual awareness`, `Deadlock auto parry`, `Deadlock hero scripts`
- Search intent: informational, feature education before comparison.
- Audience: readers who see repeated terms in Deadlock software reviews but do not yet understand which gameplay decision each category is meant to affect.

## Уникальный тезис

Deadlock combines projectile combat, lane economy, map movement and MOBA-style ability timing. Because of that mix, two products can both advertise “aim” or “visuals” while solving different decisions. The article must translate category names into reader-facing questions: what is being observed, when does it matter, how much control remains with the player and what creates clutter.

Целевая Medium-статья сравнивает Cluster, Melonity, Octarine и Predator, упоминая aim assistance, Souls/creeps, ESP/visuals, FOV/World Color, auto-parry and hero combos. Tier 2 материал не должен повторять рейтинг, цены, места или заявления о ban protection. Его задача — дать нейтральный словарь категорий, после которого сравнение продуктов становится понятнее.

## Обязательная структура и объем

1. `Why Deadlock feature lists are unusually confusing` — 65–75 слов. Объяснить сочетание shooter и MOBA decisions без маркетинговых оценок.
2. `Aim assistance: heroes, creeps and Souls are different jobs` — 90–105 слов. Пояснить различие целей и projectile context только на уровне назначения.
3. `Visual awareness: information must answer a decision` — 90–105 слов. Enemies, health, cooldown context, map activity and FOV; здесь разместить ссылку №1.
4. `Lane economy: why Souls deserve their own category` — 80–95 слов. Отделить economy assistance от hero targeting.
5. `Reactive utility: parry and defensive item timing` — 85–100 слов. Объяснить контролируемость и понятные границы, без настройки или exploitation steps.
6. `Hero automation: convenience versus predictability` — 85–100 слов. Комбо полезно оценивать по прозрачности controls и возможности manual override.
7. `How to read a product comparison after the glossary` — 75–90 слов. Проверить дату, совместимость, поддержку и источник каждого claim; здесь разместить ссылку №2.
8. Короткий вывод — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- Is aim assistance for heroes the same as assistance for Souls?
- Why should visual features be judged by readability rather than quantity?
- What makes hero automation predictable enough to evaluate?
- Can a comparison guarantee current safety or compatibility?

## Нельзя допускать

- Не делать второй Top 4, не присваивать места и не объявлять победителя.
- Не повторять цены, trial terms и ban-protection claims из Medium-статьи как текущие факты.
- Не объяснять operational aim settings, automatic last-hitting, parry timing, combo execution, injection or evasion.
- Не смешивать функцию с гарантией результата: наличие категории не доказывает качество, победу или безопасность.

## Визуалы

Inline screenshot: если у издателя есть права на изображения целевой Medium-статьи, использовать один нейтральный crop с aim/visual/hero-script categories без цены, рейтингового места и safety claims. Альтернатива — собственный разрешенный screenshot официального product UI. Роль — показать различие категорий; подпись описывает только фактически видимое.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for an English editorial guide that explains the major categories found in Deadlock software comparisons: aim, Souls and lane economy, visual awareness, reactive utility, and hero automation. Thesis: feature names become useful only when they are sorted by the decision they affect. Metaphor: one large translucent amber classification lens is mounted above a compact industrial sorting deck; five distinct but unlabeled material tokens enter through one supported rail and settle into three clearly separated physical channels, with the lens and deck reading as one dominant hero assembly. Format 16:9, 2K, art-first editorial composition. Position the assembly slightly right of center and preserve a calm empty upper-left safe zone for later headline placement, but render no text. Environment: dirty off-white dense-paper studio plane on a charcoal powder-coated base with restrained steel-blue structural parts. Camera: elevated three-quarter product view, 50 mm editorial lens, crisp main silhouette, restrained depth of field, no wide-angle distortion. Materials: translucent cast amber lens, frosted acrylic tokens, brushed steel-blue channel guides, powder-coated charcoal base, small muted-orange calibration stops. Palette: amber-orange, steel blue, charcoal, dirty off-white; no extra accent colors. Lighting: soft directional key from upper left, grounded contact shadows, controlled refraction through the lens, no neon glow. Typography mode: no letters, no numbers, no icons, no logos, no UI labels, no pseudo-text. References: none. Physical plausibility: the lens is fixed to a rigid arm, every token rests inside the intake rail or a destination channel, all channels connect to the deck, fasteners and shadows are consistent, nothing floats. Constraints: no Deadlock characters, no game logo, no copied map, no weapons, no Souls copied from the game, no HUD, no crosshair, no computer screen, no hacker imagery, no shield, no padlock, no podium, no crown, no cyberpunk city, no clutter. Priority order: 1) instantly readable feature-category sorting metaphor, 2) one dominant tactile assembly with subordinate tokens, 3) strong negative space and physical plausibility, 4) restrained Deadlock-adjacent industrial palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 95/100. Один герой, ясная сортировочная метафора, явная safe zone, физически связанная конструкция и полный запрет на текст, UI и игровые копии. Порог 80/100 пройден.

---

# ТЗ №2. Как сравнивать читы для Deadlock: критерии важнее громкого топа

## Целевая страница и ссылочная схема

- Язык статьи: русский.
- Канонический URL без tracking-параметра: https://medium.com/@aurelivoines/%D1%82%D0%BE%D0%BF-4-%D1%87%D0%B8%D1%82%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-deadlock-%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0-%D1%86%D0%B5%D0%BD-%D0%B8-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B-%D0%BE%D1%82-%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2-8a3062388f8f
- Ссылка №1: анкор `читы deadlock`.
- Ссылка №2: анкор `читы на deadlock`.

Рекомендуемый контекст первой ссылки: `Посмотреть, как эти критерии применяются к конкретным продуктам, можно в сравнении читы deadlock, но характеристики и цены перед решением все равно нужно проверять заново.`

Рекомендуемый контекст второй ссылки: `Готовый разбор читы на deadlock полезен как стартовая карта рынка, а не как замена собственной проверке совместимости и удобства.`

## SEO и позиционирование

- H1: `Как сравнивать читы для Deadlock: критерии важнее громкого топа`
- Альтернативный H1: `Чек-лист сравнения софта для Deadlock без веры в рекламу`
- SEO title: `Как сравнивать читы для Deadlock: практичный чек-лист`
- Meta description: `Разбираем, как сравнивать читы для Deadlock по назначению, интерфейсу, актуальности, поддержке и рискам, а не по рекламным обещаниям.`
- Primary keyword: `как сравнивать читы для Deadlock`
- Secondary keywords: `софт для Deadlock`, `сравнение читов Deadlock`, `функции Deadlock`, `критерии выбора`
- Интент: информационно-коммерческий, выбор по критериям.
- Аудитория: читатели рейтингов, которые видят длинные feature list, цены и заявления о защите, но не понимают, что действительно сравнивать.

## Уникальный тезис

Рейтинг без методики быстро устаревает. Полезное сравнение должно отделять подтвержденные категории функций от маркетинговых обещаний и оценивать продукт по сценарию использования, читаемости интерфейса, контролируемости автоматизации, совместимости, поддержке и дате проверки.

Целевая Medium-статья сравнивает Cluster, Melonity, Octarine и Predator по aim/visual/utility-функциям, цене и заявленной защите. Tier 2 материал не должен повторять расстановку мест, цены или заявления «лучший/самый безопасный». Его задача — научить читать подобное сравнение критически.

## Обязательная структура и объем

1. `Почему топ без критериев устаревает быстрее патча` — 65–75 слов.
2. `Сначала сценарий, потом список функций` — 85–100 слов. Разделить aim, visual awareness и hero/utility automation.
3. `Критерий 1: контролируемость и понятные настройки` — 85–100 слов. Здесь поставить ссылку №1.
4. `Критерий 2: читаемость информации, а не максимум элементов` — 85–100 слов.
5. `Критерий 3: совместимость, обновления и поддержка` — 90–105 слов. Любые текущие статусы перепроверять.
6. `Цена без контекста ничего не решает` — 70–85 слов. Считать период, набор нужных функций и условия доступа; не приводить текущие цены.
7. `Что делать с обещаниями безопасности` — 75–90 слов. Объяснить, что абсолютных гарантий нет; здесь поставить ссылку №2 в конце блока.
8. Вывод — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- Можно ли выбрать продукт только по количеству функций?
- Почему дата проверки важнее красивого рейтинга?
- Стоит ли считать цену главным критерием?
- Может ли обзор гарантировать отсутствие блокировок?

## Нельзя допускать

- Не делать новый топ-4 и не присваивать продуктам места.
- Не повторять цены и сравнительные заявления целевой статьи как вечные факты.
- Не описывать методы внедрения, обхода проверок, OBS bypass или драйверные детали.
- Не объявлять один продукт безусловно лучшим, безопасным или undetected.

## Визуалы

Inline screenshot: если у издателя есть права на изображения целевой Medium-статьи, использовать один нейтральный crop с четырьмя названиями сравниваемых продуктов или один product-menu screenshot без выделения победителя. Альтернатива — собственный лицензированный скриншот интерфейса. Роль — показать предмет сравнения, а не подтвердить рейтинг или безопасность.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for a Russian editorial guide about evaluating Deadlock software comparisons with transparent criteria instead of trusting a loud ranking. Thesis: a useful comparison measures the same qualities consistently and separates observable product behavior from marketing claims. Metaphor: one precision industrial comparison carousel holds four small interchangeable material modules and passes each beneath a single mounted amber calibration gauge; the carousel is the hero, while the four modules remain clearly subordinate and equal, with no winner indicated. Format 16:9, 2K, art-first editorial composition. Place the carousel slightly left of center and preserve a calm empty upper-right safe zone for later headline placement, but generate no text. Environment: charcoal powder-coated studio base on dirty off-white dense paper, with restrained steel-blue structural parts. Camera: elevated three-quarter product view, 55 mm editorial lens, crisp geometry, subtle depth of field. Materials: powder-coated steel, frosted acrylic modules, translucent amber gauge window, matte paper, small muted-orange calibration stops. Palette: amber-orange, steel blue, charcoal, dirty off-white; no extra accent colors. Lighting: soft upper-left studio key, controlled contact shadows, slight acrylic refraction, no emissive neon. Typography mode: no letters, no numbers, no ranking badges, no logos, no UI text, no pseudo-text. References: none. Physical plausibility: every module sits in a fitted carousel recess, the gauge is mounted on a rigid arm, the carousel rests on a visible bearing, all shadows align, nothing floats. Constraints: no Deadlock characters, no game logo, no map, no weapons, no HUD, no computer screen, no hacker stereotype, no crowns, no medals, no podium, no shield, no padlock, no cyberpunk city, no clutter. Priority order: 1) equal-criteria comparison metaphor with no declared winner, 2) one dominant tactile hero, 3) clear safe zone and restrained hierarchy, 4) Deadlock-adjacent industrial palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 94/100. Метафора прямо соответствует тезису, четыре объекта подчинены одному герою, отсутствуют текст и рейтинг, физика и палитра заданы. Порог 80/100 пройден.

---

# ТЗ №3. Deadlock Information Triage: What Matters First in a 6v6 Fight

## Целевая страница и ссылочная схема

- Язык статьи: English.
- Целевая страница: https://melonity.gg/en/deadlock
- Ссылка №1: анкор `Deadlock cheats`.
- Ссылка №2: анкор `cheats for Deadlock`.

Рекомендуемый контекст первой ссылки: `The landing page for Deadlock cheats groups its tools around visuals, aim assistance, parry and item automation, which makes it a useful example of why categories still need a clear priority order.`

Рекомендуемый контекст второй ссылки: `When reviewing cheats for Deadlock, judge the setup by how quickly it answers the next decision—not by how many elements it can display at once.`

## SEO и позиционирование

- H1: `Deadlock Information Triage: What Matters First in a 6v6 Fight`
- Альтернативный H1: `How to Prioritize Visual Information in a Chaotic Deadlock Fight`
- SEO title: `Deadlock Information Triage for Cleaner 6v6 Fights`
- Meta description: `Use a Deadlock information hierarchy to prioritize immediate threats, resources, objectives and cooldown windows without turning the screen into noise.`
- Primary keyword: `Deadlock information hierarchy`
- Secondary keywords: `Deadlock visual settings`, `Deadlock situational awareness`, `6v6 fight information`, `Deadlock screen clutter`
- Search intent: informational, optimization.
- Audience: players evaluating visual-awareness and automation tools who struggle with information overload.

## Уникальный тезис

More information is useful only when it shortens the next decision. In a fast 6v6 fight, the order should be immediate survival, actionable threats, resource/objective context and only then background detail. A clean hierarchy beats a screen full of equally loud signals.

Допустимые продуктовые факты с целевой страницы: visuals are presented as highlighting allies/enemies, souls, map activities and power-ups, with FOV adjustment; the same page groups auto-parry and auto-items as configurable automation categories. Описывать только на этом высоком уровне. Не повторять safety claims, prices or current trial terms.

## Обязательная структура и объем

1. `The real problem is equal-weight information` — 65–75 слов.
2. `Priority one: immediate survival` — 85–100 слов. Health, nearby threat and escape decision before distant context.
3. `Priority two: the next actionable target` — 85–100 слов. Here place link №1 after defining the category model.
4. `Priority three: souls, power-ups and map activity` — 90–105 слов. Explain when background context becomes actionable.
5. `Automation must remain legible` — 90–105 слов. A parry or item-saving category needs visible controls and predictable boundaries, not hidden complexity.
6. `Reduce clutter with a one-question rule` — 80–95 слов. Every element must answer one current decision; remove duplicates.
7. `A 30-second pre-match audit` — 70–85 слов. Short checklist; link №2 in the final sentence.
8. Conclusion — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- Is more visual information always better in Deadlock?
- Which information should be most prominent during a fight?
- How often should a visual profile be reviewed?
- Can automation replace situational awareness?

## Нельзя допускать

- Не объяснять настройку aim, parry, item automation or ESP at an operational level.
- Не обещать match wins, rank gains, legitimacy or protection from bans.
- Не копировать лендинговый список функций целиком.
- Не генерировать фальшивый Deadlock HUD.

## Визуалы

Inline screenshot: взять один реальный, разрешенный к использованию crop из блока Visuals на целевой странице. Роль — показать плотность реальной информации. Не добавлять придуманные подписи, hitboxes или показатели; в caption указать дату capture и отметить, что набор функций может измениться.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for an English editorial feature about prioritizing information during a chaotic Deadlock 6v6 fight. Thesis: useful awareness is a hierarchy that filters signals by urgency, not a maximum number of overlays. Metaphor: one large translucent amber signal lens contains three physically nested apertures that sort a loose stream of small steel tokens into three clean channels of decreasing urgency; the lens is the single hero, and the tokens remain subordinate. Format 16:9, 2K, art-first editorial composition. Position the lens slightly right of center and preserve a quiet upper-left safe zone for later headline placement, with no generated text. Environment: compact industrial studio surface made from charcoal powder-coated metal and dirty off-white dense paper. Camera: three-quarter close product view, 50 mm lens, restrained depth of field, no dramatic perspective. Materials: translucent cast amber, brushed steel-blue aperture rings, matte charcoal base, off-white paper, tiny muted-orange mechanical stops. Palette: amber-orange, steel blue, charcoal, dirty off-white. Lighting: soft directional key from upper left, readable contact shadows, controlled refraction through the lens, no neon glow. Typography mode: no letters, no numbers, no icons, no logos, no UI labels, no pseudo-text. References: none. Physical plausibility: all apertures are held inside the lens housing, every channel is mounted to the base, tokens sit inside the channels, shadows and refraction are consistent, nothing floats. Constraints: no Deadlock characters, no game logo, no copied map, no weapons, no HUD, no crosshair, no monitor, no hacker imagery, no shield, no padlock, no cyberpunk, no decorative data streams, no clutter. Priority order: 1) instantly readable signal-triage metaphor, 2) one dominant lens and three clear urgency levels, 3) strong negative space and tactile plausibility, 4) restrained Deadlock-adjacent palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 95/100. Один герой, три уровня иерархии, art-first safe zone, физическая причинность и полный negative prompt. Порог 80/100 пройден.

---

# ТЗ №4. Один профиль на весь матч не работает: настройки Deadlock по фазам

## Целевая страница и ссылочная схема

- Язык статьи: русский.
- Целевая страница: https://melonity.gg/deadlock
- Ссылка №1: анкор `читы deadlock`.
- Ссылка №2: анкор `читы на deadlock`.

Рекомендуемый контекст первой ссылки: `Страница читы deadlock показывает несколько разных категорий — от визуальной информации до автоматизации предметов, поэтому собирать их в один неизменный профиль не всегда разумно.`

Рекомендуемый контекст второй ссылки: `Оценивая читы на deadlock, полезнее заранее понять, какие решения нужны на линии, при перемещениях и в массовом файте, а уже потом смотреть на общий список возможностей.`

## SEO и позиционирование

- H1: `Один профиль на весь матч не работает: настройки Deadlock по фазам`
- Альтернативный H1: `Как разделить настройки Deadlock для линии, ротаций и командных драк`
- SEO title: `Настройки Deadlock по фазам матча: три понятных профиля`
- Meta description: `Разделите настройки Deadlock для линии, ротаций и командных драк, чтобы нужная информация появлялась вовремя и не превращалась в визуальный шум.`
- Primary keyword: `настройки Deadlock по фазам матча`
- Secondary keywords: `профили Deadlock`, `настройки для линии Deadlock`, `визуальная информация Deadlock`, `командный файт Deadlock`
- Интент: информационный, практическая организация интерфейса.
- Аудитория: игроки, у которых один перегруженный профиль одинаково работает во всех стадиях матча.

## Уникальный тезис

Линия, ротация и массовый файт задают разные вопросы. Поэтому хороший профиль — это не максимальный feature list, а заранее ограниченный набор сигналов и контролов под конкретную фазу. Статья не должна быть переводом ТЗ №3: здесь главный объект — смена профилей во времени, а не приоритеты внутри одного боя.

Допустимые продуктовые категории: визуалы для allies/enemies, souls, map activities, power-ups и FOV; высокоуровневые категории auto-parry и auto-items. Не описывать конкретные значения, горячие клавиши или способы сокрытия.

## Обязательная структура и объем

1. `Почему универсальный профиль быстро превращается в кашу` — 65–75 слов.
2. `Профиль линии: экономика и ближайший риск` — 90–105 слов. Сферы душ и ближайшие события важнее дальнего шума.
3. `Профиль ротации: маршрут и изменения на карте` — 90–105 слов. Здесь поставить ссылку №1.
4. `Профиль командного боя: выживание и короткие окна решений` — 95–110 слов.
5. `Что должно оставаться одинаковым` — 75–90 слов. Базовые controls, понятный on/off, предсказуемое поведение.
6. `Как переключать профиль без хаоса` — 80–95 слов. Одна логика именования, минимум режимов, тест после изменений; без пошаговой настройки функций.
7. `Мини-аудит после матча` — 70–85 слов. Удалить то, что не влияло на решения; поставить ссылку №2.
8. Вывод — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 690–760 слов.

## FAQ

- Сколько профилей достаточно для начала?
- Нужно ли менять профиль под каждого героя?
- Какие элементы лучше не переключать между фазами?
- Как понять, что профиль перегружен?

## Нельзя допускать

- Не дублировать англоязычную статью про информационную иерархию в 6v6.
- Не давать точных пресетов aim, auto-parry, auto-items или визуалов.
- Не обещать преимущество, рейтинг, легитность или отсутствие блокировок.
- Не выдавать текущие цифры лендинга и условия подписки за постоянные.

## Визуалы

Inline screenshot: один фактический crop из русского блока Visuals или меню с целевой страницы, если права позволяют. Роль — показать, что разные категории управления существуют в одном продукте. Не генерировать UI и не добавлять несуществующие переключатели.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for a Russian editorial guide about using different Deadlock information profiles for the lane, rotations, and team fights. Thesis: one overloaded setup cannot answer every phase equally well; a small set of deliberate modes keeps each moment readable. Metaphor: one large three-position rotary selector is mounted to a compact industrial base and mechanically routes a single translucent amber signal cartridge through three distinct but unlabeled channels; the selector is the hero, while the channels remain subordinate. Format 16:9, 2K, art-first editorial composition. Place the selector left-center and keep a calm empty upper-right safe zone for later headline placement, but render no text. Environment: dirty off-white dense-paper studio plane on a charcoal powder-coated frame. Camera: elevated three-quarter product view, 55 mm lens, crisp silhouette, restrained depth of field. Materials: brushed steel-blue selector ring, translucent amber cartridge, powder-coated charcoal base, muted-orange detents, dense paper backdrop. Palette: amber-orange, steel blue, charcoal, dirty off-white. Lighting: soft top-left key light, clear contact shadows, subtle refraction, no emissive neon. Typography mode: no text, no letters, no numbers, no icons, no logos, no pseudo-text. References: none. Physical plausibility: the selector shaft is visibly mounted, every channel connects to the central housing, the cartridge rests inside one channel, detents align mechanically, shadows are consistent, nothing floats. Constraints: no Deadlock heroes, no game logo, no copied map, no weapons, no HUD, no computer screen, no keyboard, no hacker cliché, no shield, no padlock, no cyberpunk city, no clutter. Priority order: 1) instantly readable three-phase selector metaphor, 2) one dominant hero and clean hierarchy, 3) generous editorial safe zone, 4) tactile Deadlock-adjacent color and material system. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 95/100. Три фазы переданы одной физической системой без текста, герой доминирует, safe zone и материалность заданы, конфликтующих метафор нет. Порог 80/100 пройден.

---

# ТЗ №5. Где ломается логистика Foxhole: путь ресурса от добычи до фронта

## Целевая страница и ссылочная схема

- Язык статьи: русский.
- Целевая страница: https://melonity.gg/foxhole
- Ссылка №1: анкор `читы для фоксхол`.
- Ссылка №2: анкор `читы foxhole`.

Рекомендуемый контекст первой ссылки: `Категории, которые предлагают читы для фоксхол, хорошо показывают сами узкие места логистики: сбор, повторяющиеся операции, транспорт, маршрут и контроль обстановки.`

Рекомендуемый контекст второй ссылки: `Перед тем как оценивать читы foxhole, разберите собственную цепочку по этапам — тогда будет ясно, где инструмент действительно сокращает рутину, а где проблема остается организационной.`

## SEO и позиционирование

- H1: `Где ломается логистика Foxhole: путь ресурса от добычи до фронта`
- Альтернативный H1: `Логистическая цепочка Foxhole: пять точек потери времени`
- SEO title: `Логистика Foxhole: где теряется время от добычи до фронта`
- Meta description: `Разбираем логистику Foxhole по этапам: добыча, переработка, склад, транспорт и передача на фронте — с практичным аудитом узких мест.`
- Primary keyword: `логистика Foxhole`
- Secondary keywords: `цепочка поставок Foxhole`, `ресурсы Foxhole`, `транспорт Foxhole`, `склад Foxhole`, `фронтовая логистика`
- Интент: информационный, оптимизация процесса.
- Аудитория: логисты и небольшие группы, у которых время теряется не на одном действии, а на стыках между этапами.

## Уникальный тезис

В Foxhole редко тормозит только один этап. Потери накапливаются при передаче ресурса между добычей, переработкой, складом, транспортом и фронтовым получателем. Полезный аудит должен измерять не только скорость действия, но и ожидание, пустые рейсы, неверный объем партии и потерю информации на handoff.

Допустимые факты с целевой страницы: продукт группирует высокоуровневые возможности вокруг autopilot, autofarm, autopull, autotrain и artillery calculator; отдельный блок situational awareness включает ESP, notifications, minimap и QOL. Можно использовать эти названия как категории задач, но не описывать настройку, автономный фарм на нескольких окнах, human-like movement, exploit abuse или обход проверок.

## Обязательная структура и объем

1. `Логистика ломается на стыках` — 65–75 слов.
2. `Этап 1: добыча и размер партии` — 80–95 слов. Проверить, нет ли перепроизводства и пустого ожидания.
3. `Этап 2: переработка и склад` — 85–100 слов. Очереди, статус заказа и понятное место передачи; здесь поставить ссылку №1.
4. `Этап 3: маршрут и транспорт` — 90–105 слов. Топливо, загрузка, обратный рейс, препятствия и смена приоритета без пошаговой автоматизации.
5. `Этап 4: handoff на фронте` — 90–105 слов. Кто принимает, сколько нужно, что происходит при изменении запроса.
6. `Информация как отдельный груз` — 75–90 слов. Уведомления, minimap и статусы полезны, если приводят к решению.
7. `Пятиминутный аудит цепочки` — 70–85 слов. Пять вопросов; поставить ссылку №2 в конце.
8. Вывод — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- Как найти самое дорогое узкое место в цепочке?
- Что важнее: скорость рейса или стабильность поставки?
- Почему пустой обратный маршрут портит эффективность?
- Могут ли инструменты заменить договоренности внутри команды?

## Нельзя допускать

- Не писать инструкцию по боту, автофарму, pathfinding или управлению несколькими окнами.
- Не давать боевых инструкций по эксплойтам, аиму или получению скрытой информации.
- Не обещать точность калькуляторов, отсутствие блокировок или постоянную совместимость.
- Не превращать статью в перечень функций лендинга.

## Визуалы

Inline screenshot: использовать разрешенный фактический кадр из блока обзора Foxhole на целевой странице — предпочтительно логистический builder, маршрут или minimap. Роль — проиллюстрировать один этап цепочки. В подписи описывать только видимое, указывать дату capture и не добавлять выводов о безопасности.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for a Russian editorial feature about bottlenecks in a Foxhole logistics chain from resource gathering to front-line delivery. Thesis: time is lost at handoffs between stages, not only inside each task. Metaphor: one sturdy olive supply crate moves along a continuous industrial rail through four compact mounted transfer stations; one station has a visibly misaligned handoff gap, while the crate remains the dominant hero and all stations are subordinate. Format 16:9, 2K, art-first editorial composition. Position the crate and broken handoff slightly right of center and preserve a calm upper-left safe zone for later headline placement, but generate no text. Environment: clean logistics workshop rendered as a dense-paper studio set, with a charcoal powder-coated rail and restrained khaki panels. Camera: elevated three-quarter product view, 50 mm editorial lens, moderate depth of field, no cinematic wide angle. Materials: worn painted wood crate, powder-coated steel rail, dense off-white paper, brushed metal rollers, one translucent amber status window. Palette: olive green, khaki, charcoal, dirty off-white, restrained amber accent. Lighting: soft directional key from upper left, grounded contact shadows, subtle wear highlights, no dramatic smoke and no neon. Typography mode: no letters, no numbers, no military markings, no logos, no UI text, no pseudo-text. References: none. Physical plausibility: the crate rests on rollers, every station is bolted to the rail, the gap is mechanically believable, shadows follow one direction, no component floats. Constraints: no Foxhole logo, no copied game map, no soldiers, no vehicles as hero objects, no weapons, no ammunition, no battlefield, no HUD, no hacker imagery, no shield, no padlock, no cyberpunk, no clutter. Priority order: 1) immediately readable logistics-handoff bottleneck, 2) one dominant crate with four subordinate stages, 3) tactile industrial plausibility and negative space, 4) restrained logistics palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 95/100. Причинно-следственная метафора считывается без текста, один объект доминирует, все станции физически связаны, safe zone и запреты заданы. Порог 80/100 пройден.

---

# ТЗ №6. Foxhole Artillery Coordination: The Information Checklist Before Every Salvo

## Целевая страница и ссылочная схема

- Язык статьи: English.
- Целевая страница: https://melonity.gg/en/foxhole
- Ссылка №1: анкор `Foxhole cheats`.
- Ссылка №2: анкор `cheats for Foxhole`.

Рекомендуемый контекст первой ссылки: `The categories presented on the Foxhole cheats page—calculation, transport automation, notifications and map awareness—show why artillery accuracy is partly an information-flow problem.`

Рекомендуемый контекст второй ссылки: `When reviewing cheats for Foxhole, treat calculators and awareness tools as inputs to a disciplined crew process, not as substitutes for clear calls and fresh data.`

## SEO и позиционирование

- H1: `Foxhole Artillery Coordination: The Information Checklist Before Every Salvo`
- Альтернативный H1: `Why Foxhole Artillery Crews Miss: Inputs, Handoffs and Timing`
- SEO title: `Foxhole Artillery Coordination: A Practical Crew Checklist`
- Meta description: `Improve Foxhole artillery coordination by checking range inputs, crew roles, ammunition flow, target updates and reset calls before each firing cycle.`
- Primary keyword: `Foxhole artillery coordination`
- Secondary keywords: `Foxhole artillery checklist`, `Foxhole crew communication`, `artillery calculator Foxhole`, `Foxhole ammunition logistics`
- Search intent: informational, team-process improvement.
- Audience: artillery crews and logistics players who need a repeatable information routine rather than another general logistics guide.

## Уникальный тезис

An artillery cycle fails when a correct number arrives late, an old target update is treated as current, the crew uses different reference points or ammunition flow breaks. Reliable coordination is a shared input contract: source, timestamp, role, confirmation and reset.

Допустимые факты с target page: artillery calculation is presented as a distance-and-azimuth category; the page also describes notifications, minimap information, transport/logistics automation and broader quality-of-life tools. Do not state that a calculator is perfectly accurate, explain firing exploits, or turn the brief into a weapons tutorial.

## Обязательная структура и объем

1. `Accuracy starts before the shot` — 65–75 слов.
2. `Define one source of range and direction` — 85–100 слов. Clarify reference point, freshness and who owns the call.
3. `Give every crew member one explicit role` — 85–100 слов. Observer, calculator/caller, operator and ammunition flow at a high level; place link №1 here.
4. `Treat target updates as expiring information` — 90–105 слов. Repeat back, timestamp and invalidate stale calls.
5. `Keep ammunition logistics in the same loop` — 85–100 слов. Supply status, batch size and interruption signal.
6. `Reset after every cycle` — 75–90 слов. Confirm what changed before the next action.
7. `The 20-second pre-cycle checklist` — 75–90 слов. Six concise checks; place link №2 in the last sentence.
8. Conclusion — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- What information should be repeated back by the crew?
- How quickly does a target call become stale?
- Can a calculator replace an observer and caller?
- Why should ammunition status be part of the firing checklist?

## Нельзя допускать

- Не давать точные инструкции по наведению, эксплуатации механик, автоматической стрельбе или обходу ограничений.
- Не заявлять идеальную точность, guaranteed hits, current safety or ban protection.
- Не смешивать статью с русскоязычным материалом про всю логистическую цепочку.
- Не использовать боевую сцену, оружие или снаряды как визуальный герой.

## Визуалы

Inline screenshot: использовать разрешенный screenshot реального artillery calculator или информационного блока с целевой страницы/официального changelog. Роль — показать, какие входные данные отображаются фактически. Не генерировать цифры и не добавлять invented accuracy claims; в caption указать дату capture.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for an English editorial guide about information discipline in Foxhole artillery coordination. Thesis: reliable results come from shared, fresh inputs and clean crew handoffs rather than one isolated number. Metaphor: one precision mechanical range-and-angle instrument is mounted on a compact workshop base; three short physical input rails feed distinct material tokens into one central calibrated dial, while a single verified output marker rests in a supported channel. The instrument is the dominant hero and all inputs remain subordinate. Format 16:9, 2K, art-first editorial composition. Place the instrument slightly left of center and preserve a calm upper-right safe zone for later headline placement, but render no text. Environment: dense dirty-off-white paper studio surface with an olive and charcoal industrial mounting frame. Camera: near-orthographic three-quarter product view, 55 mm lens, crisp structure, restrained depth of field. Materials: brushed steel, powder-coated olive metal, frosted acrylic tokens, khaki paper, one translucent amber dial window. Palette: olive green, khaki, charcoal, dirty off-white, restrained amber. Lighting: soft upper-left studio key, precise contact shadows, controlled metal highlights and acrylic refraction, no neon or battlefield haze. Typography mode: no letters, no numbers, no icons, no logos, no scale markings, no pseudo-text. References: none. Physical plausibility: all three rails connect to the dial housing, every token rests in a rail, the instrument is bolted to the base, the output marker is supported, all shadows align, nothing floats. Constraints: no Foxhole logo, no copied map, no soldiers, no artillery gun, no shell, no weapon, no explosion, no HUD, no crosshair, no hacker imagery, no shield, no padlock, no cyberpunk, no clutter. Priority order: 1) readable many-inputs-to-one-verified-output metaphor, 2) one dominant calibration instrument, 3) tactile physical plausibility and safe zone, 4) restrained Foxhole-adjacent logistics palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 96/100. Метафора передает координацию без изображения оружия, один прибор доминирует, все входы физически соединены, композиция и модель заданы полностью. Порог 80/100 пройден.

---

# ТЗ №7. GTA 5 RP Tool Compatibility: Check the Platform Before the Feature List

## Целевая страница и ссылочная схема

- Язык статьи: English.
- Целевая страница: https://melonity.gg/en/gta
- Ссылка №1: анкор `GTA 5 RP cheats`.
- Ссылка №2: анкор `cheats for GTA 5 RP`.

Рекомендуемый контекст первой ссылки: `The GTA 5 RP cheats page explicitly positions the current product around RAGE:MP, which is why platform compatibility should be checked before any feature comparison.`

Рекомендуемый контекст второй ссылки: `Before evaluating cheats for GTA 5 RP, confirm the multiplayer framework, operating environment, current support status and server rules on the product page itself.`

## SEO и позиционирование

- H1: `GTA 5 RP Tool Compatibility: Check the Platform Before the Feature List`
- Альтернативный H1: `RAGE:MP or alt:V? A GTA 5 RP Compatibility Checklist`
- SEO title: `GTA 5 RP Tool Compatibility: RAGE:MP vs alt:V Checklist`
- Meta description: `Check GTA 5 RP tool compatibility by verifying RAGE:MP or alt:V, current client support, operating environment and server rules before features.`
- Primary keyword: `GTA 5 RP tool compatibility`
- Secondary keywords: `RAGE:MP compatibility`, `alt:V compatibility`, `GTA 5 RP client`, `GTA RP server rules`
- Search intent: informational with pre-purchase validation.
- Audience: readers who assume that every GTA RP tool works across RAGE:MP, alt:V and different server ecosystems.

## Уникальный тезис

A strong feature list is irrelevant when the tool targets a different multiplayer framework. Compatibility is a stack: platform, client/build, operating environment, server rules, support status and the reader's actual use case. Each layer must be verified before discussing functions.

Подтвержденный факт target page на дату анализа: FAQ states that the product is intended for RAGE:MP and does not work with alt:V/Majestic or other multiplayer modifications. В статье сформулировать это с датой проверки и призывом перепроверить страницу перед публикацией. Не использовать claims about cleaner, executor injection, hiding, inspections or antiEAC.

## Обязательная структура и объем

1. `Compatibility beats a long feature list` — 65–75 слов.
2. `Layer 1: the multiplayer framework` — 90–105 слов. Explain that RAGE:MP and alt:V are not interchangeable product labels.
3. `Layer 2: current client and operating environment` — 85–100 слов. Version and OS support can change; place link №1 after this warning.
4. `Layer 3: the server's own rules and technical stack` — 90–105 слов. A platform match does not imply permission or universal behavior.
5. `Layer 4: support and update freshness` — 80–95 слов. Check changelog date, support channel and explicit scope.
6. `A five-question compatibility check` — 85–100 слов. Framework, server, OS, current status, rollback plan.
7. `Read the page as a current specification` — 65–80 слов. Place link №2 near the end.
8. Conclusion — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- Are RAGE:MP and alt:V tools interchangeable?
- Does matching the platform guarantee server compatibility?
- How often should compatibility be rechecked?
- Which source should override an old review or forum post?

## Нельзя допускать

- Не писать installation, injection, executor, cleaner or evasion instructions.
- Не обещать работу на конкретном сервере без его актуальной проверки.
- Не заявлять safety, invisibility to admins, automatic-ban protection or trace removal.
- Не копировать product feature list: статья посвящена совместимости, а не обзору функций.

## Визуалы

Inline screenshot: использовать фактический crop FAQ с целевой страницы, где видна совместимость с RAGE:MP и отсутствие поддержки alt:V/Majestic. Роль — первичный proof point. В подписи указать дату capture и попросить читателя проверить текущую формулировку; не генерировать или перерисовывать текст.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for an English editorial guide about checking GTA 5 RP platform compatibility before comparing tool features. Thesis: the correct platform fit is the first gate; an impressive feature list is useless when the framework does not match. Metaphor: one tactile urban access cartridge approaches a precision dual-socket gate; only one socket shares the cartridge's physical geometry, while the other is visibly incompatible, and the cartridge-plus-gate read as one dominant assembly. Format 16:9, 2K, art-first editorial composition. Position the assembly slightly right of center and preserve a calm upper-left safe zone for later headline placement, but generate no text. Environment: clean urban-industrial studio surface with asphalt-gray dense paper and a charcoal powder-coated mounting plate. Camera: elevated three-quarter product view, 50 mm editorial lens, restrained depth of field, no cityscape perspective. Materials: frosted acrylic cartridge, brushed metal sockets, matte asphalt paper, translucent muted-teal alignment insert, small warm-amber mechanical stop. Palette: asphalt gray, charcoal, dirty off-white, muted teal, warm amber. Lighting: soft directional key from upper left, grounded contact shadows, subtle acrylic refraction, no neon glow. Typography mode: no letters, no numbers, no logos, no platform names, no UI text, no pseudo-text. References: none. Physical plausibility: both sockets are mounted to one gate, the cartridge rests on a supported guide rail, only one geometry can accept it, fasteners and shadows are consistent, nothing floats. Constraints: no GTA logo, no recognizable city, no characters, no vehicles, no weapons, no money, no police imagery, no HUD, no computer screen, no hacker cliché, no shield, no padlock, no cyberpunk, no clutter. Priority order: 1) instantly readable compatibility-before-features metaphor, 2) one dominant physical assembly, 3) clear safe zone and tactile plausibility, 4) restrained urban editorial palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 95/100. Один центральный конфликт совместимости, минимум объектов, физическая логика, safe zone и строгий запрет на текст/логотипы. Порог 80/100 пройден.

---

# ТЗ №8. Три профиля вместо перегруженного меню: как организовать GTA 5 RP

## Целевая страница и ссылочная схема

- Язык статьи: русский.
- Целевая страница: https://melonity.gg/gta
- Ссылка №1: анкор `читы на gta 5 rp`.
- Ссылка №2: анкор `читы для gta 5 rp`.

Рекомендуемый контекст первой ссылки: `Даже если читы на gta 5 rp предлагают десятки категорий, рабочий профиль должен отвечать одному сценарию, а не включать все доступное одновременно.`

Рекомендуемый контекст второй ссылки: `Сравнивая читы для gta 5 rp, оценивайте не только наличие функций, но и то, насколько быстро меню позволяет собрать понятные профили без конфликтов.`

## SEO и позиционирование

- H1: `Три профиля вместо перегруженного меню: как организовать GTA 5 RP`
- Альтернативный H1: `Как разделить настройки GTA 5 RP для города, транспорта и конфликтных сцен`
- SEO title: `Настройки GTA 5 RP: три профиля без перегруженного меню`
- Meta description: `Организуйте настройки GTA 5 RP в три понятных профиля для города, транспорта и конфликтных сцен, чтобы убрать шум и конфликты управления.`
- Primary keyword: `настройки GTA 5 RP`
- Secondary keywords: `профили GTA 5 RP`, `меню GTA 5 RP`, `визуальные настройки GTA RP`, `конфликты горячих клавиш`
- Интент: информационный, организация интерфейса.
- Аудитория: пользователи больших меню, которые включают слишком много категорий и потом не понимают, какой control отвечает за конкретное поведение.

## Уникальный тезис

Удобное меню — не то, где больше переключателей, а то, где пользователь быстро собирает минимальный профиль под один сценарий. Для GTA 5 RP достаточно трех логических групп: спокойная городская сессия, транспорт/маршрут и конфликтная сцена. Между ними должны сохраняться единые базовые controls и понятный способ отката.

Допустимые факты target page: лендинг позиционирует продукт как RAGE:MP-only на дату анализа и показывает категории visuals, aim assistance, object awareness and script support. В статье они нужны только как примеры разных нагрузок на меню. Не обсуждать executor injection, hiding on recordings, admin location, cleaner, safe mode, antiEAC или способы проверки администрацией.

## Обязательная структура и объем

1. `Большое меню не равно понятному` — 65–75 слов.
2. `Профиль 1: спокойная городская сессия` — 85–100 слов. Минимум сигналов, navigation/QOL, отсутствие лишнего визуального шума.
3. `Профиль 2: транспорт и маршрут` — 85–100 слов. Контекст движения и объектов; здесь поставить ссылку №1.
4. `Профиль 3: конфликтная сцена` — 90–105 слов. Только срочные решения и жесткие границы; без operational aim settings.
5. `Общие controls для всех профилей` — 80–95 слов. Master toggle, понятные названия, одинаковая логика, ручной override.
6. `Как ловить конфликты до сессии` — 85–100 слов. Одна переменная за раз, короткий controlled test, rollback.
7. `Проверка меню после обновления` — 70–85 слов. Удалить лишнее и перепроверить совместимость; поставить ссылку №2.
8. Вывод — 35–45 слов.
9. FAQ — 100–120 слов.

Целевой итог: 680–750 слов.

## FAQ

- Сколько профилей достаточно для GTA 5 RP?
- Нужно ли дублировать общие настройки в каждом профиле?
- Как найти конфликт горячих клавиш?
- Почему профиль стоит перепроверять после обновления?

## Нельзя допускать

- Не повторять англоязычную статью про RAGE:MP и alt:V: здесь фокус только на организации профилей.
- Не давать значения aim, инструкции по executor, injection, cleaner, скрытию на записи или обходу админ-проверки.
- Не описывать местоположение администраторов как преимущество.
- Не обещать безопасность, отсутствие блокировок или совместимость с любым RP-сервером.

## Визуалы

Inline screenshot: использовать разрешенный реальный crop основного меню или блока Visuals с русской целевой страницы. Роль — показать фактическую группировку категорий. Не генерировать UI, не добавлять вымышленные вкладки и не показывать разделы, связанные со скрытием или обходом проверок.

Generated cover prompt:

```text
Create an article-editorial-poster-v1 cover for a Russian editorial guide about organizing GTA 5 RP settings into three clean scenario profiles instead of one overloaded menu. Thesis: a small set of deliberate profiles makes controls readable and reversible. Metaphor: one compact urban control deck contains a central mechanical selector rail with three clean physical cartridges docked in separate supported bays; the selector deck is the dominant hero, and the cartridges differ subtly in material density rather than labels or icons. Format 16:9, 2K, art-first editorial composition. Position the deck slightly left of center and preserve a calm upper-right safe zone for later headline placement, but render no text. Environment: asphalt-gray dense-paper studio plane with a charcoal powder-coated base and dirty off-white backdrop. Camera: elevated three-quarter product view, 55 mm editorial lens, crisp silhouette, restrained depth of field. Materials: frosted acrylic cartridges, brushed steel selector rail, matte asphalt paper, muted-teal guide inserts, one warm-amber reset stop. Palette: asphalt gray, charcoal, dirty off-white, muted teal, warm amber. Lighting: soft top-left studio key, clean contact shadows, subtle acrylic refraction, no neon or night-city glow. Typography mode: no letters, no numbers, no icons, no logos, no UI labels, no pseudo-text. References: none. Physical plausibility: every cartridge rests in a fitted bay, the selector rail is bolted to the deck, the reset stop is mechanically connected, all shadows align, nothing floats. Constraints: no GTA logo, no recognizable city, no characters, no cars, no weapons, no cash, no police imagery, no HUD, no monitor, no keyboard, no hacker cliché, no shield, no padlock, no cyberpunk, no clutter. Priority order: 1) instantly readable three-profile organization metaphor, 2) one dominant control deck with subordinate cartridges, 3) strong safe zone and tactile plausibility, 4) restrained urban editorial palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

Самооценка по visual guide: 95/100. Один герой, три физически организованных профиля, безопасная зона для верстки, полный prompt contract и строгие ограничения. Порог 80/100 пройден.

---

## Финальная приемка серии

Перед передачей автору или публикацией редактор должен проверить все восемь статей:

- Есть ровно восемь самостоятельных материалов, каждый ведет только на закрепленный за ним URL.
- Язык совпадает с целевой страницей: №1, №3, №6 и №7 — English; №2, №4, №5 и №8 — русский.
- Объем каждой статьи — 500–800 слов; рекомендуемый итог — 650–750.
- В каждой статье ровно две ссылки, анкоры совпадают с ТЗ посимвольно, ссылки разделены минимум двумя разделами.
- Нет ссылок в H1, первом абзаце, FAQ, SEO title, description и подписях к изображениям.
- Восемь тем не дублируют друг друга и не повторяют целевые страницы: feature glossary, методика сравнения, fight triage, phase profiles, supply-chain audit, artillery coordination, platform compatibility и menu profiles.
- Нет непроверенных цен, обещаний безопасности, ban-proof/VAC/EAC claims, инструкций по обходу, инжекту, скрытию или эксплуатации.
- Есть SEO front matter, description до 160 символов с primary keyword, image placement notes и FAQ из четырех вопросов.
- Нет markdown-таблиц, generic AI filler и рекламных суперлативов.
- Каждый generated cover использует полный prompt без сокращений, стиль `article-editorial-poster-v1`, Nano Banana Pro / `gemini-3-pro-image`, 2K 16:9 и оценку выше 80/100.
- Inline-скриншоты являются реальными, разрешенными к использованию и подписаны только по фактически видимому содержимому; сгенерированных интерфейсов нет.
