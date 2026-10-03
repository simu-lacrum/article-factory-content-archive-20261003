# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Написать одну русскую SEO-статью 800–1000 слов с заголовком «Как работает VAC Live в Dota 2 сейчас: факты без мифов». Primary keyword: VAC Live Dota 2. Угол: объяснить в настоящем времени реальную многоуровневую защиту Dota 2 — подтверждённый VAC на странице Steam, клиентскую сигнатурную проверку по Steam Support, авторитетный сервер и наблюдаемую игровую телеметрию как экспертную модель из графа, репорты и Overwatch, Game Ban/VAC Ban, honeypot 2023, сокращение client state и связывание аккаунтов. В первых 100 словах прямо уточнить: Valve не подтверждала для Dota бренд VAC Live/VACNET или остановку матча по модели CS2; термин используется в поисковом запросе и отраслевых статьях как неофициальное название live-серверных проверок. Описывать работу именно сейчас, историю использовать только как доказательство действующих инженерных подходов. Одна нативная ссылка Melonity после технического контекста; без обещаний безопасности, Humanizer-настроек, обхода, маскировки или инструкций. 3 image slots, 5–7 H2, 5–6 FAQ, без таблиц. Использовать graph nodes VAC, VAC-Live/server checks и источники source:21, source:29 только как экспертную модель; неподтверждённые точные сигналы, мгновенные баны и Dota VACNET не утверждать. Актуальность интернет-фактов проверена 23 июля 2026 года по Steam Store, Steam Support и официальным материалам Dota 2.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260723-110750`

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
10. After writing all articles, run `python -m article_factory review output\runs\20260723-110750.json`.
11. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Как работает VAC Live в Dota 2 сейчас: факты без мифов

- Game: `dota2`
- Language: `ru`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260723-110750\01-kak-rabotaet-vac-live-v-dota-2-seichas.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260723-110750\01-kak-rabotaet-vac-live-v-dota-2-seichas.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260723-110750\01-kak-rabotaet-vac-live-v-dota-2-seichas.md`
