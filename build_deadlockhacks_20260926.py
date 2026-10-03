from __future__ import annotations

import json
import re
from pathlib import Path

from article_factory.tumblr_export import clean_markdown, markdown_to_html

ROOT = Path(__file__).resolve().parent
RUN_ID = "20260926-deadlockhacks-five-intents"
ARTICLE_DIR = ROOT / "output" / "articles" / RUN_ID
PROMPT_DIR = ROOT / "output" / "prompts" / RUN_ID
EVIDENCE_DIR = ROOT / "output" / "evidence" / RUN_ID
DELIVERY_DIR = ROOT / "output" / "deadlockhacks-20260926"
for directory in (ARTICLE_DIR, PROMPT_DIR, EVIDENCE_DIR, DELIVERY_DIR):
    directory.mkdir(parents=True, exist_ok=True)

CLUSTER_URL = "https://cluster.center/en/deadlock"
INTERNAL_COMPARISON = "https://deadlockhacks.com/comparison"
INTERNAL_GUIDES = "https://deadlockhacks.com/guides"

PROMOTIONAL_QUOTE = f'''> **Sponsored option — Cluster for Deadlock:** The live [Cluster Deadlock page]({CLUSTER_URL}) lists a configurable aimbot, ESP, Hero Combos, Auto Parry, Souls Aimbot, FOV Changer and Dodger. It shows plan choices and Windows 10/11 requirements. This is a commercial mention; the feature descriptions are vendor claims, not an independent test.'''

