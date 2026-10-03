"""Reviewed final target-query samples; explicit intent decisions, not volume inference."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.models import key, validate_study
from article_factory.research.service import read_json, save_json, import_serps

directory = Path(sys.argv[1])
study = read_json(directory / 'study.json')
raw = read_json(directory / 'raw/google-final-target-observations.json')
types = {'discussion': 'forum', 'product_feature': 'product', 'product_listing': 'product',
         'commercial_comparison': 'comparison', 'guide': 'article', 'owned_article': 'article',
         'lineup_reference_library': 'category', 'catalog': 'category'}
snapshots = []
for capture in raw['searches']:
    row = {k: capture[k] for k in ('query', 'game', 'captured_at')}
    row.update(language='en', engine='google', country_requested='US', country_observed=None,
        method='browser_dom', session_cohort='codex-iab-signed-in', source_file='raw/google-final-target-observations.json',
        personalization_note='Results are not personalized', location_note="Unknown - Can't determine location; US requested only",
        result_scope='Public linked h3 headings; no organic ranks asserted; not a guaranteed complete top ten',
        visible_questions=capture['questions'], results=[{'title': title, 'url': url, 'type': types.get(kind, kind),
            'page_type': kind + '_provisional', 'rank': None, 'observed_heading_order': i}
            for i, (title, url, kind) in enumerate(capture['results'], 1)])
    if capture.get('visible_media_note'):
        row['visible_media_note'] = capture['visible_media_note']
    snapshots.append(row)

updates = {
    'dota2-teleport': {'publication_action': 'include_as_section', 'section_parent_id': 'dota2-maphack',
        'article_target_query': 'teleport preview meaning dota 2',
        'serp_mismatch': 'Teleport preview returns ordinary teleport references, gameplay guides, discussions, videos and an issue. Adding cheat still returns command references and ordinary mechanics, plus Melonity and an owned CheatsGaming overview. This does not establish a distinct third-party feature article intent. Keep the event/destination distinction as a short sourced section of the existing map-information article.',
        'publication_role': 'Supporting map-information section; no standalone teleport-feature URL scheduled.'},
    'dota2-maphack': {'article_target_query': 'dota 2 maphack vs esp',
        'serp_mismatch': 'The broad head query returns two product/feature pages, discussions, videos and a code release. Preserve the existing URL as an explanation of map-information claims, with an explicitly unmeasured comparison angle; it cannot substitute for obtaining a product. Keep access queries separate. The narrower comparison wording is an editorial hypothesis, not validated standalone demand.',
        'publication_role': 'Update the existing explanatory page; consolidate ward, Roshan and teleport distinctions there.',
        'intent_matched_urls': [], 'usage_phrases': ['maphack', 'ESP', 'fog of war', 'teleport', 'ward', 'Roshan'],
        'corpus_note': 'Product feature pages and general software descriptions are vocabulary evidence, not an intent-matched article corpus for the narrower proposed comparison.'},
    'dota2-skin-changer': {'article_target_query': 'dota 2 skin changer vs real items',
        'serp_mismatch': 'The broad sample includes three product pages, two videos and two discussions. Update the existing article around appearance versus ownership and visibility questions; do not pretend the explanation is a download page. The narrower angle remains an editorial hypothesis with unknown volume.',
        'intent_matched_urls': [], 'usage_phrases': ['skin changer', 'inventory changer', 'cosmetics', 'inventory', 'visible'],
        'corpus_note': 'Overplus and MetaSkins appeared for the broad acquisition query. Their copy can inform naming and claims analysis, not a density target for a comparison article.'},
    'dota2-comparison': {'serp_mismatch': 'The comparison query includes three commercial comparisons, a potentially owned external publication, discussions, a command reference and video. Update the existing named comparison using symmetric dated criteria. Vendor/reseller comparisons are not independent testing, and the mrkhertz publication is excluded from independent competitor evidence until ownership is resolved.',
        'intent_matched_urls': ['https://umbrella-dota.com/en/blog/melonity-vs-umbrella/', 'https://dota2cheat.net/blog/dota2-cheats-vs-ghostware-features-pricing/', 'https://ivsofte.biz/en/compare/dota-2-hacks/'],
        'usage_phrases': ['dota 2 cheats', 'dota2 cheats', 'Melonity', 'Umbrella', 'Octarine', 'comparison'],
        'corpus_note': 'Three commercial comparison URLs observed in the exact target-query sample. Capture availability and extraction quality determine which actually enter the count corpus. No test protocol is inferred from titles.'},
    'cs2-grenade-helper': {'serp_mismatch': 'The exact proposed comparison query returns a product-feature page, three lineup libraries, community discussion, code and video. A useful article can compare lookup, practice and assistance jobs, but the sample does not establish a dominant comparison-article format. Keep it as a supporting editorial explanation with unknown demand and explicit links to actual reference tools.',
        'intent_matched_urls': [], 'usage_phrases': ['grenade helper', 'lineup', 'lineups', 'grenade predictor'],
        'corpus_note': 'CSNADES and Distort are different formats in the exact target sample: reference library and commercial feature page. Analyse them separately; do not merge their word counts into an article length or repetition requirement.'},
    'deadlock-esp': {'publication_action': 'include_as_section', 'section_parent_id': 'deadlock-hub',
        'serp_mismatch': 'Even radar vs esp returns a different game discussion, repositories/releases, products/catalogs, video and an issue report, rather than a stable set of Deadlock comparison articles. Preserve object-versus-display distinctions in the feature hub. The cross-game result and repository do not count as commercial comparison evidence.',
        'publication_role': 'Supporting hub section explaining which object is tracked and where a publisher says information appears; no standalone URL scheduled.'},
    'cs2-free-download': {'serp_mismatch': 'The exact free query returns product pages, a software catalog, community discussions, a forum and video. Keep this as access-page research. A verified offer, limits and official destination must exist before making a download promise; no explanatory article can create that offer.'}
}
commands = {
    'cs2-commands': ('CS2 practice commands: find the command for the task', 'practice session or controlled server',
        ['https://totalcsgo.com/commands', 'https://developer.valvesoftware.com/wiki/List_of_Counter-Strike_2_console_commands_and_variables']),
    'dota2-commands': ('Dota 2 lobby cheat commands: a task-based reference', 'custom lobby or supported practice context',
        ['https://dota2.fandom.com/wiki/Cheats', 'https://liquipedia.net/dota2/List_of_Console_Commands']),
    'deadlock-commands': ('Deadlock sandbox commands: a task-based reference', 'Valve Deadlock sandbox or supported practice context',
        ['https://deadlock.wiki/Console_commands', 'https://developer.valvesoftware.com/wiki/List_of_Deadlock_console_commands_and_variables', 'https://forums.playdeadlock.com/resources/dump-of-all-available-commands-in-deadlock.25/'])
}
new_sources = {
    'dota2-comparison': updates['dota2-comparison']['intent_matched_urls'],
    'dota2-skin-changer': ['https://overplus.gg/en', 'https://metaskins.gg/en'],
    'cs2-grenade-helper': ['https://distort.wtf/features/cs2-grenade-helper']
}
for c in study['clusters']:
    if c['id'] in updates:
        c.update(updates[c['id']])
    if c['id'] in commands:
        title, context, references = commands[c['id']]
        c.update(title=title, page_type='command_reference',
            reader_job=f'Find a verified command for a named task in a {context}, with its effect and limits.',
            original_value='Short task-to-command entries with source, checked version/date, supported context and a useful explanation when a command no longer works.',
            outline=['Start with the practice task and supported game context', 'Verified commands grouped by reader task: effect, syntax and limits', 'Troubleshooting: unavailable, changed or context-restricted commands', 'Dates, sources and links to maintained full references', 'FAQ'],
            serp_mismatch='The exact cheat-commands sample is dominated by command references. A vocabulary-only explanation would under-deliver. Build a task-based reference with verified examples; keep third-party software discussion brief and separate. In the Deadlock sample all recorded results concern Valve Deadlock; older-game disambiguation is not the lead.',
            reference_urls=references,
            evidence_needed=['Inspect current primary or maintained command references before drafting exact syntax', 'Verify command effect, supported context and version; do not infer current validity from a dated title or snippet', 'Use only legitimate practice/custom-lobby functions; no anti-cheat evasion or exploit instructions', 'Check existing owned coverage before creating another URL'],
            publication_gate='Brief only until current command examples are verified. Existing reference URLs are research leads, not proof that syntax is current.')
        if c['id'] == 'deadlock-commands':
            c['semantic_terms'] = ['Valve Deadlock', 'sandbox', 'console', 'practice task', 'command syntax', 'supported context']
    if c['id'] in new_sources:
        c['competitor_urls'] = sorted(set(c['competitor_urls']) | set(new_sources[c['id']]))

ambiguous = {('dota2', 'dota 2 teleport preview'), ('dota2', 'dota 2 maphack'), ('dota2', 'dota 2 skin changer')}
clusters = {c['id']: c for c in study['clusters']}
for row in study['keywords']:
    c = clusters[row['cluster_id']]
    if (row['game'], key(row['query'])) in ambiguous:
        row.update(query_role='ambiguous_research', recommended_page_type='intent_review', intent_note='Mixed acquisition or ordinary-gameplay intent observed; see the reviewed group decision.')
    if row.get('query_role') == 'article_candidate' and c.get('section_parent_id'):
        row['recommended_page_type'] = 'section_of_' + c['section_parent_id']
    elif row.get('query_role') == 'article_candidate' and c['id'] in commands:
        row['recommended_page_type'] = 'command_reference'

for ident, urls in new_sources.items():
    for url in urls:
        study.setdefault('page_types', {})[url] = 'commercial_comparison' if ident == 'dota2-comparison' else 'product_feature' if ident == 'cs2-grenade-helper' else 'product'
        study.setdefault('source_policies', {})[url] = {'role': 'competitor_onpage_analysis_only', 'exclude_from_fact_evidence': True, 'reviewed_at': '2026-09-21',
            'reason': 'Observe copy, page format, phrase placement and links only. Advertised capabilities, access conditions, safety, tests and rankings are not independently verified. No operational steps enter the article evidence.'}
study.setdefault('extraction_rules', {})['https://overplus.gg/en'] = {
    'content_selector': 'section.hero, section.upgrade, section.inventory, section.enjoy, section.buy', 'expected_matches': 5,
    'reviewed_at': '2026-09-21', 'reason': 'Five disjoint landing-page sections. The nested inventory main contains only a counter and omits the actual hero, feature and offer copy.'}
study['extraction_rules']['https://metaskins.gg/en'] = {
    'content_selector': 'div.container.dark', 'expected_matches': 1, 'reviewed_at': '2026-09-21',
    'reason': 'Inspected single landing content wrapper containing hero, game-specific copy and subscription cards; excludes login/language navigation.'}
study['source_policies']['https://ivsofte.biz/en/compare/dota-2-hacks/'].update(
    exclude_from_onpage_analysis=True,
    reason='Observed redirect to /en/games/dota-2-hacks/ returns an access-restricted login screen. Preserve the HTTP capture but exclude its words, links and metadata from the competitor-comparison corpus; no access attempt was made.')
study['source_policies']['https://umbrella-dota.com/en/blog/melonity-vs-umbrella/']['reason'] += ' Own-product comparison contains unsupported rival capability, price, ban-rate, support and patch-speed assertions. The inspected copy does not establish a verifiable test protocol.'
study['source_policies']['https://metaskins.gg/en']['reason'] += ' Multi-game landing includes product cards; a risk-free slogan is an unverified marketing claim, not evidence of safety.'
validate_study(study)
save_json(directory / 'study.json', study)
save_json(directory / 'raw/google-final-target-intents.json', {'method_note': raw['method_note'], 'snapshots': snapshots})
print(import_serps(directory, directory / 'raw/google-final-target-intents.json'))
print({'new_source_urls': sum(len(v) for v in new_sources.values()), 'new_sections': ['dota2-teleport', 'deadlock-esp']})
