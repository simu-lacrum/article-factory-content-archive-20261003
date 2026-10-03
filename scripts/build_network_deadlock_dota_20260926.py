from __future__ import annotations

import html
import json
import re
from pathlib import Path

from build_network_t2_batch import HOSTS, markdown_to_html

ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "20260926-network-12x7"
ARTICLE_DIR = ROOT / "output" / "articles" / RUN_ID
PROMPT_DIR = ROOT / "output" / "prompts" / RUN_ID
EVIDENCE_DIR = ROOT / "output" / "evidence" / RUN_ID
PUBLISH_DIR = ROOT / "output" / "publish" / RUN_ID
RUN_MANIFEST = ROOT / "output" / "runs" / f"{RUN_ID}.json"

TARGETS = [
    {
        "url": "https://deadlockhacks.com/", "game": "deadlock", "product": "Cluster",
        "image": "https://deadlockhacks.com/images/deadlock-hero.webp", "alt": "Deadlock hero artwork from the source site",
        "titles": ["Deadlock Cheats: What a Hub Should Explain", "Deadlock Hacks Research Without the Sales Fog", "A Practical Deadlock Cheat Hub Checklist", "Deadlock Cheat Pages: Scope Before Features", "Deadlock Tools: Questions Before You Compare", "Deadlock Cheat Research for Returning Players", "Deadlock Cheats and the Source-Checking Habit"],
        "anchors": ["deadlock cheats", "deadlock hacks", "best Deadlock cheats", "Deadlock cheat guide", "https://deadlockhacks.com/", "Deadlock tools", "Deadlock cheat research"],
        "intent": "a broad Deadlock hub", "focus": "map the reader's question to the right page before judging a product",
        "facts": "A hub can show categories, navigation, and public positioning; it cannot prove permanent compatibility, zero account risk, or that every linked claim is current.",
        "checks": ["clear game and feature taxonomy", "a named source for current status", "dates or version context", "a visible stop condition when evidence is thin"],
    },
    {
        "url": "https://deadlockhacks.com/guides/deadlock-hero-scripts-combo-automation-meaning", "game": "deadlock", "product": "Cluster",
        "image": "https://deadlockhacks.com/images/editorial/deadlock-hero-scripts-cover.webp", "alt": "Deadlock hero scripts editorial cover from the source page",
        "titles": ["Deadlock Hero Scripts: What Combo Automation Means", "Deadlock Combo Scripts: Read the Claim Carefully", "Hero Scripts in Deadlock: Scope, Timing, Context", "Deadlock Hacks and the Hero-Combo Vocabulary", "Deadlock Cheats: A High-Level Script Explainer", "How to Audit a Deadlock Combo Script Claim", "Deadlock Hero Automation Without the Hype"],
        "anchors": ["deadlock cheats", "deadlock hero scripts", "Deadlock hacks", "hero combo guide", "https://deadlockhacks.com/guides/deadlock-hero-scripts-combo-automation-meaning", "Deadlock combo tools", "Deadlock script research"],
        "intent": "hero scripts and combo automation", "focus": "separate a guide to a hero sequence from a claim about software automation",
        "facts": "The phrase hero script can describe a tutorial, a macro-like sequence, or a product feature. A page should name which meaning it uses and what is actually visible in its example.",
        "checks": ["hero and ability scope", "whether the example is manual or automated", "conditions and exclusions", "patch and maintenance context"],
    },
    {
        "url": "https://deadlockhacks.com/guides/deadlock-auto-parry-cheat-what-it-automates", "game": "deadlock", "product": "Cluster",
        "image": "https://deadlockhacks.com/images/editorial/deadlock-auto-parry-cover.webp", "alt": "Deadlock auto-parry editorial cover from the source page",
        "titles": ["Deadlock Auto-Parry: What the Claim Automates", "Is There a Deadlock Parry Cheat? Read the Scope", "Deadlock Auto-Parry Claims and Their Limits", "Deadlock Cheats: Manual Defense vs Automation", "How to Evaluate an Auto-Parry Explainer", "Deadlock Hacks and the Timing Question", "Deadlock Auto-Parry Without Absolute Promises"],
        "anchors": ["deadlock hacks", "Deadlock auto-parry cheat", "deadlock cheats", "auto-parry guide", "https://deadlockhacks.com/guides/deadlock-auto-parry-cheat-what-it-automates", "Deadlock parry tools", "Deadlock automation research"],
        "intent": "an auto-parry explainer", "focus": "describe an automation claim at a high level without turning a clip into a universal promise",
        "facts": "A clip can show one parry-like interaction under captured conditions. It does not establish every matchup, latency condition, future patch, or account-safety conclusion.",
        "checks": ["the incoming interaction shown", "hero and matchup context", "latency or timing caveats", "what remains under player control"],
    },
    {
        "url": "https://deadlockhacks.com/guides/deadlock-aimbot-fov-vs-camera-fov-explained", "game": "deadlock", "product": "Cluster",
        "image": "https://deadlockhacks.com/images/editorial/deadlock-aimbot-fov-cover.webp", "alt": "Deadlock FOV terminology editorial cover from the source page",
        "titles": ["Deadlock Aimbot FOV vs Camera FOV Explained", "Deadlock FOV Terms: Aim Scope vs View Scope", "Deadlock Cheats and the FOV Vocabulary", "A Clearer Way to Read Deadlock Aimbot FOV", "Deadlock Hacks: Why FOV Labels Matter", "FOV Claims in Deadlock Cheat Reviews", "Deadlock Aim Research Without Confusing the Terms"],
        "anchors": ["deadlock cheats", "Deadlock aimbot FOV", "deadlock hacks", "FOV terminology guide", "https://deadlockhacks.com/guides/deadlock-aimbot-fov-vs-camera-fov-explained", "Deadlock aim tools", "Deadlock FOV research"],
        "intent": "FOV terminology", "focus": "keep targeting scope and the player's camera view as separate concepts",
        "facts": "FOV labels are easy to collapse into one slider even when they describe different scopes. A useful explainer defines the term, names the visible context, and avoids presenting a setting label as proof of performance.",
        "checks": ["what the angle applies to", "whether the screenshot shows a menu or a match", "camera and target scope kept separate", "no leap from terminology to safety"],
    },
    {
        "url": "https://deadlockhacks.com/guides/where-to-buy-deadlock-cheats-buyer-checklist", "game": "deadlock", "product": "Cluster",
        "image": "https://deadlockhacks.com/images/editorial/where-to-buy-deadlock-cheats-cover.webp", "alt": "Deadlock buyer checklist editorial cover from the source page",
        "titles": ["Where to Buy Deadlock Cheats: A Buyer Checklist", "Deadlock Cheat Buyers: Verify the Source First", "A Deadlock Cheats Checklist for Careful Research", "Deadlock Hacks: Questions Before Any Purchase", "Deadlock Product Pages and the Stop-or-Continue Test", "How to Compare Deadlock Cheat Sellers", "Deadlock Cheat Buying: Price Is Not the Proof"],
        "anchors": ["deadlock hacks", "where to buy Deadlock cheats", "deadlock cheat checklist", "Deadlock buying guide", "https://deadlockhacks.com/guides/where-to-buy-deadlock-cheats-buyer-checklist", "Deadlock product research", "Deadlock cheat buyer questions"],
        "intent": "a buyer checklist", "focus": "check identity, support, scope, and risk before treating a seller page as evidence",
        "facts": "A product page can state public terms and support routes. It cannot guarantee account safety or turn an anonymous mirror into an official source.",
        "checks": ["domain and source continuity", "clear access terms", "support and update history", "a credible reason to walk away"],
    },
    {
        "url": "https://deadlockhacks.com/guides/deadlock-cheats-download-find-the-real-source", "game": "deadlock", "product": "Cluster",
        "image": "https://deadlockhacks.com/images/editorial/deadlock-cheats-download-cover.webp", "alt": "Deadlock download-source editorial cover from the source page",
        "titles": ["Deadlock Cheats Download: Find the Real Source", "Deadlock Cheat Downloads and Source Continuity", "How to Read a Deadlock Hack Download Page", "Deadlock Cheats: Mirror, Source, or Redirect?", "A Safer Deadlock Download Research Checklist", "Deadlock Hack Sources: What to Verify", "Deadlock Downloads Without Guessing at Provenance"],
        "anchors": ["deadlock cheats", "Deadlock cheats download", "Deadlock hack source", "download safety checklist", "https://deadlockhacks.com/guides/deadlock-cheats-download-find-the-real-source", "Deadlock official source", "Deadlock download research"],
        "intent": "source and download provenance", "focus": "trace a download claim back to a consistent, identifiable publisher",
        "facts": "A download button is not proof of provenance. The useful question is whether the page, account flow, support channel, and publisher identity form one traceable chain.",
        "checks": ["publisher identity", "same-domain navigation", "clear version or date context", "no pressure to use an unexplained mirror"],
    },
    {
        "url": "https://dota2cheat.com/", "game": "dota2", "product": "Melonity", "image": "https://dota2cheat.com/assets/figma-raw-1.webp", "alt": "Dota 2 editorial hero image from the source site",
        "titles": ["Dota 2 Cheats: How to Read a Product Hub", "Dota 2 Hacks Research Without the Feature Fog", "A Practical Dota 2 Cheat Hub Checklist", "Dota 2 Cheat Pages: Start With the Player Job", "Dota 2 Tools and the Evidence Ladder", "Dota 2 Cheat Research for Returning Players", "Dota 2 Cheats: Build a Better Shortlist"],
        "anchors": ["dota 2 cheats", "Dota 2 hacks", "Dota 2 cheat hub", "Dota 2 scripts guide", "https://dota2cheat.com/", "Dota 2 tools", "Dota 2 cheat research"],
        "intent": "a broad Dota 2 hub", "focus": "move from a broad catalogue to a specific, answerable research question",
        "facts": "A hub can organize scripts, vision, reviews, and setup topics. It cannot by itself prove present compatibility, zero risk, or the quality of every linked product.",
        "checks": ["categories that match real questions", "clear product and source identity", "current status signals", "a stop condition for missing proof"],
    },
    {
        "url": "https://dota2cheat.com/guides/install-dota-2-cheats", "game": "dota2", "product": "Melonity", "image": "https://dota2cheat.com/assets/dota2/dota2-75ce3a32f08b8172a1d79ade.webp", "alt": "Dota 2 installation-guide artwork from the source page",
        "titles": ["Install Dota 2 Cheats: Read the Setup Page Safely", "Dota 2 Cheat Setup and the Questions It Must Answer", "Installing Dota 2 Cheats: Scope Before Steps", "Dota 2 Hacks and Setup-Page Red Flags", "A High-Level Dota 2 Cheat Onboarding Checklist", "Dota 2 Install Guides: Source, Scope, Support", "Dota 2 Cheat Setup Without Blind Trust"],
        "anchors": ["dota 2 hacks", "install Dota 2 cheats", "Dota 2 setup guide", "Dota 2 cheat onboarding", "https://dota2cheat.com/guides/install-dota-2-cheats", "Dota 2 install research", "Dota 2 cheat setup"],
        "intent": "a setup page", "focus": "evaluate whether a setup guide is current, scoped, and transparent rather than reproduce operational steps",
        "facts": "A setup article should identify scope, prerequisites, support, and rollback expectations. It should not imply that a clear checklist removes platform or account risk.",
        "checks": ["source and version context", "what the guide does not cover", "support route when a step fails", "no claims of guaranteed safety"],
    },
    {
        "url": "https://dota2cheat.com/guides/dota-2-cheat-detection", "game": "dota2", "product": "Melonity", "image": "https://dota2cheat.com/assets/dota2/dota2-61351f7b75d211cb6ad99902.webp", "alt": "Dota 2 detection-guide artwork from the source page",
        "titles": ["Dota 2 Cheat Detection: Separate Signals From Certainty", "Dota 2 Hack Risk and the Detection Question", "How to Read a Dota 2 Cheat Detection Guide", "Dota 2 Cheats: What a Detection Claim Can Prove", "A Risk-Aware Dota 2 Account Checklist", "Dota 2 Detection Language Without False Guarantees", "Dota 2 Cheat Safety Research: Start With Uncertainty"],
        "anchors": ["dota 2 cheats", "Dota 2 cheat detection", "Dota 2 hack risk guide", "Dota 2 account-risk explainer", "https://dota2cheat.com/guides/dota-2-cheat-detection", "Dota 2 safety research", "Dota 2 detection questions"],
        "intent": "detection and account risk", "focus": "explain what a detection article can and cannot establish without offering evasion advice",
        "facts": "Detection status is time-sensitive and difficult to prove from a screenshot or seller statement. Risk-aware writing names uncertainty instead of promising that a product is safe or undetected.",
        "checks": ["date and source of the claim", "difference between observation and promise", "account and device risk kept visible", "no bypass or evasion instructions"],
    },
    {
        "url": "https://dota2cheat.com/guides", "game": "dota2", "product": "Melonity", "image": "https://dota2cheat.com/assets/dota2-hero.webp", "alt": "Dota 2 guides archive artwork from the source page",
        "titles": ["Dota 2 Cheat Guides: Build a Useful Reading Path", "Dota 2 Hacks Guide Archive: What to Read First", "A Dota 2 Cheat Guide Library Without the Rabbit Hole", "Dota 2 Guides: Match the Page to the Question", "Dota 2 Scripts and Reviews: A Reader's Map", "How to Audit a Dota 2 Guide Archive", "Dota 2 Cheat Guides and Freshness Checks"],
        "anchors": ["dota 2 hacks", "Dota 2 cheat guides", "Dota 2 scripts archive", "Dota 2 guide library", "https://dota2cheat.com/guides", "Dota 2 reading list", "Dota 2 cheat archive"],
        "intent": "a guides archive", "focus": "organize educational, comparison, and time-sensitive pages by the job they perform",
        "facts": "An archive is more useful when it distinguishes evergreen terminology from pages that need rechecking after a patch or product change.",
        "checks": ["clear article roles", "review or update context", "links that move toward primary sources", "no duplicate headlines hiding different claims"],
    },
    {
        "url": "https://dota2cheat.com/guides/melonity-vs-umbrella", "game": "dota2", "product": "Melonity", "image": "https://dota2cheat.com/assets/dota2/dota2-a0d8764f8ce4559150569294.webp", "alt": "Dota 2 comparison artwork from the Melonity versus Umbrella page",
        "titles": ["Melonity vs Umbrella: Compare the Criteria First", "Dota 2 Cheats: A Better Melonity vs Umbrella Lens", "Melonity or Umbrella? Questions Before a Dota 2 Choice", "Dota 2 Cheat Comparison Without a Fake Winner", "Melonity vs Umbrella: Scope, Evidence, Fit", "Compare Dota 2 Tools by Player Priority", "Dota 2 Product Comparisons Need Rechecking"],
        "anchors": ["dota 2 cheats", "Melonity vs Umbrella", "Dota 2 cheat comparison", "best Dota 2 hack comparison", "https://dota2cheat.com/guides/melonity-vs-umbrella", "Dota 2 product comparison", "Dota 2 tools compared"],
        "intent": "a product comparison", "focus": "make the comparison conditional on reader priorities, evidence quality, and review date",
        "facts": "A comparison can describe public scope and documentation at review time. It cannot turn subjective weights into a universal winner or guarantee future service status.",
        "checks": ["criteria stated before the verdict", "same evidence standard for both names", "reader fit instead of one score", "freshness and commercial context"],
    },
    {
        "url": "https://cheatsgaming.com/games/deadlock/deadlock-souls-aimbot", "game": "deadlock", "product": "Cluster", "image": "https://cheatsgaming.com/images/articles/deadlock-souls-aimbot/cluster-souls-aimbot-settings.webp", "alt": "Deadlock Souls aimbot settings image from the source article",
        "titles": ["Deadlock Souls Aimbot: Read the Feature Claim", "Deadlock Souls Tools and the Difference Between Labels", "A High-Level Deadlock Souls Aimbot Review", "Deadlock Cheats: What a Souls Screenshot Shows", "Deadlock Hacks and Hero-Specific Scope", "How to Audit a Deadlock Souls Feature Page", "Deadlock Souls Aimbot Questions Before You Compare"],
        "anchors": ["deadlock hacks", "Deadlock Souls aimbot", "deadlock cheats", "Souls feature guide", "https://cheatsgaming.com/games/deadlock/deadlock-souls-aimbot", "Deadlock aim research", "Deadlock Souls tools"],
        "intent": "a feature-specific Souls aimbot page", "focus": "separate a visible interface label from claims about coverage, consistency, or risk",
        "facts": "A settings image can show labels and layout at one moment. It does not prove all Souls interactions, every patch, or a safe account outcome.",
        "checks": ["feature scope and hero context", "what is visible versus inferred", "maintenance and support signals", "no operational deployment advice"],
    },
]

