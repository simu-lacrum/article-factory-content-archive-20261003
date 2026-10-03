---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/write-dota-2-script.md
heading: "Keep the project easy to debug"
---

## Keep the project easy to debug

Prefer small modules: configuration stores values that may change, decision logic decides whether a behavior should run, and the adapter calls the supported Dota API. Give every skip a reason and turn logging off or down for a release build. Do not print account identifiers, tokens, or uncontrolled game objects. A narrow log makes a patch regression easier to reproduce and easier to remove.

When a behavior depends on a hero, mode, or item, state that dependency in the README and in the test matrix. A clean-install test by another creator is stronger evidence than a screenshot of a local workspace. For private-lobby state setup, use the [command reference](https://dota2cheat.com/guides/dota-2-lobby-cheat-commands); for the wider terminology, use the [script types guide](https://dota2cheat.com/guides/dota-2-scripts-guide).
