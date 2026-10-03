# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Generate 1 SEO article about Deadlock ESP, integrate cluster.center

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260623-082904`

## Required Workflow

1. Read `SEO_ARTICLE_RULES.md` and `knowledge/agent_memory/products/product-map.md`.
2. For each item below, read the `prompt` and `evidence` files.
3. Write a complete article to the target output path.
4. Use only facts supported by the evidence pack or mark uncertainty explicitly.
5. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
6. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
7. After writing all articles, run `python -m article_factory review output\runs\20260623-082904.json`.
8. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Deadlock ESP Explained: Boxes, Glow and Hero Info

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260623-082904\01-deadlock-esp-explained-boxes-glow-and-hero-info.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260623-082904\01-deadlock-esp-explained-boxes-glow-and-hero-info.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260623-082904\01-deadlock-esp-explained-boxes-glow-and-hero-info.md`