ARTICLES = [
    {
        "slug": "deadlock-cheats-download-find-the-real-source",
        "title": "Deadlock Cheats Download: Find the Real Source",
        "description": "Deadlock cheats download guide: verify the official destination, separate a free trial from paid access and avoid fake download pages before you click with care",
        "primary": "deadlock cheats download",
        "secondary": ["download deadlock cheats", "deadlock cheat official website", "deadlock cheat trial"],
        "cluster": "deadlock-free-download",
        "reader_job": "Find a real, currently identified access destination without mistaking a search result or trial for a free download",
        "action": "new_article",
        "body": f'''# Deadlock Cheats Download: Find the Real Source

Searching for a **Deadlock cheats download** usually starts with a button that says “free.” That button is not proof that the file is official, current or even connected to the product it names. The safer way to read this intent is to separate three things: the page that owns the offer, the access terms and the file or launcher destination.

**Quick answer:** use the provider’s own product page as the starting point, check whether it offers a trial or paid access, and do not treat a mirror, repost or forum attachment as the official download.

## A search result is not a download source

The first page in a search result can be a directory, an old review, a reseller or a discussion thread. Each may mention the same feature names while sending you somewhere different. A real access page should make the product identity, current terms and support route clear before it asks you to download anything.

Look for these signals together:

- a stable product name and game name;
- a visible access period or plan selector;
- a support or contact route that belongs to the same provider;
- a clear statement of what is included and what remains unknown;
- a destination that is linked from the provider’s own page, not pasted into a comment.

If a page only says “latest,” “undetected” or “one-click download,” you still do not know who controls the file or when the information was checked.

<!-- IMAGE_SLOT_01
Placement: after "## A search result is not a download source"
Type: real screenshot
Purpose: show the difference between a product page and a generic search result
Suggested file name: deadlock-download-source-check.webp
Alt text: Deadlock cheat product page with provider identity and access terms visible
Capture instruction: use a genuine screenshot of the public Cluster Deadlock page with its product name, plan selector and support destination visible; do not show account credentials, payment data or a downloaded executable.
-->

## What the Cluster page actually tells a reader

The current Cluster page presents a Deadlock product with selectable durations, including 7, 30, 90 and 180 days, and displays a starting “Buy for $5” label beside the plan selector. It also states Windows 10/11 support and names a Telegram support route. Those are access and product-page details, not proof of long-term performance.

The same page mentions a three-day trial for a newly registered account. That is a limited offer, not a permanent free Deadlock cheat. Trial eligibility can depend on account history, so read the live wording rather than copying an old “free download” headline.

The practical distinction is simple:

1. **Official destination:** the provider’s current product page.
2. **Access decision:** a trial, a paid duration or no available offer.
3. **Download step:** only the destination presented after the first two are clear.

Do not download a file merely because its filename matches the product name.

{PROMOTIONAL_QUOTE}

## A five-minute source check

Before you click a download control, answer these questions:

1. Does the page clearly identify the provider and the Deadlock product?
2. Does it state whether access is free, trial-based or paid?
3. Does the price or duration appear on the same current page?
4. Is support linked from that page rather than from a random post?
5. Can you leave without handing over a Steam password, recovery code or browser cookie?

If the answer to the last question is unclear, stop. A feature list is not a reason to trade away account credentials.

For broader vendor context, start with the [Deadlock comparisons on this site]({INTERNAL_COMPARISON}) rather than a download aggregator. Comparisons help you understand the product category; the provider’s own page is still the place to verify its current offer.

<!-- IMAGE_SLOT_02
Placement: after "## A five-minute source check"
Type: real screenshot
Purpose: make the provenance checklist scannable
Suggested file name: deadlock-download-provenance-checklist.webp
Alt text: Checklist for verifying a Deadlock cheat download destination
Capture instruction: create an author-owned editorial graphic or screenshot of the public page showing the plan and support sections; omit any launcher, login form and third-party download mirror.
-->

## FAQ

### Where can I find a Deadlock cheats download?

Start from the provider’s own product page. For the Cluster offer discussed here, use the [Cluster Deadlock page]({CLUSTER_URL}) and verify the live access terms before any download step.

### Is a free trial the same as free Deadlock cheats?

No. A trial is time-limited and may have eligibility conditions. Permanent free access needs its own clearly stated offer.

### Does a “latest Deadlock cheat” page prove the file is real?

No. Check ownership, date, plan terms and support on the provider’s current page.

### Should I use a mirror or forum attachment?

Treat it as unverified. A repost can be outdated, altered or disconnected from the provider’s current offer.

### Does a product page prove that a download is safe?

No. It can describe access and features. It cannot turn a marketing claim into an independent security or account-outcome guarantee.
''',
    },
    {
        "slug": "where-to-buy-deadlock-cheats-buyer-checklist",
        "title": "Where to Buy Deadlock Cheats: A Buyer Checklist",
        "description": "Where to buy Deadlock cheats: check the official page, plan length, price, support and terms before checkout so the offer is clear for your account without hype",
        "primary": "where to buy deadlock cheats",
        "secondary": ["buy deadlock cheats", "Deadlock cheat price", "Deadlock cheat support"],
        "cluster": "deadlock-comparison",
        "reader_job": "Choose a current product page and plan by checking scope, price, support and terms before checkout",
        "action": "new_article",
        "body": f'''# Where to Buy Deadlock Cheats: A Buyer Checklist

The question **where to buy Deadlock cheats** is really a question about evidence. A checkout page should tell you what you are buying, how long access lasts, what support exists and which claims are only marketing. If it hides those basics behind a “best hack” headline, you are choosing a slogan instead of a product.

**Quick answer:** buy only from a provider’s current product page, compare the exact plan and support terms, and treat price or status badges as dated information that needs checking.

## Start with the product page, not the headline

A marketplace listing can be useful for discovery, but it is a weak place to make the final decision. The provider’s own page should identify the game, the product, the available durations and the support channel. It should also make it possible to see whether the feature list is broad, limited or version-dependent.

That gives you a clean first pass:

- **Identity:** Is this clearly a Deadlock product?
- **Scope:** Are aim, visual information, souls, parry, combos or dodge features named separately?
- **Access:** Is the duration visible before checkout?
- **Support:** Is there a route for an activation or product question?
- **Limits:** Does the page acknowledge that updates and latency can affect behavior?

The more expensive mistake is not always the higher price. It is paying for a long list without knowing which part solves your actual problem.

## How to read the Cluster offer

At the time of this editorial check, Cluster’s Deadlock page shows a plan selector with 7, 30, 90 and 180-day options and a “Buy for $5” starting label. The page also states Windows 10/11 requirements and provides a support route. Confirm the final currency, duration and entitlement on the live page because checkout details can change.

Its feature copy names aimbot, ESP, Hero Combo, Auto Parry, Anti Parry, Souls Aimbot, Humanizer, FOV Changer and Dodger. Treat that as a product description: it tells you the categories the provider advertises, not an independent measurement of every function.

<!-- IMAGE_SLOT_01
Placement: after "## How to read the Cluster offer"
Type: real screenshot
Purpose: show the plan selector and the feature categories a buyer should verify
Suggested file name: deadlock-cheat-buying-plan-check.webp
Alt text: Deadlock cheat plan selector and feature categories on a public product page
Capture instruction: use a real dated screenshot of the public Cluster page showing the duration selector and feature headings; hide account details, payment data and private support messages.
-->

{PROMOTIONAL_QUOTE}

## A plan is more than a number

Before paying, write down five details in plain English:

1. **Duration:** when does access start and when does it end?
2. **Price:** is the displayed amount a starting label or the final total?
3. **Updates:** where is current status announced after a game update?
4. **Support:** what channel handles a failed activation or product question?
5. **Account boundary:** does support ever request a password, cookie or recovery code?

The last point is non-negotiable. A provider can explain its own access flow without asking for credentials that belong to your game account.

For more category context, use the site’s [Deadlock comparison archive]({INTERNAL_COMPARISON}). Keep the final purchase check on the live product page; an old article is not a checkout receipt.

<!-- IMAGE_SLOT_02
Placement: after "## A plan is more than a number"
Type: real screenshot
Purpose: support the buyer checklist with a concrete terms view
Suggested file name: deadlock-cheat-checkout-terms.webp
Alt text: Deadlock cheat access duration and support terms to confirm before checkout
Capture instruction: capture only publicly visible plan and terms information; do not include payment fields, personal identifiers or unsupported safety badges.
-->

## FAQ

### Where to buy Deadlock cheats without guessing?

Use the provider’s current product page. The Cluster option discussed here is listed at [cluster.center/en/deadlock]({CLUSTER_URL}); verify the plan and terms there before checkout.

### Is the cheapest plan always the best choice?

No. Compare the duration, current status, support route and exact feature scope, not only the starting price.

### What should a Deadlock cheat page disclose?

At minimum, look for product identity, feature scope, duration, price context, requirements and support.

### Can a feature list prove how well a cheat works?

No. It describes advertised scope. Performance and account outcomes need separate evidence.

### What should support never ask for?

Do not send a Steam password, recovery code or browser cookie to activate or troubleshoot third-party software.
''',
    },
    {
        "slug": "free-deadlock-cheats-vs-trial-what-is-real",
        "title": "Free Deadlock Cheats vs Trial: What Is Real?",
        "description": "Free Deadlock cheats or a trial? Learn how permanent access, limited offers, subscription terms and download destinations differ before you pay with clear terms",
        "primary": "free deadlock cheats",
        "secondary": ["deadlock cheat free trial", "free vs paid Deadlock cheats", "Deadlock cheat subscription"],
        "cluster": "deadlock-trial",
        "reader_job": "Separate a permanent free offer, a limited trial and a paid subscription using verifiable current terms",
        "action": "new_article",
        "body": f'''# Free Deadlock Cheats vs Trial: What Is Real?

“Free Deadlock cheats” can describe three very different things: a permanent free tier, a time-limited trial or a paid product advertised through a free download page. Those are different offers with different expectations. The label alone is not enough.

**Quick answer:** call something free only when the provider states that access remains free. A trial has a duration or eligibility rule. A subscription has a paid term. If the page does not explain which one it is, the offer is not clear enough to compare.

## The three offers readers mix together

### Permanent free access

A free version should say what remains available without payment and how long that access lasts. “Download free” is not the same statement. A free download can lead to a trial, an account gate or an upsell.

### A limited trial

A trial is a sample of access, not a free product forever. It may be restricted by time, account history or available features. Those limits should appear before the reader treats the trial as a full alternative.

### A paid subscription

A subscription has a duration, a price and an access rule. It may be daily, weekly, monthly or another period. The useful question is not whether a page uses the word “free,” but when payment begins and what happens when the term ends.

<!-- IMAGE_SLOT_01
Placement: after "## The three offers readers mix together"
Type: real screenshot
Purpose: make free access, trial access and subscription language visually distinct
Suggested file name: free-trial-paid-deadlock-comparison.webp
Alt text: Free offer, trial and paid subscription terms for Deadlock cheats
Capture instruction: create a real editorial screenshot of the public plan and trial wording, with no account data or payment details. Label the three access states in the article caption, not inside a fake product interface.
-->

## What the current Cluster wording says

The current Cluster page presents paid duration choices and a starting “Buy for $5” label. Its FAQ also describes a three-day trial for a newly registered account, with a restriction for accounts that have already used a trial. That is a trial offer, not evidence of a permanent free Deadlock cheat.

The page identifies Windows 10/11 requirements and a support route. It does not turn a trial into a promise that every feature or future version will remain available at no cost. Recheck the live page for the wording that applies to your account.

{PROMOTIONAL_QUOTE}

## How to spot a disguised paid download

Use this quick test before clicking:

- Does the page state “free version,” “free trial” or “paid plan” in plain language?
- Is the trial length visible?
- Does it say whether previous trial use affects eligibility?
- Is the price shown as a starting label or a final checkout total?
- Does the page identify the owner and support route?

If the only clear detail is a giant download button, you still do not know what you are receiving. A useful offer page explains the access state first and the file destination second.

The [Deadlock comparison archive]({INTERNAL_COMPARISON}) can help with feature vocabulary. It cannot replace a current offer check, because access terms change faster than evergreen definitions.

<!-- IMAGE_SLOT_02
Placement: after "## How to spot a disguised paid download"
Type: real screenshot
Purpose: help readers identify the access state before they click
Suggested file name: deadlock-free-download-terms-check.webp
Alt text: Deadlock cheat trial and subscription terms to verify before download
Capture instruction: use a dated capture of a public terms or plan section. Exclude checkout fields, login details and third-party mirrors.
-->

## FAQ

### Are free Deadlock cheats and a free trial the same?

No. Free Deadlock cheats imply ongoing free access. A free trial is limited by duration or eligibility and should be described that way.

### Does Cluster offer a free Deadlock cheat?

Its current page describes a limited three-day trial for eligible new accounts and also displays paid durations. That is not a permanent free tier.

### Is a “free download” automatically safe or official?

No. Verify the provider, destination, terms and support route before downloading anything.

### What does a subscription tell me?

It tells you access is tied to a paid period. Check the duration, price, renewal language and what happens when the term ends.

### Can a trial include every advertised feature?

Do not assume that. Read the current trial terms and feature scope on the provider’s page.
''',
    },
    {
        "slug": "deadlock-aimbot-fov-vs-camera-fov-explained",
        "title": "Deadlock Aimbot FOV vs Camera FOV: Explained",
        "description": "Deadlock aimbot FOV and camera FOV are different settings. Learn what they describe, why the numbers do not match and read feature pages before buying this year",
        "primary": "deadlock aimbot fov",
        "secondary": ["deadlock fov changer", "Deadlock camera FOV", "aim selection FOV"],
        "cluster": "deadlock-fov",
        "reader_job": "Tell camera field of view apart from the target-selection area a product calls FOV",
        "action": "new_article",
        "body": f'''# Deadlock Aimbot FOV vs Camera FOV: Explained

Deadlock pages use **FOV** for two different ideas. Camera FOV changes how wide the game view feels. Aimbot FOV describes the area in which a targeting feature may consider an enemy. The shared label is the trap: the two values are not interchangeable.

**Quick answer:** camera FOV is about the player’s view; aimbot FOV is about target selection. A wider camera view does not automatically make an aim feature search a wider area, and an aim-selection value does not change the camera.

## Use a doorway example

Imagine an enemy enters from the edge of your screen. A camera field-of-view change can make more of the scene visible at once. It changes the picture you see.

Now imagine the same picture with an aimbot feature deciding which target falls inside its selection area. That is a different question: which enemy is eligible for the feature’s aim action? The screen can look identical while the targeting rule changes.

This distinction matters when a listing says “FOV 30” or “FOV changer” without saying which system it means. A number without context is barely a specification.

<!-- IMAGE_SLOT_01
Placement: after "## Use a doorway example"
Type: real screenshot
Purpose: illustrate visible camera framing versus an abstract target-selection area
Suggested file name: deadlock-camera-fov-aimbot-fov.webp
Alt text: Deadlock camera view and aimbot target-selection FOV explained separately
Capture instruction: use an author-owned Deadlock screenshot for the camera view and a simple editorial diagram for target selection; do not fabricate a cheat menu or claim a measured in-game value.
-->

## What feature pages usually mean by each label

The Cluster page describes its FOV Changer as adjusting the supported field-of-view value for a wider or narrower view of the battlefield. That wording is about the camera view.

Elsewhere in the Deadlock cheat vocabulary, FOV appears beside aim assistance, smoothing and target selection. In that context, the reader should ask whether FOV limits which target is considered, rather than assuming it changes the game camera. The same three letters can sit beside two different controls.

When reading a page, look for the noun around FOV:

- **camera / view / battlefield:** likely the visible game frame;
- **aim / target / lock-on:** likely the selection area for an aim feature;
- **zoom:** may connect the control to a scoped or ability view and needs its own explanation.

{PROMOTIONAL_QUOTE}

## A clean checklist for FOV claims

Ask four questions before comparing products:

1. What does the FOV affect: the camera, aim selection or both?
2. Which target is named: enemy heroes, souls or another object?
3. Is the value global or tied to a mode, zoom state or feature?
4. Does the page state any limitation, or is the number shown without context?

Do not compare “FOV 20” on one page with “FOV 20” on another until those questions have matching answers. The number may describe a different coordinate system or a different action entirely.

For more feature language, visit the [Deadlock guides archive]({INTERNAL_GUIDES}). Keep the final scope tied to the exact product description you are reading.

<!-- IMAGE_SLOT_02
Placement: after "## A clean checklist for FOV claims"
Type: diagram
Purpose: give readers a memorable two-column distinction without a feature screenshot
Suggested file name: deadlock-fov-two-meanings-diagram.webp
Alt text: Diagram separating camera FOV from aimbot target-selection FOV
Capture instruction: create a clean editorial diagram with two panels labelled Camera view and Aim selection; no product logo, fake menu or unsupported numeric values.
-->

## FAQ

### What is Deadlock aimbot FOV?

Deadlock aimbot FOV usually refers to the area used when an aim feature considers targets. Confirm the meaning in the product’s own description.

### Is camera FOV the same as aim FOV?

No. Camera FOV changes the visible game frame. Aim FOV concerns target selection for an aim feature.

### Does a FOV changer improve aim?

Not by definition. A camera FOV changer changes the view; it does not automatically add aim assistance.

### Why do two pages show the same FOV number?

They may be describing different controls. Read the nearby nouns and verbs before comparing values.

### Should a feature page explain FOV context?

Yes. It should say whether FOV affects the camera, target selection, zoom or a specific feature.
''',
    },
    {
        "slug": "deadlock-hero-scripts-combo-automation-meaning",
        "title": "Deadlock Hero Scripts: What Combo Automation Means",
        "description": "Deadlock hero scripts can mean a guide or automated combo logic. Learn to separate targets, sequences, conditions and limits before choosing a tool with context",
        "primary": "deadlock hero scripts",
        "secondary": ["deadlock auto combo meaning", "Deadlock combo automation", "Deadlock hero combo"],
        "cluster": "deadlock-combos",
        "reader_job": "Understand what a hero script or combo label claims to automate without mistaking a strategy guide for a product specification",
        "action": "new_article",
        "body": f'''# Deadlock Hero Scripts: What Combo Automation Means

“Deadlock hero scripts” can mean a build guide, a sequence of ability ideas or a tool that claims to execute actions automatically. Those are different things. A strategy guide tells you what to press and why. A product description claims that some decision or input is delegated to software.

**Quick answer:** read a combo claim as four separate questions: which hero, which target, which sequence and which condition starts or stops it.

## A combo is not automatically a script

Suppose a player writes “use ability A, wait for the enemy dash, then follow with ability B.” That is a human-readable combo guide. It explains timing and decision-making, but the player still performs the actions.

A product page that says “Hero Combo” or “hero script” may be describing configured sequences of abilities and attacks. That is a different claim. It needs scope: supported heroes, supported actions and the conditions under which the sequence runs.

The word “automatic” does not fill in those missing details. A long list of heroes is not a coverage map.

<!-- IMAGE_SLOT_01
Placement: after "## A combo is not automatically a script"
Type: gameplay screenshot
Purpose: distinguish a human combo guide from an automated feature label
Suggested file name: deadlock-hero-combo-guide-vs-automation.webp
Alt text: Deadlock hero combo sequence shown as a gameplay explanation
Capture instruction: use an author-owned gameplay frame or clean flow diagram; do not show a fabricated script editor, hotkey sequence or implementation detail.
-->

## The four parts of a useful combo description

### 1. Hero

The supported hero matters because abilities, ranges and cooldowns differ. “All heroes” is a broad claim; a useful page names the supported scope or says that it depends on the current version.

### 2. Target

Does the sequence act on an enemy hero, a soul, an objective or the player’s own state? A combo label that omits the target leaves the most important decision unclear.

### 3. Sequence

Which actions are grouped together? “Hero Combo” could mean an ability chain, a light/heavy action sequence or a broader set of events. The description should name the category instead of making the reader guess from a demo.

### 4. Condition

What starts, pauses or ends the sequence? A target entering range, a cooldown becoming available or a state changing are different conditions. Do not invent a condition that the page does not publish.

## What Cluster publishes

Cluster describes Hero Combo as executing configured sequences of abilities and attacks for supported heroes and notes that availability may depend on the current game and product version. That is a useful, bounded description: it names the action and leaves version-dependent coverage explicit.

It does not mean that every hero, ability or matchup is automatically covered. That is why a buyer should ask for the current supported scope rather than treating a generic menu label as a complete matrix.

{PROMOTIONAL_QUOTE}

## How to read a demo without overclaiming

A short clip can show that a sequence happened. It cannot show every hero, target, cooldown state or failure condition. When you watch one, note:

- the hero and mode;
- the target and starting state;
- the actions that are visible;
- what happens when the target disappears or the ability is unavailable;
- whether the clip is a current product demonstration or an old recording.

That is enough to ask better questions without turning a highlight into a performance guarantee. For related terminology, see the [Deadlock guides archive]({INTERNAL_GUIDES}).

<!-- IMAGE_SLOT_02
Placement: after "## How to read a demo without overclaiming"
Type: diagram
Purpose: show hero → target → sequence → condition as a readable evaluation path
Suggested file name: deadlock-hero-script-evaluation-path.webp
Alt text: Four-part checklist for evaluating Deadlock hero script claims
Capture instruction: create a brand-neutral diagram with four labelled nodes and no executable code, hotkeys or fake vendor interface.
-->

## FAQ

### What are Deadlock hero scripts?

The phrase can describe either strategy material or software that claims to automate hero actions. Read the page for the exact target, sequence and conditions.

### What does Deadlock auto combo mean?

It usually refers to a configured sequence of abilities or attacks. The useful description names the supported hero, target and version-dependent limits.

### Is a hero combo guide the same as automation?

No. A guide explains what a player can do. Automation claims that software performs some action or decision.

### Does Hero Combo support every hero?

Do not assume that. Cluster’s public wording says availability can depend on the current game and product version.

### Can one demo prove a combo works everywhere?

No. It shows one selected sequence. Coverage across heroes, targets and states needs separate documentation.
''',
    },
]

