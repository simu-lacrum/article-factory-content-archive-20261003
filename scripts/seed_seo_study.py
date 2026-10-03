"""Reproducible editorial hypotheses; observed terms are promoted only after a page check."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "research" / "seo-20260921"

# Each row is one reader job, not one mechanically generated landing page.
# game | slug | primary | title | variants | related concepts | reader job
DATA = '''cs2|external|cs2 external cheats|CS2 external cheats: what the label tells you|external cs2 cheat;cs2 internal vs external cheats;are external cs2 cheats safer;cs2 external cheat features|external software;internal software;feature scope;vendor claim;compatibility;update history|Understand what external means and compare claims without mistaking architecture for a safety guarantee
cs2|triggerbot|cs2 triggerbot|CS2 triggerbot vs aimbot: what changes?|triggerbot vs aimbot cs2;what is a triggerbot in cs2;cs2 triggerbot meaning;cs2 triggerbot vs aim assist|crosshair;firing action;target selection;aim assistance;automation;manual input|Separate firing automation from aim movement using an understandable conceptual example
cs2|esp|cs2 esp|CS2 ESP, wallhack and radar: the useful distinctions|cs2 esp vs wallhack;what does esp mean in cs2;cs2 radar vs esp;cs2 wallhack meaning|visibility;information advantage;overlay;line of sight;radar;wallhack|Understand which information each label claims to expose and avoid treating the labels as interchangeable
cs2|aimbot|cs2 aimbot|CS2 aimbot terminology without the sales pitch|cs2 aimbot vs aim assist;what is aimbot in cs2;cs2 aim assist meaning;cs2 legitbot vs aimbot|aim assistance;crosshair movement;target selection;legitbot;input;accuracy|Decode feature descriptions without a setup guide or invented performance claims
cs2|skin-changer|cs2 skin changer|CS2 skin changers: appearance is not inventory|cs2 skin changer vs real skins;can other players see skin changer cs2;cs2 skin changer inventory;cs2 skin changer vs workshop|cosmetic appearance;inventory ownership;Steam inventory;local rendering;trade;workshop|Distinguish a cosmetic display claim from an owned or tradable inventory item
cs2|free-paid|free cs2 cheats|Free CS2 cheats: what a fair comparison should cover|free vs paid cs2 cheats;best free cs2 cheats;free cs2 cheat limitations;cs2 cheat free trial vs free version|access plan;trial;support;update history;feature limits;commercial disclosure|Compare access models and costs without equating a price with quality or safety
cs2|comparison|best cs2 cheats|How to compare CS2 cheats without a fake ranking|cs2 cheat comparison;cs2 cheats review;cs2 cheat review checklist;cs2 cheats alternatives|comparison criteria;dated source;support;feature availability;limitations;disclosure|Build a comparison from dated public claims and identify what was not independently tested
cs2|grenade-helper|cs2 grenade helper|CS2 grenade helpers: lineups, practice and automation|cs2 grenade helper vs lineups;cs2 grenade prediction feature;cs2 grenade helper meaning;cs2 lineup tool vs cheat|lineup;trajectory;practice map;grenade prediction;manual execution;automation|Separate a learning aid from a feature that automates or exposes information
cs2|status|cs2 cheat status|Reading a CS2 cheat status page: what is missing?|what does updating mean cs2 cheat;cs2 cheat status unknown;cs2 cheat detected status meaning;cs2 cheat update history|status page;timestamp;maintenance;vendor report;independent verification;support|Interpret vendor status labels and recognize why an undated badge proves little
cs2|commands|cs2 cheat commands|CS2 cheat commands and third-party software differ|cs2 console cheats vs hacks;sv cheats cs2 meaning;cs2 cheats offline vs online;cs2 practice commands|developer console;practice session;server setting;console command;third-party software|Resolve the ambiguous cheats query before choosing a command reference or software explanation
dota2|scripts|dota 2 scripts|Dota 2 scripts, macros and bots are different things|dota 2 scripts vs macros;dota 2 hero scripts meaning;dota 2 bot scripts vs cheats;what is scripting in dota 2|hero script;input macro;bot scripting;automation;workshop;decision making|Distinguish three types of scripting that search results frequently mix together
dota2|invoker|invoker scripts dota 2|Invoker scripts: what the feature claim leaves out|dota 2 invoker script features;invoker combo script meaning;invoker scripts vs hotkeys;dota 2 invoker auto combo|Invoker;spell combination;input sequence;target choice;cooldown;player decision|Explain a named hero-script claim and the decisions it cannot be assumed to solve
dota2|meepo|meepo scripts dota 2|Meepo scripts: automation claims and real decisions|dota 2 meepo script features;meepo auto combo meaning;meepo scripts vs control groups;meepo automation features|Meepo;unit control;control group;target choice;positioning;micro|Help a reader understand what a vendor means by Meepo automation without invented testing
dota2|maphack|dota 2 maphack|Dota 2 maphack, ESP and fog-of-war claims|dota 2 maphack vs esp;dota 2 jungle maphack meaning;dota 2 fog of war cheat claims;dota 2 vision cheat meaning|fog of war;vision;information advantage;minimap;ward;vendor claim|Explain information claims while distinguishing observed vision from information a vendor only promises
dota2|ward-tracker|dota 2 ward tracker|Dota 2 ward trackers: what is actually being tracked?|dota 2 ward tracker cheat meaning;ward tracker vs ward timer dota 2;dota 2 ward esp;dota 2 enemy ward tracker|observer ward;sentry ward;vision;timer;ward placement;information source|Separate timer tracking from claims about hidden enemy wards
dota2|roshan|dota 2 roshan timer|Dota 2 Roshan timers vs Roshan ESP|dota 2 roshan esp;roshan timer vs esp dota 2;dota 2 roshan tracker;dota 2 roshan cheat feature|Roshan;respawn window;timer;vision;map information;uncertainty|Distinguish a time estimate from a claim about unseen Roshan information
dota2|teleport|dota 2 teleport preview|Dota 2 teleport preview: reading the feature claim|dota 2 teleport tracker;dota 2 tp preview cheat;dota 2 teleport esp;teleport preview meaning dota 2|teleport;destination;cast;map information;visibility;preview|Explain what a teleport-preview description says and what still needs confirmation
dota2|auto-dodge|dota 2 auto dodge|Dota 2 auto-dodge claims: triggers and limitations|dota 2 auto dodge script meaning;auto dodge vs manual dodge dota 2;dota 2 skillshot dodge script;dota 2 dodger feature|projectile;cast timing;movement;reaction;automation;limitations|Distinguish a claimed reaction feature from a guarantee of dodging every spell
dota2|skin-changer|dota 2 skin changer|Dota 2 skin changers and inventory ownership|dota 2 skin changer vs real items;can others see dota 2 skin changer;dota 2 cosmetic changer;dota 2 skin changer inventory|cosmetics;inventory;local appearance;trade;ownership;visibility|Answer who sees an appearance change and whether it creates an owned item, using verified sources
dota2|comparison|dota 2 cheats comparison|Dota 2 cheat comparisons: features before verdicts|melonity vs umbrella;melonity vs octarine;dota 2 scripts comparison;dota 2 cheat review checklist|hero coverage;feature scope;trial;support;current version;commercial interest|Compare current documented capabilities with unknowns visible and no invented winner
dota2|auto-last-hit|dota 2 auto last hit|Dota 2 auto last-hit: a feature, not a lane plan|dota 2 last hit script;dota 2 auto deny script;auto last hit vs manual dota 2;dota 2 farming scripts meaning|last hit;deny;lane equilibrium;timing;target choice;automation|Separate a repeated action from lane strategy without providing automation setup
dota2|commands|dota 2 cheat commands|Dota 2 cheat commands vs third-party scripts|dota 2 lobby cheats vs scripts;dota 2 console cheat codes;dota 2 cheats custom lobby;dota 2 cheats meaning|custom lobby;console;practice;bot;script;third-party software|Route the reader to the right kind of cheats information before discussing products
deadlock|auto-parry|deadlock auto parry|Deadlock auto-parry vs manual parry|deadlock auto parry cheat;deadlock auto parry meaning;deadlock auto parry vs manual;deadlock parry script|melee;parry;timing;reaction;automation;counterplay|Explain what auto-parry claims to automate and preserve the distinction from the legitimate mechanic
deadlock|souls|deadlock souls aimbot|Deadlock souls aimbot: what the feature targets|deadlock soul aimbot;deadlock auto secure souls;deadlock soul deny cheat;deadlock souls aimbot vs player aimbot|soul orb;secure;deny;target type;aim assistance;resource|Separate resource targeting from targeting players using a clear conceptual example
deadlock|esp|deadlock esp|Deadlock ESP, radar and visibility claims|deadlock esp vs wallhack;deadlock radar cheat meaning;what is esp in deadlock;deadlock enemy visibility cheat|ESP;radar;line of sight;map information;overlay;visibility|Understand the information claimed by each label rather than treating all visuals as one feature
deadlock|aimbot|deadlock aimbot|Deadlock aimbot claims: players, projectiles and orbs|deadlock aimbot vs aim assist;deadlock projectile aimbot;deadlock aim assist cheat meaning;deadlock player aimbot vs soul aimbot|projectile;target type;aim assistance;prediction;player;orb|Distinguish advertised target types and avoid unsupported accuracy promises
deadlock|fov|deadlock fov changer|Deadlock FOV: camera view vs an aiming parameter|deadlock fov changer cheat;deadlock camera fov vs aimbot fov;deadlock fov meaning;deadlock fov changer vs settings|field of view;camera;viewport;aiming area;setting;terminology|Resolve the two different meanings of FOV before the reader mistakes one feature for another
deadlock|combos|deadlock hero combos cheat|Deadlock hero-combo features: actions vs decisions|deadlock auto combo meaning;deadlock hero scripts;deadlock combo script features;deadlock auto combo vs manual|hero;ability sequence;cooldown;target;positioning;automation|Separate automated sequences from decisions about positioning and whether to commit
deadlock|dodger|deadlock dodger|Deadlock dodger features and the limits of automation|deadlock auto dodge;deadlock auto dodge cheat meaning;deadlock dodger vs manual dodge;deadlock skillshot dodge script|movement;projectile;reaction;cast;prediction;limitations|Explain the scope of a dodger claim without settings, evasion instructions or guarantees
deadlock|comparison|deadlock cheats comparison|Comparing Deadlock cheats without a made-up winner|best deadlock cheats;deadlock cheat feature comparison;cluster vs avalanche deadlock;deadlock cheat review checklist|feature scope;hero coverage;status date;support;pricing date;disclosure|Compare source-backed claims and make missing evidence part of the verdict
deadlock|trial|free deadlock cheats|Free Deadlock cheats: trial, free tier or sales claim?|deadlock cheat free trial;free vs paid deadlock cheats;deadlock free cheat limitations;deadlock cheat subscription comparison|trial;free tier;access duration;support;feature restriction;renewal|Identify what free actually covers and what the source does not state
deadlock|commands|deadlock cheat commands|Deadlock cheat commands: which game and which context?|deadlock console commands vs cheats;deadlock sandbox cheats;deadlock valve cheats vs planetary conquest;deadlock cheat codes meaning|Valve Deadlock;sandbox;console;Planetary Conquest;Battlestar Galactica;game identity|Disambiguate Valve's game, other games called Deadlock, and console-command intent'''

URLS = {
"cs2": ["https://anyx.gg/", "https://undetek.com/", "https://insanitycheats.com/", "https://cs2hacks.net/", "https://lethality.io/cs2-cheats/", "https://cs2hacks.net/compare-cs2-cheats", "https://cheatix.to/information/counter-strike-2/best-cheats"],
"dota2": ["https://uc.zone/en/dota2", "https://umbrella-dota.com/en/scripts/", "https://dotacheats.com/blog/dota-2-cheats-features-guide", "https://dotacheats.com/", "https://dota2cheat.net/guides", "https://octarine.cc/"],
"deadlock": ["https://avalan.cc/", "https://uc.zone/en/deadlock", "https://forgecheats.com/en/game/deadlock", "https://deadlock.io/en/articles/mechanics/parry", "https://deadlock.wiki/Console_commands"]}

def main():
    clusters, keywords = [], []
    for line in DATA.splitlines():
        game, slug, primary, title, variants, terms, job = line.split("|")
        cid = game + "-" + slug
        intent = "commercial_investigation" if slug in {"comparison", "free-paid", "trial", "external"} else "informational"
        scope = "legitimate_commands" if slug == "commands" else "third_party_software"
        urls = list(URLS[game])
        if slug == "commands":
            urls = {"cs2": ["https://totalcsgo.com/commands"], "dota2": ["https://dota2.fandom.com/wiki/Cheats"], "deadlock": ["https://deadlock.wiki/Console_commands"]}[game]
        if slug == "auto-parry":
            urls += ["https://deadlock.io/en/mechanics/parry"]
        cluster = {"id": cid, "game": game, "language": "en", "primary_query": primary, "title": title,
            "reader_job": job, "intent": intent, "scope": scope, "page_type": "comparison" if intent == "commercial_investigation" else "explanatory_guide",
            "publication_action": "update_article" if slug in {"comparison", "external", "free-paid", "auto-parry", "fov"} else "write_article",
            "primary_site": "cheatsgaming.com" if intent == "commercial_investigation" or game == "dota2" else "deadlockhacks.com" if game == "deadlock" else "counterskrikecheats.com",
            "grouping_basis": "editorial_hypothesis_pending_serp_overlap_validation",
            "original_value": "A reader decision tree for " + primary + ": definition, distinct neighboring features, source-backed limitations, and what evidence would change the conclusion.",
            "semantic_terms": terms.split(";"), "competitor_urls": urls,
            "outline": ["Quick answer to the reader's specific question", "Explain the distinction with one concrete hypothetical example", "What the cited feature descriptions establish and leave unknown", "A short decision checklist", "FAQ"],
            "anchor_guidance": [f"Use a descriptive contextual link to the {game} feature hub when it helps the next reader question", "Use the brand name for a vendor reference; do not disguise promotional links as independent recommendations", "Use the raw URL only when identifying a destination is useful; avoid filler anchors such as click here", "No required exact/partial/branded/naked percentages; inbound backlink ratios remain unmeasured"],
            "evidence_needed": ["Verify each current feature claim on a dated vendor page", "Check existing owned-site coverage before making a new URL", "Collect a dedicated US SERP and real search-volume data before scheduling by demand"],
            "comparison_contract": {"axes": ["documented feature scope", "supported game/version", "access terms", "support channel", "status timestamp", "unknowns"], "claim_fields": ["subject", "claim", "source_url", "checked_at", "evidence_type", "confidence"], "unknown_value": "not publicly confirmed", "disclosure_required": True} if intent == "commercial_investigation" else None}
        clusters.append(cluster)
        for query in [primary, *variants.split(";")]:
            keywords.append({"query": query, "game": game, "language": "en", "cluster_id": cid, "intent": intent,
                             "scope": scope, "discovery": "editorial_expansion", "sources": urls[:2]})
    # Duplicate variants are assigned to the first reader job; alternate relations remain in editorial clusters.
    keywords = list({(k["game"], k["query"]): k for k in reversed(keywords)}.values())[::-1]
    study = {"schema_version": 1, "id": "seo-20260921", "captured_at": "2026-09-21",
             "market": {"country": "US", "engine": "google", "language": "en", "secondary_market": "GB"},
             "metric_policy": {"provider": None, "period": None, "match_type": None},
             "brands": ["Cluster", "Melonity", "Anyx", "Undetek", "Umbrella", "Octarine", "Avalanche"],
             "owned_domains": ["cheatsgaming.com", "deadlockhacks.com", "counterskrikecheats.com", "cluster.center", "melonity.gg"],
             "frequency_thresholds": {"low_max": 100, "mid_max": 1000}, "keywords": keywords, "clusters": clusters, "serps": [],
             "limitations": ["Volumes, CPC and keyword difficulty are not available in connected tools. Import a dated US provider export; do not fabricate tiers.", "Google browser samples request gl=us and hl=en; physical location was not independently verified and the session was signed in.", "Editorial feature variants are hypotheses, not proof that people search for every phrase.", "Outgoing anchors from sampled pages do not measure competitors' incoming backlink profiles.", "Full-body fallback extraction may include banners; inspect the saved HTML before using counts as an editorial comparison.", "Source statements about detection, status, performance and availability are vendor claims, not independently tested facts.", "UK is a separate comparison market; US observations do not establish UK demand."]}
    DIR.mkdir(parents=True, exist_ok=True)
    path = DIR / "study.json"
    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        study["serps"] = existing.get("serps", [])
    path.write_text(json.dumps(study, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"clusters": len(clusters), "keywords": len(keywords), "path": str(path)}))

if __name__ == "__main__":
    main()
