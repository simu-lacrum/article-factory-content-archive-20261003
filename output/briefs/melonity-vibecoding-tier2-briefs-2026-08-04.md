# ТЗ на две Tier 2 статьи для Melonity

Дата: 4 августа 2026 года  
Язык публикаций: русский  
Объем каждой статьи: 1000–1200 слов без учета SEO front matter и служебных заметок  
Целевая страница обеих статей: https://melonity.gg/  
Формат: самостоятельные полезные материалы, а не рекламные обзоры и не переписанные статьи о «лучших читах»

## Общая редакционная рамка

Обе статьи строятся на реальном процессе из видео: пользователь формулирует идею, дает AI контекст публичного шаблона, получает первый результат, уточняет нужный формат, загружает локальный файл в Melonity, видит отдельную панель настроек и проверяет поведение в контролируемой игровой среде. Этот материал нужно использовать как практический кейс, но не пересказывать видео поминутно.

Главная ценность серии — показать не очередной список функций, а новую для ниши тему: AI-assisted scripting, или «вайб-кодинг» кастомной игровой логики. Статья должна давать читателю применимую модель мышления: как описывать поведение, превращать идею в проверяемый прототип и отличать «файл загрузился» от «сценарий действительно работает предсказуемо».

Обязательные правила:

- Тон прямой, практичный и геймерский, но без крикливой рекламы, канцелярита и академической воды.
- Не писать, что Melonity или какой-либо скрипт «невидим», «не детектится», «не банится» или гарантирует безопасность.
- VAC и VAC Live допускается упомянуть только как границу ответственности: функциональная проверка в тестовой среде ничего не доказывает о статусе античита.
- Не публиковать код, приватные методы API, внутренние события, инструкции по инжекту, обходу, маскировке или уклонению от обнаружения.
- Не цитировать и не пересказывать нерелевантные persona/jailbreak-инструкции, видимые в начале записи. Для статьи это лишь этап подготовки AI-контекста.
- Не использовать формулировки «по локальным данным», «в evidence pack», «в базе проекта» и другие внутренние обозначения источников.
- Не утверждать точный стаж команды, если он не подтвержден единым публичным источником. Допустима нейтральная формулировка «команда с многолетним опытом».
- Не делать материал похожим на уже опубликованные интенты: «топ читов», общий обзор функций, MapHack, установка чита, безопасность, бан-риск или список консольных команд.
- Не использовать markdown-таблицы. Сравнения и чек-листы оформлять списками.
- В конце каждой статьи обязателен FAQ.

Каждый готовый материал перед основным текстом должен получить SEO front matter по этой схеме:

```yaml
---
title: "Финальный H1"
description: "До 160 символов, с основным ключом"
primary_keyword: "Основной ключ статьи"
game: "Dota 2"
language: "ru"
word_count_target: "1000-1200"
image_model: "Nano Banana Pro / gemini-3-pro-image"
---
```

Служебные поля, ТЗ, оценки промптов и пути к локальным кадрам в опубликованный текст не переносить.

## Ссылочная схема для обеих статей

В каждой статье должно быть две естественные ссылки на https://melonity.gg/:

1. Первая — точное анкорное вхождение, один раз, после того как статья уже дала читателю практическую ценность. Не ставить ссылку в первом экране, H1, SEO title или description.
2. Вторая — брендовая ссылка с анкором `Melonity` или `официальная платформа Melonity` в заключительном смысловом блоке. Она не должна повторять точный коммерческий анкор.

Ссылки не ставить рядом. Между ними должно быть не менее двух полноценных смысловых разделов. Не использовать URL без анкора и не добавлять агрессивные призывы вроде «скачай прямо сейчас».

---

# ТЗ №1. От идеи до проверяемого Dota 2-скрипта: реальный AI-workflow

## Концепция

