# Prompt: Generate SEO Article Ideas From Local Memory

## Mandatory session bootstrap (highest priority)

Before any analysis, run `python -m article_factory graph bootstrap`. Require `PASS`, 100% node coverage, and 100% edge coverage. Read `memory/graph/SESSION_BOOTSTRAP.md` and every required file completely, including the canonical visual prompt guide and the full graph JSON. Any visual direction in an idea or brief must use `article-editorial-poster-v1`, target Nano Banana Pro / `gemini-3-pro-image` by default, alternate generated assets B/A across the run (odd B, even A), require two actual warm-story references plus 4/5 fidelity for B, and reserve exact small brand accents: Cluster `#635FD5`, Melonity `#FF1469`.

Ты находишься в проекте `C:\Users\User\Desktop\articles`.

Задача: сгенерировать список идей для SEO-статей, но не писать сами статьи.

Параметры:

- Game: `dota2` или `deadlock` или `cs2` или `all`
- Language: `en` или `ru`
- Count: сколько идей нужно
- Optional focus: если я укажу конкретную тему, механику, продуктовую функцию или кластер, используй это как фильтр

Перед ответом обязательно сделай рабочую подготовку:

1. Прочитай `AGENTS.md`.
2. Прочитай `SEO_ARTICLE_RULES.md`.
3. Прочитай `knowledge/editorial_memory.md`.
4. Прочитай `published/articles.csv`.
5. Прочитай `published/avoid_topics.txt`.
6. Прочитай `knowledge/agent_memory/products/product-map.md`.
7. Используй локальные markdown-источники из `knowledge/agent_memory/sources/`, не открывай Medium/YouGame-ссылки заново.
8. Проверь `memory/ai-memory-export/index.md`, `memory/ai-memory-export/topic-priorities.md`, `memory/ai-memory-export/published-and-avoid.md`.
9. Проверь `memory/graph/knowledge-graph.json`.

Product mapping:

- Dota 2 -> Melonity.
- Deadlock -> cluster.center.
- CS2 -> cluster.center.

Если база устарела или локальные markdown-копии ссылок не созданы, сначала запусти:

```powershell
python -m article_factory materialize-links
python -m article_factory ingest --rebuild
python -m article_factory ai-memory export
python -m article_factory graph bootstrap
```

Затем подбери темы через topic engine и ручной анализ:

```powershell
python -m article_factory topics --count 80 --game dota2 --language en
python -m article_factory topics --count 80 --game deadlock --language en
python -m article_factory topics --count 80 --game cs2 --language en
```

Фильтры:

- Не предлагай прямые дубли уже опубликованных Medium-статей.
- Не бери темы, заблокированные в `published/avoid_topics.txt`.
- Можно брать соседние темы только если search intent реально другой.
- Не предлагай темы, где статья неизбежно потребует операционных инструкций по bypass/evasion/exploit/implementation.
- Приоритет: low/mid competition, понятный user intent, сильный product fit, возможность написать полезную статью на фактах.
- Не используй таблицы в ответе. Только нумерованные списки, bullet lists и короткие карточки идей.
- При оценке темы учитывай стиль будущей статьи: как в импортированных Medium-материалах `@mrkhertz` — прямой, практичный, разговорный, немного более живой и сленговый, без воды, канцеляризмов и академической тошноты.
- Если тема требует продуктовой интеграции, планируй ее как экспертный опыт, а не как ссылку на "локальные источники" или "evidence pack". Эти слова не должны попадать в будущий публичный текст.

Формат ответа:

Сначала дай короткое резюме, какие источники и память были прочитаны.

Потом выдай идеи нумерованным списком. Для каждой идеи используй такой формат:

1. `Working SEO Title <=60`
   - Priority:
   - Game:
   - Language:
   - Primary keyword:
   - Cluster:
   - Intent:
   - Why this is useful:
   - Why not duplicate:
   - Risk:
   - Image angle:

После списка добавь:

- 5 лучших идей для первой публикационной очереди.
- 5 идей, которые стоит отложить.
- Список тем, которые ты намеренно не взял из-за `published/avoid_topics.txt`.

Не пиши статьи. Нужен только список идей. Таблицы не используй.
