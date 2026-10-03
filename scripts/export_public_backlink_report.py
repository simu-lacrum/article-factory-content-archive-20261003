"""Report retained public backlink observations without new network requests."""
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from article_factory.research.service import read_json, save_json

directory = Path(sys.argv[1]).resolve()
observations = read_json(directory / "public-backlink-observations.json")
rows = read_json(directory / "public-backlink-sample.json")
summary = read_json(directory / "public-backlink-summary.json")
provider = read_json(directory / "backlink-anchor-summary.json")
unavailable = sum(o["status"] == "unavailable" for o in observations)
nofollow = sum("nofollow" in r["rel"] for r in rows)
observation_date = max(o["checked_at"] for o in observations)[:10]
pages = [read_json(p) for p in sorted((directory / "pages").glob("*.json"))]
reciprocal = []
for host in summary["targets"]:
    sources = {urlsplit(r["source_url"]).netloc for r in rows if urlsplit(r["target_url"]).netloc == host}
    sampled = [p for p in pages if urlsplit(p["url"]).netloc == host and p.get("http_status") == 200]
    matches = [{"source_url": p["url"], "target_url": link["url"], "anchor": link["text"]}
               for p in sampled for link in p.get("links", []) if urlsplit(link["url"]).netloc in sources]
    reciprocal.append({"target_host": host, "inbound_source_hosts_checked": sorted(sources),
                       "retained_pages": [{"url": p["url"], "captured_at": p.get("captured_at"), "sha256": p.get("sha256")} for p in sampled],
                       "matches": matches, "status": "domain_pair_observed" if matches else "not_found_in_sampled_html" if sampled else "no_target_page_capture",
                       "limitation": "Sampled target pages only; no claim about the entire domain or link intent."})
summary["reciprocal_check"] = reciprocal
summary["rel_counts"] = dict(Counter("nofollow" if "nofollow" in r["rel"] else "no_nofollow_attribute_observed" for r in rows))
summary["confirmed_source_pages"] = len({r["source_url"] for r in rows})
save_json(directory / "public-backlink-summary.json", summary)
availability = {
    "checked_on": "2026-09-21", "scope": "Source availability checked during the original study, not re-probed by this exporter", "moz": "not_configured", "bing_webmaster": "not_configured",
    "dataforseo": "no_callable_tool_in_session", "semrush_public": "retained_anyx_sample_quota_exhausted",
    "common_crawl": {"official_source": "https://commoncrawl.github.io/cc-webgraph-statistics/",
                     "latest_release_observed": "cc-main-2026-jun-jul-aug", "domain_metrics_retrieved": False,
                     "reason": "No per-target numeric data retrieved. The local helper's hardcoded release is stale and a capped partial scan cannot establish absence.",
                     "scope": "Graph links can include resources; domain metrics cannot supply anchor text."},
    "public_html": {"candidate_pages": len(observations), "confirmed_source_pages": summary["confirmed_source_pages"],
                    "status_counts": summary["page_status_counts"]}
}
save_json(directory / "backlink-source-availability.json", availability)
lines = [
    "# Входящие ссылки: публичные примеры Dota 2 и Deadlock", "",
    f"Дата последней проверки ссылок: {observation_date}. Это вручную выбранные страницы с проверенными ссылками, а не полный профиль конкурентов. Общие доли анкоров, оценка качества доменов и прогноз роста по этой выборке не рассчитываются.", "",
    "## 1. Обзор покрытия", "",
    f"Проверено {len(observations)} страниц-кандидатов. Ссылки подтверждены на {summary['confirmed_source_pages']} страницах с {len(summary['confirmed_source_hosts'])} хостов: {', '.join(summary['confirmed_source_hosts'])}. Получено {len(rows)} уникальных сочетаний источник → адрес назначения → текст. Недоступных страниц: {unavailable}; коды и причины сохранены в журнале. Это неизвестность, а не доказательство отсутствия или удаления ссылки.", "",
    "Отдельная выборка Semrush по Anyx содержит 15 строк с 10 хостов: 11 совпадений адреса и текста подтверждены, ещё у одной ссылки отличается извлечённый текст. Эти строки не объединяются с публичной выборкой для расчёта процентов. [Данные Anyx](METRICS_AND_ANCHORS.md).", "",
    "Moz и Bing не настроены; callable-инструмента DataForSEO в сессии нет. Публичная квота Semrush исчерпана. У [Common Crawl](https://commoncrawl.github.io/cc-webgraph-statistics/) проверен актуальный выпуск `cc-main-2026-jun-jul-aug`, но числовые метрики исследуемых доменов не получены. Граф не даёт анкоры; неполный просмотр большого файла не позволяет объявить домен отсутствующим.", "",
    "**Backlink Health Score: INSUFFICIENT DATA.** Ни для одного домена нет четырёх полноценных факторов профиля. Числовая оценка не выставлена.", "",
    "## 2. Анкоры и безанкорные ссылки", ""
]
for host, data in summary["targets"].items():
    lines.append(f"- **{host}:** {data['links']} строк; " + ", ".join(f"{k}: {v}" for k, v in data["anchor_counts"].items()) + ".")
lines += ["", "URL-образный текст выделен как `naked_url`; `VISIT` — общий анкор, `VISIT avalan.cc` — брендовый. Брендовый текст и голый URL не смешиваются, даже если оба не содержат целевой ключ. Проверенные примеры:", ""]
for row in rows:
    lines.append(f"- [{row['anchor'] or '(пустой текст)'}]({row['source_url']}) → `{row['target_url']}`; {row['anchor_kind']}; rel: {', '.join(row['rel']) or '(не задан)'}; контекст: `{row['source_context']}`.")
