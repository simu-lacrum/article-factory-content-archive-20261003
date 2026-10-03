# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Написать одну русскую SEO-статью 800–1000 слов с точным углом: 'VAC Live стал VACNET: что изменилось в античите CS2'. Primary keyword: античит CS2. Следовать ТЗ пользователя от 2026-07-22 и источнику knowledge/agent_memory/sources/vac-live-vacnet-verified-2026-07-22.md. Разделить подтвержденное переименование/уведомление в мае 2026, исторический VacNet 2018, live ban 2023 и ограниченный VacNet 3.0 2024. Не выдавать UI-изменение за новую модель и цифры 2018 за текущие мощности. Одна нативная ссылка cluster.center, 3 image slots, 6 FAQ, без таблиц и без инструкций обхода.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260722-112310`

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
10. After writing all articles, run `python -m article_factory review output\runs\20260722-112310.json`.
11. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Античит CS2 после ребрендинга: куда пропал VAC Live

- Game: `cs2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260722-112310\01-vac-live-stal-vacnet-chto-izmenilos-v-antichite-cs2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260722-112310\01-vac-live-stal-vacnet-chto-izmenilos-v-antichite-cs2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260722-112310\01-vac-live-stal-vacnet-chto-izmenilos-v-antichite-cs2.md`
