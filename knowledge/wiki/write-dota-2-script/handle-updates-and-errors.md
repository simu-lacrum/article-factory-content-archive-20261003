---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/write-dota-2-script.md
heading: "Handle updates and errors"
---

## Handle updates and errors

Record the Dota build, hero, mode, dependencies, and date for every release. Validate handles before using them, provide a clear fallback when an action is unavailable, and keep configuration values outside decision logic. A readable error is more useful than silent failure or a large uncontrolled object dump.

Do not call a script universal because one function name exists. It is supported only when the documented scenarios pass on the current build and known exceptions are stated. Re-run the test matrix after a hero, item, or API update.
