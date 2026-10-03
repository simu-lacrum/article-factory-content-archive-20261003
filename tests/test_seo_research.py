import json
import tempfile
import unittest
from pathlib import Path

from article_factory.generator import parse_spec, generate_articles
from article_factory.db import KnowledgeDb
from article_factory.graph import export_graph
from article_factory.quality import word_count, strip_front_matter, review_manifest, review_article
from article_factory.research.models import canonical_url, frequency_band, validate_metric, validate_study, scope_for
from article_factory.research.pages import extract_page, phrase_count, anchor_kind
from article_factory.research.analysis import serp_groups, term_profile, anchor_profile
from article_factory.research.service import choose_metric, import_metrics, import_backlinks, import_serps, build_study, save_json, research_evidence, export_metric_requests, writing_contract


class ResearchTests(unittest.TestCase):
    def test_reviewed_vocabulary_replaces_raw_noise_and_keeps_unknowns_explicit(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / 'research/test-study'
            study = self.minimal_study()
            entries = [{'term': 'soul orb', 'usage_note': 'Name the target without claiming an outcome.', 'source_urls': ['https://a.test/']},
                       {'term': 'camera view', 'usage_note': 'Editorial contrast; no competitor observation asserted.'}]
            study['clusters'][0]['reviewed_semantic_terms'] = entries
            save_json(directory / 'study.json', study)
            for name in ('a', 'b'):
                page = extract_page("<html lang='en'><main><p>No no so so about about. Soul orb targeting.</p></main></html>", f'https://{name}.test/')
                page['http_status'] = 200
                save_json(directory / f'pages/{name}.json', page)
            core = build_study(directory)
            self.assertIn('no', [t['term'] for t in core['clusters'][0]['corpus_related_terms']])
            save_json(root / 'config/research.json', {'active_study': 'research/test-study'})
            terms = writing_contract(root, {'source_kind': 'seo_research', 'source_ref': 'souls'})['related_terms']
            self.assertEqual([t['term'] for t in terms], ['soul orb', 'camera view'])
            self.assertEqual(terms[0]['document_frequency'], 1)
            self.assertEqual(terms[0]['sources'], ['https://a.test/'])
            self.assertEqual(terms[1]['sources'], [])
            self.assertEqual(terms[1]['origin'], 'editorial_concept_not_observed_in_sample')
            self.assertIn('Name the target', (directory / 'reviewed-semantic-terms.csv').read_text(encoding='utf-8-sig'))
            entries.append({'term': 'SOUL ORB', 'usage_note': 'Duplicate normalized phrase.'})
            with self.assertRaisesRegex(ValueError, 'Duplicate reviewed'):
                validate_study(study)

    def test_cheat_command_queries_keep_practice_scope(self):
        for game in ('cs2', 'dota 2', 'deadlock'):
            self.assertEqual(scope_for(game + ' cheat commands'), 'legitimate_commands')
        self.assertEqual(scope_for('deadlock auto parry cheat'), 'third_party_software')

    def test_access_screen_is_captured_but_not_a_competitor_article(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            study['source_policies'] = {'https://a.test/': {'exclude_from_onpage_analysis': True, 'exclude_from_fact_evidence': True}}
            study['clusters'][0]['intent_matched_urls'] = ['https://a.test/']
            save_json(root / 'study.json', study)
            page = extract_page("<html lang='en'><main><h1>Access restricted</h1><p>Sign in for soul features.</p></main></html>", 'https://a.test/private')
            page.update(http_status=200, requested_url='https://a.test/')
            save_json(root / 'pages/a.json', page)
            core = build_study(root)
            self.assertEqual(core['coverage']['pages_fetched'], 1)
            self.assertEqual(core['coverage']['page_failures'], 0)
            self.assertEqual(core['coverage']['pages_excluded_from_onpage_analysis'], 1)
            self.assertEqual(core['coverage']['english_competitor_pages'], 0)
            self.assertEqual(core['clusters'][0]['sampled_pages'], 0)
            self.assertEqual(core['clusters'][0]['intent_matched_term_usage'][0]['pages'], [])
            self.assertEqual(core['clusters'][0]['anchors']['examples'], [])

    def test_specific_publication_gate_survives_build_and_contract(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            gate = 'Verify current command syntax before drafting examples.'
            study['clusters'][0]['publication_gate'] = gate
            directory = root / 'research/test-study'
            save_json(directory / 'study.json', study)
            build_study(directory)
            save_json(root / 'config/research.json', {'active_study': 'research/test-study'})
            self.assertEqual(writing_contract(root, {'source_kind': 'seo_research', 'source_ref': 'souls'})['publication_gate'], gate)

    def test_returning_topic_revives_retired_but_preserves_used_status(self):
        with tempfile.TemporaryDirectory() as temporary:
            db = KnowledgeDb(Path(temporary) / "db.sqlite")
            db.init()
            topic = dict(game="cs2", language="en", title="Triggerbot terms", source_kind="seo_research", source_ref="cs2-triggerbot")
            ident = db.upsert_topic_idea(**topic)
            db.conn.execute("UPDATE topic_ideas SET status='retired' WHERE id=?", (ident,))
            db.upsert_topic_idea(**topic)
            self.assertEqual(db.conn.execute("SELECT status FROM topic_ideas WHERE id=?", (ident,)).fetchone()[0], "new")
            db.mark_topics_used([ident])
            db.upsert_topic_idea(**topic)
            self.assertEqual(db.conn.execute("SELECT status FROM topic_ideas WHERE id=?", (ident,)).fetchone()[0], "used")
            db.close()

    def test_graph_export_does_not_silently_truncate_memory(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            db_path = root / ".article-factory" / "articles.db"
            db = KnowledgeDb(db_path)
            db.init()
            db.conn.execute("INSERT INTO sources(path,kind,sha256) VALUES('source.csv','csv','test')")
            db.conn.executemany("INSERT INTO semantic_clusters(source_id,game,cluster,main_query) VALUES(1,'cs2',?,?)", [(f"cluster {i}", f"query {i}") for i in range(501)])
            db.conn.executemany("INSERT INTO topic_ideas(game,language,title,source_kind) VALUES('cs2','en',?,'test')", [(f"topic {i}",) for i in range(121)])
            db.conn.commit()
            db.close()
            export_graph(db_path, root / "graph", limit_topics=120)
            graph = json.loads((root / "graph" / "knowledge-graph.json").read_text(encoding="utf-8"))
            self.assertEqual(sum(n["kind"] == "semantic_cluster" for n in graph["nodes"]), 501)
            self.assertEqual(sum(n["kind"] == "topic" for n in graph["nodes"]), 121)
            ids = {n["id"] for n in graph["nodes"]}
            self.assertTrue(all(e["source"] in ids and e["target"] in ids for e in graph["edges"]))

    def minimal_study(self):
        return {"schema_version": 1, "id": "test-study", "captured_at": "2026-09-21", "market": {"country": "US", "engine": "google"},
                "keywords": [{"query": "deadlock souls aimbot", "game": "deadlock", "language": "en", "cluster_id": "souls", "discovery": "editorial_expansion", "sources": []}],
                "clusters": [{"id": "souls", "game": "deadlock", "language": "en", "primary_query": "deadlock souls aimbot", "title": "Soul features", "reader_job": "Separate targets", "original_value": "Target versus action", "semantic_terms": ["secure", "orb"], "competitor_urls": ["https://a.test/", "https://b.test/"]}], "serps": []}

    def test_build_keeps_us_and_gb_page_types_separate(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            for country, page_type in (("US", "product"), ("GB", "guide")):
                study["serps"].append({"query": "deadlock souls aimbot", "game": "deadlock", "language": "en", "engine": "google", "method": "browser_dom", "captured_at": "2026-09-21", "country_requested": country, "results": [{"url": "https://a.test/", "type": "organic", "page_type": page_type}]})
            save_json(root / "study.json", study)
            core = build_study(root)
            self.assertEqual(core["keywords"][0]["page_type_evidence"]["counts"], {"product": 1})
            self.assertIsNone(core["keywords"][0]["volume"])
            self.assertTrue((root / "semantic-terms.csv").is_file())

    def test_acquisition_queries_do_not_become_article_requirements(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            study["clusters"][0]["publication_action"] = "write_article"
            study["keywords"].append({**study["keywords"][0], "query": "deadlock souls aimbot free download", "query_role": "product_access", "search_facets": ["free", "download"], "recommended_page_type": "verified_product_or_category"})
            directory = root / "research/test-study"
            save_json(directory / "study.json", study)
            build_study(directory)
            save_json(root / "config/research.json", {"active_study": "research/test-study"})
            contract = writing_contract(root, {"source_kind": "seo_research", "source_ref": "souls"})
            self.assertEqual([k["query"] for k in contract["keywords"]], ["deadlock souls aimbot"])
            self.assertEqual(contract["non_article_queries"][0]["query_role"], "product_access")
            self.assertIn("free | download", (directory / "deadlock-core.csv").read_text(encoding="utf-8-sig"))
            self.assertIn("free | download", (directory / "query-routing.csv").read_text(encoding="utf-8-sig"))
            study["clusters"][0]["article_target_query"] = "deadlock souls aimbot free download"
            with self.assertRaisesRegex(ValueError, "article target"):
                validate_study(study)
            study["clusters"][0]["publication_action"] = "research_landing"
            validate_study(study)

    def test_sections_reach_parent_contract_without_becoming_standalone_topics(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            parent = study["clusters"][0]
            parent["publication_action"] = "write_article"
            child = {**parent, "id": "section", "title": "Aiming FOV", "publication_action": "include_as_section", "section_parent_id": "souls"}
            study["clusters"].append(child)
            save_json(root / "study.json", study)
            core = build_study(root)
            self.assertEqual(core["clusters"][0]["supporting_sections"][0]["id"], "section")
            self.assertEqual(core["clusters"][1]["supporting_sections"], [])
            child["section_parent_id"] = "section"
            with self.assertRaises(ValueError):
                validate_study(study)
            child["section_parent_id"] = "souls"
            child["game"] = "cs2"
            with self.assertRaises(ValueError):
                validate_study(study)

    def test_update_requires_a_real_url_and_short_captures_are_not_failures(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            study["clusters"][0]["publication_action"] = "update_article"
            with self.assertRaises(ValueError):
                validate_study(study)
            study["clusters"][0]["existing_url"] = "https://owned.test/article"
            save_json(root / "study.json", study)
            page = extract_page("<main><h1>Souls</h1><p>A short, complete feature description.</p></main>", "https://a.test/")
            page["http_status"] = 200
            save_json(root / "pages" / "a.json", page)
            core = build_study(root)
            self.assertEqual(core["coverage"]["pages_fetched"], 1)
            self.assertEqual(core["coverage"]["page_failures"], 0)
            self.assertEqual(core["coverage"]["short_captures_requiring_context_review"], 1)

    def test_evidence_does_not_match_secure_to_security(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study_dir = root / "research" / "test-study"
            save_json(study_dir / "study.json", self.minimal_study())
            for url, content in (("https://a.test/", "Security and secure payments. " * 60), ("https://b.test/", "Soul aimbot targets soul orbs. " * 40)):
                page = extract_page("<html lang='en'><main><h1>Features</h1><p>" + content + "</p></main></html>", url)
                page["http_status"] = 200
                save_json(study_dir / "pages" / (url[8] + ".json"), page)
            build_study(study_dir)
            save_json(root / "config" / "research.json", {"active_study": "research/test-study"})
            evidence = research_evidence(root, {"source_kind": "seo_research", "source_ref": "souls", "game": "deadlock", "language": "en"})
            self.assertEqual([item["source"] for item in evidence], ["https://b.test/"])

    def test_section_evidence_uses_reviewed_terms_only_on_its_sources(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / "research/test-study"
            study = self.minimal_study()
            study["clusters"][0]["publication_action"] = "write_article"
            study["clusters"].append({**study["clusters"][0], "id": "fov", "title": "Aiming FOV", "publication_action": "include_as_section", "section_parent_id": "souls", "competitor_urls": ["https://c.test/"], "evidence_terms": ["FOV for aimbot"]})
            save_json(directory / "study.json", study)
            for name in ("a", "c"):
                page = extract_page("<html lang='en'><main><h1>Aimed FOV</h1><p>Allows a custom FOV for aimbot while aiming.</p></main></html>", f"https://{name}.test/")
                page["http_status"] = 200
                if name == "c":
                    page["requested_url"] = "https://redirect.test/"
                save_json(directory / "pages" / f"{name}.json", page)
            build_study(directory)
            save_json(root / "config/research.json", {"active_study": "research/test-study"})
            evidence = research_evidence(root, {"source_kind": "seo_research", "source_ref": "souls", "game": "deadlock", "language": "en"})
            self.assertEqual([e["source"] for e in evidence], ["https://c.test/"])
            self.assertIn("FOV for aimbot", evidence[0]["excerpt"])

    def test_onpage_only_source_is_measured_but_excluded_from_facts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / "research" / "test-study"
            study = self.minimal_study()
            study["source_policies"] = {"https://a.test/": {"exclude_from_fact_evidence": True}}
            study["clusters"][0]["intent_matched_urls"] = ["https://a.test/"]
            save_json(directory / "study.json", study)
            page = extract_page("<main><h1>Features</h1><p>" + "Soul aimbot targets soul orbs. " * 40 + "</p></main>", "https://a.test/")
            page["http_status"] = 200
            save_json(directory / "pages" / "a.json", page)
            save_json(directory / "supplemental-evidence.json", [{"source": "https://a.test/?utm_source=x", "cluster_ids": ["souls"], "excerpt": "Do not reuse excluded claims"}])
            core = build_study(directory)
            self.assertEqual(len(core["clusters"][0]["intent_matched_term_usage"][0]["pages"]), 1)
            save_json(root / "config" / "research.json", {"active_study": "research/test-study"})
            self.assertEqual(research_evidence(root, {"source_kind": "seo_research", "source_ref": "souls", "game": "deadlock", "language": "en"}), [])

    def test_article_target_does_not_inherit_broad_volume_or_full_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            study = self.minimal_study()
            original = study["keywords"][0]
            narrow = {**original, "query": "deadlock souls aimbot meaning"}
            third = {**original, "query": "deadlock souls aimbot comparison"}
            study["keywords"] += [narrow, third]
            study["clusters"][0]["article_target_query"] = narrow["query"]
            study["metric_policy"] = {"provider": "test", "period": "2026-08", "match_type": "exact"}
            save_json(root / "metrics.json", [{"query": original["query"], "game": "deadlock", "language": "en", "country": "US", "engine": "google", "provider": "test", "period": "2026-08", "match_type": "exact", "volume": 20}])
            study["serps"] = [{"query": q["query"], "game": "deadlock", "language": "en", "engine": "google", "method": "browser_dom", "country_requested": "US", "captured_at": "2026-09-21",
                               "results": [{"url": f"https://a.test/{n}", "type": "article"} for n in range(5)]} for q in (original, narrow)]
            save_json(root / "study.json", study)
            cluster = build_study(root)["clusters"][0]
            self.assertIsNone(cluster["article_target"]["volume"])
            self.assertEqual(cluster["measured_query_count"], 1)
            self.assertEqual(len(cluster["validated_query_subsets"][0]["queries"]), 2)
            self.assertNotIn(third["query"], cluster["validated_query_subsets"][0]["queries"])
            study["clusters"][0]["article_target_query"] = "not a member"
            with self.assertRaises(ValueError):
                validate_study(study)

    def test_backlink_import_excludes_internal_and_duplicate_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            save_json(root / "study.json", self.minimal_study())
            source = root / "backlinks.csv"
            source.write_text("source_url,target_url,anchor,target_keyword,provider,checked_at\nhttps://a.test/p,https://b.test/,Read more,souls aimbot,test,2026-09-21\nhttps://a.test/p,https://b.test/,Read more,souls aimbot,test,2026-09-21\nhttps://b.test/x,https://b.test/,Home,souls aimbot,test,2026-09-21\n", encoding="utf-8")
            result = import_backlinks(root, source)
            self.assertEqual(result["backlinks"], 1)
            self.assertEqual(result["referring_domains"], 1)
            public = [{"source_url": "https://c.test/review", "target_url": "https://b.test/", "anchor": "b.test",
                       "evidence_type": "verified_public_page_sample_not_provider_index"}]
            save_json(root / "public-backlink-sample.json", public)
            core = build_study(root)
            self.assertEqual(len(core["backlink_sample"]), 1)
            self.assertEqual(core["backlink_sample"][0]["source_url"], "https://a.test/p")
            self.assertEqual(core["public_backlink_sample"], public)
            self.assertIsNone(core["public_backlink_summary"])

    def test_metrics_do_not_confuse_missing_zero_or_long_tail(self):
        self.assertEqual(frequency_band(None, 100, 1000), "unknown")
        self.assertEqual(frequency_band(0, 100, 1000), "reported_zero")
        self.assertEqual(frequency_band(100, 100, 1000), "low")
        self.assertEqual(frequency_band(101, 100, 1000), "medium")
        row = dict(query="cs2 esp", game="cs2", language="en", country="US", engine="google", provider="test", period="2026-08", match_type="exact", volume="")
        self.assertIsNone(validate_metric(row)["volume"])
        for value in ("NaN", "-1", "Infinity", "0.5"):
            with self.assertRaises(ValueError):
                validate_metric({**row, "volume": value})
        study = {"market": {"country": "US", "engine": "google"}, "metric_policy": {"provider": "test", "period": "2026-08", "match_type": "exact"}}
        metric, _ = choose_metric(row, [{**row, "country": "GB", "volume": 900}], study)
        self.assertIsNone(metric)
        metric, _ = choose_metric(row, [{**row, "period": "2025-08", "volume": 900}], study)
        self.assertIsNone(metric)

    def test_extracts_editorial_text_and_separates_anchor_context(self):
        html = '<html><head><title>CS2 ESP</title><meta name="description" content="CS2 ESP explained"></head><body><header><a href="/">CS2 ESP</a></header><main><h1>CS2 ESP</h1><p>cs2 esp versus ESP32. cs2 ESP.</p><a href="/guide">Read more</a><a href="https://vendor.test">Vendor</a></main><footer>cs2 esp</footer></body></html>'
        page = extract_page(html, "https://site.test/article", "cs2 esp", ["Vendor"])
        self.assertEqual(phrase_count(page["text"], "cs2 esp"), 3)
        self.assertEqual(phrase_count(page["text"], "esp"), 3)
        self.assertEqual(page["links"][0]["placement"], "navigation")
        self.assertEqual(page["links"][1]["kind"], "generic")
        self.assertEqual(page["links"][2]["kind"], "branded")
        self.assertEqual(page["links"][2]["relationship"], "outbound")
        self.assertEqual(anchor_kind("VISIT", "https://vendor.test/", "", ["vendor.test"]), "generic")
        self.assertEqual(anchor_kind("VISIT vendor.test", "https://vendor.test/", "", ["vendor.test"]), "branded")
        self.assertIsNone(anchor_profile([page])["inbound_backlinks"])
        self.assertEqual(term_profile("cs2 esp", [page])["pages"][0]["title_exact"], 1)

    def test_capture_month_is_not_silently_a_report_month(self):
        row = dict(query="cs2 esp", game="cs2", language="en", country="US", engine="google", provider="public_tool",
                   period="2026-09", match_type="provider_unspecified", volume=20, period_basis="capture_month")
        with self.assertRaises(ValueError):
            validate_metric(row)
        row["captured_at"] = "2026-09-21"
        row = validate_metric(row)
        study = {"market": {"country": "US", "engine": "google"},
                 "metric_policy": {"provider": "public_tool", "period": "2026-09", "match_type": "provider_unspecified"}}
        self.assertIsNone(choose_metric(row, [row], study)[0])
        study["metric_policy"]["period_basis"] = "capture_month"
        self.assertEqual(choose_metric(row, [row], study)[0]["volume"], 20)
        study["metric_policy"]["provider_order"] = ["preferred_export", "public_tool"]
        self.assertEqual(choose_metric(row, [row], study)[0]["provider"], "public_tool")
        preferred = {**row, "provider": "preferred_export", "volume": 30}
        self.assertEqual(choose_metric(row, [row, preferred], study)[0]["volume"], 30)

    def test_reviewed_extraction_excludes_widgets_and_rejects_changed_markup(self):
        html = '<body><div>ESP tournament widget</div><h1>CS2 ESP</h1><div id="copy"><p>Radar and ESP explained.</p><a href="/guide">Guide</a></div><div><a href="/sale">Sale ESP</a></div></body>'
        rule = {"content_selector": "h1, #copy", "expected_matches": 2}
        page = extract_page(html, "https://a.test/", "esp", extraction_rule=rule)
        self.assertEqual(phrase_count(page["text"], "esp"), 2)
        self.assertEqual(page["headings"], [{"level": 1, "text": "CS2 ESP"}])
        self.assertEqual([a["placement"] for a in page["links"]], ["editorial", "other"])
        self.assertEqual(page["extraction_rule"], rule)
        with self.assertRaises(ValueError):
            extract_page(html.replace('id="copy"', 'id="changed"'), "https://a.test/", extraction_rule=rule)
        with self.assertRaises(ValueError):
            extract_page(html, "https://a.test/", extraction_rule={"content_selector": "body, #copy", "expected_matches": 2})

    def test_page_h1_outside_main_is_not_reported_as_missing(self):
        page = extract_page('<title>Invoker</title><body><section><h1>Invoker scripts</h1></section><main><h2>Features</h2><p>Hero-specific descriptions.</p></main></body>', 'https://a.test/')
        profile = term_profile('Invoker scripts', [page])["pages"][0]
        self.assertEqual(page['document_h1'], ['Invoker scripts'])
        self.assertEqual(profile['h1_exact'], 1)
        self.assertEqual(profile['body_exact'], 0)
        self.assertNotIn('Invoker scripts', page['text'])

    def test_metric_requests_keep_markets_separate_and_preserve_reported_zero(self):
        with tempfile.TemporaryDirectory() as temporary:
            study = self.minimal_study()
            study["market"]["secondary_market"] = "GB"
            study["metric_policy"] = {"provider": "test", "period": "2026-08", "match_type": "exact"}
            row = dict(query="deadlock souls aimbot", game="deadlock", language="en", country="US", engine="google", provider="test", period="2026-08", match_type="exact", volume=0)
            root = Path(temporary)
            self.assertEqual(export_metric_requests(root, study, [row]), {"US": 0, "GB": 1})
            self.assertEqual((root / "keyword-lists" / "deadlock-us-missing-volume.txt").read_text(), "")
            self.assertIn(row["query"], (root / "keyword-lists" / "deadlock-gb-missing-volume.txt").read_text())

    def test_url_canonicalization_keeps_meaningful_query(self):
        self.assertEqual(canonical_url("http://www.site.test/a/?utm_source=x&id=4#top"), "https://site.test/a?id=4")
        self.assertNotEqual(canonical_url("https://site.test/a?id=4"), canonical_url("https://site.test/a?id=5"))

    def test_clustering_does_not_bridge_markets_or_intents(self):
        def snapshot(query, nums, **extra):
            return dict(query=query, game="cs2", language="en", engine="google", country_requested="US", country_observed=None,
                        method="browser_dom", captured_at="2026-09-21", results=[{"url": f"https://site.test/{n}", "type": "organic"} for n in nums], **extra)
        a = snapshot("cs2 esp", [1,2,3,4,5])
        b = snapshot("cs2 wallhack", [1,2,3,6,7])
        c = snapshot("cs2 radar", [3,6,7,8,9])
        groups = serp_groups([a,b,c])
        self.assertEqual(sorted(len(g["queries"]) for g in groups), [2,2])
        pairs = {frozenset(g["queries"]) for g in groups}
        self.assertEqual(pairs, {frozenset([a["query"], b["query"]]), frozenset([b["query"], c["query"]])})
        # Adding a bridge preserves an already supported pair, but cannot join A to C.
        self.assertIn(frozenset(serp_groups([a,b])[0]["queries"]), pairs)
        uk = {**a, "query": "cs2 visual features", "country_requested": "GB"}
        commands = {**a, "query": "cs2 console commands"}
        self.assertEqual(len(serp_groups([a,uk,commands])), 3)
        self.assertEqual(serp_groups([{**a, "grouping_eligible": False}]), [])

    def test_repeated_query_is_not_a_validated_semantic_group(self):
        s = dict(query="cs2 esp", game="cs2", language="en", engine="google", country_requested="US", country_observed=None,
                 method="browser_dom", captured_at="2026-09-21T01:00:00Z", results=[{"url": f"https://a.test/{n}", "type": "organic"} for n in range(5)])
        groups = serp_groups([s, {**s, "query": "CS2 ESP", "captured_at": "2026-09-21T02:00:00Z"}])
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["status"], "single_query_sample")
        self.assertEqual(groups[0]["queries"], ["CS2 ESP"])

    def test_serp_import_is_idempotent_and_rejects_invalid_rank_atomically(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            save_json(root / "study.json", self.minimal_study())
            snapshot = dict(query="deadlock souls aimbot", game="deadlock", language="en", engine="google", method="browser_dom",
                            captured_at="2026-09-21", country_requested="US", results=[{"url": "https://a.test/", "rank": None}])
            source = root / "input.json"
            save_json(source, [snapshot])
            import_serps(root, source)
            self.assertEqual(import_serps(root, source)["stored_snapshots"], 1)
            before = (root / "study.json").read_bytes()
            save_json(source, [{**snapshot, "results": [{"url": "https://a.test/", "rank": -1}]}])
            with self.assertRaises(ValueError):
                import_serps(root, source)
            self.assertEqual((root / "study.json").read_bytes(), before)

    def test_spec_parses_deadlock_and_multiple_games(self):
        self.assertEqual(parse_spec("Write an article about Deadlock").game, "deadlock")
        self.assertEqual(parse_spec("CS2, Dota 2 and Deadlock").game, "all")
        with self.assertRaises(ValueError):
            parse_spec("articles", count=0)

    def test_no_wrong_language_fallback(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            db = KnowledgeDb(root / "db.sqlite")
            db.init()
            db.upsert_topic_idea(game="cs2", language="ru", title="Тест", source_kind="curated", main_query="тест")
            db.conn.commit()
            db.close()
            manifest = generate_articles(root / "db.sqlite", root / "output", "One EN article", count=1, game="cs2", language="en")
            self.assertEqual(manifest["items"], [])

    def test_word_count_excludes_prompts_and_yaml_supports_crlf(self):
        self.assertEqual(word_count('Two words. <!-- ' + "fake " * 500 + ' -->'), 2)
        meta, body = strip_front_matter('---\r\ntitle: "Hello: reader"\r\nsecondary_keywords: [a, b]\r\n---\r\nText')
        self.assertEqual(meta["title"], "Hello: reader")
        self.assertEqual(body, "Text")

    def test_informational_kernel_mention_is_not_an_instruction(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "a.md"
            path.write_text('---\ntitle: CS2 terms\ndescription: CS2 terms explained.\ngame: cs2\nlanguage: en\nprimary_keyword: CS2 terms\nvisuals: none\n---\nKernel is an architectural term. No product is 100% safe.\n## FAQ\n### What about Cluster?\ncluster.center is a vendor.', encoding="utf-8")
            result = review_article(path)
            self.assertFalse(any(f["severity"] == "error" for f in result["findings"]))

    def test_metrics_import_is_atomic_on_invalid_row(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "input.csv"
            source.write_text("query,game,language,country,engine,provider,period,match_type,volume\na,cs2,en,US,google,test,2026-08,exact,10\nb,cs2,en,US,google,test,2026-08,exact,-1\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                import_metrics(root, source)
            self.assertFalse((root / "metrics.json").exists())

    def test_cross_article_clone_is_blocked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = []
            text = " ".join(f"detail{i} describes feature{i}" for i in range(100))
            for number in (1, 2):
                path = root / f"{number}.md"
                path.write_text('---\ntitle: Test\ndescription: Test article\ngame: cs2\nlanguage: en\nprimary_keyword: Test\nvisuals: none\n---\n' + text + '\n## FAQ\nWhat?\ncluster.center.', encoding="utf-8")
                paths.append(path)
            manifest = root / "manifest.json"
            save_json(manifest, {"items": [{"status": "article", "output": str(p)} for p in paths]})
            result = review_manifest(manifest)
            self.assertEqual(result["fail"], 2)
            self.assertTrue(any("duplication" in f["message"] for f in result["results"][0]["findings"]))

if __name__ == "__main__":
    unittest.main()