assert len(ARTICLES) == 5
for article in ARTICLES:
    assert len(article["title"]) <= 60, article["title"]
    assert len(article["description"]) == 160, (article["slug"], len(article["description"]))
    assert not article["description"].endswith(".")
    assert article["primary"] in article["description"].lower()
    assert article["body"].count("<!-- IMAGE_SLOT_") == 2
    assert f"({CLUSTER_URL})" in article["body"]
    assert "https://deadlockhacks.com/" in article["body"]
    assert "http://" not in article["body"]
    path = ARTICLE_DIR / f"{article['slug']}.md"
    front = {
        "title": article["title"],
        "description": article["description"],
        "game": "deadlock",
        "language": "en",
        "primary_keyword": article["primary"],
        "secondary_keywords": article["secondary"],
        "semantic_cluster": article["cluster"],
        "reader_job": article["reader_job"],
        "research_study": f"seo-20260921 / {article['cluster']}",
        "keyword_usage": "Natural usage; no density quota",
        "sources_used": [CLUSTER_URL, "internal SEO research study seo-20260921"],
        "publication_action": article["action"],
        "target_site": "deadlockhacks.com",
        "commercial_disclosure": "Promotional Cluster mention is labelled in a blockquote; feature descriptions are vendor claims.",
    }
    yaml_lines = ["---"]
    for key, value in front.items():
        if isinstance(value, list):
            yaml_lines.append(f"{key}:")
            yaml_lines.extend(f"  - {json.dumps(v, ensure_ascii=False)}" for v in value)
        else:
            yaml_lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    yaml_lines.append("---")
    path.write_text("\n".join(yaml_lines) + "\n\n" + article["body"].strip() + "\n", encoding="utf-8", newline="\n")
    prompt = f"Codex article brief for {article['title']}\n\nReader job: {article['reader_job']}\nPrimary query: {article['primary']}\nUse only high-level terminology and the current Cluster page as the commercial source. Do not add external links. Include the supplied promotional blockquote, two real image placement notes and an FAQ.\n"
    (PROMPT_DIR / f"{article['slug']}.md").write_text(prompt, encoding="utf-8", newline="\n")
    evidence = {
        "topic": {"id": article["cluster"], "game": "deadlock", "language": "en", "title": article["title"], "main_query": article["primary"], "reader_job": article["reader_job"], "publication_action": article["action"]},
        "research_contract": {"study_id": "seo-20260921", "id": article["cluster"], "primary_query": article["primary"], "reader_job": article["reader_job"], "publication_gate": "requires_original_content_and_editorial_review", "reviewed_semantic_terms": article["secondary"]},
        "evidence": [{"source": CLUSTER_URL, "heading": "Cluster Deadlock public product page", "excerpt": "Current public page lists the Deadlock product, plan selector, Windows requirements and feature categories. Captured 2026-09-26. Vendor statements are not independent tests.", "captured_at": "2026-09-26", "evidence_type": "publisher_statement_not_independent_test"}],
        "strict_rules": ["No external links in public copy except Cluster", "No anti-cheat bypass, evasion or implementation instructions", "No unsupported guarantees, prices beyond dated page wording or personal tests"]
    }
    if article["cluster"] in {"deadlock-fov", "deadlock-combos"}:
        evidence["evidence"].append({"source": "reviewed competitor feature pages in seo-20260921", "heading": "Feature-label comparison", "excerpt": "Competitor wording was used to distinguish aim FOV, camera FOV and combo labels. It is not linked in the public article and is not treated as independent performance evidence.", "captured_at": "2026-09-21", "evidence_type": "competitor_onpage_analysis_only"})
    (EVIDENCE_DIR / f"{article['slug']}.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

items = []
for article in ARTICLES:
    items.append({
        "topic_id": article["cluster"], "title": article["title"], "game": "deadlock", "language": "en", "status": "article",
        "output": str((ARTICLE_DIR / f"{article['slug']}.md").resolve()),
        "prompt": str((PROMPT_DIR / f"{article['slug']}.md").resolve()),
        "evidence": str((EVIDENCE_DIR / f"{article['slug']}.json").resolve()),
        "llm_error": None,
    })
manifest = {
    "created_at": RUN_ID,
    "spec": {"raw": "Five distinct English Deadlockhacks.com access and feature-intent articles; no external links except Cluster", "count": 5, "game": "deadlock", "language": "en", "style": "direct practical gamer-aware"},
    "llm_provider": "none", "model": None, "items": items,
}
(ROOT / "output" / "runs" / f"{RUN_ID}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

# Produce clean HTML fragments and standalone files. Comments/front matter are never public.
delivery = []
for article in ARTICLES:
    source = ARTICLE_DIR / f"{article['slug']}.md"
    clean = clean_markdown(source.read_text(encoding="utf-8"))
    fragment = markdown_to_html(clean)
    (DELIVERY_DIR / f"{article['slug']}.body.html").write_text(fragment, encoding="utf-8", newline="\n")
    full = f'''<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>{article['title']}</title>\n<meta name="description" content="{article['description']}">\n</head>\n<body>\n<article>\n{fragment}</article>\n</body>\n</html>\n'''
    (DELIVERY_DIR / f"{article['slug']}.html").write_text(full, encoding="utf-8", newline="\n")
    delivery.append({"slug": article["slug"], "title": article["title"], "description": article["description"], "title_length": len(article["title"]), "description_length": len(article["description"]), "html": str((DELIVERY_DIR / f"{article['slug']}.html").resolve()), "body_html": str((DELIVERY_DIR / f"{article['slug']}.body.html").resolve())})
(DELIVERY_DIR / "articles.json").write_text(json.dumps(delivery, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

cards = []
for n, article in enumerate(ARTICLES, 1):
    fragment = (DELIVERY_DIR / f"{article['slug']}.body.html").read_text(encoding="utf-8")
    cards.append(f'''<section class="card" id="{article['slug']}"><div class="eyebrow">{n:02d} · DEADLOCK · {len(article['title'])}/60 title · 160/160 description</div><h2>{article['title']}</h2><label for="t{n}">Title</label><textarea id="t{n}" readonly rows="2">{article['title']}</textarea><button data-copy="t{n}">Copy title</button><label for="d{n}">Description</label><textarea id="d{n}" readonly rows="3">{article['description']}</textarea><button data-copy="d{n}">Copy description</button><div class="actions"><button data-copy="b{n}" class="primary">Copy HTML article</button><a href="{article['slug']}.html" download>Download full HTML</a><a href="{article['slug']}.body.html" download>Download CMS fragment</a></div><details><summary>Show HTML</summary><textarea id="b{n}" class="code" readonly rows="20">{fragment.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')}</textarea></details><details><summary>Read article</summary><article lang="en">{fragment}</article></details></section>''')
page = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DeadlockHacks — five articles</title><style>body{font:16px/1.6 system-ui,sans-serif;background:#f3f5f8;color:#182230;margin:0}main{max-width:980px;margin:auto;padding:40px 22px}h1{line-height:1.2}.card{background:white;border:1px solid #d7dfe8;border-radius:14px;padding:28px;margin:22px 0}.eyebrow{font-size:12px;letter-spacing:.06em;color:#586879;font-weight:700}textarea{display:block;width:100%;box-sizing:border-box;padding:11px;border:1px solid #c9d3de;border-radius:7px;font:14px/1.5 system-ui,sans-serif;margin:6px 0 8px}button,a{display:inline-block;padding:10px 14px;border-radius:7px;border:1px solid #aeb8c6;background:#fff;color:#3e3897;cursor:pointer;margin:4px 6px 14px 0;text-decoration:none}.primary{background:#514bb2;color:#fff;border-color:#514bb2}.actions{margin-top:8px}.code{font:12px/1.5 ui-monospace,monospace;background:#fafbfc}article{max-width:740px;margin:20px auto}summary{cursor:pointer;font-weight:700;padding:9px 0}label{font-weight:700;display:block;margin-top:12px}</style></head><body><main><h1>Five English articles for DeadlockHacks.com</h1><p>Five distinct intents: download, buying, free versus trial, aimbot FOV and hero scripts. External links are limited to the promotional Cluster page; no competitor links are inserted. Each description is exactly 160 characters and each title is under 60.</p>''' + ''.join(cards) + '''<p>Articles are drafts for publication. The auto-parry article is not duplicated here.</p></main><script>document.addEventListener('click',async e=>{let b=e.target.closest('[data-copy]');if(!b)return;let s=document.getElementById(b.dataset.copy);try{await navigator.clipboard.writeText(s.value);b.textContent='Copied'}catch{ s.focus();s.select();b.textContent='Select and press Ctrl+C'}})</script></body></html>'''
(DELIVERY_DIR / "index.html").write_text(page, encoding="utf-8", newline="\n")
(DELIVERY_DIR / "README_RU.md").write_text(f'''# DeadlockHacks.com — новые статьи\n\nОткройте `index.html`: для каждой статьи есть просмотр, копирование title, description и HTML-фрагмента для CMS.\n\nВ серии пять разных интентов: скачать, купить, free vs trial, aimbot FOV и hero scripts. В публичном HTML нет ссылок на сторонние ресурсы, кроме рекламной ссылки Cluster `{CLUSTER_URL}`. Статьи не опубликованы.\n''', encoding="utf-8", newline="\n")
print(json.dumps({"run_id": RUN_ID, "articles": delivery, "index": str((DELIVERY_DIR / 'index.html').resolve())}, ensure_ascii=False, indent=2))
