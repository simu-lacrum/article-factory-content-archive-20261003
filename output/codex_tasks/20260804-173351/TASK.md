# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Подготовить два русскоязычных SEO-ТЗ для tier-2 статей о кастомных Dota 2 скриптах на основе видео: 1) от идеи и AI-промпта до загрузки локального JavaScript-скрипта и теста в Melonity, анкор 'читы дота 2'; 2) как составить техническое задание для AI на Dota 2 скрипт через модель цель-условия-действия-настройки-тест, анкор 'читы для dota 2'. Каждая будущая статья 1000-1200 слов, без кода и без anti-cheat bypass/evasion, с естественной ссылкой на https://melonity.gg/, уникальный интент, стиль Medium mrkhertz, визуалы Nano Banana Pro.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260804-173351`

## Required Workflow

1. Run `python -m article_factory graph bootstrap`; require PASS and 100% node/edge coverage.
2. Read `memory/graph/SESSION_BOOTSTRAP.md` and every required file it lists, including `SEO_ARTICLE_RULES.md` and the full visual prompt guide.
3. Read `knowledge/agent_memory/products/product-map.md`.
4. For each item below, read the `prompt` and `evidence` files.
5. Write a complete article to the target output path.
6. Use only facts supported by the evidence pack or mark uncertainty explicitly.
7. Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body. Use those inputs silently and write from an expert editorial voice.
8. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
9. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
10. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
11. Match the imported Medium style: direct, practical, conversational, lightly slangy, gamer-aware, no water, no bureaucratic wording, no academic filler.
12. Build every generated-image prompt with `article-editorial-poster-v1`, target Nano Banana Pro by default, assign explicit reference roles, and require a QA score of at least 80/100.
13. After writing all articles, run `python -m article_factory review output\runs\20260804-173351.json`.
14. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Дота 2 интернешнл 2025: полный разбор для Dota 2

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260804-173351\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260804-173351\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260804-173351\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`

### 2. Дота лагает: полный разбор для Dota 2

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260804-173351\02-дота-лагает-полныи-разбор-для-dota-2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260804-173351\02-дота-лагает-полныи-разбор-для-dota-2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260804-173351\02-дота-лагает-полныи-разбор-для-dota-2.md`
