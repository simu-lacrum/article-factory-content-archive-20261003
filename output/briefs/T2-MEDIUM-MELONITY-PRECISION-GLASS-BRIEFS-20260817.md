# ТЗ: 4 самостоятельные T2-статьи для Melonity

Дата пакета: 17 августа 2026 года.

## Результат

Подготовить четыре самостоятельные статьи: две на US English и две на русском. Каждая статья закрывает отдельный информационный запрос, читается как законченный редакционный материал и содержит ровно одну коммерчески значимую ссылку на назначенную страницу Melonity.

Картинки в рамках задачи не генерируются. В ТЗ оставлены восемь готовых production-промптов на случай, если визуалы понадобятся при публикации.

## Карта целей

1. EN: defensive item logic in Deadlock → https://melonity.gg/en/deadlock
2. EN: courier information in Dota 2 → https://melonity.gg/en
3. RU: телепорты и смена линий в Dota 2 → https://melonity.gg/
4. RU: подтверждение душ и экономика линии в Deadlock → https://melonity.gg/deadlock

Материалы не являются переводами друг друга. EN и RU Deadlock раскрывают разные игровые проблемы; то же правило соблюдено для двух статей по Dota 2.

## Почему выбраны эти темы по графу

- У EN Deadlock-страницы есть прямая связь с item automation, auto-counterspell и auto-dispel, но в опубликованном слое нет самостоятельного материала о конфликте защитных приоритетов и false positives. Это узкий коммерчески близкий пробел, а не ещё один общий обзор функций.
- В Dota 2-графе courier awareness выделен как отдельный long-tail-кластер и соседняя тема к общему map information. При этом прямой MapHack уже покрыт, поэтому курьер разобран как сигнал item timing, а не как повтор статьи о карте.
- Русская главная прямо связана с `Teleport Preview`. Свободный угол находится не в описании функции, а в тройном последствии одного TP: оставленная линия, усиленная линия и открывшаяся третья зона.
- Русская Deadlock-страница связана с визуальным выделением душ. Ранее подготовленные темы закрывали projectile aim, ESP-категории и перегруз интерфейса, но не полный микроцикл `добивание → подтверждение/отрицание → позиция к следующей волне`.
- Заголовки и основные интенты не совпадают с опубликованным реестром, avoid-list и предыдущим пакетом T2. Финальный текст всё равно проходит отдельный plagiarism check: отсутствие дубля темы не гарантирует отсутствие фразовых совпадений.

## Проверка целевых страниц

- Все четыре URL 17 августа 2026 года отвечали HTTP 200 без редиректа.
- `https://melonity.gg/en/deadlock` — английская Deadlock-страница, self-canonical, в `hreflang` связана с русской `/deadlock`.
- `https://melonity.gg/en` — английская главная Dota 2, self-canonical, в `hreflang` связана с русским корнем.
- `https://melonity.gg/` — русская главная Dota 2, self-canonical.
- `https://melonity.gg/deadlock` отдаёт русскую Deadlock-страницу и имеет корректный русский `hreflang`, но в текущем HTML canonical указывает на `https://melonity.gg`, а не на `/deadlock`. Желательно исправить это до размещения T2, иначе ссылка будет поддерживать URL, который сама страница не объявляет каноническим.
- На страницах есть динамические продуктовые заявления о trial, ценах, количестве функций, поддержке и защите. В статьях их не повторять как установленные факты. Если редактор всё же оставляет конкретное число или условие, перепроверить его в день публикации и атрибутировать: «на странице продукта указано…».

## Общий редакционный контракт

- Формат: экспертный T2, а не рейтинг, пресс-релиз, пересказ лендинга или рекламная простыня.
- Язык: T2-01 и T2-02 — US English; T2-03 и T2-04 — естественный русский без кальки и канцелярита.
- Объём: указан отдельно. Не добивать знаки общими рассуждениями.
- Разметка: один H1; H2 по логике материала; H3 только для реального разделения подтем.
- Первый экран сразу ставит игровую проблему. Не начинать с истории жанра, определения MOBA или фразы о «современном динамичном мире».
- Не использовать Markdown-таблицы. Сравнения давать парами тезисов, короткими списками или через игровые ситуации.
- FAQ: 4–6 вопросов в самом конце, ответы по 2–4 предложения. Ссылок в FAQ нет.
- Не создавать блоки `Internal Links`, `Related Posts`, `Read Next` или их замены.
- В финальном теле ровно одна коммерчески значимая ссылка — назначенный target URL. Не ставить её в H1/H2, первый абзац, FAQ, подпись автора или последнюю фразу.
- Не добавлять другие коммерческие URL, ссылки на конкурентов, UTM-метки или сокращатели.
- Не употреблять `undetectable`, `100% safe`, `ban-free`, `zero risk`, `guaranteed` и русские аналоги.
- Не давать инструкции по обходу anti-cheat, сокрытию поведения, injection, драйверам, чтению памяти, offsets, signatures, spoofing и эксплуатации уязвимостей.
- Не советовать отключать антивирус или системную защиту. При предупреждении безопасности остановиться, проверить домен и обратиться к официальной поддержке.
- Продуктовые возможности описывать только на уровне назначения, интерфейса и критериев оценки. Не объяснять внутреннюю реализацию.
- Текущие патчевые значения, цены, trial, совместимость, часы поддержки и статус продукта либо проверять в день публикации, либо опускать.

## Gate уникальности и живого текста

100% уникальности — редакционная цель, а не честная гарантия до проверки готового текста выбранным сервисом. Каждый автор сдаёт не пересказ этого ТЗ, а новый материал с собственной последовательностью аргументов и конкретными игровыми сценами.

Перед публикацией:

