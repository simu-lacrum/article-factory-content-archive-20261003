# Evidence-led Article Factory

The writer is Codex. Research is a reproducible local input to `prepare`; no LLM API is needed.

## Current study and commands

The initial English study is `research/seo-20260921`. US / Google is the primary market; GB is a separate comparison cohort. Browser samples record requested country separately from observed location.

```powershell
python -m article_factory research build research/seo-20260921
python -m article_factory research activate research/seo-20260921
python -m article_factory ai-memory export
python -m article_factory graph bootstrap
python -m article_factory prepare --spec "Write a clear English feature explainer" --count 1 --game deadlock --language en
```

Read the generated TASK, prompt, evidence and research contract. Write the article yourself. Review the actual text, then run the automated review. Automated PASS does not prove facts, original value or an engaging voice.

`--llm template` is a compatibility alias that creates a Codex brief. It cannot produce a fake finished article. `review` exits 2 for missing articles, errors or unresolved warnings. It does not treat an empty manifest as success.

## Data contracts

- `study.json`: keywords, reader jobs, page types, site routing, observed SERPs, editorial hypotheses and policies. Validate before building.
- `raw/`: retained public HTML and search observations. Never store account details, cookies or credentials here.
- `pages/`: parsed competitor pages with URL, capture time, hash, language, extraction method, main text and link contexts. Blocked pages stay failed; a missing page is not evidence.
- `owned-pages/` and `owned-inventory.json`: existing site coverage. Keep owned pages out of rival usage distributions.
- `core.json`: derived, versioned research contract. Per-game JSON/CSV files are convenient exports.
- `semantic-terms.csv`: observed co-occurrences and editor-proposed concepts are labeled separately. “LSI” is a familiar shorthand here, not a claim about a Google keyword system.
- `reviewed-semantic-terms.csv` and `SEMANTIC_VOCABULARY.md`: the vocabulary actually selected for each reader job, with usage notes. A group's `reviewed_semantic_terms` entries require a nonempty term and note; duplicate normalized terms are rejected. Build checks each exact phrase against the eligible page corpus and retains sources and document counts. An absent phrase remains an explicitly unobserved editorial concept. These are vocabulary observations, not volume or verified capability claims.
- Vocabulary observations cover selected main text, not title/metadata. For ambiguous words, an optional reviewed `source_urls` list limits matching to the relevant pages, including redirect/canonical aliases. For example, soul `secure` must not gain evidence from payment security or Secure Boot copy. A source list does not override corpus exclusions or language/site filtering.
- `anchor-examples.csv`: links on sampled pages, with navigation/editorial context and internal/outbound relationship. Repeated rows across clusters represent different keyword classifications; do not sum them as unique backlinks.
- `keyword-usage.csv`: observed phrase counts by page and corpus. `intent_matched_sample` uses manually selected pages from the target query's results; `general_competitor_sample` may include broader product pages. Main-text counts include extracted headings and link text. Counts are observations, not targets.
- `metric-requests.csv` and `keyword-lists/`: missing-volume requests for the primary and optional secondary country, under the selected provider policy. These are requests, not importable measurement evidence. Reported zero is retained as a known value. Lists regenerate with `research build`.
- Each keyword has an optional `query_role`: article_candidate, product_access, community_research, implementation_research or ambiguous_research. An article target must be an article_candidate. `search_facets` describe literal modifiers such as free/download/trial; they do not establish search volume or offer availability. Per-game CSVs retain roles, proposed page types and discovery notes.
- `writing_contract` separates article candidates from `non_article_queries`; the latter are routing context, not required article keywords. `research_landing` groups stay out of automatic article selection. Publish an access/download destination only after verifying the actual offer, ownership and terms. A free trial is not a permanent free tier.
- `writing_contract.related_terms` uses only the reviewed vocabulary, including usage notes and observation status. Raw co-occurrence terms are never promoted automatically into the writing brief; frequent filler, navigation and payment words are not meaningful merely because they recur. Parent contracts retain their sections' reviewed vocabulary. If no reviewed list exists, this field stays empty instead of falling back to noise.
- Autocomplete observations must exclude visible search-history suggestions, retain seed/date/session limitations and stay separate from volume. Typing a phrase into Google and receiving results does not itself make that phrase observed keyword discovery. Exact phrases found in publisher copy are labeled as publisher wording, not proven demand.

Short nonempty HTTP-200 captures remain analyzable. Below 80 words is a context-review flag, not a failure or a minimum article length: a feature description or product card can be complete and short. Check extraction notes and page type before using counts.

Fetched HTML can be re-extracted without a network request with `python scripts/reparse_research_pages.py research/seo-20260921`. The dated seed/enrichment scripts reproduce this study's editorial assumptions, not a current SERP. Do not run the seed script to refresh a study with new manual edits; create a new dated study instead.

