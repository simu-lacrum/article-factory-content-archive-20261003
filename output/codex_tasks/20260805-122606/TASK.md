# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create the exact eight standalone Tier 2 articles in the user brief dated 2026-08-05: Dota 2 AI script QA (en), Deadlock comparison criteria (ru), Deadlock information triage (en), Deadlock phase profiles (ru), Foxhole logistics bottlenecks (ru), Foxhole artillery coordination (en), GTA 5 RP compatibility (en), and GTA 5 RP menu profiles (ru). Each must follow its assigned target URL and exact anchors, include supplied visual notes and prompt, and remain non-operational and risk-aware.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260805-122606`

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
13. After writing all articles, run `python -m article_factory review output\runs\20260805-122606.json`.
14. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. How to QA an AI-Generated Dota 2 Script Before You Trust It

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\.codex\attachments\65c6ac2c-ac9b-4a85-bac1-213c623d7aca\pasted-text-1.txt`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\01-ai-dota-2-script-qa.md`

### 2. Как сравнивать читы для Deadlock: критерии важнее громкого топа

- Game: `deadlock`
- Language: `ru`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\02-kak-sravnivat-deadlock.md`

### 3. Deadlock Information Triage: What Matters First in a 6v6 Fight

- Game: `deadlock`
- Language: `en`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\03-deadlock-information-triage.md`

### 4. Один профиль на весь матч не работает: настройки Deadlock по фазам

- Game: `deadlock`
- Language: `ru`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\04-nastroiki-deadlock-po-fazam.md`

### 5. Где ломается логистика Foxhole: путь ресурса от добычи до фронта

- Game: `foxhole`
- Language: `ru`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\05-logistika-foxhole.md`

### 6. Foxhole Artillery Coordination: The Information Checklist Before Every Salvo

- Game: `foxhole`
- Language: `en`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\06-foxhole-artillery-coordination.md`

### 7. GTA 5 RP Tool Compatibility: Check the Platform Before the Feature List

- Game: `gta`
- Language: `en`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\07-gta-5-rp-tool-compatibility.md`

### 8. Три профиля вместо перегруженного меню: как организовать GTA 5 RP

- Game: `gta`
- Language: `ru`
- Prompt: same fixed user brief above
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260805-122606\shared-tier2-evidence.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260805-122606\08-profili-gta-5-rp.md`
