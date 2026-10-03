You are an expert SEO editor and game-content researcher.

Write a useful, non-generic SEO article in English.

USER SPEC:
Сгенерируй 10 SEO статей объемом 1800-2400 words, в экспертном живом стиле, с нативной интеграцией Melonity

ARTICLE TARGET:
- Title: Random Dota 2 Hero and Build Challenge: How to Make Any Pick Playable
- Game: dota2
- Main query: Random Dota 2 Hero and Build Challenge: How to Make Any Pick Playable
- Cluster: `GENERAL: рандомизер` -> Random Hero / Random Build Challenge
- Risk level: normal
- Target volume: 2400 words
- Style: expert, clear, human, useful, SEO-aware
- Advertising mode: native

SEO / TOPIC EVIDENCE:
- `GENERAL: рандомизер` -> Random Hero / Random Build Challenge
- SERP в основном фан-сайты генераторов, Reddit и простые страницы. Нормальная статья с challenge-форматом может получать long-tail + social.

SUGGESTED OUTLINE:
- What random hero/build challenges are
- How to generate a random hero pool
- Rules for a ranked-safe challenge vs fun lobby challenge
- Why all-hero knowledge matters
- Melonity angle: All Heroes Combo, auto-cast, hero scripts for unfamiliar picks
- Content idea: YouTube Shorts "random hero with Melonity"
- CTA: try 7 days free and run the challenge

LOCAL KNOWLEDGE SOURCES:
### Source: melonity-seo-cluster-map-en.md / 4. `GENERAL: changer / smurf utility` -> Skin Changer
### 4. `GENERAL: changer / smurf utility` -> Skin Changer

**Почему кластер:** KD 6 в основном кластере и KD 3 в long-tail: `skin changer dota 2`, `dota 2 skin changer`, `dota 2 skin changer free`, `банят ли за скин чейнджер`.

**EN article title:** `Dota 2 Skin Changer in 2026: Free Tools, Ban Risks and Premium Alternatives`

**Объем:** 2,000-2,600 words.

**Почему можно ранжироваться:** EN выдача содержит YouTube, GitHub, старые Reddit-треды и сомнительные free-инструменты. Хорошая статья с risk-checklist может выглядеть надежнее.

**Оглавление:**

- What a Dota 2 skin changer does
- Why players search for free skin changers
- Free GitHub/tools vs premium cheat-suite skin changer
- What ban-risk questions users ask
- How Melonity Skin Changer fits into a broader premium toolkit
- Skins, landscapes, Dota Plus visuals and customization
- Safe wording: no 100% ban-proof promises
- CTA: try Melonity instead of random free tools

**Рекламная интеграция:** прямой сравнительный блок. Акцент: Melonity - не просто skin changer, а полный Dota 2 cheat suite с поддержкой, обновлениями и комьюнити.

---

### Source: PRODUCT_REQUIREMENTS.md / Required end state
## Required end state

A user can give a natural task such as:

> Generate 10 SEO articles of N volume, in this style, with native integration of my project.

The system should then:

1. Read clustered semantic cores and published-article history.
2. Select non-duplicate article topics with strong SEO potential.
3. Retrieve real evidence from local knowledge, URLs, markdown, CSV, PDF, and future sources.
4. Build an evidence pack for each article.
5. Generate a useful, human, SEO-structured article.
6. Integrate advertising naturally without unsupported claims.
7. Run quality/fact/risk checks.
8. Save prompts, evidence, articles, manifests, and review reports.
9. Export durable memory for `ai-memory`, Obsidian, or another MCP/wiki-memory layer.

### Source: SYSTEM_ARCHITECTURE.md / Universal domain model
## Universal domain model

The code treats `dota2` and `cs2` as current domains, not the only possible domains. Unknown future CSVs are assigned to `general` unless a file name or headers allow detection. Commands accept arbitrary `--game` values, so future domain-specific importers can be added without changing the article pipeline.

### Source: melonity-knowledge-base.md / 4. TONE OF VOICE (TOV)
## 4. TONE OF VOICE (TOV)

### Source: melonity-knowledge-base.md / 10.2. EN-сленг Dota 2
### 10.2. EN-сленг Dota 2 | Term | Definition | Usage | | --- | --- | --- | | MMR | Match Making Rating | Universal | | Climb / climbing | improving MMR | SEO content | | Boost / boosting | external help with MMR | targeting boosters | | Smurf / smurfing | playing low-rank account | SEO «anti-smurf» | | Smurf pool | matchmaking penalty for smurfs | NICHE SEO | | LP / Low Priority | punishment queue | content kluster | | Behavior Score | поведенческий рейтинг | NICHE SEO ⭐ | | Conduct Summary | Valve's behavior report | technical SEO | | Throw / throwing | griefing / sabotaging | Behavior Score content | | Feed / feeding | dying excessively | Behavior Score content | | Tilt / tilting | emotional spiral | mental game content | | Carry / hard carry | role + role | hero guides | | Mid / offlane / safe lane | positions | hero guides | | Pos 1–5 | role positions |...

