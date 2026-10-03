---
title: "Промпт для Dota 2-скрипта: 5 блоков хорошего ТЗ"
description: "Промпт для Dota 2-скрипта: как описать цель, триггер, настройки, формат результата и тест без лишней технической воды."
primary_keyword: "промпт для Dota 2-скрипта"
game: "Dota 2"
language: "ru"
word_count_target: "1000-1200"
image_model: "Nano Banana Pro / gemini-3-pro-image"
---

# Промпт для Dota 2-скрипта: 5 блоков хорошего ТЗ

Запрос «напиши скрипт» звучит понятно только человеку, который уже держит всю идею в голове. Для AI в нем нет ни границ, ни формата, ни критериев готовности. Поэтому модель легко создает ответ, похожий на серьезную разработку, но неудобный для реального теста. Сильный промпт для Dota 2-скрипта работает иначе: он фиксирует пять блоков наблюдаемого поведения и заранее превращает будущий результат в набор проверяемых сценариев.

> **Коротко:** хорошее ТЗ описывает цель и границы, триггер и переходы состояний, полезные настройки, контекст и формат выдачи, а также функциональную приемку.

<!-- IMAGE_SLOT_01
Placement: after the quick answer block
Type: generated image
Purpose: визуализировать сильное ТЗ как физический калибратор будущей логики
Suggested file name: dota-2-ai-prompt-specification-cover-16x9-v01.webp
Alt text: Прозрачная карта спецификации проходит пять калибровочных ворот в промышленном стенде
Caption: Сильный промпт заранее связывает цель, триггер, переход, настройки и тест.
If generated, Nano Banana prompt:
Create an article-editorial-poster-v1 cover for a Russian editorial guide about writing a strong AI specification for a custom Dota 2 script. Thesis: a good prompt is a behavior contract that makes the result configurable and testable. Metaphor: one large translucent lavender specification card is locked into a precision industrial calibration jig with five physical gates, suggesting goal, trigger, transition, settings, and test without using icons or text. Format 16:9, 2K, art-first editorial composition. One dominant hero: the specification card and its connected jig read as a single object, positioned left-center; preserve a calm empty safe zone on the upper right for later editorial headline placement, but generate no text. Environment: clean off-white dense-paper studio backdrop with a charcoal powder-coated base. Camera: elevated three-quarter product view, 50 mm lens, subtle depth of field, no wide-angle distortion. Materials: frosted acrylic card, translucent cast-plastic gates, powder-coated charcoal metal, muted-coral stops, one translucent amber timing component. Palette: editorial lavender, off-white, muted coral, translucent amber, charcoal. Lighting: soft directional key from upper left, controlled contact shadows, gentle subsurface refraction, no neon glow. Typography mode: no letters, no numbers, no logos, no UI copy, no pseudo-text. References: none. Physical plausibility: every gate is mounted to the base, the card passes through aligned slots, fasteners and shadows are consistent, no unsupported or floating parts. Constraints: no Dota heroes, no game logo, no map, no source code, no chatbot screen, no keyboard, no HUD, no cyberpunk, no hacker cliché, no padlock or shield, no decorative data streams, no clutter. Priority order: 1) instantly readable specification-as-calibration metaphor, 2) one hero with five subordinate gates and strong negative space, 3) tactile editorial materials, 4) restrained Dota-adjacent color system. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 16:9.
Model: Nano Banana Pro / gemini-3-pro-image
Aspect ratio and size: 16:9, 2K
Typography mode: art-first
Reference roles: none; no references attached
Visual style version: article-editorial-poster-v1
Prompt QA score: 95/100
-->

## Поведенческий контракт вместо технической магии

Поведенческий контракт описывает то, что можно увидеть: когда логика должна работать, что запускает переход, какое состояние ожидается и как понять, что результат готов. Он не требует от автора выдумывать внутренние методы API. Это особенно полезно без глубокого опыта разработки: реализацию предлагает AI, а человек остается владельцем продукта, пользовательского опыта и критериев приемки.

