---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/write-dota-2-script.md
heading: "Define one behavior on paper"
---

## Define one behavior on paper

Write four lines before writing Lua:

1.   **Trigger:** what observable state starts the behavior?
2.   **Inputs:** which hero, target, ability, or resource is read?
3.   **Action:** what one supported order should be attempted?
4.   **Stop condition:** when must the script do nothing?

For example, a practice bot can retreat when health is low and no allied tower is nearby. Add edge cases: the hero is dead, the target disappears, the ability is on cooldown, the order is interrupted, or the current mode does not expose the expected handle.
