---
source: PRODUCT_REQUIREMENTS.md
heading: "Design principles"
---

## Design principles

- Local-first: the knowledge base must work without paid SaaS.
- Source-first: no article is generated before evidence retrieval.
- Universal schema: domain-specific facts live in data/config, not hardcoded code paths.
- Auditable output: every generated article must have a manifest and evidence pack.
- Incremental memory: new sources update the wiki and topic engine without starting over.
- Publication memory: already published topics must not be selected again by default.
- Safety and accuracy: current facts must be sourced; unsupported guarantees are rejected.