1. Писать по тезисам с чистого листа. Не держать рядом target-страницу и не переставлять слова в её абзацах.
2. Не переводить EN-статью в RU или наоборот. У четырёх материалов разные hook, метафора, структура и финальный вывод.
3. Сравнить текст с опубликованными статьями проекта и ранее подготовленным T2-пакетом. Переписать совпадающие цепочки от восьми слов, кроме названий игр, продуктов и официальных терминов.
4. Проверить факты отдельно от стилистики. Общая правдоподобная формулировка без источника не становится фактом.
5. Прогнать финальный body через согласованный plagiarism checker. Для буквальной отметки 100% сохранить название сервиса, дату и скрин результата.
6. Прочитать вслух и убрать фразы, которые автор не сказал бы тиммейту или читателю одним дыханием.

Редакторская вычитка против типичных машинных маркеров:

- вырезать `delve`, `landscape`, `realm`, `game-changer`, `ever-evolving`, `robust`, `seamless`, `comprehensive guide`, `crucial`, `pivotal`, `it is worth noting`;
- не открывать текст вопросами `Have you ever wondered…?` или `Are you struggling with…?`;
- не строить подряд H2 вида `Understanding…`, `Why It Matters…`, `Key Takeaways…`;
- не вставлять автоматические переходы `Moreover`, `Furthermore`, `In addition`, `В современном мире`, `Важно отметить`, если они не меняют мысль;
- не делать каждый раздел одинаковым: вступление, три симметричных пункта, мини-вывод;
- избегать конструкции «это не просто X — это Y» и серии риторических противопоставлений;
- чередовать длину абзацев по смыслу, а не имитировать случайность; короткая фраза должна что-то резать или фиксировать;
- не придумывать личный тест, Discord-игрока, статистику, цитату, матч или «мы проверили»;
- оставить редакторскую позицию и неудобные оговорки: ложная реакция, устаревшая информация, конфликт приоритетов, цена лишнего сигнала;
- не делать тон постоянно восторженным. Полезная функция может мешать, если даёт слишком много сигналов или выбирает неверный момент;
- не маскировать происхождение текста намеренными опечатками;
- не считать AI-detector доказательством авторства. Контроль — факты, оригинальная мысль, нормальный ритм и ручная редактура.

Основа gate: people-first рекомендации Google, правила Medium об AI-контенте и плагиате, а также исследования о клише, лишней экспозиции и повторяемой формуле машинного текста.

## Визуальный язык: Precision Glass Editorial v1

Визуалы не генерировать сейчас. Если они понадобятся, использовать промпты без упрощения контракта.

- Система: `article-editorial-poster-v1`, локальная ветка `Precision Glass Editorial v1`.
- Модель по умолчанию: Nano Banana Pro / `gemini-3-pro-image`.
- Нечётные индексы 01, 03, 05, 07: branch B3, обложка 16:9, обязательны два реально прикреплённых файла из warm-story reference set.
- Чётные индексы 02, 04, 06, 08: branch A, inline 3:2, референсы не нужны.
- Цвет Melonity `#FF1469`: в B заменяет жёлто-янтарное доминирующее поле и занимает 35–70% кадра; в A остаётся малым смысловым акцентом 3–8%.
- В кадре один физически правдоподобный hero object: оптическое стекло, глазурованная керамика, матовый алюминий, frosted polycarbonate.
- Обложка содержит один точный headline из 3–7 слов. Inline-изображение — без текста.
- Запреты: cartoon, mascot, люди, животные, toy-like 3D, cyberpunk, neon gamer room, fake HUD, fake screenshot, код, логотипы, оружейный гламур, визуальный шум.
- Каждый B-промпт должен пройти fidelity 4/5; каждый промпт — preflight не ниже 80/100.

---

## T2-01 — Defensive item logic in Deadlock → EN Deadlock

Целевая страница: `https://melonity.gg/en/deadlock`

### SEO

- Язык: US English.
- Working title / H1: `Deadlock Auto-Dispel Logic: Why Fast Reactions Still Fail`
- Slug: `deadlock-auto-dispel-logic-fast-reactions-fail`
- Primary keyword: `Deadlock auto dispel`
- Secondary keywords: `Deadlock item automation`, `auto counterspell Deadlock`, `Deadlock save items`, `defensive item priority`, `false positive automation`
- Meta description: `Deadlock auto dispel is only useful when timing, threat and item priority agree. Learn why fast defensive reactions still fail.`
- Search intent: informational/commercial investigation; reader wants to understand what separates useful defensive automation from a noisy trigger.
- Ориентир объёма: 1,350–1,650 слов.
- Risk: restricted. Discuss decision logic and evaluation only; no implementation, detection-evasion or configuration recipes.

### Уникальный редакционный угол

Статья не продаёт «instant reaction». Её тезис: defensive automation is a small decision system, not a faster key press. A correct response needs three things at once — a real threat, an action that still has value, and a priority that does not waste the stronger save.

Opening hook: the save fires instantly, removes something harmless, and leaves the player with no answer for the disable that lands half a second later. Technically fast. Strategically wrong.

### Структура

1. H1: Deadlock Auto-Dispel Logic: Why Fast Reactions Still Fail
2. H2: The fastest save can still be the wrong save
3. H2: A trigger sees an event; a player reads a threat
4. H2: Dispel, counterspell and rescue are different jobs
5. H2: Priority matters when two answers are available
6. H2: False positives spend resources before the real danger
7. H2: Latency, state changes and the stale-decision problem
8. H2: What to inspect before trusting item automation
9. H2: Keep the player in the loop
10. H2: FAQ
11. Финал: one sharp rule — judge a defensive tool by the bad activations it avoids, not by how quickly it can activate.

### Обязательно раскрыть

