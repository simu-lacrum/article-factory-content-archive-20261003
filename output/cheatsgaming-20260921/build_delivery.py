"""Build this four-article delivery from the reviewed Markdown originals."""
from pathlib import Path
import html
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import yaml
from article_factory.tumblr_export import clean_markdown, markdown_to_html

OUT = Path(__file__).resolve().parent
RUNS = [
    ('20260921-105840-967517', 'cs2-triggerbot-vs-aimbot', 'A CS2 triggerbot fires; an aimbot handles aiming. Compare both with clear examples, learn where ESP fits and see what product feature descriptions actually mean'),
    ('20260921-105945-702353', 'cs2-radar-vs-esp', 'CS2 radar vs ESP explained: compare map markers, on-screen overlays and wallhack claims with clear examples that separate visual information from aim assistance'),
    ('20260921-105845-113024', 'deadlock-souls-aimbot', 'Deadlock souls aimbot, soul triggerbot and soul ESP explained. Compare aiming, firing and orb highlights, including how different developers use the same labels'),
    ('20260921-110014-516265', 'deadlock-auto-parry', 'Deadlock auto parry cheat explained: manual parries, advertised automation, anti-parry and why a successful parry alone cannot prove another player used a cheat'),
]
articles = []
items = []
for run_id, slug, description in RUNS:
    assert len(description) == 160 and not description.endswith('.')
    manifest = json.loads((ROOT / 'output/runs' / f'{run_id}.json').read_text(encoding='utf-8'))
    item = manifest['items'][0]
    source = Path(item['output'])
    text = source.read_text(encoding='utf-8')
    text = re.sub(r'^description: .*$', 'description: ' + json.dumps(description), text, count=1, flags=re.M)
    source.write_text(text, encoding='utf-8', newline='\n')
    meta = yaml.safe_load(text.split('---', 2)[1])
    assert len(meta['title']) <= 60
    assert meta['primary_keyword'] in description.lower()
    body = markdown_to_html(clean_markdown(text))
    # Copyable CMS fragment deliberately has no stylesheet, scripts or metadata.
    (OUT / f'{slug}.body.html').write_text(body, encoding='utf-8', newline='\n')
    document = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    document += f'<title>{html.escape(meta["title"])}</title>\n<meta name="description" content="{html.escape(description, quote=True)}">\n'
    document += '</head>\n<body>\n<article>\n' + body + '</article>\n</body>\n</html>\n'
    (OUT / f'{slug}.html').write_text(document, encoding='utf-8', newline='\n')
    notes = '\n\n'.join(re.findall(r'<!--(.*?)-->', text, flags=re.S))
    (OUT / f'{slug}.editorial.txt').write_text(notes.strip() + '\n', encoding='utf-8', newline='\n')
    articles.append({
        'slug': slug, 'game': meta['game'], 'title': meta['title'], 'description': description,
        'title_length': len(meta['title']), 'description_length': len(description),
        'primary_keyword': meta['primary_keyword'], 'body': body,
        'action': meta['publication_action'], 'existing_url': meta.get('existing_url'),
        'source_markdown': str(source), 'sources': meta['sources_used'],
        'html': str(OUT / f'{slug}.html'), 'body_html': str(OUT / f'{slug}.body.html'),
    })
    items.append(item)

batch = {'created_at': '20260921-cheatsgaming-cs2-deadlock-4',
         'spec': {'raw': '2 CS2 and 2 Deadlock English articles for cheatsgaming.com; title <=60, description exactly160 without a final period; HTML delivery', 'count': 4, 'game': 'all', 'language': 'en'},
         'llm_provider': 'none', 'model': None, 'items': items}
