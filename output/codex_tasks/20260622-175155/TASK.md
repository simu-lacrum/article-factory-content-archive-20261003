# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Сгенерируй 3 SEO статьи объемом 1800-2400 words, в экспертном живом стиле, с нативной интеграцией Melonity

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260622-175155`

## Required Workflow

1. For each item below, read the `prompt` and `evidence` files.
2. Write a complete article to the target output path.
3. Use only facts supported by the evidence pack or mark uncertainty explicitly.
4. Keep native Melonity integration grounded and avoid unsupported guarantees.
5. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
6. After writing all articles, run `python -m article_factory review output\runs\20260622-175155.json`.
7. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260622-175155\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260622-175155\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260622-175155\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

### 2. Dota 2 Skin Changer in 2026: Free Tools, Ban Risks and Premium Alternatives

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260622-175155\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260622-175155\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260622-175155\02-dota-2-skin-changer-in-2026-free-tools-ban-risks-and-premium-alternatives.md`

### 3. Dota 2 Couriers: Best Unusual Couriers, Courier Value and Why Courier Info Wins Games

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260622-175155\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260622-175155\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260622-175155\03-dota-2-couriers-best-unusual-couriers-courier-value-and-why-courier-info-wins-games.md`