- Separate reaction speed from decision quality. A lower delay is not automatically a better outcome.
- Explain the three evaluation layers in plain language: threat classification, eligible response, response priority.
- Use three fictional, patch-agnostic scenes: harmless debuff before a hard disable; two defensive items available; target becomes safe before the reaction completes.
- Show why a conservative no-action result can be better than a confident false positive.
- Explain that interface feedback matters: the user should understand what fired and why without a wall of logs.
- Give a seven-point buyer/evaluator checklist: readable categories, exclusions, priority order, manual override, visible cooldown state, conflict handling, update/support path.
- When mentioning that the target page lists auto-counterspell, auto-dispel and save-item automation, clearly attribute the statement to the page and avoid endorsing safety claims.
- Treat product availability and feature labels as publication-day facts that may change.

### Не включать

- Trigger conditions with exact values, per-item presets, config strings or recommended delay ranges.
- Any explanation of how game state is read, how inputs are generated or how detection is avoided.
- A list of current items presented as permanent. Deadlock changes; specific examples require same-day verification.
- Claims that automation is legitimate, safe, undetected or guaranteed.
- A generic comparison of every Deadlock feature. The article is about defensive decision quality.

### Research note

The English target page currently describes customizable auto-counterspell, auto-dispel and other save-item automation. Treat this as first-party product positioning, not independent proof. Official Deadlock forum discussions show that players routinely debate how parry and defensive-item interactions should be prioritized; use them only to capture the language of the problem, never as authoritative mechanics documentation.

### Backlink

- Anchor: `Melonity for Deadlock`
- Позиция: H2 `What to inspect before trusting item automation`, примерно 60% body.
- Предлагаемая фраза: `For a concrete feature list, the current [Melonity for Deadlock](https://melonity.gg/en/deadlock) page groups auto-counterspell, auto-dispel and other save-item options in one product; verify the live labels before comparing them against the checklist above.`
- В финальной статье эта ссылка используется один раз. Не повторять URL в источниках, FAQ или подписи.

### FAQ

- What does auto dispel mean in Deadlock?
- Why can an instant defensive reaction be wrong?
- What is a false positive in item automation?
- Should counterspell and dispel share the same priority?
- Can item automation guarantee account safety?

### Изображение 01 — cover

- Placement: сразу после front matter.
- Alt: A precision glass selector chooses one defensive response while rejecting two premature triggers.
- Prompt: Asset role: editorial cover for an English article about defensive item decision logic in Deadlock. Global generated index: 01. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: B3 symbolic object. Thesis: reaction speed has no value without threat context and response priority. Metaphor: a single transparent optical selector with three physical channels; one channel opens cleanly while two premature pink glass pulses stop at frosted gates before reaching it. Single hero: the optical decision selector, no game item replicas and no character. Aspect ratio: 16:9. Composition: selector occupies the lower-right 44% of the frame; broad headline field in the upper-left; preserve the directional dissolve and single-symbol clarity of reference-08 without copying its literal scene. Palette: Melonity pink #FF1469 is the dominant luminous field across about 58% of the frame and fully replaces all yellow or amber; secondary colors are cool white, graphite and faint blue-grey reflections. Materials: optical glass, satin aluminum, glazed ceramic, frosted polycarbonate. Camera: premium 70 mm studio product photograph, slight high angle, realistic lens behavior. Lighting: one large diffused key from upper left, controlled pink bounce, crisp contact shadow, no glowing fantasy fog. Typography mode: exact headline `REACTION NEEDS CONTEXT`, uppercase neutral neo-grotesk, three lines maximum, dark graphite, optically aligned; no other text. Reference 1: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-08.png`; composition role only — single geometric hero, directional transition and generous text field. Reference 2: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-07.png`; render/palette/typography role — macro device crop, bold headline scale, polished material lighting; replace its yellow/amber field with #FF1469. B fidelity target: 4/5 or better. Constraints: no copied source text, logos, people, animals, game UI, fake HUD, cartoon, cyberpunk, code, weapon glamour, extra labels or clutter. Priority: readable thesis and headline first, physically plausible selector second, decoration last. Model: Nano Banana Pro / gemini-3-pro-image. Output: 3840×2160 PNG. Preflight score: 94/100.

### Изображение 02 — inline

- Placement: после H2 `False positives spend resources before the real danger`.
- Alt: Two glass pulses are stopped while one valid signal reaches a ceramic gate.
- Prompt: Asset role: inline explanatory editorial image for false positives in defensive automation. Global generated index: 02. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: A tactile industrial macro. Thesis: rejecting a harmless trigger preserves the response for a meaningful threat. Metaphor: a compact machined rail carries three glass pulses toward one ceramic latch; two pulses rest safely behind frosted blockers while the third aligns with the latch. Single hero: the three-channel rejection rail. Aspect ratio: 3:2. Composition: diagonal macro assembly across the lower two thirds, clean negative space above, outcome readable without arrows or captions. Palette: cool white, graphite, brushed aluminum and smoked glass; Melonity pink #FF1469 appears only inside the valid pulse and one narrow calibration seam, about 5% of the frame. Materials: machined aluminum, optical glass, frosted polycarbonate, glazed ceramic. Camera: 100 mm macro product photography, controlled shallow depth of field with all three gates legible. Lighting: soft raking key, low-contrast fill, precise edge highlights and credible contact shadows. Typography mode: no text. References: none, branch A. Constraints: no UI, digits, arrows, code, logos, people, animals, cartoon, neon background, weapons or busy machinery. Priority: immediate false-positive metaphor, premium physical realism, quiet composition. Model: Nano Banana Pro / gemini-3-pro-image. Output: 2048×1365 PNG. Preflight score: 92/100.

---

## T2-02 — Courier information in Dota 2 → EN homepage

Целевая страница: `https://melonity.gg/en`

### SEO

- Язык: US English.
- Working title / H1: `Dota 2 Courier Information: The Delivery That Reveals the Next Fight`
- Slug: `dota-2-courier-information-next-fight`
- Primary keyword: `Dota 2 courier information`
- Secondary keywords: `Dota 2 courier guide`, `courier item timing`, `courier map awareness`, `Dota 2 power spike`, `enemy courier information`
- Meta description: `Dota 2 courier information can reveal an item timing before the fight starts. Learn what matters, what misleads and when to disengage.`
- Search intent: informational; reader wants a practical explanation of why courier movement and cargo matter beyond a courier kill.
- Ориентир объёма: 1,400–1,750 слов.
- Risk: restricted adjacent topic. Discuss visible/inferred information and decision value; do not explain access to hidden data or targeting automation.

