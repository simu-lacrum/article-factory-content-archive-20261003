# ТЗ на публикацию GitBook

## Цель

Опубликовать один публичный индексируемый GitBook-сайт с четырьмя экспертными T2-статьями, шестью тематическими хабами, полным архивом из 32 Medium-статей и стабильными URL.

## Рекомендуемые настройки сайта

- Site title: `Cluster Cheats Docs`
- Site slug: `cluster-cheats-docs`
- Audience: `Public`
- Search engine indexing: `On`
- Git Sync direction for first import: `GitHub/GitLab → GitBook`
- GitBook project root: папка, содержащая `.gitbook.yaml`, `README.md` и `SUMMARY.md`
- Изображения на этом этапе не загружать: production-промпты хранятся отдельно в исходном Article Factory run.

## Структура

- Главная страница
- English
  - Deadlock
  - Dota 2
  - CS2
- Русский
  - Dota 2
  - Deadlock
  - CS2

## Карта статей и коммерческих анкоров

### Deadlock Auto-Dispel Logic: Why Fast Reactions Still Fail

- GitBook path: `en/deadlock/deadlock-auto-dispel-logic-fast-reactions-fail`
- Description: `Deadlock auto dispel is only useful when timing, threat and item priority agree. Learn why fast defensive reactions still fail.`
- Primary keyword: `Deadlock auto dispel`
- Commercial anchor: `Melonity for Deadlock`
- Target: `https://melonity.gg/en/deadlock`
- Placement H2: `What to inspect before trusting item automation`
- Link count rule: ровно одна коммерческая ссылка в теле статьи.

### Dota 2 Courier Information: The Delivery That Reveals the Next Fight

- GitBook path: `en/dota-2/dota-2-courier-information-next-fight`
- Description: `Dota 2 courier information can reveal an item timing before the fight starts. Learn what matters, what misleads and when to disengage.`
- Primary keyword: `Dota 2 courier information`
- Commercial anchor: `Melonity Dota 2 tools`
- Target: `https://melonity.gg/en`
- Placement H2: `What a useful courier-information feature should show`
- Link count rule: ровно одна коммерческая ссылка в теле статьи.

### Телепорт в Dota 2: как одно перемещение меняет три линии

- GitBook path: `ru/dota-2/teleport-v-dota-2-kak-menyaetsya-karta`
- Description: `Телепорт в Dota 2 меняет давление сразу на нескольких линиях. Разбираем, как читать направление, окно уязвимости и ложные выводы.`
- Primary keyword: `телепорт в Dota 2`
- Commercial anchor: `Melonity для Dota 2`
- Target: `https://melonity.gg/`
- Placement H2: `Каким должен быть полезный Teleport Preview`
- Link count rule: ровно одна коммерческая ссылка в теле статьи.

### Души в Deadlock: как проигрывают линию между добиванием и подтверждением

- GitBook path: `ru/deadlock/dushi-v-deadlock-dobivanie-podtverzhdenie-liniya`
- Description: `Души в Deadlock теряются не только из-за плохого аима. Разбираем цикл добивания, подтверждения, отрицания и давления на линии.`
- Primary keyword: `души в Deadlock`
- Commercial anchor: `Melonity для Deadlock`
- Target: `https://melonity.gg/deadlock`
- Placement H2: `Как должна выглядеть полезная подсветка душ`
- Link count rule: ровно одна коммерческая ссылка в теле статьи.

## Карта ссылочных хабов

- English / Dota 2: 16 Medium-статей и анкор `Dota 2 cheats and scripts from Melonity` → `https://melonity.gg/en`.
- Русский / Dota 2: 2 Medium-статьи и анкор `читы для Dota 2 от Melonity` → `https://melonity.gg/`.
- English / Deadlock: 4 Medium-статьи, Melonity EN, Cluster EN product и безанкорный Cluster EN hub.
- Русский / Deadlock: 2 Medium-статьи, Melonity RU, Cluster RU product и безанкорный Cluster RU hub.
- English / CS2: 6 Medium-статей, анкор `Cluster CS2 product page` и безанкорный Cluster EN hub.
- Русский / CS2: 2 Medium-статьи, анкор `читы для CS2 от Cluster` и безанкорный Cluster RU hub.
- Каждая из 32 Medium-статей размещается ровно в одном тематическом хабе; обе страницы профиля Medium размещаются на главной.
- Безанкорные URL окружены тематическими словами cheats / читы / читы КС2 / читы Deadlock.

## Порядок публикации

1. Авторизоваться в GitBook и создать Space.
2. Подключить Git Sync к репозиторию или импортировать папку с Markdown-файлами.
3. Для первичного sync выбрать направление из Git в GitBook.
4. Проверить, что GitBook прочитал `SUMMARY.md` и создал иерархию без дубликатов.
5. В Page options сверить description каждой статьи; лимит GitBook — 200 символов.
6. Закрепить точные slug из карты URL. Не переименовывать страницы после индексации без redirect.
7. Создать Docs site, выбрать Public и включить индексацию поисковиками.
8. Нажать Publish, открыть каждую публичную страницу и проверить H1, FAQ и коммерческий анкор.
9. Проверить `sitemap-pages.xml` на публичном домене.
10. Сохранить фактические публичные URL в `URL_MAP.md` вместо шаблонного base URL.

## Финальный QA

- В навигации 13 страниц: главная, 2 языковых индекса, 6 игровых индексов и 4 статьи.
- Все внутренние ссылки относительные и открываются без 404.
- В каждой статье один H1, девять H2 и FAQ последним H2.
- В каждой статье ровно одна внешняя коммерческая ссылка с заданным анкором.
- Не публиковать абсолютные обещания безопасности и не добавлять инструкции по обходу anti-cheat.
- После публикации проверить canonical URL, sitemap и доступность страниц без входа в GitBook.