Это практический кейс о том, как человек без длинной ручной разработки превращает игровую идею в тестируемый кастомный сценарий. Уникальность материала — не в обещании «AI напишет все за вас», а в разборе реальной итерации: первая выдача оказалась не в том формате, одна точная правка задания изменила результат, а удобная панель настроек стала частью тестирования.

В статье нельзя создавать иллюзию магии. Главная мысль: скорость дает AI, но качество определяют исходная спецификация, правильный контекст, формат результата и проверка переходов состояния.

## SEO и позиционирование

- Рабочий H1: `От идеи до рабочего Dota 2-скрипта: как устроен вайб-кодинг с AI`
- Альтернативный H1: `Как собрать кастомный скрипт для Dota 2 с AI и нормально его проверить`
- SEO title: `Как написать скрипт для Dota 2 с AI: реальный workflow`
- Meta description: `Как написать скрипт для Dota 2 с AI: от описания логики и шаблона до панели настроек и функционального теста.`
- Основной ключ: `как написать скрипт для Dota 2`
- Дополнительные ключи: `кастомный скрипт Dota 2`, `AI для скриптов Dota 2`, `вайб-кодинг Dota 2`, `Melonity V8 API`, `тестирование игрового скрипта`
- Интент: информационный с мягким переходом к продукту.
- Аудитория: игроки Dota 2, которые пользуются готовыми скриптами, интересуются кастомизацией или хотят понять AI-workflow без глубокого погружения в программирование.
- Целевой объем: 1080–1150 слов.

## Уникальный тезис

Рабочий AI-скрипт начинается не с кода, а с описания наблюдаемого поведения. Если заранее зафиксировать три состояния — что происходит до действия, в момент действия и после него, — результат проще сгенерировать, настроить и проверить.

## Обязательная структура и объем блоков

### 1. Вступление: идея на одну фразу — это еще не техническое задание — 80–90 слов

Начать с узнаваемой ситуации: игрок замечает повторяемую микро-операцию и думает, что ее можно превратить в отдельную настраиваемую логику. Сразу пообещать читателю не код, а понятный маршрут от идеи до проверки.

### 2. Что именно показал практический кейс — 90–110 слов

Кратко описать цепочку из видео:

- идея формулируется обычным русским языком;
- к запросу добавляется публичный шаблон как контекст;
- AI создает первую версию;
- формат результата уточняется отдельным сообщением;
- локальный файл появляется в интерфейсе Melonity;
- настройки и поведение проверяются в тестовой игровой среде.

Не перечислять внутренние имена методов и не превращать блок в инструкцию по эксплуатации чита.

### 3. Шаг 1. Описать поведение, а не название функции — 115–125 слов

Объяснить модель `условие → действие → состояние после действия`. На примере из записи допустимо сказать, что автор хотел связать изменение атрибута предмета с применением способности и последующим возвратом состояния. Не давать код и не раскрывать реализацию.

Подчеркнуть, что фраза «сделай полезный скрипт» не проверяема, а формулировка с начальным состоянием, триггером, итоговым состоянием и задержкой уже дает критерии приемки.

### 4. Шаг 2. Дать AI правильный контекст — 105–115 слов

Показать роль официального или публичного шаблона: он задает ожидаемую структуру проекта и снижает число выдуманных решений. В видео использовался публичный template custom scripts. Нельзя называть любой случайный архив «безопасным» или советовать брать неизвестные сборки.

Сделать важное различие: шаблон — это технический контекст, а не готовый ответ. AI все равно должен получить ясное описание поведения.

### 5. Шаг 3. Зафиксировать контракт результата — 115–125 слов

Это главный уникальный фрагмент статьи. В первой итерации AI подготовил архив и TypeScript-структуру, тогда как практически требовался самостоятельный `.js`-файл. Короткое уточнение исправило формат.

Вывести урок: в запросе заранее нужно указать тип результата, количество файлов, наличие панели настроек и то, что именно должно быть готово к проверке. Не показывать исходный код с видео; на скриншоте имя файла можно оставить, а код нужно обрезать или размыть.

