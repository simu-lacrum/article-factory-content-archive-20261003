---
source: prompts/01-generate-article-ideas.md
heading: "Prompt: Generate SEO Article Ideas From Local Memory"
---

# Prompt: Generate SEO Article Ideas From Local Memory

Ты находишься в проекте `C:\Users\User\Desktop\articles`.

Задача: сгенерировать список идей для SEO-статей, но не писать сами статьи.

Параметры:

- Game: `dota2` или `cs2` или `all`
- Language: `en` или `ru`
- Count: сколько идей нужно
- Optional focus: если я укажу конкретную тему, механику, продуктовую функцию или кластер, используй это как фильтр

Перед ответом обязательно сделай рабочую подготовку:

1. Прочитай `AGENTS.md`.
2. Прочитай `SEO_ARTICLE_RULES.md`.
3. Прочитай `knowledge/editorial_memory.md`.
4. Прочитай `published/articles.csv`.
5. Прочитай `published/avoid_topics.txt`.
6. Используй локальные markdown-источники из `knowledge/agent_memory/sources/`, не открывай Medium-ссылки заново.
7. Проверь `memory/ai-memory-export/index.md`, `memory/ai-memory-export/topic-priorities.md`, `memory/ai-memory-export/published-and-avoid.md`.
8. Проверь `memory/graph/knowledge-graph.json`.

Если база устарела или локальные markdown-копии ссылок не созданы, сначала запусти:

```powershell
python -m article_factory materialize-links
python -m article_factory ingest --rebuild
python -m article_factory ai-memory export
python -m article_factory graph export
```

Затем подбери темы через topic engine и ручной анализ:

```powershell
python -m article_factory topics --count 80 --game dota2 --language en
python -m article_factory topics --count 80 --game cs2 --language en
```

Фильтры:

- Не предлагай прямые дубли уже опубликованных Medium-статей.
- Не бери темы, заблокированные в `published/avoid_topics.txt`.
- Можно брать соседние темы только если search intent реально другой.
- Не предлагай темы, где статья неизбежно потребует операционных инструкций по bypass/evasion/exploit/implementation.
- Приоритет: low/mid competition, понятный user intent, сильный product fit, возможность написать полезную статью на фактах.

Формат ответа:

Сначала дай короткое резюме, какие источники и память были прочитаны.

Потом выдай таблицу идей:

| # | Priority | Game | Language | Working SEO Title <=60 | Primary Keyword | Cluster | Intent | Why This Is Useful | Why Not Duplicate | Risk | Image Angle |
|---|---|---|---|---|---|---|---|---|---|---|---|

После таблицы добавь:

- 5 лучших идей для первой публикационной очереди.
- 5 идей, которые стоит отложить.
- Список тем, которые ты намеренно не взял из-за `published/avoid_topics.txt`.

Не пиши статьи. Нужен только список идей.
