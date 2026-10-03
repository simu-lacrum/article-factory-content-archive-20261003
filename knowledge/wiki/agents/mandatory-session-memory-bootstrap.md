---
source: AGENTS.md
heading: "Mandatory Session Memory Bootstrap"
---

## Mandatory Session Memory Bootstrap

This section applies to **every new Codex dialog in this workspace**, including article work, research, code changes, maintenance, and follow-up tasks. It must run before planning or taking task actions.

1. From the project root, run:

```powershell
python -m article_factory graph bootstrap
```

2. Require `status: PASS`, node coverage `100%`, and edge coverage `100%`. The command deterministically traverses every connected component, every node (including isolated nodes), and validates every edge. Reading a random subset, only the Mermaid file, or only search results does not satisfy this requirement.
3. Read `memory/graph/SESSION_BOOTSTRAP.md` completely.
4. Read every file listed under `Required reading` completely. This includes the canonical visual guide at `knowledge/agent_memory/rules/article-visual-prompt-guide.md`.
5. Do not continue if coverage is incomplete, a mandatory instruction node is absent, or a required file is missing. Fix the graph/bootstrap problem first.
6. Re-run the bootstrap after any change to graph facts, required instructions, or the source set.

For article and visual tasks, all image prompts must follow `article-editorial-poster-v1`; Nano Banana Pro / `gemini-3-pro-image` is the default target model. Number generated assets across the current run and alternate B/A (odd = warm narrative B, even = tactile industrial A); real screenshots do not consume an index. Every B prompt must actually attach two files from the persistent warm-story reference set, assign one as composition and one as render/palette/typography, and pass 4/5 fidelity. Use exact mapped colors: Cluster `#635FD5`, Melonity `#FF1469`; in A they are small 3–8% semantic accents, while in B they replace the dominant yellow/amber field and occupy roughly 35–70% of the frame. Every reference image must have an explicit role, and every final prompt must pass the guide's minimum contract and score at least 80/100.
