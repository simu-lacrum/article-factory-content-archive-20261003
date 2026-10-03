"""Synchronize current overview/cache after the final target-query review."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
directory = root / 'research/seo-20260921'
core = json.loads((directory / 'core.json').read_text(encoding='utf-8'))
report = directory / 'REPORT_RU.md'
text = report.read_text(encoding='utf-8')
replacements = {
    'Назначения групп: 9 новых статей, 11 обновлений статей, 12 разделов внутри других страниц': 'Назначения групп: 7 новых статей, 11 обновлений статей, 14 разделов внутри других страниц',
    '67 поисковых наблюдений: 55 браузерных': '78 поисковых наблюдений: 66 браузерных',
    '47 успешных загрузок страниц, 46 уникальных URL после нормализации; 43 уникальные англоязычные конкурентные страницы. Одиннадцать адресов отказали в обычной загрузке.': '52 успешных ответа, 51 уникальный URL после нормализации; 47 пригодных англоязычных конкурентных страниц. Один успешный ответ — экран ограничения доступа, исключённый из анализа текста и ссылок. Двенадцать адресов отказали в обычной загрузке.',
    'Пять пар проходят формальный порог перекрытия URL.': 'Семь пар проходят формальный порог перекрытия URL.',
    'Проверены 38 тестов': 'Проверен 41 тест',
    '5. **Dota 2 teleport preview.** Пояснить, какое событие и какую информацию обещает функция. До утверждений об актуальной реализации нужен прямой источник, а не пересказ общих возможностей мапхака.': '5. **Dota 2 teleport preview.** После проверки выдачи это раздел существующей статьи о maphack, без самостоятельного URL. Широкая формулировка в основном относится к обычным телепортам и командам. Для конкретного описания функции нужен прямой источник.',
    '2. Проверить выдачу по ещё не проверенным узким запросам и подтвердить группировку перекрытием результатов. 38 редакционных групп нельзя представлять как 38 уже доказанных SERP-кластеров.': '2. Дополнить проверку групп после получения измеренного спроса: приоритетные целевые формулировки просмотрены, но все перестановки и длинные хвосты не проверены. Часть узких углов остаётся редакционными гипотезами. 38 групп нельзя представлять как 38 уже доказанных SERP-кластеров.'
}
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
    elif new not in text:
        raise ValueError('Overview wording changed: ' + old[:90])
marker = '- [Редакционный план на 38 групп]'
line = '- [Последние целевые запросы и команды](FINAL_TARGET_DECISIONS.md): 11 выборок, решения по Dota 2, раздел radar/ESP, анализ сравнений и исключение экрана входа из корпуса.\n'
if line.strip() not in text:
    text = text.replace(marker, line + marker)
report.write_text(text, encoding='utf-8')

for name in ['FEATURE_PAGE_DECISIONS.md', 'ACQUISITION_AND_FEATURE_INTENTS.md', 'DOTA_AUTOMATION_INTENTS.md']:
    path = directory / name
    old = path.read_text(encoding='utf-8')
    note = '> Исторический этап. Последующие решения и текущие количества см. в [FINAL_TARGET_DECISIONS.md](FINAL_TARGET_DECISIONS.md) и [EDITORIAL_PLAN.md](EDITORIAL_PLAN.md).\n\n'
    if note not in old:
        first, rest = old.split('\n', 1)
        path.write_text(first + '\n\n' + note + rest.lstrip('\n'), encoding='utf-8')

now = datetime.now(timezone.utc).isoformat()
path = root / '.seo-cache/sxo.json'
sxo = json.loads(path.read_text(encoding='utf-8'))
new = json.loads((directory / 'raw/google-final-target-intents.json').read_text(encoding='utf-8'))['snapshots']
rows = sxo['findings']['snapshots']
seen = {(r['query'], r['captured_at']) for r in rows}
rows.extend({'query': r['query'], 'captured_at': r['captured_at'], 'types': dict(Counter(x['type'] for x in r['results']))}
            for r in new if (r['query'], r['captured_at']) not in seen)
sxo.update(analyzed_at=now)
sxo['findings']['decisions'].update({c['id']: c['serp_mismatch'] for c in core['clusters'] if c.get('serp_mismatch')})
path.write_text(json.dumps(sxo, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
path = root / '.seo-cache/programmatic.json'
cache = json.loads(path.read_text(encoding='utf-8'))
cache.update(analyzed_at=now, publication_actions=dict(Counter(c['publication_action'] for c in core['clusters'])))
cache['safeguards'][0] = 'Fourteen topic groups are parent sections'
cache['safeguards'] = list(dict.fromkeys(cache['safeguards'] + ['Login/access screens excluded from phrase, term and link analysis', 'Group-specific publication gates preserved in writing contracts']))
path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print({'coverage': core['coverage'], 'actions': cache['publication_actions']})