When a reviewed capture contains unrelated widgets, add `extraction_rules[url]` with a CSS `content_selector`, positive integer `expected_matches` (default 1), review date and reason. The selector may cover multiple disjoint content blocks, such as `h1, .entry-content`; nested matches are rejected to avoid double counting. Fetch and reparse both apply the rule and retain it in page metadata. A changed match count or empty selection fails rather than silently using the whole body. Review the selected text before relying on keyword counts. This is a documented per-page correction, not a universal site selector or a word-count requirement.

`document_h1` records H1 text from the complete fetched HTML, separately from headings inside the extracted content. H1 counts use this field: a hero heading outside `<main>` must not be reported as absent. Body/intro and H2–H3 counts still use the selected content. Static HTML does not establish rendered visibility; these counts are not a visual audit.

## Real frequency data

Use a real provider export. Required CSV columns:

```csv
query,game,language,country,engine,provider,period,match_type,volume
```

`country` uses US or GB, `period` is YYYY-MM, and match_type is exact, phrase, broad, provider_grouped or provider_unspecified. The last value explicitly means the source does not document match/close-variant semantics. Empty volume means unknown; numeric zero means the provider reported zero. Nonnegative whole numbers only. Do not copy an arbitrary search-result count into volume.

Keep `source_url`, `captured_at` and `volume_basis` with manually transcribed public-provider observations. Semrush volume is a modeled rolling 12-month monthly average, not an exact count of searches. If a public tool does not display its measurement/report month, set `period_basis=capture_month` and use the retrieval month in `period`; leave the measurement-window end unknown. This labels the collection cohort without inventing a data period. The default `period_basis=provider_report_month` is appropriate only when the report identifies that month. A metric policy must select the same period basis. CSV exports include provenance alongside numeric values.

```powershell
python -m article_factory research import-metrics research/seo-20260921 --input research/provider-us.csv
```

Set `metric_policy.provider`, `.period`, and `.match_type` in study.json to the intended cohort, then build again. Other provider/month/match records remain visible but cannot silently replace the selected cohort. Import snapshots are retained under metric-imports. Repeat UK as a separate study with country GB; do not sum US and UK and call that US demand.

When deliberately combining complementary public tools, `metric_policy.provider_order` may list an explicit preference order. The first matching source supplies the row; values are never averaged or added. Market, period and period basis must still match. Every selected row keeps its actual source. The current study prioritizes Semrush's volume checker, then its Keyword Magic public sample for gaps.

Project convenience thresholds are 1–100 low, 101–1000 medium, above 1000 high monthly searches. They are configurable and are not a universal SEO standard. Long-tail describes specificity; it does not imply low frequency. An unknown metric stays unknown.

## Incoming anchors

To study competitors' backlinks, import a provider sample:

```csv
source_url,target_url,anchor,target_keyword,provider,checked_at,rel
```

```powershell
python -m article_factory research import-backlinks research/seo-20260921 --input research/backlinks.csv
```

This imports a selected snapshot; it does not claim to discover every backlink. Internal links are excluded, repeated source/target/anchor triples deduplicated. Record exact, partial, branded, naked URL, generic and image/empty anchors separately. A naked URL and “click here” are both non-keyword anchors but serve different purposes. Do not prescribe percentages copied from a rival: editorial context and an honestly described destination decide the anchor. Qualify paid links according to the publishing platform and Google's guidance.

Public examples can also be checked with `python scripts/verify_public_backlinks.py research/seo-20260921`, using the manually selected `backlink-public-candidates.json`. It writes `public-backlink-observations.json`, a separate `public-backlink-sample.json`/CSV and `public-backlink-summary.json`. These remain distinct from `backlinks.json` in the built core; do not pool their ratios. A 403 or hidden-link placeholder is unverified, not a removed link. Retain the observed href, rel, context, capture time and HTML hash. The parser's `editorial` placement means a body link outside detected navigation, not an endorsement or a confirmed independent editorial decision. UGC complaints and automated reputation reports need their own context labels. Generate the human report and shared cache with `python scripts/export_public_backlink_report.py research/seo-20260921`, then rebuild the core. Reciprocal checks cover only retained target pages, not an entire domain.

## Clustering and publication decisions

Import retained SERP observations without replacing previous research:

```powershell
python -m article_factory research import-serps research/seo-20260921 --input research/observations.json
```

Input is a JSON list, or an object with `snapshots`. Each snapshot requires query, game, language, engine, captured_at, method and result URLs. Record requested/observed country, session_cohort and source_file. A browser heading order is `observed_heading_order`, not an asserted organic rank; leave rank null when it is unknown. Import validates all rows before writing and retains the input under `serp-imports/`. Reimporting the same snapshot is idempotent.

