# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write exactly two Tier 2 Russian Dota 2 articles for Melonity, each 1000-1200 words, based on a real AI-assisted custom scripting workflow but without code or operational cheat instructions. Article 1: Как написать скрипт для Dota 2 с AI: реальный workflow; explain idea -> public template context -> first wrong TypeScript/archive deliverable -> clarified standalone .js -> configurable UI -> repeatable controlled functional test. Primary keyword: как написать скрипт для Dota 2. Exact anchor once after value: читы дота 2 to https://melonity.gg/; later branded Melonity link, separated by at least two full sections. Article 2: Промпт для Dota 2-скрипта: 5 блоков хорошего ТЗ; focus at least 60% on a five-part observable behavior contract: goal/boundaries, trigger/state transitions, useful settings, context/deliverable format, acceptance test, plus a fillable no-code prompt template. Primary keyword: промпт для Dota 2-скрипта. Exact anchor once after value: читы для dota 2 to https://melonity.gg/; later branded официальная платформа Melonity link, separated by at least two full sections. Both need exact user-specified SEO front matter, 2-4 screenshot placement notes based on local output/video_analysis frames, two generated-image slots carrying the full supplied article-editorial-poster-v1 Nano Banana Pro prompts and QA scores above 80, practical FAQ with five questions, direct gamer-aware tone, no markdown tables. Treat VAC/VAC Live only as a boundary: functional testing proves behavior, not anti-cheat status or account safety. Never give code, private API methods, injection, bypass, masking, evasion, fake safety, detection, current patch, ban, or guarantee claims. Do not duplicate published topics such as best cheats, installation, MapHack, safety, ban risk, or commands.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260804-175441`

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
13. After writing all articles, run `python -m article_factory review output\runs\20260804-175441.json`.
14. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Как написать скрипт для Dota 2 с AI: реальный workflow

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260804-175441\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260804-175441\01-дота-2-интернешнл-2025-полныи-разбор-для-dota-2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260804-175441\01-kak-napisat-skript-dlya-dota-2-s-ai.md`

### 2. Промпт для Dota 2-скрипта: 5 блоков хорошего ТЗ

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260804-175441\02-дота-лагает-полныи-разбор-для-dota-2.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260804-175441\02-дота-лагает-полныи-разбор-для-dota-2.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260804-175441\02-prompt-dlya-dota-2-skripta-5-blokov.md`