(ROOT / 'output/runs/20260921-cheatsgaming-cs2-deadlock-4.json').write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(OUT / 'articles.json').write_text(json.dumps(articles, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

cards = []
for index, a in enumerate(articles, 1):
    esc = html.escape
    status = 'Обновить существующую страницу' if a['existing_url'] else 'Новая статья'
    target = f'<p class="notice">Обновить <a href="{esc(a["existing_url"], quote=True)}">существующий URL auto-parry</a>, без создания дубликата.</p>' if a['existing_url'] else ''
    cards.append(f'''<section class="card" id="{a['slug']}">
      <div class="eyebrow">{index:02d} · {esc(a['game'].upper())} · {status}</div>
      <h2>{esc(a['title'])}</h2>{target}
      <div class="field"><label for="title-{index}">Title <span>{a['title_length']}/60</span></label><textarea id="title-{index}" rows="2" readonly>{esc(a['title'])}</textarea><button data-copy="title-{index}">Копировать title</button></div>
      <div class="field"><label for="description-{index}">Description <span>160/160 · без точки в конце</span></label><textarea id="description-{index}" rows="3" readonly>{esc(a['description'])}</textarea><button data-copy="description-{index}">Копировать description</button></div>
      <div class="actions"><button class="primary" data-copy="body-{index}">Копировать HTML статьи</button><a href="{a['slug']}.html" download>Скачать полный HTML</a><a href="{a['slug']}.body.html" download>HTML для CMS</a></div>
      <details><summary>HTML-код для вставки</summary><textarea class="code" id="body-{index}" rows="18" readonly spellcheck="false" aria-label="HTML статьи {index}">{esc(a['body'])}</textarea></details>
      <details><summary>Прочитать статью</summary><article lang="en">{a['body']}</article></details>
    </section>''')

page = '''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CheatsGaming — 4 статьи для публикации</title>
<style>
:root{color-scheme:light;--ink:#182230;--muted:#516172;--accent:#514bb2;--line:#d7dfe8}
*{box-sizing:border-box}body{margin:0;background:#f3f5f8;color:var(--ink);font:16px/1.6 system-ui,sans-serif}main{max-width:980px;margin:0 auto;padding:44px 24px 64px}h1{font-size:clamp(26px,5vw,40px);line-height:1.18;margin:10px 0 16px}header p{max-width:760px;color:var(--muted)}h2{font-size:25px;line-height:1.3;margin:10px 0 24px}.card{background:white;border:1px solid var(--line);border-radius:16px;padding:30px;margin:24px 0}.eyebrow{font-size:12px;font-weight:700;letter-spacing:.07em;color:var(--muted)}nav{display:flex;gap:8px;flex-wrap:wrap;margin:22px 0}nav a{background:white;padding:7px 12px;border:1px solid var(--line);border-radius:8px}a{color:var(--accent);text-underline-offset:3px}.field{margin:20px 0}label{font-weight:700;display:block;margin-bottom:6px}label span{font-weight:400;color:var(--muted);font-size:13px;margin-left:8px}textarea{font:15px/1.5 system-ui,sans-serif;color:var(--ink);display:block;width:100%;border:1px solid var(--line);border-radius:8px;background:#fafbfc;padding:12px;resize:vertical}button{font:600 14px/1.4 system-ui,sans-serif;cursor:pointer;background:#fff;border:1px solid #aab6c5;border-radius:8px;color:var(--ink);padding:11px 15px;margin-top:8px;min-height:44px}button:hover{background:#eceef7}button:focus-visible,a:focus-visible,summary:focus-visible,textarea:focus-visible{outline:3px solid #817adb;outline-offset:3px}.primary{background:var(--accent);color:white;border-color:var(--accent)}.primary:hover{background:#413b91}.actions{display:flex;align-items:center;flex-wrap:wrap;gap:16px;margin:22px 0}.actions button{margin:0}.actions a{font-size:14px}.notice{padding:12px 16px;background:#f1effb;border-radius:8px}details{border-top:1px solid var(--line);padding:16px 0}summary{cursor:pointer;font-weight:600;min-height:28px}.code{font:13px/1.6 ui-monospace,monospace;margin-top:14px}article{max-width:740px;margin:26px auto;font-size:17px}article h1{font-size:32px}article h2{margin:28px 0 12px;font-size:24px}article h3{font-size:19px}article li{margin:8px 0}#status{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#182230;color:#fff;border-radius:9px;padding:12px 20px;max-width:90vw;box-shadow:0 5px 24px #0003;z-index:2}#status:empty{display:none}footer{font-size:14px;color:var(--muted)}@media(max-width:600px){main{padding:24px 12px}.card{padding:20px 16px}h2{font-size:23px}.actions{gap:12px}.actions button{width:100%}label span{display:block;margin-left:0}article{font-size:16px}}
</style></head><body><main><header><div class="eyebrow">CHEATSGAMING.COM · ENGLISH · 21.09.2026</div><h1>Четыре статьи, готовые к переносу в CMS</h1><p>Две статьи о CS2 и две о Deadlock. Title — до 60 символов; description — ровно 160, без точки в конце. HTML статьи содержит текст, заголовки и ссылки. Метаданные копируются отдельно.</p><nav aria-label="Статьи"><a href="#cs2-triggerbot-vs-aimbot">CS2: Triggerbot</a><a href="#cs2-radar-vs-esp">CS2: Radar / ESP</a><a href="#deadlock-souls-aimbot">Deadlock: Souls</a><a href="#deadlock-auto-parry">Deadlock: Auto Parry</a></nav></header>
'''
page += '\n'.join(cards)
page += '''<footer>Кнопка копирования HTML включает H1. Если CMS сама выводит заголовок статьи, удалите первый H1 из вставляемого фрагмента. Изображения не вставлены: задания для настоящих скриншотов сохранены в отдельных editorial.txt. Статьи не опубликованы.</footer></main><div id="status" role="status" aria-live="polite"></div>
<script>
let statusTimer;
function message(text){const status=document.getElementById('status');status.textContent=text;clearTimeout(statusTimer);statusTimer=setTimeout(()=>status.textContent='',5000)}
document.addEventListener('click',async event=>{const button=event.target.closest('button[data-copy]');if(!button)return;const source=document.getElementById(button.dataset.copy);const value=source.value;try{if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');await navigator.clipboard.writeText(value);message('Скопировано')}catch{const temp=document.createElement('textarea');temp.value=value;temp.setAttribute('aria-hidden','true');temp.style.position='fixed';temp.style.opacity='0';document.body.appendChild(temp);temp.select();let copied=false;try{copied=document.execCommand('copy')}catch{}temp.remove();button.focus();if(copied){message('Скопировано')}else{const details=source.closest('details');if(details)details.open=true;source.focus();source.select();message('Текст выделен — нажмите Ctrl+C')}}});
</script></body></html>'''
(OUT / 'index.html').write_text(page, encoding='utf-8', newline='\n')
print(json.dumps([{k:a[k] for k in ('slug','title_length','description_length','action')} for a in articles], ensure_ascii=False, indent=2))