### Уникальный редакционный угол

This is not a courier cosmetics list and not a guide to chasing couriers. The courier is treated as a moving receipt: its route, timing and destination can change how a team reads the next minute. The core editorial distinction is observation versus inference. A delivery suggests a power spike; it does not prove the exact plan.

Opening hook: the enemy core disappears for ten seconds, the courier completes a delivery, and a lane that looked safe suddenly is not. The valuable signal was not the courier’s bounty. It was the timing.

### Структура

1. H1: Dota 2 Courier Information: The Delivery That Reveals the Next Fight
2. H2: A courier is a moving receipt, not a side quest
3. H2: Delivery timing can matter more than cargo value
4. H2: Route, destination and return trip tell different stories
5. H2: Observation is not certainty
6. H2: The three decisions courier information can improve
7. H2: Why chasing the courier often throws away the advantage
8. H2: What a useful courier-information feature should show
9. H2: A one-minute review drill for your own replays
10. H2: FAQ
11. Финал: read the delivery, adjust the next decision, and stop there — information loses value when it turns into a detour.

### Обязательно раскрыть

- Explain three different signals: route suggests destination; delivery timing suggests an item window; return movement may indicate the transaction is complete.
- Keep `suggests` and `proves` separate in every example.
- Use three patch-agnostic scenarios: lane pressure before a delivery; objective setup after a delivery; baiting a courier chase away from a wave.
- Show three reasonable responses: delay the fight, force action before the delivery, or keep farming while updating expectations.
- Explain why courier information must be filtered by recency and destination; old or ambiguous data can be worse than no data.
- Include a compact evaluation list: freshness, path clarity, cargo-label clarity, screen clutter, uncertain-state handling, replay value, support/update path.
- Add a replay drill using only normal replay observation: pause before a fight, note visible courier movement, predict the next item window, then compare with what happened. No hidden-data method.
- Connect the topic to the Melonity Dota 2 homepage only in the evaluation section, not in the instructional core.

### Не включать

- Routes for killing couriers, exact current bounty/respawn values or hero-specific courier snipe setups.
- Any method for revealing hidden position, inventory, network data or fog-of-war information.
- A promise that one courier signal identifies the exact item or enemy plan.
- A catalogue of unusual courier cosmetics. It would split the intent and weaken the thesis.
- Current patch facts unless checked against Valve material on publication day.

### Research note

Valve’s official Dota 2 material has repeatedly framed courier logistics and information gathering as meaningful interface concerns. The older Outlanders page is useful only for the durable fact that every player has a courier; its numerical values are historical and must not be reused as current. Project memory also identifies courier awareness as an adjacent, underused editorial cluster rather than another generic MapHack article.

### Backlink

- Anchor: `Melonity Dota 2 tools`
- Позиция: H2 `What a useful courier-information feature should show`, примерно 62% body.
- Предлагаемая фраза: `Readers comparing a broader feature set can use the current [Melonity Dota 2 tools](https://melonity.gg/en) page as one product example, then judge every information claim by freshness, clarity and whether it changes a real decision.`
- В финальной статье эта ссылка используется один раз. Не повторять её в FAQ, research note или финале.

### FAQ

- Why does courier information matter in Dota 2?
- Can a courier route reveal an exact enemy item?
- Is chasing an enemy courier always worth it?
- What makes courier information stale?
- How can I practice reading courier timings in replays?

### Изображение 03 — cover

- Placement: сразу после front matter.
- Alt: A glass delivery capsule crosses a precision rail toward a waiting item socket.
- Prompt: Asset role: editorial cover for an English article about the decision value of courier information in Dota 2. Global generated index: 03. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: B3 symbolic object. Thesis: a delivery can reveal an upcoming power window before the fight begins. Metaphor: one sealed optical-glass delivery capsule travels along a curved satin-aluminum rail toward a vacant ceramic socket, with the return rail fading into a fine pattern behind it. Single hero: the delivery capsule and its receiving socket, no creature or literal game courier. Aspect ratio: 16:9. Composition: centered-low hero with a wide calm headline field above; borrow reference-04’s focused central transformation and negative space without copying its character or setting. Palette: Melonity pink #FF1469 fills about 60% of the frame and fully replaces yellow or amber; secondary colors are cool white, graphite and smoke-grey glass. Materials: optical glass, satin aluminum, glazed ceramic, frosted polycarbonate. Camera: premium 65 mm product photograph at rail height, subtle perspective compression. Lighting: large diffused source, controlled pink bounce, a narrow white rim on the moving capsule and credible contact shadows. Typography mode: exact headline `THE COURIER TELLS FIRST`, uppercase neutral neo-grotesk, three lines maximum, dark graphite, no subtitle or microcopy. Reference 1: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-04.png`; composition role — centered hero, one semantic transformation and generous upper text field. Reference 2: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-05.png`; render/palette/typography role — bold headline hierarchy, soft architectural depth and rounded material lighting; replace all yellow/amber with #FF1469 and do not copy the house. B fidelity target: 4/5 or better. Constraints: no source text, logos, people, animals, literal flying courier, game UI, fake map, cartoon, cyberpunk, code, coins or clutter. Priority: readable delivery-before-fight thesis, clear headline, physical plausibility. Model: Nano Banana Pro / gemini-3-pro-image. Output: 3840×2160 PNG. Preflight score: 93/100.

### Изображение 04 — inline

