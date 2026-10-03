---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/dota-2-cheats-work.md
heading: "Four parts of a third-party tool"
---

## Four parts of a third-party tool

Most products can be understood as four connected parts:

1.   **Data source.** The program receives visible game events, client state, or claims to access information the normal interface hides.
2.   **Decision logic.** Rules interpret that data: a timer expires, a target enters a range, or a hero ability becomes available.
3.   **Presentation or input.** The result appears in a panel, marker or alert, or the program sends an input sequence.
4.   **Patch dependency.** Any change to the client, hero data, rendering or input handling can break the chain.

Ask a seller to describe each part in plain language. “Smart map” is not a specification. Ask which event creates a marker, whether the marker is an estimate, and how it behaves when the source is missing. A useful answer includes a limitation, not only a benefit.
