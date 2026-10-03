"""Build a GitBook Git Sync project from a reviewed Article Factory run.

The exporter keeps the public article copy, reduces front matter to the page
description understood by GitBook, and creates a deterministic SUMMARY.md
navigation tree plus an editorial publication specification.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from .quality import strip_front_matter, word_count


@dataclass(frozen=True)
class PageSpec:
    slug: str
    language: str
    game: str
    output_path: str
    backlink_anchor: str
    backlink_target: str
    backlink_section: str
    nav_title: str


PAGE_SPECS = (
    PageSpec(
        slug="deadlock-auto-dispel-logic-fast-reactions-fail",
        language="en",
        game="Deadlock",
        output_path="en/deadlock/deadlock-auto-dispel-logic-fast-reactions-fail.md",
        backlink_anchor="Melonity for Deadlock",
        backlink_target="https://melonity.gg/en/deadlock",
        backlink_section="What to inspect before trusting item automation",
        nav_title="Deadlock Auto-Dispel Logic",
    ),
    PageSpec(
        slug="dota-2-courier-information-next-fight",
        language="en",
        game="Dota 2",
        output_path="en/dota-2/dota-2-courier-information-next-fight.md",
        backlink_anchor="Melonity Dota 2 tools",
        backlink_target="https://melonity.gg/en",
        backlink_section="What a useful courier-information feature should show",
        nav_title="Dota 2 Courier Information",
    ),
    PageSpec(
        slug="teleport-v-dota-2-kak-menyaetsya-karta",
        language="ru",
        game="Dota 2",
        output_path="ru/dota-2/teleport-v-dota-2-kak-menyaetsya-karta.md",
        backlink_anchor="Melonity для Dota 2",
        backlink_target="https://melonity.gg/",
        backlink_section="Каким должен быть полезный Teleport Preview",
        nav_title="Телепорт в Dota 2",
    ),
    PageSpec(
        slug="dushi-v-deadlock-dobivanie-podtverzhdenie-liniya",
        language="ru",
        game="Deadlock",
        output_path="ru/deadlock/dushi-v-deadlock-dobivanie-podtverzhdenie-liniya.md",
        backlink_anchor="Melonity для Deadlock",
        backlink_target="https://melonity.gg/deadlock",
        backlink_section="Как должна выглядеть полезная подсветка душ",
        nav_title="Души в Deadlock",
    ),
)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def _yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _article_page(meta: dict[str, str], body: str) -> str:
    description = meta.get("description", "").strip()
    return "\n".join(
        [
            "---",
            f"description: {_yaml_string(description)}",
            "---",
            "",
            body.strip(),
            "",
        ]
    )


def _find_source_articles(source_dir: Path) -> dict[str, tuple[Path, dict[str, str], str]]:
    found: dict[str, tuple[Path, dict[str, str], str]] = {}
    for path in sorted(source_dir.glob("*.md")):
        meta, body = strip_front_matter(path.read_text(encoding="utf-8"))
        slug = meta.get("slug", "").strip()
        if not slug:
            continue
        if slug in found:
            raise ValueError(f"duplicate article slug: {slug}")
        found[slug] = (path, meta, body)
    missing = [spec.slug for spec in PAGE_SPECS if spec.slug not in found]
    if missing:
        raise ValueError(f"missing source articles: {', '.join(missing)}")
    return found


def _summary() -> str:
    return """# Summary

* [Cluster & Melonity Game Guides](README.md)

## English

* [English Guides](en/README.md)
  * [Deadlock](en/deadlock/README.md)
    * [Deadlock Auto-Dispel Logic](en/deadlock/deadlock-auto-dispel-logic-fast-reactions-fail.md)
  * [Dota 2](en/dota-2/README.md)
    * [Dota 2 Courier Information](en/dota-2/dota-2-courier-information-next-fight.md)
  * [CS2](en/cs2/README.md)

## Русский

* [Гайды на русском](ru/README.md)
  * [Dota 2](ru/dota-2/README.md)
    * [Телепорт в Dota 2](ru/dota-2/teleport-v-dota-2-kak-menyaetsya-karta.md)
  * [Deadlock](ru/deadlock/README.md)
    * [Души в Deadlock](ru/deadlock/dushi-v-deadlock-dobivanie-podtverzhdenie-liniya.md)
  * [CS2](ru/cs2/README.md)