- Placement: после H2 `Observation is not certainty`.
- Alt: One delivery capsule approaches two possible sockets without selecting either.
- Prompt: Asset role: inline explanatory editorial image for uncertainty in courier-route inference. Global generated index: 04. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: A tactile industrial macro. Thesis: a visible route can narrow possibilities without proving one destination. Metaphor: a glass capsule pauses at a precision Y-junction whose two ceramic sockets remain equally open; a small physical index mark shows the last confirmed position but no arrow chooses the branch. Single hero: the Y-junction delivery mechanism. Aspect ratio: 3:2. Composition: junction spans the lower two thirds, two branches balanced but not perfectly symmetrical, quiet negative space above. Palette: cool white, brushed aluminum, graphite and smoked glass; Melonity pink #FF1469 appears only on the last-confirmed index and a slim gasket, about 4% of the frame. Materials: optical glass, machined aluminum, glazed ceramic. Camera: 95 mm macro product photography, both sockets and capsule sharp, background gently soft. Lighting: broad side key, controlled reflections, true contact shadows. Typography mode: no text. References: none, branch A. Constraints: no labels, arrows, map, UI, code, logos, people, animals, cartoon, neon or decorative cargo. Priority: unresolved choice legible at a glance, tactile finish, visual restraint. Model: Nano Banana Pro / gemini-3-pro-image. Output: 2048×1365 PNG. Preflight score: 91/100.

---

## T2-03 — Телепорты и смена линий в Dota 2 → RU главная

Целевая страница: `https://melonity.gg/`

### SEO

- Язык: русский.
- Working title / H1: `Телепорт в Dota 2: как одно перемещение меняет три линии`
- Slug: `teleport-v-dota-2-kak-menyaetsya-karta`
- Primary keyword: `телепорт в Dota 2`
- Secondary keywords: `куда телепортируется враг Dota 2`, `перемещение по линиям Dota 2`, `Town Portal Scroll`, `чтение карты Dota 2`, `Teleport Preview`
- Meta description: `Телепорт в Dota 2 меняет давление сразу на нескольких линиях. Разбираем, как читать направление, окно уязвимости и ложные выводы.`
- Search intent: информационный; читатель хочет лучше понимать смену линий и ценность информации о направлении телепорта.
- Ориентир объёма: 1 350–1 650 слов.
- Risk: restricted adjacent topic. Обсуждать решение и интерфейс, но не получение скрытых данных и не автоматизацию реакции.

### Уникальный редакционный угол

Материал не объясняет, как нажимать телепорт. Он разбирает карту как систему сообщающихся сосудов: уход героя с одной линии одновременно ослабляет старую точку, усиливает новую и создаёт короткое окно на третьем участке карты. Главная мысль — направление важнее самого визуального эффекта.

Opening hook: враг начал телепорт и исчез с линии. Большинство смотрит только туда, где он появится. Полезнее задать три вопроса: что он бросил, что усилил и где теперь стало можно играть наглее.

### Структура

1. H1: Телепорт в Dota 2: как одно перемещение меняет три линии
2. H2: Телепорт начинается в одной точке, а меняет всю карту
3. H2: Точка отправления говорит не меньше точки прибытия
4. H2: Три линии, которые нужно перечитать за несколько секунд
5. H2: Начатый телепорт не равен завершённому
6. H2: Когда информация свежая, но вывод уже неверный
7. H2: Четыре нормальные реакции команды
8. H2: Каким должен быть полезный Teleport Preview
9. H2: Упражнение для реплея без дополнительных инструментов
10. H2: FAQ
11. Финал: после каждого замеченного TP назвать вслух не героя, а освободившийся участок карты.

### Обязательно раскрыть

- Разделить три сигнала: откуда ушёл герой, куда он направился, дошёл ли он туда.
- Показать три связанные зоны: покинутая линия, усиленная линия, нейтральная зона или объект, где изменился риск.
- Дать четыре реакции без универсального рецепта: продавить оставленную линию, отступить от усиленной, ускорить объект, сохранить позицию и обновить информацию.
- Привести три вымышленных патч-независимых эпизода: защитный TP на башню, присоединение к драке, отменённое перемещение.
- Объяснить цену устаревшего сигнала: герой мог отменить действие, сменить маршрут после прибытия или уже уйти из точки.
- В блоке оценки интерфейса проверить читаемость отправления и назначения, отметку отмены, срок жизни сигнала, цветовую иерархию, отсутствие лишних эффектов.
- Упражнение по реплею: остановить запись в момент начала TP, записать три изменившиеся зоны, досмотреть десять–пятнадцать секунд, сверить решение. Не выдавать это за текущий точный тайминг механики.
- Target упомянуть только как пример страницы, где заявлен Teleport Preview; не превращать статью в обзор всего продукта.

### Не включать

- Точные текущие длительности, cooldown, стоимость свитка и правила прерывания без проверки актуального патча.
- Способ получения направления через память, сетевые события, particles или иные внутренние данные.
- Формулу автоматической реакции, скрипт, настройку или готовые значения задержки.
- Тезис «увидел TP — обязан драться». Статья должна показывать несколько допустимых решений.
- Пересказ общего MapHack-материала, ward guide или списка функций Melonity.

### Research note

На русской и английской главной Melonity функция называется `Teleport Preview` и описывается как показ направления перемещения по линиям. Это заявление страницы. Из официальных материалов Valve допустимо использовать лишь устойчивую идею: интерфейс Dota показывает выбранную цель телепорта и информация на миникарте влияет на решение. Конкретные правила проверять в актуальном клиенте и patch notes перед публикацией.

### Backlink

- Anchor: `Melonity для Dota 2`
- Позиция: H2 `Каким должен быть полезный Teleport Preview`, примерно 58% body.
- Предлагаемая фраза: `На странице [Melonity для Dota 2](https://melonity.gg/) Teleport Preview заявлен как отдельный информационный инструмент; оценивать его стоит по тому, различает ли он отправление, назначение и отмену, а не по яркости отметки.`
- В финальной статье ссылка ставится один раз. Не дублировать её в FAQ, выводе или подписи.

