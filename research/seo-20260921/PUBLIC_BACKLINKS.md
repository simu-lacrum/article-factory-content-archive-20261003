# Входящие ссылки: публичные примеры Dota 2 и Deadlock

Дата последней проверки ссылок: 2026-09-21. Это вручную выбранные страницы с проверенными ссылками, а не полный профиль конкурентов. Общие доли анкоров, оценка качества доменов и прогноз роста по этой выборке не рассчитываются.

## 1. Обзор покрытия

Проверено 11 страниц-кандидатов. Ссылки подтверждены на 5 страницах с 3 хостов: github.com, www.scam-detector.com, www.scamadviser.com. Получено 8 уникальных сочетаний источник → адрес назначения → текст. Недоступных страниц: 6; коды и причины сохранены в журнале. Это неизвестность, а не доказательство отсутствия или удаления ссылки.

Отдельная выборка Semrush по Anyx содержит 15 строк с 10 хостов: 11 совпадений адреса и текста подтверждены, ещё у одной ссылки отличается извлечённый текст. Эти строки не объединяются с публичной выборкой для расчёта процентов. [Данные Anyx](METRICS_AND_ANCHORS.md).

Moz и Bing не настроены; callable-инструмента DataForSEO в сессии нет. Публичная квота Semrush исчерпана. У [Common Crawl](https://commoncrawl.github.io/cc-webgraph-statistics/) проверен актуальный выпуск `cc-main-2026-jun-jul-aug`, но числовые метрики исследуемых доменов не получены. Граф не даёт анкоры; неполный просмотр большого файла не позволяет объявить домен отсутствующим.

**Backlink Health Score: INSUFFICIENT DATA.** Ни для одного домена нет четырёх полноценных факторов профиля. Числовая оценка не выставлена.

## 2. Анкоры и безанкорные ссылки

- **avalan.cc:** 2 строк; generic: 1, branded: 1.
- **octarine.cc:** 1 строк; naked_url: 1.
- **uc.zone:** 5 строк; naked_url: 5.

URL-образный текст выделен как `naked_url`; `VISIT` — общий анкор, `VISIT avalan.cc` — брендовый. Брендовый текст и голый URL не смешиваются, даже если оба не содержат целевой ключ. Проверенные примеры:

- [https://uc.zone/ru/dota2](https://github.com/ValveSoftware/Dota2-Gameplay/issues/25629) → `https://uc.zone/ru/dota2`; naked_url; rel: nofollow; контекст: `user_complaint_on_public_issue_tracker`.
- [https://octarine.cc/p/home](https://github.com/ValveSoftware/Dota2-Gameplay/issues/25629) → `https://octarine.cc/p/home`; naked_url; rel: nofollow; контекст: `user_complaint_on_public_issue_tracker`.
- [https://uc.zone/](https://github.com/ValveSoftware/Dota2-Gameplay/issues/6892) → `https://uc.zone/`; naked_url; rel: nofollow; контекст: `user_complaint_on_public_issue_tracker`.
- [uc.zone/ru/dota2](https://github.com/Nerve11/uczone-docs-UmbrellaDota2) → `https://uc.zone/ru/dota2`; naked_url; rel: nofollow; контекст: `third_party_documentation_repository_readme`.
- [uc.zone](https://github.com/Nerve11/uczone-docs-UmbrellaDota2) → `https://uc.zone/ru/dota2`; naked_url; rel: nofollow; контекст: `third_party_documentation_repository_readme`.
- [VISIT](https://www.scamadviser.com/check-website/avalan.cc) → `https://avalan.cc/`; generic; rel: noopener, noreferrer; контекст: `automated_reputation_report`.
- [VISIT avalan.cc](https://www.scamadviser.com/check-website/avalan.cc) → `https://avalan.cc/`; branded; rel: noopener, noreferrer; контекст: `automated_reputation_report`.
- [uc.zone](https://www.scam-detector.com/validator/uc-zone-review/) → `https://uc.zone/`; naked_url; rel: nofollow; контекст: `automated_reputation_report`.

Ссылка в списке выше открывает страницу-источник для проверки. Исходный `observed_href` сохранён в CSV: у ScamAdviser это HTTP-адрес с UTM-параметрами. Нормализованный HTTPS-адрес служит ключом сопоставления и не доказывает исходный протокол ссылки. Строк с `nofollow`: 6, без этого атрибута: 2; это не устанавливает передачу рейтингового веса. `noopener`/`noreferrer` записаны как обнаруженные атрибуты.

Практическое применение: ссылка на продукт — ясное название бренда или адрес; ссылка на соседнюю статью — конкретный вопрос или содержание статьи. Например, `how soul aimbot differs from soul ESP` уместен только для страницы, которая объясняет это различие. Эти редакционные примеры не выдаются за анкоры конкурентов. Целевые проценты exact/branded/naked не назначены.

## 3. Контекст источников

GitHub issues содержат сообщения пользователей. Наличие ссылки в репозитории ValveSoftware не превращает пользовательскую жалобу в заявление Valve или рекомендацию продукта. Сторонний README также не подтверждает авторство вендора. ScamAdviser и Scam Detector — автоматические отчёты о доменах; их наличие не подтверждает качество ПО. Оценки безопасности и обвинения из этих страниц в статьи не переносятся.

Поле `placement=editorial` означает расположение вне распознанной навигации. Это техническая эвристика HTML, а не оценка редакционной независимости. Авторство, оплата размещений, география аудитории и авторитет источников не установлены.

## 4. Проверка подозрительных связей

Оснований объявлять эти домены токсичными, частью PBN или кандидатами на disavow нет. Встречные ссылки проверены на сохранённых страницах доменов назначения; совпадений с подтверждёнными входящими хостами: 0. Это вывод только о просмотренном HTML, не обо всех страницах сайтов. Подробности проверки сохранены в `public-backlink-summary.json`.

При первоначальной проверке форумы Elitepvpers, обращение на Palo Alto LIVEcommunity и два отчёта Gridinsoft были недоступны обычной загрузкой. Сниппет или картинка скрытой ссылки не заменяют установленный href. Такие наблюдения не включаются в подтверждённые строки.

## 5. Страницы назначения

- `https://uc.zone/ru/dota2` — 3 сочетаний в этой выборке.
- `https://uc.zone/` — 2 сочетаний в этой выборке.
- `https://avalan.cc/` — 2 сочетаний в этой выборке.
- `https://octarine.cc/p/home` — 1 сочетаний в этой выборке.

Это не рейтинг страниц по всем бэклинкам. Нет данных для вывода о страницах без ссылок или о потерянном весе на 404.

## 6. Сравнение с собственными сайтами

Полных сопоставимых профилей CheatsGaming, DeadlockHacks и CS2-площадки нет. Нельзя утверждать, что источник ссылается только на конкурента, и составлять из этого списка план размещений. Жалобы и автоматические репутационные страницы не являются рекомендованными площадками для публикации статей. Следующий полезный вход — сопоставимые экспорты собственных и конкурентных доменов с датой, source URL, target URL, анкором и rel.

## 7. Новые и потерянные ссылки

Есть одна временная точка наблюдений; появления и потери не рассчитаны. Для динамики нужны повторные сопоставимые снимки или история провайдера. HTTP 403 сегодня не считается потерянной ссылкой.

## Файлы и воспроизводимость

- [Проверенные строки CSV](public-backlink-sample.csv), [JSON](public-backlink-sample.json).
- [Все попытки загрузки, даты и хеши](public-backlink-observations.json).
- [Сводка и встречные ссылки](public-backlink-summary.json).
- [Доступность источников данных](backlink-source-availability.json).
- Повторная проверка: `python scripts/verify_public_backlinks.py research/seo-20260921`.
- Отчёт без повторной загрузки: `python scripts/export_public_backlink_report.py research/seo-20260921`.
- Обновление ядра: `python -m article_factory research build research/seo-20260921`.
