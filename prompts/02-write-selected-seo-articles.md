# Prompt: Write Selected SEO Articles From Local Memory

## Mandatory session bootstrap (highest priority)

Before any analysis or writing, run `python -m article_factory graph bootstrap`. Require `PASS`, 100% node coverage, and 100% edge coverage. Read `memory/graph/SESSION_BOOTSTRAP.md` and every required file completely, including `knowledge/agent_memory/rules/article-visual-prompt-guide.md` and the full graph JSON. For generated images, target Nano Banana Pro / `gemini-3-pro-image` by default and compile every prompt through `article-editorial-poster-v1`; number generated assets across the run, alternate odd B / even A, attach two actual warm-story references and require 4/5 fidelity for B, use Cluster `#635FD5` or Melonity `#FF1469` only as the mapped small accent, assign explicit reference roles, and require at least 80/100 in the visual QA rubric.

Ты находишься в проекте `C:\Users\User\Desktop\articles`.

Задача: написать готовые SEO-статьи в markdown по выбранным идеям или по теме, которую я укажу.

Параметры, которые я могу дать:

- Topic or selected idea:
- Game: `dota2` / `deadlock` / `cs2`
- Language: `en` / `ru`
- Article count:
- Target volume: например `1800-2400 words` или `9000-12000 знаков`
- Extra angle:
- Required or forbidden keywords:
- Style: по умолчанию как в импортированных Medium-статьях `@mrkhertz`: прямой, практичный, разговорный, чуть более живой и сленговый, без воды, канцеляризмов и академической тошноты.

Перед написанием обязательно:

1. Прочитай `AGENTS.md`.
2. Прочитай `SEO_ARTICLE_RULES.md`.
3. Прочитай `knowledge/editorial_memory.md`.
4. Прочитай `published/articles.csv`.
5. Прочитай `published/avoid_topics.txt`.
6. Прочитай `knowledge/agent_memory/products/product-map.md`.
7. Используй локальные markdown-источники из `knowledge/agent_memory/sources/`, не открывай Medium/YouGame-ссылки заново.
8. Прочитай `memory/ai-memory-export/index.md`, `memory/ai-memory-export/published-and-avoid.md`, `memory/ai-memory-export/topic-priorities.md`, `memory/ai-memory-export/semantic-clusters.md`.
9. Прочитай `memory/graph/knowledge-graph.json`.

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

Затем подготовь writing task:

```powershell
python -m article_factory prepare --spec "<моя тема, язык, игра, объем, стиль и количество>" --count <N> --game <dota2|deadlock|cs2> --language <en|ru>
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
- Не используй markdown-таблицы. Только списки, нумерованные списки, короткие подзаголовки и comparison lists.
- Объем должен быть нормальным: достаточно, чтобы полностью закрыть intent, но без лишних абзацев ради объема. Если я указал Target volume, следуй ему; если нет, пиши кратчайшую полноценную версию.
- Стиль держи как в импортированных Medium-статьях: живой экспертный тон, понятные фразы, игровой контекст, практичные выводы, спокойная уверенность, без корпоративного или академического звучания.
- Не показывай читателю внутреннюю механику проекта. В финальной статье нельзя писать "локальные источники", "локальная память", "evidence pack", "local evidence", "knowledge base", "по данным локальных источников" и похожие фразы.
- Используй локальную память только внутри анализа. В самом тексте выступай как эксперт: "по нашему опыту", "на практике", "мы обычно видим", "для игрока это значит..." Особенно это важно в блоках с интеграцией продукта.
- Добавляй немного простого игрового языка и сленга там, где это звучит естественно: ranked, pubs, tilt, legit, sketchy, hard-sell, match pressure. Не превращай текст в чатик, но убери лишнюю строгость.
- Не используй AI-филлер и пустые SEO-фразы вроде "in today's gaming landscape", "delve into", "comprehensive overview", "it is important to note", если они не нужны по смыслу.
- В конце обязателен FAQ: 4-7 вопросов.
- Добавь 2-5 image placement notes в формате из `SEO_ARTICLE_RULES.md`.
- Для generated image напиши готовый Nano Banana prompt, проставь общий индекс и ветку B/A; реальные скриншоты индекс не сдвигают. Для каждого B фактически приложи два файла из warm-story set и укажи цель fidelity 4/5. Для Cluster используй малый акцент `#635FD5`, для Melonity — `#FF1469`.
- Используй факты только из локальной памяти/evidence или свежих проверенных источников, но не называй эти источники в теле статьи как "локальные". Не выдумывай патчи, цены, бан-волны, anti-cheat status, текущую доступность функций.
- Продукт интегрируй строго по `knowledge/agent_memory/products/product-map.md`: Dota 2 -> Melonity, Deadlock/CS2 -> cluster.center. Интеграция должна быть нативной и спокойной: после полезной образовательной части, без неподтвержденных гарантий.
- Не давай операционные инструкции по bypass/evasion/exploit/implementation.

После написания запусти:

```powershell
python -m article_factory review output\runs\<run_id>.json
```

Исправь все ошибки и предупреждения, которые реально мешают публикации: title/description, FAQ, image notes, факты, плейсхолдеры, повторы, unsupported claims.
Отдельно проверь, что в финальных markdown-файлах нет таблиц и что стиль не скатился в воду, канцеляризмы или академическое объяснение ради объяснения.

Финальный ответ в чате:

- Укажи путь к каждой готовой статье.
- Укажи primary keyword и SEO description для каждой статьи.
- Укажи, что review был запущен и какой статус получился.
- Кратко перечисли, какие темы были отклонены как дубли опубликованных материалов.