### FAQ

- Что можно понять по телепорту врага в Dota 2?
- Почему точка отправления так же важна, как назначение?
- Может ли начатый телепорт быть отменён?
- Когда информация о TP становится устаревшей?
- Как тренировать чтение телепортов по реплеям?

### Изображение 05 — cover

- Placement: сразу после front matter.
- Alt: Стеклянный модуль перемещения одновременно меняет давление в трёх керамических каналах.
- Prompt: Asset role: editorial cover for a Russian article about how one teleport changes several areas of the Dota 2 map. Global generated index: 05. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: B3 symbolic object. Thesis: one relocation strengthens one lane, abandons another and opens a third opportunity. Metaphor: a single transparent transfer capsule has just moved between three connected ceramic channels; the arrival socket compresses, the departure socket opens and a third side channel gains a clear path. Single hero: the three-channel transfer instrument, no literal map and no character. Aspect ratio: 16:9. Composition: hero object sits in the lower-left-to-center band with a large headline field on the right; use reference-06 for the modular flow and clean editorial rhythm without copying its objects. Palette: Melonity pink #FF1469 is the dominant field covering about 56% of the frame and fully replaces yellow or amber; secondary colors are cool white, graphite and pale smoke-blue. Materials: optical glass, satin aluminum, glazed ceramic, frosted polycarbonate. Camera: premium 75 mm product photograph, slight overhead angle that keeps the three channels readable. Lighting: one broad softbox, controlled pink bounce, precise white edge highlights and realistic contact shadows. Typography mode: exact headline `ТЕЛЕПОРТ МЕНЯЕТ КАРТУ`, uppercase neutral neo-grotesk, three lines maximum, dark graphite, no subtitle. Reference 1: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-06.png`; composition role — modular route, directional flow and disciplined negative space. Reference 2: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-07.png`; render/palette/typography role — premium macro crop, large headline hierarchy and polished material light; replace every yellow/amber region with #FF1469. B fidelity target: 4/5 or better. Constraints: no copied source text, logos, people, animals, game UI, fake minimap, arrows with labels, cartoon, cyberpunk, code, weapons or clutter. Priority: three consequences from one transfer, perfectly readable Russian headline, physical realism. Model: Nano Banana Pro / gemini-3-pro-image. Output: 3840×2160 PNG. Preflight score: 94/100.

### Изображение 06 — inline

- Placement: после H2 `Начатый телепорт не равен завершённому`.
- Alt: Капсула остановилась между точкой отправления и приёмным гнездом.
- Prompt: Asset role: inline explanatory editorial image for an interrupted or unresolved teleport. Global generated index: 06. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: A tactile industrial macro. Thesis: a started transfer is not proof of arrival. Metaphor: one optical-glass capsule is suspended halfway between an open departure ring and an unoccupied receiving socket; a physical brake fin has engaged before contact. Single hero: the interrupted transfer mechanism. Aspect ratio: 3:2. Composition: horizontal mechanism across the lower two thirds, visible gap before the destination, calm empty background above. Palette: cool white, graphite, brushed aluminum and smoked glass; Melonity pink #FF1469 appears only on the brake fin and one narrow status seam, about 5% of the frame. Materials: optical glass, machined aluminum, glazed ceramic. Camera: 100 mm macro, both rings and the suspended capsule sharp. Lighting: soft raking key, restrained fill, clean edge reflections, credible contact shadows on the base. Typography mode: no text. References: none, branch A. Constraints: no UI, numbers, captions, arrows, logos, people, animals, cartoon, neon, code or map iconography. Priority: unfinished transfer instantly legible, tactile precision, quiet frame. Model: Nano Banana Pro / gemini-3-pro-image. Output: 2048×1365 PNG. Preflight score: 92/100.

---

## T2-04 — Подтверждение душ и экономика линии → RU Deadlock

Целевая страница: `https://melonity.gg/deadlock`

### SEO

- Язык: русский.
- Working title / H1: `Души в Deadlock: как проигрывают линию между добиванием и подтверждением`
- Slug: `dushi-v-deadlock-dobivanie-podtverzhdenie-liniya`
- Primary keyword: `души в Deadlock`
- Secondary keywords: `как подтверждать души Deadlock`, `отрицание душ Deadlock`, `экономика линии Deadlock`, `soul orb`, `приоритет целей Deadlock`
- Meta description: `Души в Deadlock теряются не только из-за плохого аима. Разбираем цикл добивания, подтверждения, отрицания и давления на линии.`
- Search intent: информационный; читатель хочет понять, почему хорошее добивание ещё не гарантирует выигранную экономику линии.
- Ориентир объёма: 1 400–1 700 слов.
- Risk: restricted adjacent topic. Игровую механику и принятие решений можно объяснять; реализацию автоматического наведения на души — нельзя.

### Уникальный редакционный угол

Это не общий гайд по всем источникам фарма. Объект анализа — короткий цикл одной линии: подготовить добивание, забрать крипа, подтвердить свою сферу, помешать отрицанию и не отдать позицию ради следующей. Тезис: игрок проигрывает экономику не одним промахом, а цепочкой маленьких долгов внимания.

Opening hook: крип добит, число на экране вроде бы выросло, но размен всё равно проигран. Пока игрок смотрел на свою сферу, соперник забрал вторую, нанёс бесплатный урон и занял угол к следующей волне.

### Структура

1. H1: Души в Deadlock: как проигрывают линию между добиванием и подтверждением
2. H2: Добить крипа — только половина микроцикла
3. H2: Подтверждение, отрицание и позиция спорят за одну секунду внимания
4. H2: Почему ближайшая сфера не всегда главная
5. H2: Магазин, укрытие и перезарядка меняют приоритет
6. H2: Задержка сигнала превращает уверенность в ошибку
7. H2: Как должна выглядеть полезная подсветка душ
8. H2: Пять эпизодов для разбора собственного реплея
9. H2: Где заканчивается информация и начинается решение игрока
10. H2: FAQ
11. Финал: считать не отдельные попадания по сферам, а полный цикл — доход, урон, позиция к следующей волне.