Контракт одновременно выполняет две роли. Для модели это точное задание. Для редактора или тестировщика — будущий план проверки. Если фразу нельзя превратить в тест, ее стоит уточнить до генерации.

Еще один плюс такого подхода — удобные итерации. Когда результат не совпал с ожиданием, можно исправить конкретный блок контракта, а не переписывать весь запрос и надеяться на другой случайный ответ.

<!-- SCREENSHOT_SLOT_02
Placement: after "## Поведенческий контракт вместо технической магии"
Type: real screenshot
Purpose: показать исходную идею, пользовательские условия и прикрепленный публичный шаблон без нерелевантных инструкций
Suggested file name: dota-2-ai-prompt-initial-brief-01.webp
Alt text: Исходный запрос описывает игровое поведение и отдельную вкладку настроек рядом с шаблоном
Caption: Даже живой запрос полезно разложить на цель, условия, настройки, формат и тест.
Source file: C:\Users\User\Desktop\articles\output\video_analysis\frame-140.png
Crop/redaction: выделить нижнее поле запроса и карточку template-custom-scripts; скрыть верхний persona-текст, вкладки, имя пространства и персональные элементы
-->

## Блок 1. Цель и границы

Начните не с названия функции, а с повторяемой ручной операции, которую хотите упростить. Затем ответьте на четыре вопроса:

- в какой ситуации логика нужна;
- когда она не должна вмешиваться;
- какой результат увидит пользователь;
- что точно не входит в задачу.

В практическом кейсе цель связана с контролируемым переключением состояния предмета вокруг применения способности. Этого достаточно для продуктового описания. Способ перехвата событий и внутреннюю реализацию придумывать не нужно: такие детали без подтвержденной документации только делают запрос хрупким.

Границы лучше формулировать симметрично: «работает при таких условиях» и «не вмешивается при таких». Вторая половина часто важнее первой, потому что защищает прототип от слишком широкого поведения и дает отдельный негативный тест.

## Блок 2. Триггер и переходы состояния

Триггер — это наблюдаемое действие или событие, после которого поведение меняется. Удобный каркас выглядит так: `до события → событие → временное состояние → состояние после → задержка или условие возврата`.

Эта последовательность полезнее названия предполагаемого метода API. Она объясняет AI логику и сразу превращается в тест-кейс. Например, можно проверить исходное состояние, выполнить действие, увидеть переход, дождаться возврата и повторить цикл. Если какой-то этап невозможно наблюдать, нужно уточнить ожидание, а не добавлять в промпт выдуманную техническую функцию.

Для каждого перехода полезно указать одно ожидаемое исключение: прерванное действие, изменившееся условие или повторный триггер. Не нужно описывать десятки краев — достаточно показать модели, что состояние обязано возвращаться предсказуемо.

## Блок 3. Настройки, которыми будут пользоваться

Для первого прототипа обычно достаточно четырех типов контроля:

- главный переключатель;
- выбор состояния до и после действия;
- один временной параметр;
- область применения или исключения.

