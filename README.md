# Article Factory

## Mandatory Codex session bootstrap

Every new Codex dialog in this workspace must first run `python -m article_factory graph bootstrap`, require 100% node and edge coverage, then read `memory/graph/SESSION_BOOTSTRAP.md` and every required file it lists. The mandatory visual system is `article-editorial-poster-v1`; its primary generator is Nano Banana Pro / `gemini-3-pro-image`.

Универсальная локальная система контент-памяти и производства SEO-статей: источники -> wiki/SQLite -> topic engine -> evidence pack -> Codex writing task -> quality gate -> память публикаций.

Основной сценарий: статьи пишет Codex внутри проекта. Внешний LLM API не нужен.

Тематики: Dota 2, CS2 и Deadlock. Основной рынок — США / Google, UK исследуется отдельно. Начать с [отчёта исследования](research/seo-20260921/REPORT_RU.md), [редакционного плана](research/seo-20260921/EDITORIAL_PLAN.md) и [рабочего процесса](docs/SEO_RESEARCH_WORKFLOW.md).

## Что уже умеет

- Индексирует текущие `*.md` и `*.csv` в SQLite.
- Рекурсивно индексирует `.md`, `.txt`, `.html`, `.csv`, `.tsv` и `.pdf` при установленном `pypdf`.
- Делает wiki-слой из markdown-разделов в `knowledge/wiki/`.
- Кластеризует семантические ядра Dota 2 и CS2 в таблицу `semantic_clusters`.
- Хранит реальные SERP-наблюдения, конкурентные страницы, задачи читателя, варианты запросов, семантические термины и контекст ссылок.
- Отделяет подтверждённую частотность от неизвестной, а редакционные гипотезы от наблюдений. Старые CSV-цифры не используются как актуальные метрики США.
- Учитывает `published/articles.csv`, чтобы не плодить дубли опубликованных статей.
- Собирает evidence pack для каждой темы.
- Генерирует Codex writing tasks, prompts и article briefs без платных зависимостей.
- `--llm template` создаёт только бриф для Codex: повторяющиеся шаблонные статьи больше не генерируются.
- Может писать полные статьи через локальный Ollama или OpenAI API, если ключ/модель подключены.
- Запускает review/quality gate по manifest.
- Экспортирует snapshot для `ai-memory`/wiki-памяти в `memory/ai-memory-export/`.

## Быстрый старт

```powershell
python -m article_factory init
python -m article_factory doctor
python -m article_factory prepare --spec "Три понятные статьи по CS2, Dota 2 и Deadlock: конкретная задача читателя, проверяемые примеры и естественный язык" --count 3 --game all --language en
python -m article_factory review output\runs\<timestamp>.json
```

После `prepare` открой `CURRENT_CODEX_TASK.md`; Codex сам прочитает prompts/evidence и напишет финальные markdown-статьи в `output/articles/<run_id>/`.

При активном исследовании `prepare` включает задачу читателя, формат страницы, реальные источники, конкурентные наблюдения и редакционные ограничения. Codex пишет текст; автоматическая проверка дополнена обязательной проверкой фактов и качества чтения.

## Как добавлять знания

- Markdown: клади рядом с проектом или в `knowledge/raw/`, затем запускай `ingest`.
- CSV: добавляй семантические ядра в корень или `knowledge/raw/`.
- TXT/HTML: можно класть как обычные источники.
- PDF: установи бесплатный пакет `pypdf`, затем клади PDF в `knowledge/raw/`.
- Постоянные ссылки: добавляй `.txt`-файлы в `knowledge/link_sources/`, по одной ссылке на строку. Формат: `URL | optional note`.
- Разовые ссылки: создай `links.txt`, по одной ссылке на строку, затем:

```powershell
python -m article_factory ingest --links links.txt
```

```powershell
python -m pip install -r requirements.txt
python -m article_factory ingest --rebuild
```

## Где результат

- `output/codex_tasks/<run>/` - задание для Codex.
- `output/prompts/<run>/` - промпты/брифы для Codex.
- `output/evidence/<run>/` - evidence pack для каждой статьи.
- `output/briefs/<run>/` - briefs, если LLM не запускалась.
- `output/articles/<run>/` - тексты, написанные Codex; готовность определяется редакционной и автоматической проверкой.
- `output/runs/<timestamp>.json` - manifest конкретного запуска.
- `output/runs/<timestamp>.review.json` - review-отчёт после `python -m article_factory review ...`.

## Диагностика и тесты

```powershell
python -m article_factory doctor
python -m unittest discover -s tests
```

`doctor` показывает, что внешний LLM не обязателен, установлен ли `pypdf`, запущен ли Docker для `ai-memory`, есть ли Ollama/OpenAI как необязательные усилители.

## Память публикаций

После публикации добавляй материал, чтобы topic engine не выбирал его снова:

```powershell
python -m article_factory published add --title "How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery" --slug behavior-score-dota-2 --game dota2 --language en --url "https://example.com/article"
python -m article_factory ingest
```

Можно также вручную редактировать `published/articles.csv`.

Чтобы заблокировать не только точный title, но и похожий topic angle, добавь паттерны в `published/avoid_topics.txt`.

## Risk-tier

Темы получают один из уровней:

- `normal` - можно автоматически включать в задание для Codex.
- `elevated` - допустимо, но review обязателен: коммерческие/спорные ключи, конфиги, scripts, skin changer.
- `restricted` - операционные инструкции по обходу защиты, эксплуатации уязвимостей и реализации читов не включаются в написание. Само упоминание ESP, aimbot или античита в объяснении терминов не равно такой инструкции.

Посмотреть всё:

```powershell
python -m article_factory topics --count 20 --game dota2 --language en --include-restricted
```

Система не должна генерировать операционные инструкции по обходу античита, эксплуатации уязвимостей или реализации чит-функций.

## Как сюда вписывается ai-memory

`ai-memory` полезен как долговременная память агента между сессиями, но ядро контентной системы здесь локальное: SQLite + markdown wiki. Команда:

```powershell
python -m article_factory ai-memory export
```

создаёт `memory/ai-memory-export/` с `index.md`, `project-summary.md`, `topic-priorities.md`, `source-inventory.md`, `semantic-clusters.md`. Эти файлы можно подключить к `ai-memory` или любому MCP/wiki-memory инструменту как сжатый снимок проекта.

## MCP-сервер

В проекте есть простой stdio MCP server. Его можно подключить к MCP-клиенту как локальный инструмент:

```json
{
  "mcpServers": {
    "article-factory": {
      "command": "python",
      "args": [
        "-m",
        "article_factory.mcp_server",
        "--root",
        "C:\\Users\\User\\Desktop\\articles"
      ]
    }
  }
}
```

Инструменты:

- `article_factory_status`
- `article_factory_search`
- `article_factory_topics`
- `article_factory_draft`
- `article_factory_codex_task`
- `article_factory_prepare`
- `article_factory_export_memory`
- `article_factory_export_graph`
- `article_factory_graph_bootstrap`

Так Codex сможет сам искать знания, выбирать темы и подготавливать writing tasks через локальную систему.

## Важное правило качества

Генератор специально заставляет модель сначала получить evidence pack и запрещает выдумывать текущий патч, цены, бан-волны, anti-cheat статус и продуктовые гарантии. Для спорных или быстро меняющихся фактов нужно добавлять свежий источник и переиндексировать базу.