### Обязательно раскрыть

- Объяснить микроцикл без привязки к текущим числам: подготовка здоровья крипа, добивание, появление сферы, подтверждение или отрицание, восстановление позиции.
- Развести свою сферу, вражескую возможность отрицания и давление по герою. Это три конкурирующие цели, а не один aim challenge.
- Дать четыре критерия приоритета: доступное окно, цена промаха, безопасность позиции, состояние магазина/перезарядки.
- Использовать три конкретные патч-независимые сцены: две сферы появляются почти одновременно; подтверждение требует выйти из укрытия; игрок опустошает магазин перед важной сферой.
- Объяснить, почему визуал должен различать тип цели, свежесть и реальную доступность, а не просто красить всё ярче.
- Показать цену screen clutter: душа может быть видна, но потеряться среди рамок, дистанций, health bars и эффектов.
- В replay-блоке дать пять вопросов: что было добито, какая сфера появилась первой, кто имел угол, сколько внимания ушло, где оказался игрок к следующему крипу.
- При упоминании Melonity сказать только, что целевая страница заявляет подсветку душ среди визуальных функций. Не переносить оттуда обещания о безопасности и эффективности.

### Не включать

- Точные тайминги, награды, проценты распределения и правила unsecured souls без проверки текущего патча.
- Настройки aim, FOV, hitbox, задержки, приоритетные кости или любую реализацию наведения на soul orb.
- Утверждение, что один цвет или автоматическая реакция гарантирует выигранную линию.
- Полный гайд по лесу, урне, боссу и всем источникам дохода: это другой интент.
- Повтор прежней статьи о projectile aiming. Здесь проблема — внимание и экономика микроцикла, а не расчёт упреждения.

### Research note

Русская target-страница заявляет подсветку душ, союзников/противников, активностей карты и power-up. В официальном форуме Deadlock встречаются вопросы игроков о подтверждённых и неподтверждённых душах и о ситуациях, когда визуальный результат попадания воспринимается неоднозначно. Эти сообщения показывают реальную путаницу, но не служат доказательством текущих правил: механику проверять в актуальной версии игры.

### Backlink

- Anchor: `Melonity для Deadlock`
- Позиция: H2 `Как должна выглядеть полезная подсветка душ`, примерно 56% body.
- Предлагаемая фраза: `На странице [Melonity для Deadlock](https://melonity.gg/deadlock) души указаны как отдельная категория визуальной подсветки; при оценке важнее проверить различимость цели, свежесть сигнала и нагрузку на экран, чем количество доступных цветов.`
- В финальной статье ссылка ставится ровно один раз и не повторяется в FAQ, источниках или финальной строке.

### FAQ

- Как работают души на линии в Deadlock?
- Чем подтверждение души отличается от отрицания?
- Почему добивание крипа ещё не означает выигранный размен?
- Когда не стоит выходить за сферой из безопасной позиции?
- Может ли подсветка душ заменить решение игрока?

### Изображение 07 — cover

- Placement: сразу после front matter.
- Alt: Две стеклянные сферы претендуют на одно узкое окно подтверждения.
- Prompt: Asset role: editorial cover for a Russian article about the lane-economy cycle of securing and denying souls in Deadlock. Global generated index: 07. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: B3 symbolic object. Thesis: winning the lane requires choosing between confirmation, denial and safe positioning within one short attention window. Metaphor: two optical-glass spheres approach one narrow ceramic confirmation gate from different channels while a protective frosted shield limits the available angle. Single hero: the dual-sphere confirmation gate, no character and no literal game orb screenshot. Aspect ratio: 16:9. Composition: hero occupies the lower-right 46%; wide headline field upper-left; follow reference-08’s directional material transition and single decision point without copying its literal object. Palette: Melonity pink #FF1469 dominates about 59% of the frame and completely replaces yellow or amber; secondary colors are cool white, graphite and muted blue-grey glass. Materials: optical glass, glazed ceramic, satin aluminum, frosted polycarbonate. Camera: premium 70 mm studio product photograph, shallow high angle that keeps both spheres and gate sharp. Lighting: large soft source from upper left, controlled pink bounce, narrow white edge highlights and real contact shadows. Typography mode: exact headline `ДУШИ РЕШАЮТ ЛИНИЮ`, uppercase neutral neo-grotesk, three lines maximum, dark graphite, no other text. Reference 1: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-08.png`; composition role — directional dissolve, single symbolic conflict and generous text area. Reference 2: attach `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-04.png`; render/palette/typography role — centered semantic accent, calm depth and clear headline hierarchy; replace yellow/amber with #FF1469 and do not copy its figure. B fidelity target: 4/5 or better. Constraints: no copied source text, logos, people, animals, game UI, fake HUD, cartoon, cyberpunk, code, weapons, coins or clutter. Priority: two competing spheres and one decision window first, readable Russian headline second, premium physical plausibility third. Model: Nano Banana Pro / gemini-3-pro-image. Output: 3840×2160 PNG. Preflight score: 95/100.

### Изображение 08 — inline