Каждая настройка обязана соответствовать отдельному сценарию проверки. Если переключатель ничего заметно не меняет, это декоративный UI. Если задержку нельзя сравнить в двух прогонах, критерий сформулирован слабо. Такой принцип хорошо ложится на экосистему, где [читы для dota 2](https://melonity.gg/) могут оформлять кастомную логику как управляемый пользовательский модуль. Это описание интерфейсной ценности, а не заявление о безопасности продукта.

Названия контролов тоже должны отражать пользовательский выбор, а не внутреннюю терминологию. Человек должен понимать эффект до запуска теста. Если подпись требует длинного объяснения, возможно, настройка объединяет несколько решений и ее стоит разделить.

<!-- SCREENSHOT_SLOT_03
Placement: after "## Блок 3. Настройки, которыми будут пользоваться"
Type: product UI
Purpose: сопоставить четыре типа настроек с отдельными тест-сценариями
Suggested file name: dota-2-script-settings-as-tests-02.webp
Alt text: Панель пользовательского модуля с переключателем, состояниями, задержкой и областью применения
Caption: Каждый контрол должен менять наблюдаемое поведение и иметь собственную проверку.
Source file: C:\Users\User\Desktop\articles\output\video_analysis\frame-230.png
Crop/redaction: сохранить вкладку PT ABUSE и пользовательские настройки; убрать идентификатор аккаунта, отладочные элементы и лишний игровой фон
-->

## Блок 4. Контекст и формат результата

Контекст и deliverable — разные требования. Публичный шаблон или документация платформы задают структуру и ограничения. Формат результата отвечает на другой вопрос: что именно должен вернуть AI — один самостоятельный `.js`, архив проекта или иной заранее названный комплект.

Видео показывает цену этой разницы. Первая версия пришла архивом с TypeScript-структурой. После короткого уточнения модель подготовила самостоятельный JS-файл. Вывод простой: формат приемки нужно писать до генерации. Укажите расширение, количество файлов, необходимость отдельной панели параметров и состояние, в котором результат считается готовым к функциональному тесту.

Полезно также явно назвать, чего в выдаче быть не должно: дополнительных архивов, демонстрационного кода или неподтвержденных зависимостей. Это не микроменеджмент, а защита следующего шага от лишней ручной разборки.

<!-- SCREENSHOT_SLOT_04
Placement: after "## Блок 4. Контекст и формат результата"
Type: real screenshot
Purpose: показать, как одно уточнение меняет контракт поставки с архива на самостоятельный JS-файл
Suggested file name: dota-2-ai-prompt-format-correction-03.webp
Alt text: Карточка архива рядом с уточнением о необходимости одного самостоятельного JS-файла
Caption: Формат результата — отдельный блок ТЗ, а не мелкая деталь в конце.
Source file: C:\Users\User\Desktop\articles\output\video_analysis\frame-170.png
Crop/redaction: оставить карточку архива и фразу о формате .js; скрыть вкладки, имя пространства и любой исходный код
-->

## Блок 5. Тест до первого файла

Критерии приемки пишутся вместе с промптом, а не после первого удачного запуска. Для базового прототипа проверьте:

- файл появляется в ожидаемом разделе;
- включение и отключение функции меняет поведение;
- состояния до и после воспроизводятся отдельно;
- изменение задержки заметно влияет на возврат;
- область применения соблюдается;
- несколько повторов дают один и тот же исход;
- нештатное состояние не оставляет логику в непредсказуемом режиме.

Это функциональная приемка. Она отвечает на вопрос «работает ли сценарий так, как описано», но не проверяет VAC или VAC Live, не доказывает незаметность и не дает гарантий для аккаунта. Смешивать эти вопросы в одном критерии — плохой QA.

Порядок прогонов тоже важен: сначала базовое состояние, затем изменение одного параметра и только потом граничный сценарий. Если менять все сразу, невозможно понять, какая настройка дала новый результат.

## Мини-шаблон промпта без кода

Ниже не готовый скрипт, а заполняемый каркас задания:

```text
Цель: [какую повторяемую операцию упрощаем].
Работает только когда: [наблюдаемые условия].
До действия: [исходное состояние].
Триггер: [действие пользователя или игровое событие обычными словами].
После действия: [ожидаемое состояние и правило возврата].
Настройки в интерфейсе: [переключатель, варианты, задержка, область применения].
Контекст: [официальный или публичный шаблон либо документация].
Результат: [один конкретный формат файла или проекта].
Приемка: [пять-семь наблюдаемых тестов].
Ограничения: без инструкций по обходу античита, скрытию или эксплуатации уязвимостей.
```

Заполните квадратные скобки своими условиями. Не выдавайте этот шаблон за реализацию: его задача — убрать двусмысленность до того, как AI начнет собирать результат.

<!-- IMAGE_SLOT_05
Placement: after "## Мини-шаблон промпта без кода"
Type: generated image
Purpose: показать, как пять блоков задания сходятся в один проверяемый результат
Suggested file name: dota-2-ai-prompt-five-blocks-inline-3x2-v01.webp
Alt text: Пять физических каналов сходятся в одну прозрачную капсулу проверяемого контракта
Caption: Раздельные требования полезны, когда собираются в один наблюдаемый контракт.
Internal-link suggestions: «Полный AI-workflow: от идеи до функционального теста»; «Как проверить переходы состояний кастомного скрипта»; «Что должен содержать интерфейс первого прототипа».
If generated, Nano Banana prompt:
Create an article-editorial-poster-v1 inline illustration for a Russian guide about the five blocks of an AI behavior specification. Thesis: separate requirements become useful only when they converge into one testable contract. Metaphor: one central frosted-acrylic logic capsule held in a circular precision jig; five short material channels feed into the capsule from evenly spaced mounted modules, while one clean output rail leaves the capsule toward a small calibration stop. Format 3:2, 2K, art-first educational editorial composition. One dominant hero: the central logic capsule, with five clearly subordinate feeders and one output rail. Keep the background calm and avoid infographic clutter. Environment: off-white dense-paper studio plane on a charcoal powder-coated frame. Camera: near-orthographic top-three-quarter view, 55 mm lens, crisp geometry, restrained depth of field. Materials: frosted acrylic capsule, translucent cast-plastic channels, powder-coated metal jig, muted-coral adjustment tabs, translucent amber output stop. Palette: editorial lavender, off-white, muted coral, translucent amber, charcoal. Lighting: soft upper-left studio key, gentle contact shadows and internally consistent refraction, no emissive effects. Typography mode: no text, no letters, no numbers, no logos, no icons, no pseudo-text. References: none. Physical plausibility: all five channels connect to the capsule, every module is fixed to the jig, the output rail is supported, shadow direction is consistent, nothing floats. Constraints: no game characters, no Dota logo, no source code, no UI panels, no copied game objects, no brain imagery, no robot, no hacker aesthetic, no padlock, no shield, no neon, no clutter. Priority order: 1) readable five-inputs-to-one-testable-output structure, 2) central hero dominance, 3) tactile physical plausibility, 4) restrained premium editorial finish. Target model: Nano Banana Pro / gemini-3-pro-image. Output: 2K, 3:2.
Model: Nano Banana Pro / gemini-3-pro-image
Aspect ratio and size: 3:2, 2K
Typography mode: art-first
Reference roles: none; no references attached
Visual style version: article-editorial-poster-v1
Prompt QA score: 94/100
-->