### 6. Шаг 4. Панель настроек — это часть качества, а не декор — 125–135 слов

Описать видимые настройки высокого уровня: включение функции, состояние до действия, состояние после действия, задержка возврата и область применения к предметам. Объяснить, почему UI превращает скрытую логику в проверяемый инструмент: параметры можно менять без редактирования файла, а разные сценарии — воспроизводить.

После первого содержательного абзаца этого раздела органично поставить ссылку с точным анкором [читы дота 2](https://melonity.gg/). Контекст ссылки: экосистема с поддержкой кастомных скриптов и настраиваемых сценариев, а не утверждение о безопасности.

### 7. Шаг 5. Проверять переходы состояний, а не факт загрузки — 135–150 слов

Дать практический чек-лист функциональной проверки:

- исходное состояние соответствует настройке;
- нужное действие вызывает ожидаемый переход;
- возврат происходит с заданной задержкой;
- повторный запуск дает тот же результат;
- включение и отключение области применения действительно меняет поведение;
- изменение параметра в UI отражается в следующем тесте.

Прямо сказать: успешная загрузка файла — лишь нулевая проверка. Тестирование в демо или контролируемом лобби подтверждает функцию, но не дает гарантий относительно античита, VAC Live или риска для аккаунта.

### 8. Три ошибки, из-за которых AI-workflow разваливается — 85–95 слов

Разобрать три ошибки:

1. Слишком общая идея без наблюдаемого результата.
2. Не указан формат выдачи — AI выбирает удобную ему структуру.
3. Проверяется один удачный эпизод, а не повторяемость и граничные состояния.

### 9. Вывод — 55–65 слов

Закончить мыслью, что AI сокращает путь до прототипа, но не заменяет спецификацию и тестирование. Здесь разместить вторую ссылку с брендовым анкором [Melonity](https://melonity.gg/) как платформу, в которой кастомная логика получает понятный пользовательский интерфейс и среду для функциональной проверки.

### 10. FAQ — 140–160 слов

Дать короткие ответы на 5 вопросов:

- Нужно ли знать JavaScript, чтобы сформулировать идею скрипта?
- Зачем прикладывать шаблон, если AI уже умеет писать код?
- Почему важно сразу указать формат `.js`?
- Что проверять после появления скрипта в меню?
- Доказывает ли тест в демо безопасность для основного аккаунта?

В последнем ответе не запугивать, но четко разделить функциональную работоспособность и античит-риск.

## Видеофакты и скриншоты

Использовать не более четырех скриншотов. Каждый должен подтверждать отдельный этап, а не повторять соседний кадр.

`[SCREENSHOT_SLOT 1 — 02:10–02:25 — исходное описание поведения и прикрепленный публичный шаблон — обрезать персональные вкладки и нерелевантные инструкции]`

`[SCREENSHOT_SLOT 2 — 03:38 — готовый самостоятельный JS-файл — оставить имя/факт выдачи, код обрезать или размыть]`

`[SCREENSHOT_SLOT 3 — 03:50 — вкладка PT ABUSE с переключателем, состояниями и задержкой — сохранить читаемыми только пользовательские настройки]`

`[SCREENSHOT_SLOT 4 — 04:05–04:45 — функциональная проверка в контролируемой среде — подпись должна объяснять, какое изменение состояния проверяется]`

Подходящие локальные кадры для редактора:

- `C:\Users\User\Desktop\articles\output\video_analysis\frame-130.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-222.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-230.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-245.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-280.png`

## Generated visual 1 — обложка

- Модель: Nano Banana Pro / `gemini-3-pro-image`
- Размер: 2K, 16:9
- Роль: editorial cover, которая передает путь от сырой идеи к проверяемому модулю без буквальной игровой сцены.
- References: none. Не использовать видеокадры как style reference; фактические кадры идут отдельно как скриншоты.
- Финальный prompt:

```text
Create an article-editorial-poster-v1 cover for a Russian editorial feature about turning a rough Dota 2 automation idea into a testable custom script with AI. Thesis: speed comes from AI, reliability comes from a clear behavior specification and an iteration loop. Metaphor: one translucent frosted-acrylic logic cartridge travels through a compact industrial assembly rail and emerges calibrated; the rail has three visually distinct but unlabeled stations suggesting idea, configuration, and test. Format 16:9, 2K, art-first editorial composition. One dominant hero object: the logic cartridge, large and slightly right of center. Keep the upper-left quadrant calm and empty as a safe zone for later headline placement, but render no text. Environment: clean studio tabletop with dense off-white paper backdrop, powder-coated charcoal rail, small muted-coral calibration elements, translucent amber timing dial. Camera: three-quarter isometric view, 50 mm editorial product lens, restrained depth of field, no dramatic wide angle. Materials must feel tactile and physically plausible: frosted acrylic, translucent cast plastic, powder-coated metal, dense paper. Palette: editorial lavender, off-white, muted coral, translucent amber, charcoal. Soft directional key light from upper left, gentle contact shadows, subtle internal refraction, no neon glow. Typography mode: no lettering, no numbers, no logos, no UI text, no pseudo-text. References: none. Physical plausibility: every component must be supported by the rail, shadows must match the light direction, translucent parts must refract consistently, no floating decorative pieces. Constraints: no Dota heroes, no game logo, no copied map, no computer screen, no code, no HUD, no cyberpunk city, no hacker cliché, no padlock, no shield, no weapon, no clutter, no tiny interface labels. Priority order: 1) instantly readable idea-to-tested-module metaphor, 2) one clear hero and generous negative space, 3) tactile materials and Dota-adjacent lavender/coral palette, 4) restrained premium editorial finish. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

- Самооценка по visual guide: 94/100 — есть тезис, единая метафора, один герой, иерархия, safe zone, материалы, свет, физика, запреты, приоритеты, модель и размер. Проходит порог 80/100.

## Generated visual 2 — inline illustration после раздела о тестировании

- Модель: Nano Banana Pro / `gemini-3-pro-image`
- Размер: 2K, 3:2
- Роль: объяснить цикл проверки переходов состояния без кода и интерфейсного скриншота.
- References: none.
- Финальный prompt:

```text
Create an article-editorial-poster-v1 inline illustration for a Russian article about functional testing of a custom Dota 2 script. Thesis: a file loading successfully is not enough; quality is proven by repeatable before-action-after state transitions. Metaphor: one compact mechanical state-transition cassette with two translucent chambers and a central timing dial; a single lavender token passes from the first chamber through the dial into the second and returns along a clearly visible looped channel. Format 3:2, 2K, art-first educational editorial image. Composition: the cassette is the only hero, centered slightly low, with clear breathing room around it and an uncluttered upper band. Environment: off-white dense-paper studio surface, minimal charcoal mounting plate. Camera: near-orthographic three-quarter product view, 55 mm lens, crisp structure, restrained depth of field. Materials: frosted acrylic chambers, translucent cast-plastic channel, powder-coated metal base, muted-coral mechanical stops, translucent amber dial. Palette: editorial lavender, off-white, muted coral, translucent amber, charcoal. Lighting: soft top-left studio light, readable contact shadows, subtle refraction inside the chambers, no emissive neon. Typography mode: no text, no letters, no numbers, no logos, no UI labels, no pseudo-text. References: none. Physical plausibility: the token sits inside the channel, the channel connects both chambers, the dial is mechanically mounted, all shadows are consistent, nothing floats. Constraints: no game characters, no logos, no source code, no HUD, no keyboard, no hacker imagery, no shield or padlock, no copied game item, no clutter, no arrows made from text. Priority order: 1) readable repeatable transition loop, 2) single tactile hero object, 3) clean editorial hierarchy, 4) restrained Dota-adjacent palette. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 3:2.
```

- Самооценка по visual guide: 93/100 — метафора объясняет тезис, композиция компактна, все материалы и физические связи заданы, запрещены логотипы, код и псевдотекст. Проходит порог 80/100.

## Критерии приемки статьи №1

- Объем 1000–1200 слов.
- Точное словосочетание `как написать скрипт для Dota 2` естественно встречается в H1 или первом абзаце и еще 1–2 раза в тексте без переспама.
- Ровно две ссылки на https://melonity.gg/: одна с анкором `читы дота 2`, одна брендовая.
- Ссылки разделены минимум двумя смысловыми блоками.
- Есть реальный урок о несовпадении первого формата выдачи и требуемого `.js`.
- Есть модель `до → действие → после` и чек-лист повторяемой проверки.
- Нет кода, внутренних методов, обхода античита и гарантий безопасности.
- Есть SEO front matter, description до 160 символов, image placement notes и FAQ.
- Все скриншоты подписаны по функции; код и нерелевантные инструкции не читаются.
- Оба generated-image prompt используются без упрощения контракта и остаются назначенными на Nano Banana Pro / `gemini-3-pro-image`.

---

# ТЗ №2. Пять блоков сильного AI-промпта для кастомной Dota 2-логики

## Концепция

Вторая статья не повторяет маршрут первой. Это разбор «поведенческого контракта» — структуры задания, по которой AI может создать не просто кодоподобный ответ, а понятный, настраиваемый и проверяемый прототип. Практический кейс из видео используется как доказательство каждого элемента: цель, триггер, действие, пользовательские настройки, формат выдачи и тест.

Уникальная информация — связь между качеством промпта и качеством будущего интерфейса. Если в задании нет режимов, задержки, возврата и области действия, AI может сгенерировать логику, которую трудно проверить и неудобно настраивать.

## SEO и позиционирование

- Рабочий H1: `Пять блоков сильного промпта для кастомного Dota 2-скрипта`
- Альтернативный H1: `Как составить ТЗ для AI, чтобы Dota 2-скрипт можно было проверить`
- SEO title: `Промпт для Dota 2-скрипта: 5 блоков хорошего ТЗ`
- Meta description: `Промпт для Dota 2-скрипта: как описать цель, триггер, настройки, формат результата и тест без лишней технической воды.`
- Основной ключ: `промпт для Dota 2-скрипта`
- Дополнительные ключи: `ТЗ на скрипт Dota 2`, `AI scripting Dota 2`, `кастомные скрипты Melonity`, `поведенческий контракт`, `как проверить скрипт Dota 2`
- Интент: образовательный/problem-solving с нативным product discovery.
- Аудитория: игроки, которые уже пробовали просить AI «написать скрипт», но получали неудобный формат, неполную логику или результат без нормальных настроек.
- Целевой объем: 1050–1130 слов.

## Уникальный тезис

Хороший промпт описывает не внутреннюю реализацию, а наблюдаемый контракт: какую проблему решаем, что запускает логику, как меняется состояние, что пользователь может настроить и по каким признакам результат считается рабочим.

## Обязательная структура и объем блоков

### 1. Вступление: почему «напиши скрипт» почти всегда слабый запрос — 75–85 слов

Начать с проблемы: AI легко создает убедительно выглядящий ответ, но «похож на код» и «готов к использованию» — разные состояния. Пообещать читателю универсальный каркас задания из пяти блоков.

### 2. Поведенческий контракт вместо технической магии — 75–85 слов

Коротко ввести понятие: автор задания фиксирует то, что можно увидеть и проверить, а не придумывает внутренние методы. Это особенно полезно человеку без глубокого знания API: он остается владельцем продукта и критериев приемки, даже если реализацию предлагает AI.

### 3. Блок 1. Цель и границы — 85–95 слов

Ответить на вопросы:

- какую повторяемую ручную операцию нужно упростить;
- в каких ситуациях функция должна работать;
- в каких ситуациях она не должна вмешиваться;
- что не входит в задачу.

На примере записи цель связана с контролируемым переключением состояния предмета вокруг применения способности. Не раскрывать код или конкретный способ перехвата игровых событий.

### 4. Блок 2. Триггер и переходы состояния — 95–105 слов

Предложить шаблон формулировки: `до события → событие → временное состояние → состояние после → задержка/условие возврата`. Объяснить, что такая последовательность одновременно помогает генерации и превращается в будущий тест-кейс.

Здесь ценность не в названии события API, а в наблюдаемом результате. Запретить автору статьи вставлять выдуманные функции и методы.

### 5. Блок 3. Настройки, которыми действительно будут пользоваться — 95–105 слов

Разделить настройки на четыре типа:

- главный переключатель;
- выбор состояния до и после действия;
- временной параметр;
- область применения или исключения.

Связать это с видимой в видео вкладкой настроек. Объяснить: каждая настройка должна соответствовать отдельному проверяемому сценарию, иначе это декоративный контрол.

После основной полезной мысли поставить точный анкор [читы для dota 2](https://melonity.gg/) в предложении об экосистеме, где кастомные скрипты могут быть оформлены как управляемые пользовательские модули. Не делать ссылку оценкой «лучший/самый безопасный».

### 6. Блок 4. Контекст и формат результата — 105–115 слов

Разобрать два независимых требования:

1. Контекст: публичный шаблон или документация платформы задают структуру и ограничения.
2. Формат: один самостоятельный `.js`, архив проекта или другой заранее названный deliverable.

Использовать видео как мини-кейс: первая версия пришла архивом с TypeScript-структурой, после уточнения AI выдал самостоятельный JS-файл. Вывести практический принцип: формат приемки нужно писать до генерации, а не угадывать после.

### 7. Блок 5. Тест до того, как написан первый файл — 115–130 слов

Научить формулировать критерии заранее:

- файл появляется в ожидаемом разделе;
- включение и отключение функции меняет поведение;
- каждое состояние воспроизводится отдельно;
- задержка заметно влияет на результат;
- область применения соблюдается;
- повторный тест дает тот же исход;
- нештатное состояние не оставляет функцию в непредсказуемом режиме.

Добавить границу: это функциональная приемка. Она не проверяет и не доказывает обход VAC/VAC Live, «невидимость» или безопасность аккаунта.

### 8. Мини-шаблон промпта без кода — 110–120 слов

Дать заполняемую структуру, но не готовую реализацию:

```text
Цель: [какую повторяемую операцию упрощаем].
Работает только когда: [наблюдаемые условия].
До действия: [исходное состояние].
Триггер: [действие пользователя или игровое событие обычными словами].
После действия: [ожидаемое состояние и правило возврата].
Настройки в интерфейсе: [переключатель, варианты, задержка, область применения].
Контекст: [официальный/публичный шаблон или документация].
Результат: [один конкретный формат файла/проекта].
Приемка: [5–7 наблюдаемых тестов].
Ограничения: без инструкций по обходу античита, скрытию или эксплуатации уязвимостей.
```

После шаблона пояснить, что квадратные скобки нужно заполнять своими условиями; нельзя выдавать этот каркас за готовый скрипт.

### 9. Четыре красных флага слабого задания — 80–90 слов

Короткий список:

- оценочные слова вместо результата: «умный», «идеальный», «безопасный»;
- не указан формат;
- много настроек без сценариев проверки;
- требование «чтобы не банило» вместо функционального критерия.

### 10. Вывод — 45–55 слов

Сформулировать, что хороший запрос одновременно является кратким product brief и планом QA. Здесь поставить вторую, брендовую ссылку на [официальную платформу Melonity](https://melonity.gg/) как контекст для кастомной экосистемы, не повторяя точный анкор.

### 11. FAQ — 135–150 слов

Ответить на 5 вопросов:

- Нужно ли указывать конкретные методы API в промпте?
- Чем триггер отличается от условия работы?
- Сколько настроек достаточно для первого прототипа?
- Почему AI иногда выдает архив вместо одного файла?
- Можно ли считать один удачный тест доказательством готовности?

## Видеофакты и скриншоты

Этой статье нужны другие акценты кадров, даже если исходное видео то же:

`[SCREENSHOT_SLOT 1 — 02:10–02:25 — текст исходной идеи — выделить цель, условие и требование отдельной вкладки; скрыть нерелевантные инструкции]`

`[SCREENSHOT_SLOT 2 — 02:35–03:00 — первая выдача архивом/TypeScript и последующее уточнение про самостоятельный JS — показать контраст форматов без читаемого кода]`

`[SCREENSHOT_SLOT 3 — 03:50 — итоговая панель настроек — подписью сопоставить каждый контрол с отдельным тестом]`

`[SCREENSHOT_SLOT 4 — 04:20–04:45 — повторная игровая проверка — показать, что приемка оценивает переход и возврат, а не только загрузку]`

Подходящие локальные кадры для редактора:

- `C:\Users\User\Desktop\articles\output\video_analysis\frame-125.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-140.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-170.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-222.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-230.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-260.png`
- `C:\Users\User\Desktop\articles\output\video_analysis\frame-280.png`

## Generated visual 1 — обложка

- Модель: Nano Banana Pro / `gemini-3-pro-image`
- Размер: 2K, 16:9
- Роль: визуализировать сильное ТЗ как физический калибратор будущей логики.
- References: none. Видеокадры не использовать как художественный референс.
- Финальный prompt:

```text
Create an article-editorial-poster-v1 cover for a Russian editorial guide about writing a strong AI specification for a custom Dota 2 script. Thesis: a good prompt is a behavior contract that makes the result configurable and testable. Metaphor: one large translucent lavender specification card is locked into a precision industrial calibration jig with five physical gates, suggesting goal, trigger, transition, settings, and test without using icons or text. Format 16:9, 2K, art-first editorial composition. One dominant hero: the specification card and its connected jig read as a single object, positioned left-center; preserve a calm empty safe zone on the upper right for later editorial headline placement, but generate no text. Environment: clean off-white dense-paper studio backdrop with a charcoal powder-coated base. Camera: elevated three-quarter product view, 50 mm lens, subtle depth of field, no wide-angle distortion. Materials: frosted acrylic card, translucent cast-plastic gates, powder-coated charcoal metal, muted-coral stops, one translucent amber timing component. Palette: editorial lavender, off-white, muted coral, translucent amber, charcoal. Lighting: soft directional key from upper left, controlled contact shadows, gentle subsurface refraction, no neon glow. Typography mode: no letters, no numbers, no logos, no UI copy, no pseudo-text. References: none. Physical plausibility: every gate is mounted to the base, the card passes through aligned slots, fasteners and shadows are consistent, no unsupported or floating parts. Constraints: no Dota heroes, no game logo, no map, no source code, no chatbot screen, no keyboard, no HUD, no cyberpunk, no hacker cliché, no padlock or shield, no decorative data streams, no clutter. Priority order: 1) instantly readable specification-as-calibration metaphor, 2) one hero with five subordinate gates and strong negative space, 3) tactile editorial materials, 4) restrained Dota-adjacent color system. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
```

- Самооценка по visual guide: 95/100 — одна метафора и один герой, пять элементов подчинены иерархии, предусмотрен safe zone, заданы физика, запреты, модель и размер. Проходит порог 80/100.

## Generated visual 2 — inline illustration после мини-шаблона

- Модель: Nano Banana Pro / `gemini-3-pro-image`
- Размер: 2K, 3:2
- Роль: показать, как пять блоков задания сходятся в один проверяемый результат.
- References: none.
- Финальный prompt:

```text
Create an article-editorial-poster-v1 inline illustration for a Russian guide about the five blocks of an AI behavior specification. Thesis: separate requirements become useful only when they converge into one testable contract. Metaphor: one central frosted-acrylic logic capsule held in a circular precision jig; five short material channels feed into the capsule from evenly spaced mounted modules, while one clean output rail leaves the capsule toward a small calibration stop. Format 3:2, 2K, art-first educational editorial composition. One dominant hero: the central logic capsule, with five clearly subordinate feeders and one output rail. Keep the background calm and avoid infographic clutter. Environment: off-white dense-paper studio plane on a charcoal powder-coated frame. Camera: near-orthographic top-three-quarter view, 55 mm lens, crisp geometry, restrained depth of field. Materials: frosted acrylic capsule, translucent cast-plastic channels, powder-coated metal jig, muted-coral adjustment tabs, translucent amber output stop. Palette: editorial lavender, off-white, muted coral, translucent amber, charcoal. Lighting: soft upper-left studio key, gentle contact shadows and internally consistent refraction, no emissive effects. Typography mode: no text, no letters, no numbers, no logos, no icons, no pseudo-text. References: none. Physical plausibility: all five channels connect to the capsule, every module is fixed to the jig, the output rail is supported, shadow direction is consistent, nothing floats. Constraints: no game characters, no Dota logo, no source code, no UI panels, no copied game objects, no brain imagery, no robot, no hacker aesthetic, no padlock, no shield, no neon, no clutter. Priority order: 1) readable five-inputs-to-one-testable-output structure, 2) central hero dominance, 3) tactile physical plausibility, 4) restrained premium editorial finish. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 3:2.
```

- Самооценка по visual guide: 94/100 — точное соответствие тезису, минимальная иерархия, единый герой, физически связанные элементы, строгие запреты и полный технический контракт. Проходит порог 80/100.

## Критерии приемки статьи №2

- Объем 1000–1200 слов.
- Статья не превращается в повтор первой: минимум 60% текста посвящено структуре промпта, критериям приемки и ошибкам постановки задачи.
- Ровно две ссылки на https://melonity.gg/: одна с анкором `читы для dota 2`, одна брендовая.
- Точный анкор появляется один раз и только после полезного объяснения настроек.
- Есть пять обязательных блоков: цель/границы, триггер/состояния, настройки, контекст/формат, тест.
- Есть заполняемый мини-шаблон без кода и без методов API.
- Пример несовпадения TypeScript-архива и требуемого JS-файла передан как урок о контракте результата.
- Нет инструкций по обходу античита, эксплуатации уязвимостей или сокрытию поведения.
- Нет обещаний безопасности, undetected-статуса и гарантий от VAC/VAC Live.
- Есть SEO front matter, description до 160 символов, image placement notes и FAQ.
- Оба generated-image prompt используются целиком, с Nano Banana Pro / `gemini-3-pro-image`, заданным размером и оценкой выше 80/100.

## Финальная проверка серии перед публикацией

Редактор должен проверить обе статьи вместе:

- H1, вступления, структура и FAQ не дублируют друг друга.
- Первая статья отвечает на вопрос «как выглядит полный workflow», вторая — «как написать проверяемое задание для AI».
- Анкоры распределены строго: `читы дота 2` только в статье №1, `читы для dota 2` только в статье №2.
- В каждой статье две ссылки, но только одна exact-match.
- Melonity интегрирован через реальную ценность кастомной экосистемы, V8 scripting/API positioning и пользовательские настройки, а не через неподтвержденные сравнительные заявления.
- Видеокадры подтверждают описанные шаги; код и нерелевантные системные инструкции не раскрываются.
- Иллюстрации не имитируют интерфейс Dota 2 и не конкурируют с фактическими скриншотами.
- В тексте нет внутренних названий файлов источников, графа памяти или редакционного пайплайна.