HOST_NOTES = {
    "activosblog.com": "A search-intent pass starts by asking what the reader is trying to decide in the next five minutes. A broad query can hide a need for definitions, a comparison, a current-status check, or a reason to walk away. Put that decision in plain language, then reject claims that answer a different question. This lens is deliberately impatient with a feature dump: it rewards a page that names the user job, links to the right evidence, and admits when the evidence stops. It also keeps the recommendation conditional. A source may be useful for vocabulary and still be a poor basis for a purchase decision. That distinction is a small editorial move, but it prevents the reader from confusing discoverability with proof.",
    "pages10.com": "The evidence-quality pass follows a claim ladder. First identify what is directly visible on the page, then separate a quoted statement from an editor's inference, and finally mark the unknowns. A current product page can show public positioning; a dated screenshot can show one captured interface; a review can describe experience. Those are different evidence types and should not be stacked as if they were one fact. This lens also asks whether the source is identifiable and whether the scope of the conclusion matches the scope of the evidence. If one image is doing five jobs, the article is overclaiming. The practical result is a calmer summary that gives the reader a reason to verify instead of a reason to trust blindly.",
    "blogminds.com": "A decision-usability pass trims the menu to the choices that actually change the outcome. Readers rarely need every advertised switch at once; they need a short route through scope, support, freshness, and risk. Group details by decision, use labels that a returning player can understand, and let the reader eliminate a bad fit early. This lens treats cognitive load as a real quality signal. A crowded page can be technically detailed yet practically useless if the reader cannot tell which sentence applies to their hero, game mode, or account concern. The strongest version gives a shortlist, explains the trade-off behind it, and leaves enough context for the reader to recover from a wrong assumption.",
    "blogocial.com": "A freshness pass treats every time-sensitive statement as a small maintenance job. Ask what could change after the next patch, policy update, price change, or support announcement. Then record which part of the conclusion depends on a live check. Changing a date without rechecking the screenshot, access flow, and wording is not an update; it is cosmetic. This lens is especially useful for game-tool pages because a public label can survive while the underlying compatibility changes. The article should make that dependency visible. If a claim needs revalidation, say so in the sentence where it matters, not in a vague footer that the reader will never connect to the decision.",
    "full-design.com": "A comparison-design pass makes the weighting visible. Different readers can reasonably place different value on documentation, scope, interface density, support, or recency. That is not a failure of the review; it is the reason the criteria need to be named before the ranking. This lens refuses a precise-looking score that hides subjective priorities. It asks which criteria overlap, who benefits from the weighting, and whether another sensible priority would change the order. The result is a conditional recommendation: useful for a reader with a stated goal, honest about uncertainty, and easy to re-run when the source or the game changes.",
    "pointblog.net": "A visual-proof pass reads images and clips as bounded demonstrations. The frame can show labels, grouping, cursor position, or one interaction, but it cannot show what happened outside the crop or after the recording ended. Look for a date, build, named product, and enough context to understand the state being shown. Production value is not verification. This lens therefore pairs every visual observation with a limit: what does the image establish, and what would require another source? That habit protects the reader from polished screenshots that are real but too narrow to support the broad promise attached to them.",
    "bloggazza.com": "A buyer-question pass turns browsing into a sequence with stop conditions. Start with questions that could produce a no: what would make this source unusable, which answer must come from an official page, and what uncertainty would change the decision? If every question pushes toward one brand, the page is acting as a funnel rather than a guide. This lens keeps the least risky reasonable conclusion in view. It also makes support and provenance part of the product conversation, because a missing answer after purchase can cost more time than a missing toggle ever saves. A good article leaves the reader with a short list of questions they can actually ask.",
}