lines += ["", f"Ссылка в списке выше открывает страницу-источник для проверки. Исходный `observed_href` сохранён в CSV: у ScamAdviser это HTTP-адрес с UTM-параметрами. Нормализованный HTTPS-адрес служит ключом сопоставления и не доказывает исходный протокол ссылки. Строк с `nofollow`: {nofollow}, без этого атрибута: {len(rows)-nofollow}; это не устанавливает передачу рейтингового веса. `noopener`/`noreferrer` записаны как обнаруженные атрибуты.", "",
    "Практическое применение: ссылка на продукт — ясное название бренда или адрес; ссылка на соседнюю статью — конкретный вопрос или содержание статьи. Например, `how soul aimbot differs from soul ESP` уместен только для страницы, которая объясняет это различие. Эти редакционные примеры не выдаются за анкоры конкурентов. Целевые проценты exact/branded/naked не назначены.", "",
    "## 3. Контекст источников", "",
    "GitHub issues содержат сообщения пользователей. Наличие ссылки в репозитории ValveSoftware не превращает пользовательскую жалобу в заявление Valve или рекомендацию продукта. Сторонний README также не подтверждает авторство вендора. ScamAdviser и Scam Detector — автоматические отчёты о доменах; их наличие не подтверждает качество ПО. Оценки безопасности и обвинения из этих страниц в статьи не переносятся.", "",
    "Поле `placement=editorial` означает расположение вне распознанной навигации. Это техническая эвристика HTML, а не оценка редакционной независимости. Авторство, оплата размещений, география аудитории и авторитет источников не установлены.", "",
    "## 4. Проверка подозрительных связей", "",
    f"Оснований объявлять эти домены токсичными, частью PBN или кандидатами на disavow нет. Встречные ссылки проверены на сохранённых страницах доменов назначения; совпадений с подтверждёнными входящими хостами: {sum(len(r['matches']) for r in reciprocal)}. Это вывод только о просмотренном HTML, не обо всех страницах сайтов. Подробности проверки сохранены в `public-backlink-summary.json`.", "",
    "При первоначальной проверке форумы Elitepvpers, обращение на Palo Alto LIVEcommunity и два отчёта Gridinsoft были недоступны обычной загрузкой. Сниппет или картинка скрытой ссылки не заменяют установленный href. Такие наблюдения не включаются в подтверждённые строки.", "",
    "## 5. Страницы назначения", ""
]
for target, count in Counter(r["target_url"] for r in rows).most_common():
    lines.append(f"- `{target}` — {count} сочетаний в этой выборке.")
lines += ["", "Это не рейтинг страниц по всем бэклинкам. Нет данных для вывода о страницах без ссылок или о потерянном весе на 404.", "",
    "## 6. Сравнение с собственными сайтами", "",
    "Полных сопоставимых профилей CheatsGaming, DeadlockHacks и CS2-площадки нет. Нельзя утверждать, что источник ссылается только на конкурента, и составлять из этого списка план размещений. Жалобы и автоматические репутационные страницы не являются рекомендованными площадками для публикации статей. Следующий полезный вход — сопоставимые экспорты собственных и конкурентных доменов с датой, source URL, target URL, анкором и rel.", "",
    "## 7. Новые и потерянные ссылки", "",
    "Есть одна временная точка наблюдений; появления и потери не рассчитаны. Для динамики нужны повторные сопоставимые снимки или история провайдера. HTTP 403 сегодня не считается потерянной ссылкой.", "",
    "## Файлы и воспроизводимость", "",
    "- [Проверенные строки CSV](public-backlink-sample.csv), [JSON](public-backlink-sample.json).",
    "- [Все попытки загрузки, даты и хеши](public-backlink-observations.json).",
    "- [Сводка и встречные ссылки](public-backlink-summary.json).",
    "- [Доступность источников данных](backlink-source-availability.json).",
    "- Повторная проверка: `python scripts/verify_public_backlinks.py research/seo-20260921`.",
    "- Отчёт без повторной загрузки: `python scripts/export_public_backlink_report.py research/seo-20260921`.",
    "- Обновление ядра: `python -m article_factory research build research/seo-20260921`.", ""
]
(directory / "PUBLIC_BACKLINKS.md").write_text("\n".join(lines), encoding="utf-8")
root = Path(__file__).resolve().parents[1]
save_json(root / ".seo-cache" / "backlinks.json", {
    "cache_type": "backlinks", "analyzed_at": datetime.now(timezone.utc).isoformat(), "domain": "cheatsgaming.com", "url": "https://cheatsgaming.com/",
    "scope": "Competitor selected samples for the multi-site editorial project; not an owned-domain backlink audit",
    "score": None, "status": "partial_data", "data_sources": ["Semrush public Anyx sample", "Verified public HTML"],
    "findings": {"provider_sample": provider, "public_sample": summary},
    "issues": ["Full comparable profiles unavailable", f"Unavailable public candidate pages: {unavailable}"],
    "recommendations": ["Use descriptive contextual anchors", "Import same-period competitor and owned-site exports before a link-gap comparison"],
    "limitations": ["No inferred optimal percentages", "No domain health or toxicity score", "Common Crawl per-domain metrics not retrieved"],
    "artifacts": [str((directory / name).relative_to(root)) for name in ("PUBLIC_BACKLINKS.md", "public-backlink-sample.csv", "backlink-source-availability.json")]
})
print({"public_rows": len(rows), "source_pages": summary["confirmed_source_pages"], "reciprocal_matches": sum(len(r["matches"]) for r in reciprocal), "report": str(directory / "PUBLIC_BACKLINKS.md")})
