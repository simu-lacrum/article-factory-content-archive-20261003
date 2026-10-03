# Product Requirement: Universal Article Intelligence System

## Non-negotiable goal

This project must become a universal, fully working, thoughtfully designed content-intelligence system, not a one-off script or a narrow first MVP.

The current Dota 2 / CS2 / Melonity use case is the first domain. The architecture must stay reusable for other games, products, languages, markets, and SEO datasets.

## Required end state

A user can give a natural task such as:

> Generate 10 SEO articles of N volume, in this style, with native integration of my project.

The system should then:

1. Read clustered semantic cores and published-article history.
2. Select non-duplicate article topics with strong SEO potential.
3. Retrieve real evidence from local knowledge, URLs, markdown, CSV, PDF, and future sources.
4. Build an evidence pack for each article.
5. Let Codex generate a useful, human, SEO-structured article from the evidence pack without requiring an external LLM API.
6. Integrate advertising naturally without unsupported claims.
7. Run quality/fact/risk checks.
8. Save prompts, evidence, articles, manifests, and review reports.
9. Export durable memory for `ai-memory`, Obsidian, or another MCP/wiki-memory layer.

## Design principles

- Local-first: the knowledge base must work without paid SaaS.
- Source-first: no article is generated before evidence retrieval.
- Universal schema: domain-specific facts live in data/config, not hardcoded code paths.
- Auditable output: every generated article must have a manifest and evidence pack.
- Incremental memory: new sources update the wiki and topic engine without starting over.
- Publication memory: already published topics must not be selected again by default.
- Safety and accuracy: current facts must be sourced; unsupported guarantees are rejected.

## Current domain rules

- Dota 2 and CS2 are current games.
- Melonity is current product/brand context.
- The system may support SEO terms from the brand context, but must not generate operational instructions for anti-cheat evasion, exploit use, vulnerability abuse, or cheat implementation.
- Product claims must be limited to facts present in the knowledge base.
