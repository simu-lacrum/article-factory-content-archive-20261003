# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Создай одну полностью самостоятельную русскоязычную SEO-версию авторской статьи https://medium.com/@mrkhertz/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710. Сохрани исходную смысловую рамку: зачем выбирать официальный источник, что проверить до загрузки, высокоуровневая последовательность через официальный сайт/аккаунт/доступ/лаунчер, спокойное знакомство с интерфейсом, обзор категорий Aimbot, TriggerBot, ESP и HUD/Misc, FAQ. Полностью измени композицию, формулировки, примеры и переходы. Язык русский, около 1000-1200 слов. Primary keyword: как установить читы для CS2. Укажи, что бесплатность зависит от текущих условий: исходная публикация описывала семидневный пробный доступ через OAuth, но актуальная официальная страница сейчас показывает семидневный тариф, поэтому читателю нужно проверить кабинет. Не советуй отключать антивирус. Не давай инструкций по обходу античита, маскировке поведения, инъекции или низкоуровневой реализации. Не обещай безопасность или недетектируемость. Добавь SEO front matter, 2-3 image slots, одну нативную ссылку cluster.center и 5 вопросов FAQ. Без markdown-таблиц, без переспама.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260723-174302`

## Required Workflow

1. Read `SEO_ARTICLE_RULES.md` and `knowledge/agent_memory/products/product-map.md`.
2. For each item below, read the `prompt` and `evidence` files.
3. Write a complete article to the target output path.
4. Use only facts supported by the evidence pack or mark uncertainty explicitly.
5. Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body. Use those inputs silently and write from an expert editorial voice.
6. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
7. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
8. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
9. Match the imported Medium style: direct, practical, conversational, lightly slangy, gamer-aware, no water, no bureaucratic wording, no academic filler.
10. After writing all articles, run `python -m article_factory review output\runs\20260723-174302.json`.
11. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Как установить читы для CS2: понятная инструкция

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260723-174302\01-kak-ustanovit-chity-dlya-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260723-174302\01-kak-ustanovit-chity-dlya-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260723-174302\01-kak-ustanovit-chity-dlya-cs2.md`