"""


def _landing_pages() -> dict[str, str]:
    return {
        "README.md": """---
description: "English and Russian research hubs for Dota 2, Deadlock and CS2."
---

# Cluster & Melonity Game Guides

Practical, risk-aware guides and an organized archive of related reading about Dota 2, Deadlock and CS2. Choose a language to start.

* [English guides](en/README.md)
* [Гайды на русском](ru/README.md)

The source archive also includes the Medium profiles of [Mrk Hertz](https://medium.com/@mrkhertz) and [Aureli Voines](https://medium.com/@aurelivoines). Article names are preserved for navigation; a title is not a promise of safety, compatibility or current product status.
""",
        "en/README.md": """---
description: "English research hubs and decision guides for Dota 2, Deadlock and CS2."
---

# English Guides

* [Deadlock guides](deadlock/README.md)
* [Dota 2 guides](dota-2/README.md)
* [CS2 reading hub](cs2/README.md)
""",
        "en/deadlock/README.md": """---
description: "Deadlock guides, reviews and related reading in English."
---

# Deadlock Guides

Use this hub to compare terminology, product pages and editorial perspectives. If you are researching **Deadlock cheats**, start with [Melonity for Deadlock](https://melonity.gg/en/deadlock) and the [Cluster Deadlock product page](https://clustercheats.com/en/deadlock). The broader Cluster cheats catalog is available at <https://clustercheats.com/en>.

## Original guide

* [Deadlock Auto-Dispel Logic: Why Fast Reactions Still Fail](deadlock-auto-dispel-logic-fast-reactions-fail.md)

## Medium reading

* [Top 4 cheats for Deadlock: features, prices and software comparison](https://medium.com/@aurelivoines/top-4-cheats-for-deadlock-comparison-of-features-prices-and-the-best-software-choice-0f737d360121)
* [Cluster Deadlock review and feature overview](https://medium.com/@mrkhertz/cluster-deadlock-review-download-the-deadlock-cheat-an-overview-of-hacks-features-74a5bcb25b74)
* [Deadlock cheat safety and VAC protection explained](https://medium.com/@mrkhertz/deadlock-cheat-safety-and-vac-protection-explained-why-cheats-are-safe-b297c2f0f2b8)
* [Top cheats for Deadlock](https://medium.com/@mrkhertz/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e)

These links are an editorial archive. Re-check current requirements and risks on the relevant product page; no undetectability or zero-risk claim is implied.
""",
        "en/dota-2/README.md": """---
description: "Dota 2 guides and a curated English Medium reading archive."
---

# Dota 2 Guides

For a current product overview, see [Dota 2 cheats and scripts from Melonity](https://melonity.gg/en). The list below organizes the Medium articles by topic without treating older titles as current safety or compatibility guarantees.

## Original guide

* [Dota 2 Courier Information: The Delivery That Reveals the Next Fight](dota-2-courier-information-next-fight.md)

## Medium reading

* [A complete guide to cheat commands in the Dota 2 lobby](https://medium.com/@mrkhertz/a-complete-guide-to-cheat-commands-in-the-dota-2-lobby-2026-1a32b1c1b58c)
* [Dota 2 and LoL anti-cheat: VAC vs Riot Vanguard](https://medium.com/@mrkhertz/dota-2-and-lol-anti-cheat-vac-vs-riot-vanguard-a-comparison-now-4ab8cf56aff5)
* [Dota 2 cheats and scripts explained](https://medium.com/@mrkhertz/dota-2-cheats-scripts-explained-2025-all-about-dota-hacks-82ff479af22d)
* [Dota 2 skin changer: risks and tools](https://medium.com/@mrkhertz/dota-2-skin-changer-2026-risks-and-tools-baeb9ed150af)
* [How hacks work in Dota 2](https://medium.com/@mrkhertz/how-hacks-work-in-dota-2-4a2d06d5969e)
* [Choosing an account and smurf-ban risk in Dota 2](https://medium.com/@mrkhertz/how-to-avoid-a-smurf-ban-in-dota-2-guide-to-choosing-an-account-for-dota-f2e7434083ca)
* [How to install cheats, scripts and hacks for Dota 2](https://medium.com/@mrkhertz/how-to-install-cheats-scripts-hacks-for-dota-2-free-27478fc2625f)
* [How to install custom skins and sets in Dota 2](https://medium.com/@mrkhertz/how-to-install-custom-skins-and-sets-in-dota-2-b3f627941c6e)
* [How to install Dota 2 cheats and hacks](https://medium.com/@mrkhertz/how-to-install-dota-2-cheats-hacks-for-free-de9e42a6b202)
* [How to write a script for a Dota 2 hero](https://medium.com/@mrkhertz/how-to-write-your-own-script-for-dota-2-on-any-hero-72043d903e1e)
* [Maphack for Dota 2: overview](https://medium.com/@mrkhertz/maphack-for-dota-2-everything-you-need-to-know-how-to-download-it-a5126f8bc05f)
* [Raise behavior score in Dota 2](https://medium.com/@mrkhertz/raise-behavior-score-in-dota-2-fast-recovery-cdfb4cad6820)
* [A Dota 2 cheat overview](https://medium.com/@mrkhertz/this-is-the-best-cheat-for-dota-2-download-the-hack-for-dota-2-2a6a276251a1)
* [Top 5 hacks and cheats for Dota 2](https://medium.com/@mrkhertz/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6)
* [Top skin changers for Dota 2](https://medium.com/@mrkhertz/top-skinchangers-for-dota-2-best-skinchanger-373b10b67f31)
* [Why cheaters in Dota 2 are not banned: an explanation](https://medium.com/@mrkhertz/why-cheaters-in-dota-2-are-not-banned-a-detailed-explanation-of-why-cheats-are-safe-3f28752a7f98)
""",
        "en/cs2/README.md": """---
description: "English CS2 cheats research hub with reviews and product links."
---

# CS2 Reading Hub

For readers comparing **CS2 cheats**, the dedicated [Cluster CS2 product page](https://clustercheats.com/en/cs2) is the primary product reference. The wider cheats catalog is at <https://clustercheats.com/en>.

## Medium reading

* [CS2 cheats: Cluster review](https://medium.com/@mrkhertz/cs2-cheats-a-review-of-the-best-cs-hack-cluster-center-0ae21415c908)
* [How to install CS2 aimbot and wallhack](https://medium.com/@mrkhertz/how-to-install-cs2-aimbot-wallhack-for-free-d88e11b39100)
* [How to install CS2 cheats and hacks](https://medium.com/@mrkhertz/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710)
* [Top 5 external cheats for CS2](https://medium.com/@mrkhertz/top-5-external-cheats-for-cs2-the-best-external-hack-2cfd5e5de7a4)
* [Top 5 legit cheats for CS2](https://medium.com/@mrkhertz/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364)
* [Top cheats for CS2](https://medium.com/@mrkhertz/top-cheats-for-cs2-the-best-hack-cfab8351f70b)

Titles are reproduced for accurate navigation. They do not establish present-day safety, detection status or compatibility.
""",
        "ru/README.md": """---
description: "Русскоязычные гайды и тематические хабы по Dota 2, Deadlock и CS2."
---

# Гайды на русском

* [Гайды по Dota 2](dota-2/README.md)
* [Гайды по Deadlock](deadlock/README.md)
* [Материалы по CS2](cs2/README.md)
""",
        "ru/dota-2/README.md": """---
description: "Гайды по Dota 2 и архив русскоязычных материалов на Medium."
---

# Гайды по Dota 2

Актуальную страницу продукта смотрите по ссылке [читы для Dota 2 от Melonity](https://melonity.gg/). Заголовки материалов ниже сохранены для навигации и сами по себе не означают гарантию безопасности или совместимости.

## Оригинальный гайд

* [Телепорт в Dota 2: как одно перемещение меняет три линии](teleport-v-dota-2-kak-menyaetsya-karta.md)

## Статьи на Medium

* [Топ читов для Dota 2](https://medium.com/@mrkhertz/%D1%82%D0%BE%D0%BF-%D1%87%D0%B8%D1%82%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-dota-2-%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%B9-%D1%87%D0%B8%D1%82-7317890f8f18)
* [Maphack для Dota 2: обзор](https://medium.com/@mrkhertz/maphack-%D0%B4%D0%BB%D1%8F-dota-2-%D0%B2%D1%81%D1%91-%D1%87%D1%82%D0%BE-%D0%BD%D1%83%D0%B6%D0%BD%D0%BE-%D0%B7%D0%BD%D0%B0%D1%82%D1%8C-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B3%D0%BE-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-e4e962740539)
""",
        "ru/deadlock/README.md": """---
description: "Русские гайды и материалы о Deadlock, продуктах и механиках."
---

# Гайды по Deadlock

Для сравнения страниц по теме **читы для Deadlock** доступны [Melonity для Deadlock](https://melonity.gg/deadlock) и [продукт Cluster для Deadlock](https://clustercheats.com/ru/deadlock). Общий русскоязычный каталог читов: <https://clustercheats.com/ru>.

## Оригинальный гайд

* [Души в Deadlock: как проигрывают линию между добиванием и подтверждением](dushi-v-deadlock-dobivanie-podtverzhdenie-liniya.md)

## Статьи на Medium

* [Топ-4 читов для Deadlock: сравнение функционала, цен и защиты](https://medium.com/@aurelivoines/%D1%82%D0%BE%D0%BF-4-%D1%87%D0%B8%D1%82%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-deadlock-%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0-%D1%86%D0%B5%D0%BD-%D0%B8-%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B-%D0%BE%D1%82-%D0%B1%D0%B0%D0%BD%D0%BE%D0%B2-8a3062388f8f)
* [Топ читов на Deadlock](https://medium.com/@mrkhertz/%D1%82%D0%BE%D0%BF-%D1%87%D0%B8%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-deadlock-%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%B9-%D1%87%D0%B8%D1%82-%D0%B4%D0%BB%D1%8F-%D0%B4%D0%B5%D0%B4%D0%BB%D0%BE%D0%BA-ab30144f5b47)

Это редакционный архив ссылок. Перед любым решением проверяйте актуальные условия и риски на странице продукта.
""",
        "ru/cs2/README.md": """---
description: "Русскоязычный хаб материалов про читы CS2 и страницы Cluster."
---

# Материалы по CS2

Для запроса **читы КС2** основная продуктовая ссылка — [читы для CS2 от Cluster](https://clustercheats.com/ru/cs2). Весь русскоязычный каталог читов находится по адресу <https://clustercheats.com/ru>.

## Статьи на Medium

* [Обзор функционала чита Cluster для CS2](https://medium.com/@aurelivoines/%D0%BE%D0%B1%D0%B7%D0%BE%D1%80-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0-%D1%87%D0%B8%D1%82%D0%B0-cluster-%D0%B4%D0%BB%D1%8F-cs2-%D0%B4%D0%B5%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80-%D0%BB%D1%83%D1%87%D1%88%D0%B5%D0%B3%D0%BE-external-%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-f97205b8aa90)
* [Топ читов для CS2](https://medium.com/@mrkhertz/%D1%82%D0%BE%D0%BF-%D1%87%D0%B8%D1%82%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-cs2-%D0%BB%D1%83%D1%87%D1%88%D0%B8%D0%B9-%D1%87%D0%B8%D1%82-da769c840abc)

Названия сохранены как навигационные подписи и не являются обещанием безопасности, статуса обнаружения или совместимости.
""",
    }


def _publishing_spec(pages: list[dict[str, object]]) -> str:
    lines = [
        "# ТЗ на публикацию GitBook",
        "",
        "## Цель",
        "",
        "Опубликовать один публичный индексируемый GitBook-сайт с четырьмя экспертными T2-статьями, шестью тематическими хабами, полным архивом из 32 Medium-статей и стабильными URL.",
        "",
        "## Рекомендуемые настройки сайта",
        "",
        "- Site title: `Cluster Cheats Docs`",
        "- Site slug: `cluster-cheats-docs`",
        "- Audience: `Public`",
        "- Search engine indexing: `On`",
        "- Git Sync direction for first import: `GitHub/GitLab → GitBook`",
        "- GitBook project root: папка, содержащая `.gitbook.yaml`, `README.md` и `SUMMARY.md`",
        "- Изображения на этом этапе не загружать: production-промпты хранятся отдельно в исходном Article Factory run.",
        "",
        "## Структура",
        "",
        "- Главная страница",
        "- English",
        "  - Deadlock",
        "  - Dota 2",
        "  - CS2",
        "- Русский",
        "  - Dota 2",
        "  - Deadlock",
        "  - CS2",
        "",
        "## Карта статей и коммерческих анкоров",
        "",
    ]
    for page in pages:
        lines.extend(
            [
                f"### {page['title']}",
                "",
                f"- GitBook path: `{page['public_path']}`",
                f"- Description: `{page['description']}`",
                f"- Primary keyword: `{page['primary_keyword']}`",
                f"- Commercial anchor: `{page['backlink_anchor']}`",
                f"- Target: `{page['backlink_target']}`",
                f"- Placement H2: `{page['backlink_section']}`",
                "- Link count rule: ровно одна коммерческая ссылка в теле статьи.",
                "",
            ]
        )
    lines.extend(
        [
            "## Карта ссылочных хабов",
            "",
            "- English / Dota 2: 16 Medium-статей и анкор `Dota 2 cheats and scripts from Melonity` → `https://melonity.gg/en`.",
            "- Русский / Dota 2: 2 Medium-статьи и анкор `читы для Dota 2 от Melonity` → `https://melonity.gg/`.",
            "- English / Deadlock: 4 Medium-статьи, Melonity EN, Cluster EN product и безанкорный Cluster EN hub.",
            "- Русский / Deadlock: 2 Medium-статьи, Melonity RU, Cluster RU product и безанкорный Cluster RU hub.",
            "- English / CS2: 6 Medium-статей, анкор `Cluster CS2 product page` и безанкорный Cluster EN hub.",
            "- Русский / CS2: 2 Medium-статьи, анкор `читы для CS2 от Cluster` и безанкорный Cluster RU hub.",
            "- Каждая из 32 Medium-статей размещается ровно в одном тематическом хабе; обе страницы профиля Medium размещаются на главной.",
            "- Безанкорные URL окружены тематическими словами cheats / читы / читы КС2 / читы Deadlock.",
            "",
        ]
    )
    lines.extend(
        [
            "## Порядок публикации",
            "",
            "1. Авторизоваться в GitBook и создать Space.",
            "2. Подключить Git Sync к репозиторию или импортировать папку с Markdown-файлами.",
            "3. Для первичного sync выбрать направление из Git в GitBook.",
            "4. Проверить, что GitBook прочитал `SUMMARY.md` и создал иерархию без дубликатов.",
            "5. В Page options сверить description каждой статьи; лимит GitBook — 200 символов.",
            "6. Закрепить точные slug из карты URL. Не переименовывать страницы после индексации без redirect.",
            "7. Создать Docs site, выбрать Public и включить индексацию поисковиками.",
            "8. Нажать Publish, открыть каждую публичную страницу и проверить H1, FAQ и коммерческий анкор.",
            "9. Проверить `sitemap-pages.xml` на публичном домене.",
            "10. Сохранить фактические публичные URL в `URL_MAP.md` вместо шаблонного base URL.",
            "",
            "## Финальный QA",
            "",
            "- В навигации 13 страниц: главная, 2 языковых индекса, 6 игровых индексов и 4 статьи.",
            "- Все внутренние ссылки относительные и открываются без 404.",
            "- В каждой статье один H1, девять H2 и FAQ последним H2.",
            "- В каждой статье ровно одна внешняя коммерческая ссылка с заданным анкором.",
            "- Не публиковать абсолютные обещания безопасности и не добавлять инструкции по обходу anti-cheat.",
            "- После публикации проверить canonical URL, sitemap и доступность страниц без входа в GitBook.",
        ]
    )
    return "\n".join(lines)


def _url_map(pages: list[dict[str, object]]) -> str:
    hubs = (
        ("Home", "", "README.md"),
        ("English", "en", "en/README.md"),
        ("English / Deadlock", "en/deadlock", "en/deadlock/README.md"),
        ("English / Dota 2", "en/dota-2", "en/dota-2/README.md"),
        ("English / CS2", "en/cs2", "en/cs2/README.md"),
        ("Русский", "ru", "ru/README.md"),
        ("Русский / Dota 2", "ru/dota-2", "ru/dota-2/README.md"),
        ("Русский / Deadlock", "ru/deadlock", "ru/deadlock/README.md"),
        ("Русский / CS2", "ru/cs2", "ru/cs2/README.md"),
    )
    lines = [
        "# GitBook URL map",
        "",
        "Suggested base URL: `https://<organization>.gitbook.io/cluster-cheats-docs`",
        "",
        "Replace `<organization>` and confirm every final URL after the site is published.",
        "",
    ]
    for title, public_path, source_file in hubs:
        suffix = f"/{public_path}" if public_path else ""
        lines.extend(
            [
                f"## {title}",
                "",
                f"- Expected URL: `https://<organization>.gitbook.io/cluster-cheats-docs{suffix}`",
                f"- Source file: `{source_file}`",
                "",
            ]
        )
    for page in pages:
        lines.extend(
            [
                f"## {page['title']}",
                "",
                f"- Expected URL: `https://<organization>.gitbook.io/cluster-cheats-docs/{page['public_path']}`",
                f"- Source file: `{page['output_path']}`",
                f"- Commercial anchor: [{page['backlink_anchor']}]({page['backlink_target']})",
                "",
            ]
        )
    return "\n".join(lines)


def export_gitbook(source_dir: Path, output_dir: Path) -> dict[str, object]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    source_articles = _find_source_articles(source_dir)

    _write(
        output_dir / ".gitbook.yaml",
        """root: ./

structure:
  readme: README.md
  summary: SUMMARY.md
""",
    )
    _write(output_dir / "SUMMARY.md", _summary())
    for relative_path, text in _landing_pages().items():
        _write(output_dir / relative_path, text)

    pages: list[dict[str, object]] = []
    for spec in PAGE_SPECS:
        source_path, meta, body = source_articles[spec.slug]
        output_path = output_dir / spec.output_path
        _write(output_path, _article_page(meta, body))
        pages.append(
            {
                **asdict(spec),
                "title": meta.get("title", ""),
                "description": meta.get("description", ""),
                "primary_keyword": meta.get("primary_keyword", ""),
                "risk": meta.get("risk", ""),
                "source": str(source_path),
                "output": str(output_path),
                "word_count": word_count(body),
                "public_path": spec.output_path.removesuffix(".md"),
            }
        )

    ops_dir = output_dir / "_ops"
    _write(ops_dir / "PUBLISHING_TZ.md", _publishing_spec(pages))
    _write(ops_dir / "URL_MAP.md", _url_map(pages))
    manifest: dict[str, object] = {
        "format": "gitbook-git-sync",
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "site_title": "Cluster Cheats Docs",
        "suggested_site_slug": "cluster-cheats-docs",
        "public_page_count": 13,
        "medium_article_count": 32,
        "medium_profile_count": 2,
        "commercial_targets": [
            "https://melonity.gg/en",
            "https://melonity.gg/deadlock",
            "https://melonity.gg/",
            "https://melonity.gg/en/deadlock",
            "https://clustercheats.com/ru",
            "https://clustercheats.com/en",
            "https://clustercheats.com/ru/cs2",
            "https://clustercheats.com/en/cs2",
            "https://clustercheats.com/ru/deadlock",
            "https://clustercheats.com/en/deadlock",
        ],
        "article_count": len(pages),
        "pages": pages,
    }
    _write(ops_dir / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a GitBook Git Sync project from reviewed articles.")
    parser.add_argument("--source", type=Path, required=True, help="Reviewed article directory")
    parser.add_argument("--output", type=Path, required=True, help="GitBook project directory")
    args = parser.parse_args()
    if not args.source.is_dir():
        parser.error(f"source directory does not exist: {args.source}")
    manifest = export_gitbook(args.source, args.output)
    print(
        json.dumps(
            {
                "status": "PASS",
                "public_page_count": manifest["public_page_count"],
                "article_count": manifest["article_count"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