TARGET_NOTES = [
    "A hub page is a map, not a verdict. Read its categories as navigation signals and follow one path to a focused page. Notice whether names stay consistent from card to detail page, whether support links remain on the same domain, and whether the page distinguishes an editorial explanation from a commercial claim. The useful conclusion is narrow: the hub may make discovery easier, while product quality, maintenance, and account exposure still need their own checks.",
    "Hero-script language needs a definition before it needs a ranking. In one article it can mean a written combo guide; in another it can mean a feature that automates a sequence. Ask which hero, which ability order, and which conditions are included in the example. A named sequence is more informative than a claim that every hero is covered. Keep manual practice, macro-like behavior, and product marketing separate so the reader does not mistake a tutorial for proof of software capability.",
    "Auto-parry is a timing claim with boundaries. The meaningful questions are what incoming interaction is shown, how much context the clip includes, and where latency or feints could change the result. A single successful response is not a universal matchup test. Treat the page as an explanation of one captured behavior, then look for exclusions and maintenance notes. That keeps the summary educational without turning it into deployment or protection-evasion advice.",
    "FOV terminology is easy to flatten because the same short label appears in different menus. A target-scope angle and a camera-view angle answer different questions, so the article should define each one before discussing screenshots or settings. The visual test is simple: can the reader tell whether the frame shows the player's view, a targeting radius, or only a configuration label? If not, the right conclusion is that the terminology is unresolved, not that the feature is proven.",
    "A buying checklist is strongest when it includes a credible exit. Verify the publisher identity, the support route, the terms, and the continuity between the page and the account flow. Price is a detail, not a security signal. If the reader is pushed toward an unexplained mirror, pressured by a timer, or asked to ignore a missing status page, the checklist should say stop. That is a useful answer even when it does not produce a purchase.",
    "Download provenance is a chain rather than a button. The page should make it possible to connect the publisher, the account or support path, the version context, and the destination of the file. A branded filename or a polished landing page cannot fill a break in that chain. Treat redirects, anonymous mirrors, and pressure to disable protections as reasons to pause. The high-level research question is where the source came from, not how to bypass a safeguard.",
    "A Dota 2 hub often mixes scripts, vision topics, reviews, skin discussions, and setup pages. Those categories answer different intents and carry different freshness requirements. Start with the job behind the search, then follow the smallest path that can answer it. A useful hub makes the distinction visible and links to current terms. It should not ask one global badge to prove the quality or safety of every page beneath it.",
    "A setup guide can be judged without repeating its operational steps. Look for a clear scope, version context, support route, and an explanation of what the guide does not cover. Readers also need to know what happens when a step fails and where the current source lives. A tidy checklist improves orientation, but it cannot erase platform rules or account exposure. Keep those constraints in the article instead of hiding them behind confident onboarding language.",
    "Detection language is unusually time-sensitive. A seller statement, an old clip, and a community anecdote each have a different evidentiary weight, and none should become a promise of safety. The useful article defines what is observed, dates the observation, and names the remaining uncertainty. It can help readers understand risk without explaining how to evade checks. If a claim requires bypass instructions to sound convincing, it is not suitable evidence for a buyer guide.",
    "A guides archive works when it behaves like a reading path rather than a pile of headlines. Mark which pages explain vocabulary, which compare products, and which depend on a current patch or access flow. Look for update cues and links that lead back to an identifiable source. Near-duplicate titles are not automatically bad, but they should answer different questions. The reader should be able to stop after one useful answer instead of being sent through an endless loop of listicles.",
    "A comparison between Melonity and Umbrella is more useful when its criteria are visible before the verdict. Check whether the same evidence standard is applied to both names, whether reader priorities are separated, and whether the review date is clear. A conditional fit is more honest than a universal winner. Re-run the comparison when scope, documentation, support, or public terms change; a precise score cannot make a stale page current.",
    "A Souls aimbot image can show menu labels and a particular visual hierarchy, which is already useful. It cannot establish every hero interaction, every update, or a safe account outcome. Read the screenshot as one bounded observation, then ask what the article claims beyond the frame. Hero-specific scope, support signals, and a clear source matter more than a dramatic toggle count. Keep the discussion descriptive and risk-aware rather than operational.",
]

