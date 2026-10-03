# Codex Article Task

Codex writes the final articles without an external LLM provider.

## User Spec

Create the ten safe, high-level Hashnode technical articles from the supplied campaign brief. Each article must contain 800–1000 body words excluding SEO front matter and image comments, use the specified English or Russian language, include exactly one assigned commercial target link once, and avoid operational evasion or implementation details.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260801-130438`

## Required Workflow

1. Read `SEO_ARTICLE_RULES.md` and the product map.
2. Use the generated evidence corpus plus the specific product memories and primary technical sources named in the campaign brief.
3. Write the ten exact adjacent-angle articles listed below.
4. Include SEO front matter, subtitle, quick answer, 4–6 substantive H2 sections, Sources, three image slots, conclusion, and a final four-question FAQ.
5. Keep Dota 2 mapped to Melonity and CS2/Deadlock mapped to cluster.center.
6. Run `python -m article_factory review output\runs\20260801-130438.json` and fix every finding.

## Articles

1. `01-external-vs-internal-cs2-tools-architecture.md` — English, CS2 architecture comparison.
2. `02-why-dota-2-automation-is-harder-than-it-looks.md` — English, Dota 2 event-system complexity.
3. `03-verify-cs2-tool-download-before-running.md` — English, defensive Windows download verification.
4. `04-deadlock-aim-esp-design-technical-breakdown.md` — English, Deadlock aim and ESP design.
5. `05-kak-ustroen-esp-v-cs2-dannye-filtry-vizual.md` — Russian, CS2 ESP pipeline.
6. `06-dota-2-tool-setup-safer-configuration-workflow.md` — English, Dota 2 configuration lifecycle.
7. `07-fov-sglazhivanie-kak-ustroen-aimbot-cs2.md` — Russian, CS2 FOV and smoothing concepts.
8. `08-cs2-triggerbot-logic-timing-hitboxes-latency.md` — English, TriggerBot state machine.
9. `09-how-multi-game-tools-separate-shared-game-logic.md` — English, multi-game platform architecture.
10. `10-kak-chitat-katalog-igrovyh-instrumentov.md` — Russian, technical catalog reading guide.

## Finish Check

The corrected run manifest is `C:\Users\User\Desktop\articles\output\runs\20260801-130438.json`. The human-readable article index is `C:\Users\User\Desktop\articles\output\codex_tasks\20260801-130438\ARTICLE_INDEX.md`.