## Четыре красных флага слабого задания

1. **Оценки вместо результата:** «умный», «идеальный» и «безопасный» ничего не говорят о поведении.
2. **Не указан формат:** AI выбирает удобную структуру, которая не совпадает с приемкой.
3. **Много настроек без тестов:** контролы выглядят солидно, но не добавляют управляемости.
4. **Требование «чтобы не банило»:** это не функциональный критерий и не проверяется обычным прогоном.

Хорошая правка любого красного флага начинается с вопроса: «Что именно я должен увидеть, чтобы принять результат?»

## Вывод

Сильный запрос — одновременно короткий product brief и план QA. Он оставляет реализацию AI, но жестко фиксирует наблюдаемое поведение и формат поставки. [Официальная платформа Melonity](https://melonity.gg/) дает контекст кастомной экосистемы, где такой контракт можно превратить в настраиваемый модуль и проверить функционально.

## FAQ

### Нужно ли указывать конкретные методы API в промпте?

Нет, если они не взяты из подтвержденной документации. Наблюдаемые условия и результат важнее выдуманного технического названия.

### Чем триггер отличается от условия работы?

Условие определяет, когда логика разрешена. Триггер — конкретное действие или событие, которое запускает переход состояния.

### Сколько настроек достаточно для первого прототипа?

Обычно хватает главного переключателя, состояний до и после, задержки и области применения. Добавляйте новый контрол только вместе с тестом.

### Почему AI иногда выдает архив вместо одного файла?

Если формат не задан, модель выбирает привычную ей структуру проекта. Укажите deliverable явно до генерации.

### Можно ли считать один удачный тест доказательством готовности?

Нет. Нужны повторные прогоны, изменение параметров и проверка граничного состояния. Один успех показывает возможность, но не предсказуемость.