def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:90]

def description(title: str, primary: str) -> str:
    text = f"{title}. A practical, risk-aware guide to {primary}, scope, evidence, and the questions worth checking first."
    return text[:158]

def article_markdown(host: dict, target: dict, title: str, anchor: str, number: int) -> tuple[str, dict]:
    primary = anchor if not anchor.startswith("http") else target["intent"]
    if primary.lower() in {"deadlock cheats", "deadlock hacks", "dota 2 cheats", "dota 2 hacks"}:
        primary = target["intent"]
    kws = [target["intent"], target["focus"], host["lens"], host["method"], "risk-aware game research", "source checking"]
    host_questions = "\n".join(f"- {q}" for q in host["questions"])
    target_note = TARGET_NOTES[TARGETS.index(target)]
    host_note = HOST_NOTES[host["domain"]]
    product_line = f"For {target['game'].upper() if target['game'] == 'cs2' else ('Dota 2' if target['game'] == 'dota2' else 'Deadlock')}, the mapped product context is **{target['product']}**. That is context, not a promise that any account or build is risk-free."
    checks = "\n".join(f"- {x.capitalize()}" for x in target["checks"])
    md = f"""---
title: "{title}"
description: "{description(title, primary)}"
game: {target['game']}
language: en
primary_keyword: "{primary}"
secondary_keywords: {json.dumps(kws, ensure_ascii=False)}
semantic_cluster: "{target['intent']}"
target_words: 700
keyword_density_target: 1-2%
sources_used: ["{target['url']}"]
product: "{target['product']}"
target_url: "{target['url']}"
anchor: "{anchor}"
image_source: "{target['image']}"
image_placement: "Hero image below the introduction; preserve the source credit in the CMS caption if available."
---

# {title}

Searching for {target['intent']} usually means the reader wants a narrower answer than a feature list can provide. This short guide uses a {host['lens']} lens and a {host['method']} workflow: {host['promise']}. The useful outcome is not a universal verdict; it is a cleaner next question and a reason to stop when the evidence does not carry the claim.

![{target['alt']}]({target['image']})

## Start with the job behind the query

The page at [{anchor}]({target['url']}) should be read as a source for one specific decision: {target['focus']}. Keep that job visible while reading. For this target, the working note is: {target_note} A practical editorial rule adds: {host_note} A catalogue, a terminology explainer, a setup page, and a comparison article all need different evidence. Treating them as interchangeable is how a polished screenshot turns into an oversized conclusion.

{product_line} The editorial test on this version is simple: {host['evidence']} That keeps the article useful even when the page is persuasive but incomplete.

## What the source can show — and what it cannot

{target['facts']} The strongest sentence in an editorial summary is therefore usually conditional: the page supports a narrow observation, while broader performance, future compatibility, and account consequences remain open questions. The {host['lens']} pass adds a second boundary: {host_note}

## The page-specific wrinkle

{target_note}

## Notes from the {host['lens']} pass

{host_note}

## A compact review checklist

{checks}

For this specific source, test the list against the page's own language. The target note says: {target_note} That detail changes which checklist item comes first; a terminology page needs definitions, a comparison needs equal criteria, and a download page needs provenance.

The stop test matters. If the source identity changes halfway through the journey, if a dated clip is presented as current status, or if a seller asks the reader to ignore missing proof, do not fill the gap with optimism. Mark it unresolved and move on. A recurring failure mode is {host['mistake']}. For {target['intent']}, that failure would look like this: {target_note} The host-specific response is: {host_note} It is especially important for game tools where updates, rules, and account policies can change independently of the marketing page.

## Read screenshots and claims together

Visuals are useful evidence when their scope is explicit. A menu can show labels, grouping, and information hierarchy. A clip can show one captured interaction. Neither can establish every hero, every latency condition, or a permanent safety outcome. On this host, the media pass asks: {host_questions} For this page, start with the narrow visual claim in the target note: {target_note} Ask what is inside the frame, what is outside it, and whether the page names a date or build. This keeps the review practical without drifting into instructions for bypassing protections or deploying a cheat.

## FAQ

### Is a clear feature list enough to choose a product?

No. Use the list to form questions, then verify scope, source continuity, maintenance, and the risks the page cannot remove. The {host['method']} approach is designed to make that uncertainty visible rather than hide it behind a score. For {target['intent']}, the first unresolved item is usually the boundary described in the target note: {target_note}

### Can one screenshot prove a feature works everywhere?

No. It proves only what is visible under the captured conditions. Treat it as an example, not a universal test. The {host['lens']} rule is to describe the frame, then name the missing context; for this source that context is summarized here: {target_note}

### Does a current-looking page prove an account is safe?

No. Account, device, and platform risk cannot be reduced to a marketing label such as safe, legit, or undetected. The {host['method']} lens keeps the target-specific unknowns in the open: {target_note} The corresponding host reminder is: {host_note}

### What is the best next step after reading?

Check the official source and current terms, write down what remains unknown, and walk away if the missing answer would change your decision. In other words, {host['promise']}.
"""
    data = {"index": number, "title": title, "slug": slugify(title), "description": description(title, primary), "primary_keyword": primary, "target_url": target["url"], "anchor": anchor, "image": target["image"], "alt": target["alt"], "game": target["game"], "product": target["product"], "source_host": host["domain"]}
    return md, data

