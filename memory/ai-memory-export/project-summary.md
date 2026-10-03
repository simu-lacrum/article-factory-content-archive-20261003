# Project Summary

The workspace is a local knowledge base for generating SEO articles about Dota 2, Deadlock, and CS2 from factual sources.

Product mapping: Dota 2 articles integrate Melonity. Deadlock and CS2 articles integrate cluster.center.

Core rule: articles must be built from evidence packs retrieved from local markdown, CSV semantic cores, uploaded PDFs/text, and materialized link sources. Persistent URLs are copied into `knowledge/agent_memory/sources/` as markdown before indexing, so future agents read local files instead of opening links. The generator should avoid unsupported current facts and should not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheats.

Public-facing voice rule: final article bodies must not mention "local sources", "local evidence", "evidence pack", "knowledge base", or similar internal-provenance wording. Use the evidence silently and write from an expert editorial perspective: practical, conversational, lightly slangy, gamer-aware, and based on experience.

Visual rule: number generated conceptual assets across each run and alternate odd branch B (warm narrative) with even branch A (tactile industrial), so a one-cover run uses the new reference family. Real screenshots do not consume an index. Every B asset must actually attach two persistent warm-story references and pass 4/5 fidelity. Use Cluster #635FD5 and Melonity #FF1469 by branch: one small 3–8% semantic accent in A; the dominant 35–70% field replacing yellow/amber in B.

Recommended flow:
1. Ingest new CSV/markdown/PDF/link sources.
2. Rebuild topic ideas from semantic clusters.
3. Select topics that balance search demand, lower difficulty, product fit, and non-duplication.
4. Generate evidence pack and article prompt.
5. Use an LLM provider only after evidence is assembled.
6. Review generated articles before publication and mark published topics in `published/articles.csv`.
