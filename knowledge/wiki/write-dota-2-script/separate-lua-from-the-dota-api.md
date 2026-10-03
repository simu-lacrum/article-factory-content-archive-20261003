---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/write-dota-2-script.md
heading: "Separate Lua from the Dota API"
---

## Separate Lua from the Dota API

Lua gives you variables, tables, functions, and control flow. The Dota API gives you game-specific handles and calls. Keep those layers separate in notes and code. A normal Lua tutorial cannot prove that a Dota function exists in the current Workshop build, and an old snippet may reference a removed field.

![Image 3: Dota 2 script logic and configuration example](https://dota2cheat.com/assets/dota2/dota2-c3ebd928845db5e45465d658.webp)

Use the API reference for names and parameters, then log the values you actually receive in the current environment. Avoid copying an undocumented cheat-platform API whose permissions and update cycle have no relationship to Workshop support.