### Source: melonity-knowledge-base.md / EN
#### EN
1. **«Stuck in low priority»** — emotional content
2. **«Toxic teammates»** — universal
3. **«Behavior score reset»** — техническое + эмоциональное
4. **«Why is my matchmaking so bad?»** — endless discussion
5. **«Hero balance complaints»** — patch reactions
6. **«How to play [hero] in 2026»** — high SEO + viral
7. **«Pro tips from [pro player]»** — authority content
8. **«Ranked vs Turbo mode»** — debate-fueling
9. **«Smurf detection by Valve»** — technical interest

### Source: PRODUCT_REQUIREMENTS.md / Non-negotiable goal
## Non-negotiable goal

This project must become a universal, fully working, thoughtfully designed content-intelligence system, not a one-off script or a narrow first MVP.

The current Dota 2 / CS2 / Melonity use case is the first domain. The architecture must stay reusable for other games, products, languages, markets, and SEO datasets.

### Source: melonity-knowledge-base.md / 10.1. RU-сленг Dota 2 (используем в постах и SEO для аудитории)
### 10.1. RU-сленг Dota 2 (используем в постах и SEO для аудитории) | Слово | Значение | Когда использовать | | --- | --- | --- | | MMR | Match Making Rating | Везде | | ММР | то же на кириллице | альтернативное нап��сание для SEO | | Бустить / буст | поднимать рейтинг (себе или другому) | целевая аудитория «бустеры» | | Смурф / смурфинг | играть на новом аккаунте с занижением | контент про «защиту от смурф-бана» | | Скрытый пул | shadow ban / matchmaking penalty | НЧ-золото для SEO | | Behavior score / порядочность / порядок | поведенческий рейтинг | гайды | | Ливать / лив | покинуть матч до конца | гайды по Behavior Score | | Руинить / руинер | намеренно п��оигрыват�� | контекст Behavior Score | | Фидить | умирать слишком много | негативное поведение | | Тилт | эмоциональный спад после поражений | контекст «как не сливать MMR» | | Тащить / тащит | вести команду к победе | celebratory tone | | Олды / олдфаги | пользователи с...

### Source: README.md / Быстрый старт
## Быстрый старт ```powershell python -m article_factory init python -m article_factory ingest --rebuild python -m article_factory doctor python -m article_factory topics --count 10 --game dota2 --language en python -m article_factory draft --spec "Сгенерируй 10 SEO статей объемом 1800-2400 words, в экспертном стиле, с нативной интеграцией Melonity" --count 10 --game dota2 --language en --llm none python -m article_factory draft --spec "Сгенерируй 10 SEO статей объемом 1800-2400 words, в экспертном стиле, с нативной интеграцией Melonity" --count 10 --game dota2 --language en --llm template python -m article_factory review output\runs\<timestamp>.json python -m article_factory ai-memory export ``` Режим `--llm none` не тратит деньги: он создаёт `output/briefs/...` и `output/prompts/...`. Режим `--llm template` тоже не тратит деньги: он создаёт полноценные markdown-файлы в `output/articles/...` на основе evidence pack. Это fallback для автономного цикла; для максимально живого стиля лучше подключить Ollama/OpenAI. Когда будет локальная модель: ```powershell python -m article_factory draft --spec "Сгенерируй 3 SEO статьи на русском, 9000 знаков, живым экспертным стилем" --game cs2 --language ru --llm ollama --model llama3.1:8b ``` С OpenAI: ```powershell $env:OPENAI_API_KEY="sk-..." python -m article_factory draft --spec "Generate 5 English SEO articles, 1800 words, native Melonity...

### Source: melonity-knowledge-base.md / 9.5. Web2.0 SEO article operating model
### 9.5. Web2.0 SEO article operating model

> Цель web2.0-статей — не просто вставить ссылку на melonity.gg, а создать страницу, которая выглядит как полезный материал от человека из Dota-комьюнити: объясняет механику, отвечает на запрос, использует актуальные термины и только после этого нативно рекомендует Melonity как решение.

STRICT RULES:
- Use only facts supported by the local knowledge sources or mark uncertainty explicitly.
- Do not invent current patch, price, ban-wave, anti-cheat, or product-status facts.
- Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheats.
- If risk level is `restricted`, write only a high-level educational/risk-aware article and refuse operational steps.
- You may mention Melonity as a product/brand in a native ad block, but do not make unsupported safety guarantees.
- Make the article genuinely useful: explain context, user intent, mistakes, practical checklists, FAQ, and internal-link ideas.
- Return Markdown with front matter: title, description, game, language, primary_keyword, secondary_keywords.