Automatic SERP overlap pairs require at least five sampled eligible results per query and three shared normalized URLs. Same date, engine, language, country request/observation, collection method and session are required. Every qualifying pair is retained, even when one query belongs to multiple pairs; there is no forced partition or transitive bridge merge. A-B and B-C do not validate A-C. The compatibility status `serp_validated` means only that the shared-URL threshold passed; `validation_scope` explicitly excludes intent equivalence and publication approval. Generic vendor hubs may overlap across distinct features. URL query parameters with semantic meaning are preserved; tracking parameters and fragments are removed. Video, repository and unrelated-intent results remain observations, not editorial-page overlap evidence.

Within a cohort, only the latest capture of a query participates in grouping; repeated captures cannot validate a cluster by themselves. `validated_query_subsets` records only the tested members, never promotes all editorial variants. Counts of page types retain separate samples so repeated URLs across providers/dates are visible. Running an editor-proposed query does not itself prove demand or turn it into a provider-discovered phrase.

An optional `article_target_query` must be a keyword in the group. Its own `article_target.volume` stays unknown when only the broader family has a measurement. Topic generation uses the article target for the brief. `intent_matched_urls` and `usage_phrases` allow comparisons against the right page type and natural shorter terms. `source_policies[url].exclude_from_fact_evidence` excludes a source from writing passages (including supplements), while retaining it for on-page analysis. A ranking competitor is not automatically a trustworthy factual source.

Editorial groups remain hypotheses until evidence validates them. A query with a commercial or repository SERP does not automatically deserve a blog post. Use category/product pages for transactional intent, feature explainers for definition/distinction questions, comparison pages for supported purchasing criteria, and separate official-command references from third-party software.

Each planned page needs a different reader job and a concrete new contribution. Do not create a page for every spelling, hero or modifier. Update a matching live URL first. When a narrow topic cannot stand alone, make it a subsection. For multiple owned domains, assign one primary destination for each job and give any additional page a materially different purpose; do not cross-post near-identical articles as a link scheme.

Use `publication_action=include_as_section` with `section_parent_id` to retain a narrow group inside a parent article. The parent must be a standalone writing/update target in the same game and language; nested/self-parent sections are rejected. `supporting_sections` carries the reader jobs and evidence pointers into the parent's writing contract. Children are not selected as standalone writing tasks. `update_article` requires an `existing_url`; do not imply an existing page without one.

Optional `evidence_terms` are reviewed, nonempty phrases for finding passages when a source uses different word order from the target query. A section's terms apply only to that section's listed source URLs (including redirect aliases), not to every page in the parent's corpus. Source-exclusion policies still take precedence. This lets a specific FOV description reach an article about soul/player targeting without broadening retrieval to unrelated pages.

## Editorial acceptance

An HTTP 200 response can still be a login/access screen. After inspection, mark such a URL with `source_policies[url].exclude_from_onpage_analysis: true` and `exclude_from_fact_evidence: true`. The saved capture remains auditable, but it contributes no competitor phrase, semantic-term or anchor observations. Requested, final and canonical URL aliases are checked. Coverage distinguishes successful captures, excluded captures and usable English competitor pages. A short legitimate feature description is not excluded just because it is short.

Preserve each group's specific `publication_gate` through the core and writing contract. For example, a console-command brief must verify current syntax, effects and supported practice/lobby context before drafting examples. Broad `cheat commands` queries belong to legitimate command-reference scope; a vocabulary-only article does not satisfy that task. Third-party feature pages remain high-level explanations without implementation or evasion steps.

Before publication, a human/Codex editorial review must record:

1. The exact reader question and whether the opening answers it.
2. A source for every material claim, distinguishing a vendor statement from an independent test. Recheck changing features, prices and availability; capture time is not proof of claim truth.
3. A concrete original contribution: a useful distinction, annotated comparison, sourced limitation or worked hypothetical example.
4. Why this URL is distinct from existing site coverage and nearby drafts.
5. A read-aloud edit: remove interchangeable introductions, repeated conclusions, exaggerated slang, fake experience and unnecessary sections.
6. Natural keyword/link use, correct product mapping, commercial disclosure where relevant, metadata, ending FAQ and the full canonical visual contract.

Comparisons state methodology and commercial interest, acknowledge competitor strengths, and say “not publicly confirmed” for unknown cells. No fabricated winner, safety guarantee, review score or testing record. Article prose uses lists instead of Markdown tables.

GEO means clear entities, direct answers, attributable claims and useful accessible content here. There is no fixed 134–167-word passage requirement, special Google AI schema or required llms.txt. FAQ remains a reader feature; commercial FAQ content should not be promised Google FAQ rich results.

## Primary guidance checked September 21, 2026

- [Google: people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content): original value and meeting the reader's need; no preferred word count.
- [Google: generative AI search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide): ordinary SEO fundamentals; no special chunk size or llms.txt requirement.
- [Google: link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable): descriptive contextual links without forced keyword repetition.
- [Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies): avoid keyword stuffing, doorway abuse, scaled low-value pages and manipulative links.
- [Google: qualifying outbound links](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links): paid links and user-generated links have different rel attributes.

These primary sources take precedence over unsupported numeric heuristics in reusable SEO skills.
