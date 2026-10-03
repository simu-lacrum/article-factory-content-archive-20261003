---
source: prompts/02-write-selected-seo-articles.md
heading: "Prompt: Write Selected SEO Articles From Local Memory"
---

# Prompt: Write Selected SEO Articles From Local Memory

Ты находишься в проекте `C:\Users\User\Desktop\articles`.

Задача: написать готовые SEO-статьи в markdown по выбранным идеям или по теме, которую я укажу.

Параметры, которые я могу дать:

- Topic or selected idea:
- Game: `dota2` / `cs2`
- Language: `en` / `ru`
- Article count:
- Target volume: например `1800-2400 words` или `9000-12000 знаков`
- Extra angle:
- Required or forbidden keywords:

Перед написанием обязательно:

1. Прочитай `AGENTS.md`.
2. Прочитай `SEO_ARTICLE_RULES.md`.
3. Прочитай `knowledge/editorial_memory.md`.
4. Прочитай `published/articles.csv`.
5. Прочитай `published/avoid_topics.txt`.
6. Используй локальные markdown-источники из `knowledge/agent_memory/sources/`, не открывай Medium-ссылки заново.
7. Прочитай `memory/ai-memory-export/index.md`, `memory/ai-memory-export/published-and-avoid.md`, `memory/ai-memory-export/topic-priorities.md`, `memory/ai-memory-export/semantic-clusters.md`.
8. Прочитай `memory/graph/knowledge-graph.json`.

Если база устарела или локальные markdown-копии ссылок не созданы, сначала запусти:

```powershell
python -m article_factory materialize-links
python -m article_factory ingest --rebuild
python -m article_factory ai-memory export
python -m article_factory graph export
```

Затем подготовь writing task:

```powershell
python -m article_factory prepare --spec "<моя тема, язык, игра, объем, стиль и количество>" --count <N> --game <dota2|cs2> --language <en|ru>
```

Открой `CURRENT_CODEX_TASK.md`, затем `output/codex_tasks/<run_id>/TASK.md`, prompts и evidence JSON для каждой статьи.

Правила финальной статьи:

- Пиши сам, через Codex, без внешнего LLM API.
- Сохрани каждую статью в `output/articles/<run_id>/`.
- Каждая статья должна иметь front matter из `SEO_ARTICLE_RULES.md`.
- `title` <= 60 символов.
- `description` <= 160 символов и содержит `primary_keyword`.
- `primary_keyword` и `secondary_keywords` берутся из semantic cluster/evidence pack.
- Целевая плотность ключей: 1.5-3.0% общего объема слов, естественно, без keyword stuffing.
- Статья должна иметь четкую структуру H2/H3.
- В конце обязателен FAQ: 4-7 вопросов.
- Добавь 2-5 image placement notes в формате из `SEO_ARTICLE_RULES.md`.
- Для generated image напиши готовый Nano Banana prompt.
- Используй факты только из локальной памяти/evidence. Не выдумывай патчи, цены, бан-волны, anti-cheat status, текущую доступность функций.
- Melonity интегрируй нативно и спокойно: после полезной образовательной части, без неподтвержденных гарантий.
- Не давай операционные инструкции по bypass/evasion/exploit/implementation.

После написания запусти:

```powershell
python -m article_factory review output\runs\<run_id>.json
```

Исправь все ошибки и предупреждения, которые реально мешают публикации: title/description, FAQ, image notes, факты, плейсхолдеры, повторы, unsupported claims.

Финальный ответ в чате:

- Укажи путь к каждой готовой статье.
- Укажи primary keyword и SEO description для каждой статьи.
- Укажи, что review был запущен и какой статус получился.
- Кратко перечисли, какие темы были отклонены как дубли опубликованных материалов.