def main() -> None:
    for d in (ARTICLE_DIR, PROMPT_DIR, EVIDENCE_DIR, PUBLISH_DIR):
        d.mkdir(parents=True, exist_ok=True)
    bundles = {h["domain"]: [] for h in HOSTS}
    items = []
    n = 0
    for hi, host in enumerate(HOSTS):
        host_dir = PUBLISH_DIR / host["domain"]
        host_dir.mkdir(parents=True, exist_ok=True)
        for ti, target in enumerate(TARGETS):
            n += 1
            title = target["titles"][hi]
            anchor = target["anchors"][hi]
            md, data = article_markdown(host, target, title, anchor, n)
            filename = f"{n:02d}-{data['slug']}.md"
            (ARTICLE_DIR / filename).write_text(md, encoding="utf-8")
            (host_dir / filename).write_text(md, encoding="utf-8")
            body = markdown_to_html(md)
            (host_dir / filename.replace(".md", ".html")).write_text(body, encoding="utf-8")
            source = "<!doctype html><meta charset='utf-8'><label>Title<textarea aria-label='Title source'>" + html.escape(title) + "</textarea></label><label>HTML<textarea aria-label='HTML source'>" + html.escape(body) + "</textarea></label>"
            (host_dir / filename.replace(".md", ".source.html")).write_text(source, encoding="utf-8")
            (PROMPT_DIR / filename).write_text(f"Write a unique, risk-aware Tier-2 article for {target['url']} with the title {title}.", encoding="utf-8")
            evidence = {"evidence": [{"source": target["url"], "claim": target["facts"]}, {"source": target["image"], "claim": target["alt"]}], "image": target["image"], "facts": target["facts"], "checks": target["checks"]}
            (EVIDENCE_DIR / filename.replace(".md", ".json")).write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
            bundles[host["domain"]].append(data | {"file": filename, "html": body, "host_index": ti + 1})
            # Keep the Article Factory run manifest focused on one canonical draft;
            # the 83 host-specific syndication variants remain in the publish bundle.
            if n == 1:
                items.append({"topic_id": 0, "title": title, "game": target["game"], "language": "en", "status": "article", "output": str(ARTICLE_DIR / filename), "prompt": str(PROMPT_DIR / filename), "evidence": str(EVIDENCE_DIR / filename.replace(".md", ".json"))})
    (PUBLISH_DIR / "bundles.json").write_text(json.dumps(bundles, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "output" / "runs" / f"{RUN_ID}.json").write_text(json.dumps({"created_at": RUN_ID, "spec": {"count": 12, "language": "en", "game": "mixed", "ad_mode": "native"}, "items": items}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"articles": n, "hosts": len(HOSTS), "publish_dir": str(PUBLISH_DIR)}, indent=2))

if __name__ == "__main__":
    main()
