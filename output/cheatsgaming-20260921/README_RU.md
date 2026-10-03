# Статьи для CheatsGaming.com

Откройте `index.html` в браузере. Для каждой статьи доступны просмотр текста и отдельные кнопки копирования title, description и HTML для CMS. Страница автономная: интернет и локальный сервер для её работы не требуются.

Материалы:

- CS2 Triggerbot vs Aimbot: What Each Feature Does — новая статья, title 48 символов.
- CS2 Radar vs ESP vs Wallhack: What's the Difference? — новая статья, title 52 символа.
- Deadlock Souls Aimbot, Triggerbot and ESP Explained — новая статья, title 51 символ.
- Deadlock Auto Parry Cheat: What It Actually Automates — обновление существующей статьи, title 53 символа.

Все четыре description содержат ровно 160 символов, включают основной ключ и не заканчиваются точкой.

## Файлы

- `*.html` — полный HTML-документ с title и meta description.
- `*.body.html` — чистый HTML статьи для редактора CMS: H1, H2, H3, абзацы, списки и ссылки.
- `*.editorial.txt` — задания для двух настоящих скриншотов и заметки о перелинковке. Они не включены в публичный HTML.
- `articles.json` — тексты, метаданные, источники и пути к Markdown-оригиналам.
- `editorial-review.md` — редакционная проверка, выбор тем и ограничения исходных данных.
- `review.json` — автоматическая проверка всех четырёх материалов.
- `build_delivery.py` — повторная сборка HTML из Markdown-оригиналов.

HTML статьи включает H1. Если CMS выводит заголовок сама, удалите первый H1 из фрагмента, чтобы на странице остался один основной заголовок. Title и description вставляются в отдельные SEO-поля. Изображения не генерировались и не вставлены в готовые фрагменты.

Для auto-parry замените текст на существующей странице:
https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924

Новые URL не выдуманы. После публикации двух CS2-статей можно добавить взаимные ссылки по заметкам из editorial.txt. Публикация на сайте не выполнялась; записи в память опубликованных материалов не добавлены.
