# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write one English Medium-style SEO article/section describing the functionality of a Deadlock cheat, following the provided Dota 2 example style: direct, practical, feature-focused, conversational. Topic: Deadlock cheat features explained. Cover Aimbot: default, silent, default + silent; FOV, show default FOV, show silent FOV, smooth, target lock; targets players, XP orbs, creeps; hitboxes head, neck, spine, hips; ignore invisible, in air, easing in-out; easing modes easing in-out, static, decreases when aiming, easing out-back; anti frog. Cover ESP: box, player name, hero name, hero icon, health, healthBar, glow, thickness, orbs gear. Cover Misc: FOV changer, world color, disable skybox, skybox color, auto dash jump, auto parry. Game: deadlock. Product: cluster.center. Do not write installation, bypass, evasion, exploit, or implementation steps. No absolute safety guarantees.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260623-134627`

## Required Workflow

1. Read `SEO_ARTICLE_RULES.md` and `knowledge/agent_memory/products/product-map.md`.
2. For each item below, read the `prompt` and `evidence` files.
3. Write a complete article to the target output path.
4. Use only facts supported by the evidence pack or mark uncertainty explicitly.
5. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
6. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
7. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
8. Match the imported Medium style: direct, practical, conversational, gamer-aware, no water, no bureaucratic wording, no academic filler.
9. After writing all articles, run `python -m article_factory review output\runs\20260623-134627.json`.
10. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Deadlock Cheat Feature Glossary

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260623-134627\01-deadlock-cheat-feature-glossary.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260623-134627\01-deadlock-cheat-feature-glossary.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260623-134627\01-deadlock-cheat-feature-glossary.md`