- Placement: после H2 `Подтверждение, отрицание и позиция спорят за одну секунду внимания`.
- Alt: Три механических окна внимания конкурируют за одну стеклянную сферу.
- Prompt: Asset role: inline explanatory editorial image for competing attention during a Deadlock lane soul cycle. Global generated index: 08. Style system: article-editorial-poster-v1, Precision Glass Editorial v1. Branch: A tactile industrial macro. Thesis: one brief attention window must balance confirmation, denial and safe position. Metaphor: one glass sphere sits on a precision turntable facing three distinct ceramic apertures; only one aperture can align at a time, while a frosted guard makes the unsafe angle visibly narrower. Single hero: the three-aperture attention turntable. Aspect ratio: 3:2. Composition: macro mechanism fills the lower two thirds, apertures readable by shape rather than labels, clean negative space above. Palette: cool white, graphite, brushed aluminum and smoked glass; Melonity pink #FF1469 appears only on the active alignment notch and a small gasket, about 4% of the frame. Materials: optical glass, machined aluminum, glazed ceramic, frosted polycarbonate. Camera: 100 mm macro product photograph, all three apertures and sphere sharp. Lighting: soft side key, low-contrast fill, precise reflections and credible contact shadows. Typography mode: no text. References: none, branch A. Constraints: no UI, numbers, arrows, captions, logos, people, animals, cartoon, neon, code, fake game objects or busy machinery. Priority: three-way competition readable without annotation, tactile realism, quiet editorial frame. Model: Nano Banana Pro / gemini-3-pro-image. Output: 2048×1365 PNG. Preflight score: 92/100.

---

## Исследовательская база и правила атрибуции

Основные страницы:

- English Deadlock product page: https://melonity.gg/en/deadlock
- English Dota 2 homepage: https://melonity.gg/en
- Русская Dota 2 главная: https://melonity.gg/
- Русская Deadlock product page: https://melonity.gg/deadlock

Игровые источники:

- Valve, Dota 2 New HUD: https://www.dota2.com/700/hud/
- Valve, The Outlanders Update: https://www.dota2.com/outlanders
- Official Deadlock forum, `Neutrals and Soul securing`: https://forums.playdeadlock.com/threads/neutrals-and-soul-securing.19227/
- Official Deadlock forum, `Ammo return on soul denies/secures`: https://forums.playdeadlock.com/threads/ammo-return-on-soul-denies-secures-doesnt-work-properly-with-last-bullet-in-the-mag.69869/
- Official Deadlock forum, `More items around parries?`: https://forums.playdeadlock.com/threads/more-items-around-parries.103019/latest

Редакторские источники:

- Google, Creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google, Guidance about generative AI content: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- Medium, AI content policy: https://help.medium.com/hc/en-us/articles/22576852947223-Artificial-Intelligence-AI-content-policy
- Medium, Plagiarism Guidelines: https://help.medium.com/hc/en-us/articles/360041640213-Plagiarism-Guidelines
- Microsoft, Humanize AI text: https://www.microsoft.com/en-us/microsoft-copilot/copilot-101/humanize-ai-text
- ACL Anthology, `People who frequently use ChatGPT for writing tasks`: https://aclanthology.org/2025.acl-long.267/

Правила:

- Melonity — первичный источник только для того, что Melonity заявляет о собственных страницах и функциях. Это не независимое подтверждение безопасности, эффективности или статуса anti-cheat.
- Valve и актуальный клиент — источник механики Dota 2. Старые страницы показывают развитие интерфейса, но их числа нельзя выдавать за текущие.
- Официальный форум Deadlock используется для формулировок вопросов, пограничных случаев и пользовательской путаницы. Пост участника форума не равен документации Valve.
- Не переносить цитаты длиннее необходимого. Все финальные формулировки писать своими словами.
- Если факт изменяемый и не подтверждён в день публикации, удалить число или прямо обозначить неопределённость.

## Финальный QA перед передачей в публикацию

### SEO

- У статьи один H1, и он совпадает с согласованным working title либо имеет документированную редакторскую причину изменения.
- Primary keyword есть в H1, description до 160 символов и естественно появляется в первых 120 словах.
- Description не обрывается, не обещает безопасность и соответствует реальному содержанию.
- Slug короткий, без года и без искусственного набора синонимов.
- FAQ стоит в конце и не повторяет дословно H2.
- Front matter содержит как минимум `title`, `slug`, `description`, `primary_keyword`, `language`, `target_url`, `risk`.

### Ссылки

- В финальном body ровно один target backlink.
- URL и язык совпадают с назначением конкретного ТЗ.
- Ссылка не находится в первом абзаце, заголовке, FAQ, bio или последней фразе.
- Anchor читается естественно и не набит точными коммерческими ключами.
- Нет второго коммерческого URL, UTM, сокращателя и блока внутренних ссылок.
- Перед RU Deadlock-публикацией повторно проверить canonical `/deadlock`.

### Факты и безопасность

- Каждый изменяемый факт проверен в день публикации.
- Числа из старых patch notes не представлены как текущие.
- Product claim либо атрибутирован странице, либо удалён.
- Нет обещаний `undetected`, `safe`, отсутствия бана или гарантированного результата.
- Нет bypass/evasion, injection, memory reading, offsets, drivers, signatures, spoofing и конфигураций автоматической реакции.
- Форумные наблюдения не выданы за доказанную причину или правило игры.

### Голос и уникальность

- Материал не повторяет структуру target-страницы и не переводит соседнее ТЗ.
- Opening hook содержит конкретную игровую сцену, а не универсальный вопрос.
- В каждом разделе есть новая мысль, пример или критерий; плавные пустые переходы удалены.
- Нет выдуманных тестов, цитат, статистики, личного опыта и намеренных опечаток.
- Ритм абзацев меняется по смыслу; нет серии одинаковых трёхпунктовых блоков.
- Убраны канцелярит, корпоративный восторг и слова из anti-AI stop-list.
- Готовый body проверен plagiarism checker; результат и дата сохранены.

### Визуалы

- В текущей задаче изображения не создавались.
- Если генерация будет заказана: индексы 01–08 и ветки B/A сохранены.
- У каждой B-обложки реально приложены два указанных файла и прописаны разные роли.
- В B цвет `#FF1469` занимает 35–70% и заменяет жёлтый/янтарный; в A занимает 3–8%.
- В prompt нет людей, животных, мультяшности, fake UI, логотипов и копирования референса.
- Headline на обложке воспроизведён дословно; inline не содержит текста.
- Fidelity B не ниже 4/5, итоговый visual score не ниже 80/100.
