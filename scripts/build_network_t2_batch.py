from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "20260913-085721"
ARTICLE_DIR = ROOT / "output" / "articles" / RUN_ID
RUN_MANIFEST = ROOT / "output" / "runs" / f"{RUN_ID}.json"
PUBLISH_DIR = ROOT / "output" / "publish" / "20260913-network-7x10"


HOSTS = [
    {
        "domain": "activosblog.com",
        "lens": "search intent",
        "method": "intent-first review",
        "promise": "translate a vague search into a concrete question before comparing pages",
        "evidence": "A page is useful only when its answer matches the job behind the query. A broad catalog, a feature explainer, and an installation article should not be judged by the same checklist.",
        "mistake": "treating the keyword as if every searcher meant the same thing",
        "questions": ["What decision brought the reader here?", "Which claim would change that decision?", "What remains uncertain after the page is read?"],
    },
    {
        "domain": "pages10.com",
        "lens": "evidence quality",
        "method": "claim ladder",
        "promise": "separate visible evidence from inference, marketing language, and missing proof",
        "evidence": "Evidence has levels. A current official page can show present positioning; a dated screenshot can show a past interface; a reviewer opinion can explain experience. None of those automatically proves the others.",
        "mistake": "allowing one attractive screenshot to support several unrelated claims",
        "questions": ["Is the source identifiable?", "Is the evidence dated and scoped?", "Does the conclusion stay inside what the evidence can prove?"],
    },
    {
        "domain": "blogminds.com",
        "lens": "decision usability",
        "method": "low-friction shortlist",
        "promise": "reduce menu noise and comparison fatigue without pretending risk disappears",
        "evidence": "A useful comparison lowers cognitive load. It groups information by decisions, uses plain labels, and lets the reader remove bad fits quickly instead of counting every advertised toggle.",
        "mistake": "rewarding the page with the longest feature list instead of the clearest fit",
        "questions": ["Can the choice be explained in one sentence?", "Which details are essential now?", "Can the reader recover from a wrong assumption?"],
    },
    {
        "domain": "blogocial.com",
        "lens": "freshness and maintenance",
        "method": "revalidation loop",
        "promise": "identify which statements expire after a game, product, or access-flow update",
        "evidence": "Freshness is not a year in the headline. It is a record of what was checked, when it was checked, and which parts of the conclusion still depend on a live status page.",
        "mistake": "changing the publication date while leaving old screenshots and claims untouched",
        "questions": ["What can change after the next patch?", "Where is the latest status recorded?", "Which claim needs a new check before action?"],
    },
    {
        "domain": "full-design.com",
        "lens": "comparison design",
        "method": "weighted criteria model",
        "promise": "compare options by reader priorities instead of manufacturing a universal winner",
        "evidence": "Comparisons become honest when criteria and weights are visible. Different priorities can produce different shortlists without either reader being wrong.",
        "mistake": "hiding subjective weights behind a precise-looking score",
        "questions": ["Which criteria are independent?", "Who benefits from this weighting?", "Would another reasonable priority change the order?"],
    },
    {
        "domain": "pointblog.net",
        "lens": "visual proof",
        "method": "screenshot-and-demo audit",
        "promise": "read screenshots and clips for context while resisting polished-but-thin proof",
        "evidence": "Visuals are powerful because they feel concrete. They can demonstrate layout, labels, and one captured state, but they rarely establish current compatibility, security, or broad performance by themselves.",
        "mistake": "confusing production value with verification",
        "questions": ["What exactly is visible?", "What context is outside the frame?", "Is the media tied to a date, build, and named product?"],
    },
    {
        "domain": "bloggazza.com",
        "lens": "buyer questions",
        "method": "question-led research path",
        "promise": "turn browsing into a short sequence of answerable questions and stop conditions",
        "evidence": "Good buyer research begins with questions that can produce a no. If every answer pushes toward the same product, the page is a funnel, not a decision aid.",
        "mistake": "starting with a preferred brand and inventing criteria that justify it",
        "questions": ["What would make the reader walk away?", "Which answer must come from the official source?", "What is the least risky reasonable conclusion?"],
    },
]


TARGETS = [
    {
        "url": "https://cluster.center/en",
        "anchors": ["cheats"] * 7,
        "image": "https://cluster.center/images/subscriptions.gif",
        "alt": "Cluster multi-game subscription page used for an editorial catalog review",
        "subject": "a multi-game cheat catalog",
        "audience": "players comparing more than one supported game or access option",
        "page_job": "organize products, supported games, access choices, and official navigation without forcing the reader to decode a wall of promotions",
        "proof_limit": "A catalog can show structure and current public positioning. It cannot prove zero account risk, permanent compatibility, or the security of every future build.",
        "dimensions": ["game coverage", "access clarity", "official-source continuity", "status visibility", "support routing"],
        "red_flags": ["mixed or unexplained access periods", "product cards with no current status", "download paths that leave the official domain"],
        "detail_heading": "A Catalog Is a Navigation System, Not a Verdict",
        "detail": "A multi-game catalog should help a reader move from game choice to product scope, then to current access and support. Its information architecture is part of the evidence: separate game pages, consistent product names, and an obvious official account path reduce ambiguity. A catalog becomes less useful when one global badge appears to describe every product or when an old promotion is allowed to stand in for current terms. Review the hub as a map. Check whether it leads to a focused page, whether that page explains the relevant game, and whether status or support information stays consistent along the route. The catalog can make discovery faster, but the final decision still belongs at the product level.",
        "primary": ["game cheat search intent", "cheat catalog verification", "cheat shortlist workflow", "cheat catalog freshness", "cheat platform comparison", "cheat catalog screenshots", "first-time cheat research"],
        "titles": [
            "What Game Cheat Searches Are Really Comparing",
            "How to Verify a Multi-Game Cheat Catalog",
            "Build a Cheat Shortlist Without the Hype",
            "Why Cheat Product Pages Need Freshness Labels",
            "Compare Cheat Platforms Without Fake Winners",
            "How to Read Cheat Screenshots Without the Hype",
            "First-Time Cheat Research: Seven Questions",
        ],
    },
    {
        "url": "https://cluster.center/en/cs2",
        "anchors": ["cs2 cheats", "cs2 cheats", "cs2 cheats", "cs2 cheats", "cs2 hacks", "https://cluster.center/en/cs2", "CS2 cheat tools"],
        "image": "https://cluster.center/_next/image?url=%2Fimages%2Fproducts%2Fcs2%2Fhud.webp&w=3840&q=75",
        "alt": "Cluster CS2 HUD screenshot used to discuss interface and claim quality",
        "subject": "a CS2 product page",
        "audience": "CS2 readers trying to compare features, interface clarity, and current support",
        "page_job": "explain feature groups and the interface in language that connects each control to a real user decision",
        "proof_limit": "A product page and HUD preview can show categories and presentation. They cannot establish future compatibility or remove account and device-security risks.",
        "dimensions": ["feature grouping", "HUD readability", "configuration control", "update communication", "support clarity"],
        "red_flags": ["every toggle presented as equally important", "undated interface media", "absolute safety language"],
        "detail_heading": "For CS2, Screen Space Is Part of the Comparison",
        "detail": "CS2 places a heavy premium on readable motion, sound cues, radar awareness, and a clean center of screen. That makes interface density a meaningful review dimension. Count not only advertised visual elements but also how many compete for attention at once. A product image can reveal grouping, color hierarchy, label length, and whether status is distinguishable from configuration. It cannot show how the same layout behaves across maps, resolutions, or updates. A useful CS2 review therefore separates the menu from the match view and asks whether the page documents both. When screenshots show only a dramatic fully enabled setup, look for a quieter baseline before drawing conclusions about usability.",
        "primary": ["CS2 cheat buyer intent", "CS2 cheat claims", "CS2 cheat usability", "CS2 cheat compatibility", "CS2 cheats comparison", "CS2 cheat HUD screenshots", "CS2 cheat search checklist"],
        "titles": [
            "CS2 Cheat Buyers: Feature Lists vs Everyday Use",
            "CS2 Cheat Claims: An Evidence Ladder",
            "CS2 Cheat Feature Density vs Usability",
            "How to Read CS2 Cheat Compatibility Windows",
            "Compare CS2 Cheats by Workflow and Support",
            "CS2 Cheat HUD Screens: What Clutter Reveals",
            "A CS2 Cheat Search Checklist for Returning Players",
        ],
    },
    {
        "url": "https://cluster.center/en/deadlock",
        "anchors": ["deadlock cheats", "deadlock cheats", "deadlock cheats", "deadlock cheats", "deadlock hacks", "https://cluster.center/en/deadlock", "Deadlock hack guide"],
        "image": "https://cluster.center/_next/image?url=%2Fimages%2Fproducts%2Fdeadlock%2Fpreview.webp&w=3840&q=75",
        "alt": "Cluster Deadlock product preview used for an editorial feature review",
        "subject": "a Deadlock product page",
        "audience": "Deadlock players comparing roster-wide systems with hero-specific support",
        "page_job": "separate general features from hero-dependent functions and explain how coverage may change with game updates",
        "proof_limit": "A preview can show a menu state and named categories. It does not prove equal depth for every hero or uninterrupted support after patches.",
        "dimensions": ["hero coverage", "roster-wide features", "control clarity", "patch context", "documented limitations"],
        "red_flags": ["all-hero claims with no depth", "features detached from hero context", "old clips presented as live status"],
        "detail_heading": "Deadlock Coverage Has Breadth and Depth",
        "detail": "Deadlock combines shooting, movement, abilities, items, and a growing roster. A page saying that many heroes are supported may refer to roster-wide visuals, shared mechanics, or genuinely hero-specific behavior. Those are different kinds of coverage. Ask the writer to label them. Breadth matters to players with a wide hero pool; depth matters to a specialist who cares about one kit and its edge cases. Patch context matters to both. A dated named-hero example is more informative than a grid of portraits, while a roster-wide feature should not be counted repeatedly as if it were a custom module for every hero. Honest exclusions make the coverage claim stronger, not weaker.",
        "primary": ["Deadlock cheat research", "Deadlock cheat changelog", "Deadlock cheat menu design", "Deadlock cheat update notes", "Deadlock cheats comparison", "Deadlock cheat previews", "Deadlock cheat FAQ"],
        "titles": [
            "Deadlock Cheat Research: Questions Before Comparing",
            "What a Deadlock Cheat Changelog Can Prove",
            "Deadlock Cheat Menus and Information Hierarchy",
            "Deadlock Cheat Update Notes Need Patch Context",
            "Compare Deadlock Cheats by Coverage and Controls",
            "Deadlock Cheat Previews: Readability Over Spectacle",
            "Deadlock Cheat FAQ: Scope, Updates, Expectations",
        ],
    },
    {
        "url": "https://cheatsgaming.com/",
        "anchors": ["gaming cheat guides", "independent cheat article library", "practical cheat guide hub", "updated cheat articles", "cheat comparison resources", "visual cheat review archive", "cheat research articles"],
        "image": "https://cheatsgaming.com/images/game-sections/cs2-cheats-editorial.webp",
        "alt": "CheatsGaming CS2 editorial image used to explain guide navigation",
        "subject": "an editorial cheat-guide hub",
        "audience": "readers moving from broad discovery to a specific game, feature, or comparison",
        "page_job": "provide a clear taxonomy, transparent article dates, traceable product sources, and a path from overview to focused guide",
        "proof_limit": "An editorial hub can organize research and expose useful vocabulary. Its existence does not make every linked claim current or independent.",
        "dimensions": ["topic taxonomy", "bylines and dates", "source links", "comparison scope", "navigation depth"],
        "red_flags": ["many near-duplicate headlines", "no distinction between guide and advertisement", "roundups without selection criteria"],
        "detail_heading": "A Guide Hub Should Show Its Editorial Map",
        "detail": "An editorial home page earns trust by making relationships clear. Category pages should separate game overviews, feature explainers, comparisons, and time-sensitive setup articles. Readers should be able to tell whether a post is educational, commercial, or both. Byline, review date, named criteria, and direct source links matter more than the number of published pages. When dozens of similar headlines point toward the same conclusion, check whether each article answers a genuinely different question. A useful hub reduces repetition through deliberate internal paths: glossary to comparison, comparison to official source, and official source to current support. That structure helps readers leave the site with a defined answer instead of an endless loop of listicles.",
        "primary": ["cheat guide credibility", "cheat editorial verification", "cheat guide navigation", "cheat review freshness", "cheat site comparison", "cheat review images", "cheat directory navigation"],
        "titles": [
            "Cheat Guide Credibility: Five Signals to Check",
            "How to Audit an Editorial Cheat Guide",
            "From Cheat Glossary to Buyer Guide: A Better Path",
            "What Cheat Reviews Must Recheck After Updates",
            "Cheat Sites vs Single-Game Tools: How to Research",
            "Cheat Review Images: Proof, Context, Missing Detail",
            "Cheat Directory Navigation Without the Rabbit Hole",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/cs2/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52",
        "anchors": ["free CS2 cheat guide", "free CS2 hack research", "no-cost CS2 cheat overview", "free CS2 hack checklist", "free versus paid CS2 cheat guide", "free CS2 cheat demo article", "best free CS2 cheat questions"],
        "image": "https://cheatsgaming.com/media/medium/4c8440c116bd2d5030f28a81.png",
        "alt": "CS2 menu image from the referenced free-cheat editorial guide",
        "subject": "a free CS2 cheat roundup",
        "audience": "readers who use the word free but may mean a trial, limited tier, giveaway, or permanently free build",
        "page_job": "define what free means, identify the official source, explain limits, and keep price separate from security and account risk",
        "proof_limit": "A zero price can be verified at a moment in time. It says nothing by itself about provenance, maintenance, detection, or hidden costs.",
        "dimensions": ["type of free access", "source identity", "maintenance cadence", "limitations", "total risk cost"],
        "red_flags": ["anonymous mirrors", "a trial described as permanently free", "security promises based only on popularity"],
        "detail_heading": "The Word Free Needs a Type and a Time Frame",
        "detail": "Free may mean an unrestricted public build, a short trial, a limited feature tier, a temporary promotion, or access bundled with something else. A useful article names the type and the date. It also separates monetary price from other costs: time spent troubleshooting, exposure to unofficial mirrors, missing support, and the possibility of account consequences. None of those costs proves that paid software is safe; price is simply a poor proxy. For a free-CS2 roundup, the first audit is source continuity. The product name, official site, account flow, and download origin should form one traceable chain. If that chain breaks, the correct advice is to stop rather than search for a random replacement file.",
        "primary": ["free CS2 cheat fine print", "free CS2 hack evidence", "free CS2 cheat risk screen", "abandoned free CS2 hacks", "free vs paid CS2 cheats", "free CS2 cheat videos", "what free CS2 hacks mean"],
        "titles": [
            "Free CS2 Cheat Pages: Read the Fine Print First",
            "Free CS2 Hacks: Evidence Beyond the Price Tag",
            "Free CS2 Cheat Research: A Stoplight Risk Screen",
            "Free CS2 Hacks and Abandoned Builds: Warning Signs",
            "Free vs Paid CS2 Cheats: Questions Price Cannot Answer",
            "Free CS2 Cheat Videos: What a Demo Cannot Establish",
            "Free CS2 Hack Search: Decide What Free Means",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924",
        "anchors": ["Deadlock auto-parry cheat overview", "Deadlock auto-parry hack explainer", "Deadlock auto-parry cheat analysis", "Deadlock auto-parry cheat page", "Deadlock auto-parry hack review", "Deadlock auto-parry cheat clip guide", "Deadlock auto-parry hack FAQ"],
        "image": "https://cheatsgaming.com/media/medium/047332b84a6d6b180f78af24.gif",
        "alt": "Deadlock auto-parry animation from the referenced feature article",
        "subject": "a Deadlock auto-parry explainer",
        "audience": "readers trying to understand an automation claim without turning a short demo into a universal promise",
        "page_job": "describe the concept at a high level, name trigger assumptions and exclusions, and separate observable timing from marketing conclusions",
        "proof_limit": "A clip can show that one interaction occurred under captured conditions. It cannot establish every matchup, latency condition, future patch, or safety claim.",
        "dimensions": ["trigger conditions", "timing context", "hero and matchup scope", "player control", "documented exclusions"],
        "red_flags": ["perfect language with no conditions", "looped clips with no build context", "one matchup generalized to the whole roster"],
        "detail_heading": "Auto-Parry Claims Depend on Conditions",
        "detail": "Auto-parry is best discussed as a timing and scope claim, not as a magic outcome. A useful explainer names the kind of incoming interaction shown, the player's remaining control, the hero or matchup context, and any stated exclusions. Latency, feints, overlapping effects, and future balance changes are reasons to avoid absolute language even without detailing implementation. A short loop can make the response look universal because failures and setup conditions are outside the frame. Reviewers should therefore describe what the clip demonstrates in one sentence, then list what it does not test. That keeps the article educational without drifting into configuration instructions or methods for defeating protective systems.",
        "primary": ["Deadlock auto-parry trade-offs", "auto-parry evidence", "auto-parry player agency", "auto-parry maintenance", "auto-parry comparison", "auto-parry demo context", "Deadlock auto-parry questions"],
        "titles": [
            "Deadlock Auto-Parry: Timing, Scope, Trade-Offs",
            "How to Evaluate Deadlock Auto-Parry Claims",
            "Deadlock Auto-Parry and the Limits of Automation",
            "Why Deadlock Auto-Parry Needs Maintenance Context",
            "Auto-Parry vs Manual Defense: A High-Level Lens",
            "Deadlock Auto-Parry Clips: Watch the Conditions",
            "Deadlock Auto-Parry FAQ Before You Evaluate",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/cs2/top-cheats-for-cs2-the-best-hack-cfab8351f70b",
        "anchors": ["top CS2 cheat comparison", "best CS2 hack shortlist", "leading CS2 cheat guide", "current CS2 hack ranking", "top CS2 hacks comparison", "CS2 cheat gallery and ranking", "top CS2 cheat buyer guide"],
        "image": "https://cheatsgaming.com/media/medium/6abd436a24150a9a4abe2970.jpg",
        "alt": "CS2 product image from the referenced top-cheat comparison",
        "subject": "a ranked CS2 cheat article",
        "audience": "readers looking for a fast shortlist but needing to understand how the order was produced",
        "page_job": "state selection criteria, disclose weighting, define the review date, and explain which type of reader each option may fit",
        "proof_limit": "A ranking summarizes one editor's criteria at one time. It cannot create a universal winner or guarantee future product status.",
        "dimensions": ["criteria transparency", "reader fit", "feature relevance", "documentation", "review recency"],
        "red_flags": ["precise scores with no method", "permanent winner language", "rank changes that mirror commission value"],
        "detail_heading": "A Ranking Needs a Reader Model",
        "detail": "A top-CS2 list is not a fact until the word top is defined. One reader may value clear onboarding, another a restrained interface, and another public update notes. Give those readers separate lenses rather than averaging them into an imaginary universal buyer. The ranking should disclose selection rules, comparison date, and whether commercial relationships influence placement. It should also distinguish feature presence from feature quality. Ten named controls do not necessarily create ten independent benefits, and one well-documented workflow may matter more than a crowded menu. The strongest conclusion is conditional: best for a stated priority under the evidence available at review time.",
        "primary": ["CS2 cheat ranking criteria", "best CS2 hack evidence", "CS2 cheat priority shortlist", "CS2 hack ranking updates", "weighted CS2 hack comparison", "CS2 hack gallery audit", "CS2 cheat buyer questions"],
        "titles": [
            "Top CS2 Cheat Lists: Criteria That Deserve Weight",
            "Best CS2 Hack Articles Need an Evidence Ladder",
            "Rank CS2 Cheats by Player Priority, Not Feature Count",
            "A Revalidation Schedule for CS2 Cheat Rankings",
            "Top CS2 Hacks: Weighted Criteria for Real Players",
            "CS2 Hack Galleries: Read Labels and Status Signals",
            "CS2 Cheat Buyer Questions Rankings Cannot Answer",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/cs2/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364",
        "anchors": ["legit CS2 hack guide", "legit-style CS2 cheat review", "legit CS2 cheat breakdown", "legit CS2 hack article", "legit CS2 cheat comparison", "legit CS2 hack visuals", "legit CS2 cheat FAQ"],
        "image": "https://cheatsgaming.com/media/medium/bb7e3f764ea76d2c8e62fab6.jpg",
        "alt": "CS2 interface image from the referenced legit-style cheat comparison",
        "subject": "a legit-style CS2 cheat comparison",
        "audience": "readers using the word legit to describe restrained presentation rather than official approval",
        "page_job": "define ambiguous language, translate style labels into observable criteria, and keep subtlety separate from safety claims",
        "proof_limit": "A restrained interface or smooth-looking clip can illustrate presentation. It cannot prove permission, detection status, or security.",
        "dimensions": ["terminology", "visual restraint", "user control", "claim precision", "risk disclosure"],
        "red_flags": ["legit used as a synonym for approved", "human-like treated as proof of safety", "subtle screenshots with no product identity"],
        "detail_heading": "Legit Is Style Vocabulary, Not Approval",
        "detail": "In this niche, legit usually describes restrained presentation or behavior intended to appear less dramatic. It should not be read as official permission, verified security, or protection from penalties. A careful comparison translates the label into observable properties: quieter visuals, more manual control, configurable limits, or a less aggressive default profile. Then it evaluates those properties without extending them into a safety claim. This semantic cleanup matters for search quality because normal-language readers may hear legitimate where the article means subtle. Put the definition near the top, repeat the boundary in the FAQ, and avoid pairing the label with guarantees that the page cannot substantiate.",
        "primary": ["legit CS2 hack meaning", "legit CS2 cheat evidence", "legit CS2 cheat behavior", "old legit CS2 cheat advice", "legit-style CS2 cheats", "legit CS2 cheat visuals", "legit CS2 hack terminology"],
        "titles": [
            "What Legit CS2 Hack Means in Search Results",
            "Legit CS2 Cheat Reviews: Read Language, Not Labels",
            "Define Legit CS2 Cheat Behavior Before Comparing",
            "When Legit CS2 Cheat Recommendations Expire",
            "Legit-Style CS2 Cheats: Compare Control and Limits",
            "Legit CS2 Cheat Visuals Can Still Mislead",
            "Legit CS2 Hack Terminology: A Plain-English FAQ",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/deadlock/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e",
        "anchors": ["best Deadlock cheat roundup", "Deadlock hack comparison", "top Deadlock hack guide", "Deadlock cheat ranking", "best Deadlock cheats list", "Deadlock hack feature roundup", "best Deadlock hack research"],
        "image": "https://cheatsgaming.com/media/medium/79a4acf3465c24536ad2fc25.jpg",
        "alt": "Deadlock menu image from the referenced cheat roundup",
        "subject": "a Deadlock cheat roundup",
        "audience": "players comparing broad suites, focused tools, and hero-dependent functions",
        "page_job": "connect each recommendation to a player problem, distinguish breadth from depth, and expose patch-sensitive claims",
        "proof_limit": "A roundup can reduce discovery time. It cannot verify every hero, mode, update, or private support claim on the reader's behalf.",
        "dimensions": ["problem fit", "hero depth", "suite breadth", "control design", "maintenance evidence"],
        "red_flags": ["one ranking for every hero pool", "generic features counted as hero modules", "no date beside patch-sensitive claims"],
        "detail_heading": "Deadlock Shortlists Should Begin With the Player Problem",
        "detail": "A player confused by screen information has a different problem from a player researching hero-specific support. A third reader may care mostly about maintenance signals. Organize the roundup around those jobs before listing products. Broad suites can appeal to varied play, while focused tools may present one concept more clearly; neither category wins automatically. For each option, distinguish roster-wide systems, mechanic-level assistance, and hero-specific modules. Then ask whether the evidence is recent enough for a patch-sensitive game. The shortlist should shrink as criteria become clearer. If a page cannot state which player problem an entry solves, its position probably comes from feature-count theater rather than fit.",
        "primary": ["Deadlock cheat feature language", "Deadlock hack scope evidence", "Deadlock cheat suite choice", "dated Deadlock cheat claims", "Deadlock cheat suite comparison", "Deadlock cheat demo context", "best Deadlock cheat questions"],
        "titles": [
            "Deadlock Cheat Categories: Learn the Feature Language",
            "Deadlock Hack Comparisons Need Hero and Mode Scope",
            "Deadlock Cheat Tools: Broad Suite or Focused Utility?",
            "Date Every Claim in a Deadlock Cheat Roundup",
            "Deadlock Cheat Suites vs One-Feature Tools",
            "Deadlock Cheat Demos Need Hero Context",
            "Best Deadlock Cheat Research Starts With the Problem",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/cs2/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710",
        "anchors": ["CS2 cheat installation guide", "CS2 hack setup article", "CS2 cheat onboarding guide", "CS2 cheat install article", "CS2 hack installation guide", "CS2 cheat setup screenshots", "CS2 hack install FAQ"],
        "image": "https://cheatsgaming.com/media/medium/4eabd161daef048624051f45.png",
        "alt": "CS2 product page screenshot from the referenced installation article",
        "subject": "a CS2 cheat installation article",
        "audience": "readers who need source, access, version, and support context before following any product-specific instructions",
        "page_job": "separate orientation from live documentation, confirm provenance, and define clear stop conditions without teaching protection bypasses",
        "proof_limit": "A successful screenshot can show a historical step. It does not validate today's file, compatibility, access terms, or account safety.",
        "dimensions": ["official source chain", "access prerequisites", "version context", "support path", "safe stop conditions"],
        "red_flags": ["unofficial mirrors", "instructions that override security warnings", "screenshots from an unnamed or old build"],
        "detail_heading": "Installation Content Needs a Provenance Chain",
        "detail": "A responsible installation article begins before any download: identify the official product page, current access requirements, supported build, and legitimate support route. It then keeps product-specific steps on the current official documentation. Screenshots are useful orientation when they name the page and visible state, but old button locations should not be treated as commands. A changed interface, broken official link, unexpected domain, or security warning is a stop condition. The article should never fill gaps with mirror links, credential requests, or advice for suppressing protections. Its value is a clean provenance chain and clear escalation path, not a clever workaround for outdated instructions.",
        "primary": ["CS2 cheat preflight checklist", "CS2 hack setup evidence", "CS2 cheat onboarding", "versioned CS2 cheat guides", "CS2 cheat support docs", "CS2 cheat setup images", "CS2 cheat install questions"],
        "titles": [
            "CS2 Cheat Install Content: A Preflight Checklist",
            "Separate CS2 Cheat Setup Claims From Evidence",
            "What Clear CS2 Cheat Onboarding Should Explain",
            "Versioning Makes CS2 Cheat Guides More Useful",
            "CS2 Cheat Install Guides vs Support Documentation",
            "What CS2 Cheat Setup Screenshots Should Explain",
            "CS2 Cheat Installation FAQ Before Any Download",
        ],
    },
]


def slugify(value: str) -> str:
    value = value.lower().replace("’", "").replace("'", "")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:78].rstrip("-")


def oxford(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + ", and " + items[-1]


def article_markdown(host_index: int, target_index: int) -> tuple[str, dict]:
    host = HOSTS[host_index]
    target = TARGETS[target_index]
    title = target["titles"][host_index]
    primary = target["primary"][host_index]
    anchor = target["anchors"][host_index]
    description = f"{primary}: a practical guide to {host['promise']} for {target['subject']}."
    if len(description) > 160:
        description = f"{primary}: how to {host['promise']}."
    if len(description) > 160:
        description = description[:157].rstrip(" ,.;:") + "."

    dimensions = target["dimensions"]
    red_flags = target["red_flags"]
    q1, q2, q3 = host["questions"]
    related = [f"{dimensions[0]} signals", f"{dimensions[1]} checks", f"{dimensions[2]} evidence"]
    target_kind = (
        "Deadlock" if "Deadlock" in title or "Deadlock" in primary
        else "CS2" if "CS2" in title or "CS2" in primary
        else "Dota 2" if "Dota 2" in title or "Dota 2" in primary
        else "multi-game"
    )
    game_slug = "dota2" if target_kind == "Dota 2" else target_kind.lower().replace("-", "")
    product_note = (
        "For Dota 2 research, Melonity is the mapped product source in this editorial set. "
        "That mapping keeps brand references consistent; it is not a safety certificate or a substitute for checking the live page."
        if target_kind == "Dota 2"
        else "For CS2 and Deadlock research, cluster.center is the mapped product source in this editorial set. "
             "That mapping keeps brand references consistent; it is not a safety certificate or a substitute for checking the live page."
    )

    product_name = "Melonity" if target_kind == "Dota 2" else "cluster.center"
    front_matter = f'''---
title: "{title}"
seo_title: "{title}"
description: "{description}"
game: "{game_slug}"
language: "en"
primary_keyword: "{primary}"
secondary_keywords: {json.dumps(related)}
product: "{product_name}"
target_url: "{target['url']}"
anchor: "{anchor}"
source_host: "{host['domain']}"
image_source: "{target['image']}"
---
'''

    shared_link = f"[{anchor}]({target['url']})"

    if host_index == 0:
        article = f'''
# {title}

{primary} starts with a deceptively simple question: what is the reader actually trying to decide? With {target['subject']}, the keyword may describe discovery, verification, comparison, or preparation. Treating all four as the same intent produces an article that ranks words but solves no real problem.

The practical answer is to name the decision first. For {target['audience']}, the page should {target['page_job']}. Everything else is supporting detail. Third-party tools may violate game rules and create account or device-security risks, so a useful article must also leave room for “do not proceed.”

![{target['alt']}]({target['image']})

## One Search Can Hide Three Different Jobs

A discovery reader wants vocabulary and a map of the category. A comparison reader wants meaningful differences. A verification reader already saw a claim and wants to know whether it holds up. Those jobs can share a keyword while needing different answers.

For {target['subject']}, begin by sorting the visit into one of three buckets:

- “Explain it” — define the feature, label, or page type;
- “Compare it” — show trade-offs using explicit criteria;
- “Check it” — test a specific statement against dated, traceable evidence.

This prevents the classic intent mismatch: a person asks what a term means and receives a sales ranking, or asks for a current comparison and receives a timeless glossary. Strong {primary} makes the page type obvious in the opening paragraph.

## Turn the Keyword Into a Decision Sentence

Rewrite the query as: “I need to decide whether this page gives me enough information about {dimensions[0]} and {dimensions[1]}.” That sentence is far more useful than a pile of related keywords. It tells the writer what belongs in the article and what is a tangent.

Next, add a boundary: {target['proof_limit']} The boundary matters because readers routinely transfer confidence from one visible detail to a much larger conclusion. A clean menu can demonstrate organization. It cannot certify safety. A current price can demonstrate an offer. It cannot prove maintenance quality.

The best opening answer is therefore narrow and testable. It should say what the page can help with, what must be verified elsewhere, and which uncertainty remains.

## Match Evidence to the Reader's Intent

Check {oxford(dimensions)} one at a time. For an explainer, clear definitions and examples may be enough. For a current comparison, look for live official pages, review dates, and stated limitations. For verification, trace the exact claim back to a named source rather than relying on another roundup that copied it.

Use this quick intent-first review:

1. State the reader's decision in one sentence.
2. Choose the two criteria that could change that decision.
3. Identify which claims are time-sensitive.
4. Mark screenshots as demonstrations, not universal proof.
5. Write a stop condition before writing a recommendation.

That last step keeps the article honest. If the source is unclear, the terms conflict, or the live page no longer matches the guide, stopping is a successful research outcome.

## Intent Errors That Create Bad Advice

The biggest error is {host['mistake']}. Topic-specific warning signs include {red_flags[0]}, {red_flags[1]}, and {red_flags[2]}. Each one signals that the page may be answering its own promotional goal rather than the reader's question.

Another error is packing several intents into one conclusion. “Easy to understand,” “currently available,” and “low risk” are separate claims. They need separate support. A writer can praise clarity while remaining uncertain about current status; those conclusions do not conflict.

Do not fill missing evidence with operational instructions, especially guidance about bypassing protections. A safer article keeps product-specific action on the official source and focuses on evaluation.

## Use the Referenced Page as an Orientation Point

The referenced {shared_link} page can help orient the reader to this topic. Its headings, images, and product names show how the subject is presented, but time-sensitive details should be checked on the live official source.

{product_note} Separate discovery, verification, and action. That three-step rhythm makes {primary} easier to scan, easier to quote accurately, and less likely to turn an old claim into new misinformation.

## FAQ

### What does {primary} try to solve?

{primary} should identify the real decision behind the query and supply only the evidence needed for that decision.

### Why can two people use the same keyword differently?

One may want a definition, another a shortlist, and another a current verification. The wording is shared; the job is not.

### Is a source-page image enough evidence?

No. It can show a captured interface or example, but it cannot prove future compatibility, safety, or every advertised use case.

### When should the reader stop?

Stop when the official source is unclear, current terms contradict the article, or the next step requires ignoring a security warning.
'''
    elif host_index == 1:
        article = f'''
# {title}

The right way to assess {target['subject']} is to build an evidence ladder. Put the weakest material at the bottom—unsupported adjectives—and the strongest available material at the top—current, identifiable, scope-limited information from the relevant source. {primary} fails when those levels are blended together.

For {target['audience']}, the key rule is simple: a claim may travel only as far as its evidence. Third-party competitive tools can create rule, account, and device-security risks; no screenshot, ranking, or “undetected” label removes them.

![{target['alt']}]({target['image']})

## Inventory the Claims Before Judging the Page

Do not start by deciding whether the page feels convincing. First list what it is asking you to believe. On this topic, likely claims concern {oxford(dimensions)}. These are not one bundle. Each needs a separate source and time frame.

Classify statements as observable, reported, inferred, or promotional. “The screenshot contains a settings panel” is observable. “The vendor reports support for a feature” is reported. “The interface will remain compatible” is an inference. “The safest choice” is promotional unless the page defines and supports that comparison.

This small inventory changes the whole read. Instead of debating tone, you can point to the exact sentence that needs stronger support.

## Build a Four-Rung Evidence Ladder

Use four rungs for {primary}:

1. An unattributed statement or slogan.
2. A visual with an identifiable product but no date or build context.
3. A dated first-party page that states the relevant scope.
4. A conclusion that combines current sourcing, direct observation, limitations, and a clear review date.

Higher does not mean infallible. A first-party page is authoritative for what the vendor currently says, not independent proof of every outcome. A reviewer's test may add experience, but only for the conditions actually described.

{target['proof_limit']} Good evidence writing says that directly instead of letting a reader assume the biggest possible conclusion.

## Test the Five Important Dimensions Separately

Evaluate {dimensions[0]}, {dimensions[1]}, {dimensions[2]}, {dimensions[3]}, and {dimensions[4]} as five columns in your notes—even if the published article uses no table. Give each claim its own source, date, and limitation.

Ask:

- Is the source identifiable and official for this statement?
- Is the date meaningful, or merely the page's latest edit timestamp?
- Does the media show the named product and relevant state?
- Does the conclusion match the sample size?
- Could a game or product update invalidate it?

If one answer is missing, lower that claim on the ladder. Do not drag the entire page down automatically; reduce only the unsupported conclusion.

## Watch for Evidence Laundering

Evidence laundering happens when many sites repeat the same unsourced sentence until it looks established. It also happens when {host['mistake']}. For this topic, be especially cautious around {red_flags[0]}, {red_flags[1]}, and {red_flags[2]}.

Trace a strong claim backwards. If every article points to another article and none reaches an official page, dated media, or a described observation, the chain is circular. Search visibility is not verification.

The most trustworthy wording often sounds modest: “shown on the page,” “reported at the time of review,” or “not independently established.” Precision is more useful than swagger.

## Place the Referenced Page on the Right Rung

Use the {shared_link} article as a discovery and context source. It may introduce terminology, images, and candidates for a shortlist. Before relying on patch-sensitive or access-related details, compare them with the current official product page.

{product_note} For {target_kind} readers, the result should be a claim ledger, not blind acceptance or automatic dismissal. That is what makes {primary} useful: it preserves the difference between what is seen, what is said, and what is still unknown.

## FAQ

### What is the strongest evidence for {primary}?

The strongest practical evidence combines a current identifiable source, clear scope, direct observation, a review date, and stated limitations.

### Can an official page prove every product claim?

No. It reliably shows what the publisher states. Independent outcomes require appropriately scoped observation, and future behavior remains uncertain.

### Why are screenshots weak for safety claims?

They show pixels from one captured state. They do not show detection history, file security, future updates, or permission under game rules.

### What should happen when evidence is missing?

Narrow the conclusion or mark it unverified. Do not replace the missing proof with a stronger adjective.
'''
    elif host_index == 2:
        article = f'''
# {title}

{primary} is a usability problem before it is a feature-count problem. A reader should be able to move from “I am curious” to a small, understandable shortlist without memorizing dozens of labels. If the page increases decision fatigue, more information is not helping.

For {target['audience']}, the best approach is a low-friction shortlist: define the job, remove obvious mismatches, then compare the survivors on {dimensions[0]} and {dimensions[1]}. This does not make third-party tools safe or permitted; it simply makes the research legible.

![{target['alt']}]({target['image']})

## Reduce the Information Burden First

The page should {target['page_job']}. That job gets lost when every menu item, screenshot, and marketing badge receives equal visual weight. Readers need hierarchy: what matters now, what can wait, and what requires a live check.

Start with three buckets. Put must-have criteria in the first, useful extras in the second, and interesting-but-irrelevant features in the third. For this topic, {dimensions[0]} and {dimensions[1]} often belong near the top; {dimensions[2]} and {dimensions[3]} need verification; {dimensions[4]} can decide a tie.

This is not a universal order. It is a way to make the reader's priorities visible before the page's feature list rewrites them.

## Shortlist in Three Passes

The first pass checks fit. Does the page address the actual game, feature, hero scope, or access question? The second checks clarity. Can the reader understand the interface, limitation, and support route? The third checks risk and freshness.

Use this sequence:

1. Remove candidates that do not answer the core job.
2. Remove pages with unclear official-source continuity.
3. Compare remaining options on only two or three dimensions.
4. Confirm that the live page still matches the article.
5. Keep “none of these” as a valid result.

The final option matters. A shortlist designed only to produce a purchase is not neutral decision support.

## Read Interface Signals as Interface Signals

Visual hierarchy, plain labels, reset controls, and understandable states can indicate thoughtful interface design. They do not establish detection status or software security. {target['proof_limit']}

When reviewing an image, ask whether it helps explain {dimensions[0]} or {dimensions[1]}. If it is only decorative, do not let it influence the score. If it shows a panel, check whether labels are readable and whether active, inactive, and unavailable states are distinguishable.

The same discipline applies to feature names. Translate each name into a user job. If two toggles solve the same job, counting both may exaggerate practical breadth.

## Avoid Feature-Count Theater

Feature-count theater rewards long menus and verbose descriptions. It ignores whether settings overlap, whether defaults are usable, and whether the documentation explains limitations. The pattern becomes obvious around {red_flags[0]}, {red_flags[1]}, or {red_flags[2]}.

Instead of asking “Which page lists the most?”, ask three cleaner questions: {q1} {q2} {q3} A strong article answers them in plain English and lets the reader reverse a mistaken assumption.

No operational bypass guidance belongs in this process. If a current product requires special action, the only responsible route is its official documentation; if that documentation conflicts with security warnings, stop.

## Put the Referenced Guide in the Shortlist Flow

The {shared_link} page is useful at the discovery stage. It can expose names, categories, and screenshots worth checking. Use it to create candidates, then return to current official sources before treating any time-sensitive detail as settled.

{product_note} That separation keeps {primary} focused on the user's decision rather than on promotional momentum. A clearer, smaller shortlist is more valuable than a crowded “best of” page.

## FAQ

### What makes {primary} usable?

{primary} is usable when it groups details by reader decisions, limits the active criteria, and preserves a clear way to reject every option.

### Are more advertised features always better?

No. Overlap, poor labels, weak defaults, and missing documentation can make a longer list less useful.

### Can a clean interface prove low risk?

No. Interface quality and account or device-security risk are different evaluation layers.

### How many candidates should a shortlist contain?

Only enough to compare meaningful differences. Two or three well-documented candidates can be more useful than ten poorly scoped entries.
'''
    elif host_index == 3:
        article = f'''
# {title}

The central question in {primary} is not “When was this page published?” It is “Which claims were rechecked after the last relevant change?” A fresh date can sit above stale screenshots, expired access terms, and product language copied from an older build.

For {target['audience']}, split the article into stable facts and expiring facts. Stable sections explain concepts and evaluation methods. Expiring sections cover {dimensions[0]}, {dimensions[1]}, or any live status. Third-party tools still carry rule, account, and security risks regardless of how recently a page was updated.

![{target['alt']}]({target['image']})

## Build an Expiration Map

The page should {target['page_job']}. Mark every statement that can change after a game patch, product release, pricing edit, domain move, or support-policy change. Those statements need a visible review trail.

An expiration map for this topic includes {oxford(dimensions)}. The items do not age at the same speed. Terminology may remain useful for months. Current availability can change overnight. A screenshot may stay valuable as historical interface evidence while becoming useless as proof of today's compatibility.

{target['proof_limit']} The article should label that limitation beside the media instead of relying on a catch-all note at the end.

## Make the Review Date Mean Something

“Updated” should describe work, not cosmetics. A meaningful review note says which live source was checked, which claim changed, and whether the conclusion moved. It can also say that no change was found.

Use a compact review record:

- page and product identity checked;
- access and status wording checked;
- screenshots compared with the live interface;
- limitations and unavailable areas checked;
- outbound links tested.

This record does not need to clutter the article. A short “reviewed on” note and a tiny change log are enough if the process behind them is real.

## Run a Revalidation Loop After Relevant Changes

When a game or product changes, do not rewrite from memory. Reopen the official source, check the patch-sensitive dimensions, and update only conclusions supported by the new state.

The loop is straightforward:

1. Identify the event that could invalidate the article.
2. Recheck {dimensions[0]} and {dimensions[1]}.
3. Compare old and current evidence for {dimensions[2]}.
4. Mark changed screenshots as historical when useful.
5. Amend the conclusion and record the review date.

If the official status is unclear, publish uncertainty rather than filling the gap. “Not confirmed after the update” is more useful than a recycled green badge.

## Archive Old Proof Instead of Pretending It Is Current

Historical media can explain product evolution, terminology, or prior interface design. Keep it, but date it. Problems begin when old material is silently reused to support present-tense claims.

Watch especially for {red_flags[0]}, {red_flags[1]}, and {red_flags[2]}. These are signs that the page's freshness label may be cosmetic. The common mistake is {host['mistake']}.

Do not compensate for stale official guidance with unofficial operational steps or advice for bypassing protections. A broken or conflicting source chain is a reason to pause.

## Recheck the Referenced Page Before Acting

The {shared_link} article can provide background and a useful snapshot of its subject. Treat its images and rankings as time-bounded. For live status, access, or compatibility, compare them with the official page at the moment the decision is made.

{product_note} A reliable {primary} article is therefore a maintained document, not a frozen verdict. It tells the reader which parts age, how they were checked, and when uncertainty returned.

## FAQ

### What makes {primary} genuinely current?

{primary} is current when the patch-sensitive claims, source links, images, and conclusion were actually rechecked—not merely when the displayed date changed.

### Should old screenshots be deleted?

Not always. They can remain useful as historical evidence if the capture date and old context are clear.

### How often should a guide be reviewed?

Review it after relevant game, product, access, or domain changes. A fixed calendar helps, but event-driven checks matter more.

### Does a recent update remove risk?

No. Fresh documentation reduces confusion. It does not guarantee permission, detection status, or file security.
'''
    elif host_index == 4:
        article = f'''
# {title}

A fair comparison of {target['subject']} should not force one permanent winner. It should show how the result changes when a reader gives more weight to {dimensions[0]}, {dimensions[1]}, or {dimensions[2]}. {primary} is credible when the criteria are visible and the ranking can be challenged.

For {target['audience']}, define the persona and the weights before reading the candidates. Otherwise the longest feature list becomes the default scoring system. Remember that third-party tools can violate game rules and create account or device-security risks; no matrix can turn them into risk-free choices.

![{target['alt']}]({target['image']})

## Define the Reader Before the Criteria

The page's job is to {target['page_job']}. That requires a real reader, not a generic “gamer.” Someone prioritizing simple navigation will rank choices differently from someone prioritizing narrow hero support or transparent update notes.

Write a one-sentence persona: “This comparison is for a reader who values X, accepts Y, and will reject Z.” For this topic, X might be {dimensions[0]}, Y might be a limited choice around {dimensions[1]}, and Z might be unclear {dimensions[4]}.

Once the persona is explicit, readers can decide whether the result applies to them. A ranking without a persona silently assumes everyone shares the editor's priorities.

## Weight Independent Criteria

Choose criteria that measure different things. {oxford(dimensions)} are useful only if the article avoids double-counting. For example, a detailed feature list and broad coverage may describe overlapping value. Scoring both heavily can inflate one advantage.

A practical weighting might give the largest share to the reader's main job, a second share to current documentation, and smaller shares to interface or convenience factors. Do not use false precision. “High, medium, low” can be more honest than 8.73 out of 10 when the evidence is qualitative.

{target['proof_limit']} That is why safety should not be awarded as a simple score based on a vendor slogan.

## Score Claims and Evidence Separately

Create two notes for every important criterion: what the page claims, and what the reviewer can verify. A strong claim with weak evidence should not outrank a modest claim with clear support automatically.

Use this review sequence:

1. Record the claim in the page's own scope.
2. Identify the source and date.
3. Note what is directly observable.
4. Record limitations or unanswered questions.
5. Apply the persona's weight only after those steps.

This makes disagreements productive. Two reviewers can share the same evidence and reach different rankings because their weights differ. The article should show that rather than pretending the score is universal truth.

## Run a Sensitivity Check

After ranking, change the two largest weights. If a small adjustment flips the winner, say the result is close. If one option remains ahead across several reasonable weight sets, the conclusion is more robust—but still time-bound.

Red flags for this topic include {red_flags[0]}, {red_flags[1]}, and {red_flags[2]}. They often accompany {host['mistake']}. A fair comparison also includes “none” when every candidate misses a hard requirement.

Keep operational bypass advice out of the article. Comparison methodology can explain evidence and fit without teaching readers to defeat protective systems.

## Use the Linked Roundup as Input, Not a Verdict

The {shared_link} page can supply candidates, terminology, and screenshots for an initial comparison. Recheck official sources before scoring live status, access, or compatibility, and label editorial judgments as judgments.

{product_note} The result is a comparison readers can adapt. Good {primary} does not ask them to trust a winner badge; it gives them enough structure to recompute the answer for their own priorities.

## FAQ

### What makes {primary} fair?

{primary} is fair when it declares the reader persona, uses independent criteria, exposes weights, dates evidence, and permits no winner.

### Should feature count receive the highest weight?

Only if raw breadth genuinely matches the reader's job. Relevance, documentation, and control often matter more.

### Why separate a claim from its evidence?

Because ambitious positioning and strong proof are different qualities. Combining them hides uncertainty.

### Can a comparison identify a risk-free option?

No. It can organize evidence and trade-offs, but it cannot guarantee account safety, permission, or file security.
'''
    elif host_index == 5:
        article = f'''
# {title}

Visuals make {target['subject']} easier to understand, but they also create a shortcut in the reader's brain: polished looks true. {primary} pushes against that shortcut by asking what is inside the frame, what is missing, and which conclusion the image can honestly support.

For {target['audience']}, screenshots are strongest when they explain layout, labels, and a named state. Clips are strongest when they show a defined sequence. Neither format can prove future compatibility, account safety, or every advertised condition.

![{target['alt']}]({target['image']})

## Inventory What Is Actually in the Frame

Begin with observation, not interpretation. Note the game context, visible product identity, readable labels, date or build marker, active state, and any cropped area. Then connect those details to {oxford(dimensions)}.

The page should {target['page_job']}. A useful image supports one part of that job. It should not act as decoration beside a paragraph making unrelated promises.

Describe the visual literally: “The image shows X in state Y.” Only after that should the article explain why X matters. This two-step caption makes exaggerated conclusions easier to spot.

## Know What Screenshots Cannot Establish

{target['proof_limit']} A single frame also cannot show consistency over time, behavior outside the chosen example, or what happened before and after the capture.

For {primary}, keep four boundaries visible:

- layout evidence is not performance evidence;
- a feature label is not proof that the feature currently works;
- a successful moment is not a representative sample;
- visual restraint is not a security guarantee.

These boundaries do not make images useless. They make them precise.

## Give Every Visual a Verification-Ready Caption

A strong caption names the source page, the product or topic, the captured state, and the editorial purpose. If the media is old, say so. If it is a vendor image, say that too. Readers should never have to guess whether the writer captured the screen independently.

Use this audit:

1. Can the named product be identified?
2. Is the text readable at normal size?
3. Does the caption describe only what is visible?
4. Is the media tied to a date or clearly marked undated?
5. Does the surrounding paragraph add limitations?

When a clip loops, note the start and end condition. Repetition can make one successful sequence feel like a broad reliability test even when it is only one example.

## Compare Like With Like

Do not compare one product's polished marketing render with another product's rough troubleshooting screenshot and call the first interface better. Align the evidence type: menu with menu, status page with status page, feature demo with feature demo.

The warning signs here are {red_flags[0]}, {red_flags[1]}, and {red_flags[2]}. Each can produce {host['mistake']}. If media context is unavailable, narrow the caption rather than guessing.

Avoid screenshots that teach operational bypasses or expose readers to suspicious downloads. The visual goal is comprehension and verification, not evasion.

## Read the Referenced Image in Context

The {shared_link} page contains media that can orient readers to the topic. Use it to inspect presentation and named claims, then visit the current official source for time-sensitive details.

{product_note} For {target_kind}, that distinction matters after every interface or game update. {primary} remains useful when the caption is modest, the visual is identifiable, and the article says what the frame cannot show.

## FAQ

### What can {primary} reliably show?

{primary} can show visible interface structure, labels, captured states, and the exact sequence present in a clip when context is included.

### Can a polished demo prove broad reliability?

No. Production quality and sample quality are separate. One polished example is still one example.

### What belongs in an image caption?

Name the source, subject, visible state, date when known, and the narrow claim the image supports.

### Should old media be reused?

Only with clear historical labeling. It should not support present-tense compatibility or access claims without a fresh check.
'''
    else:
        article = f'''
# {title}

The quickest way to improve research on {target['subject']} is to replace browsing momentum with buyer questions. {primary} should help a reader ask what would confirm the fit, what would disqualify the option, and which answer must come from a current official source.

For {target['audience']}, begin with a written stop rule. A useful guide may end with no recommendation. Third-party competitive tools may violate game rules and create account or device-security risks, so “not enough evidence” is a legitimate outcome.

![{target['alt']}]({target['image']})

## Ask Seven Questions Before Opening More Tabs

The page should {target['page_job']}. Test that job with seven questions:

1. What exact decision am I making?
2. What does {dimensions[0]} mean on this page?
3. Which source supports {dimensions[1]}?
4. When was {dimensions[2]} last checked?
5. What limitation applies to {dimensions[3]}?
6. Where is {dimensions[4]} documented?
7. What answer would make me stop?

These questions keep research from expanding forever. Every new tab should answer one of them. If it does not, close it.

## Distinguish a Decision Aid From a Funnel

A decision aid allows rejection. It defines terms, dates claims, names limits, and acknowledges alternatives. A funnel treats every answer as a reason to continue toward one predetermined action.

{host['evidence']} For this topic, watch whether the article gives independent attention to {dimensions[0]} and {dimensions[1]}, or simply uses them as stepping stones to a product link.

{target['proof_limit']} A responsible buyer guide states that boundary early. It never turns words such as “best,” “free,” or “legit” into implied safety guarantees.

## Use Questions That Can Produce a No

Good questions are falsifiable. “Does this seem popular?” invites confirmation. “Can I identify the official source and current terms?” can produce a clear no.

Add these checks to {primary}:

- Does the live page match the article's image and description?
- Are patch-sensitive claims dated?
- Are limitations as specific as benefits?
- Does the support path stay on identifiable official channels?
- Can I explain the conclusion without repeating a slogan?

If the answer to a hard requirement is no, do not compensate with a long feature list. A missing source chain is not offset by attractive screenshots.

## Write Stop Conditions Beside the Questions

For {target['subject']}, stop around {red_flags[0]}, {red_flags[1]}, or {red_flags[2]}. Also stop if the workflow asks you to ignore security warnings, share game-platform credentials, or use an unrelated mirror.

The common research failure is {host['mistake']}. Reverse it by writing your rejection criteria before naming any brand. Then a page earns its place by answering questions rather than by matching an expectation.

No buyer FAQ should provide methods for bypassing anti-cheat or other protections. Product-specific steps belong to current official documentation, and conflicting documentation is a reason to pause.

## Where the Linked Article Helps

The {shared_link} page is a starting source for terminology, screenshots, and candidates. Use those elements to sharpen questions; do not treat the article as the final authority for current product status or access.

{product_note} This question-led path is deliberately short: define, verify, stop or continue. It gives {primary} a clear answer-first structure that readers and search systems can reuse without stripping away the risk boundary.

## FAQ

### What should {primary} answer first?

{primary} should state the buyer's real decision, the two or three relevant criteria, and a reason not to proceed.

### Why write rejection criteria before comparing brands?

It reduces confirmation bias and stops the preferred option from defining the scoring rules.

### Which details need an official source?

Current status, access terms, compatibility, support channels, and product-specific instructions should be checked on the live official source.

### Can a buyer guide guarantee safety?

No. A guide can improve source checking and clarify trade-offs, but it cannot remove rule, account, or device-security risk.
'''

    topic_detail = (
        f"\n## {target['detail_heading']}\n\n{target['detail']}\n\n"
        f"Imagine a reader reviewing {target['subject']} and finding a clear statement about {dimensions[0]} but no usable context for {dimensions[4]}. "
        f"The disciplined conclusion is not that the whole page is false, and not that the missing detail must be favorable. It is that {dimensions[0]} can remain in the shortlist while {dimensions[4]} stays unresolved. "
        f"The same reader should treat {red_flags[0]} as a prompt to verify the source, then check whether {red_flags[1]} changes the practical fit. "
        f"This small scenario keeps the recommendation proportional: confirmed details support narrow conclusions, open questions remain open, and {red_flags[2]} can still trigger a full stop.\n\n"
        f"Viewed through the {host['lens']} lens, this topic-specific check answers the article's narrow question without pretending to settle every risk or future update."
        "\n\n## FAQ\n"
    )
    article = article.replace("\n## FAQ\n", topic_detail, 1)
    body = front_matter + article
    data = {
        "host": host["domain"],
        "title": title,
        "slug": slugify(title),
        "description": description,
        "primary_keyword": primary,
        "target_url": target["url"],
        "anchor": anchor,
        "image": target["image"],
    }
    return body, data


def inline_markup(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: f'<img loading="lazy" decoding="async" src="{html.escape(m.group(2), quote=True)}" alt="{html.escape(m.group(1), quote=True)}" />', text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = text.replace("“", "&ldquo;").replace("”", "&rdquo;")
    return text


def markdown_to_html(markdown: str) -> str:
    body = re.sub(r"\A---\n.*?\n---\n", "", markdown, flags=re.S)
    lines = body.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None

    def flush_paragraph() -> None:
        if paragraph:
            out.append(f"<p>{inline_markup(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_paragraph()
            close_list()
            continue
        if line.startswith("# "):
            flush_paragraph(); close_list()
            continue
        if line.startswith("## "):
            flush_paragraph(); close_list()
            out.append(f"<h2>{inline_markup(line[3:])}</h2>")
            continue
        if line.startswith("### "):
            flush_paragraph(); close_list()
            out.append(f"<h3>{inline_markup(line[4:])}</h3>")
            continue
        bullet = re.match(r"^- (.+)$", line)
        numbered = re.match(r"^\d+\. (.+)$", line)
        if bullet or numbered:
            flush_paragraph()
            desired = "ul" if bullet else "ol"
            if list_type != desired:
                close_list()
                list_type = desired
                out.append(f"<{list_type}>")
            item = (bullet or numbered).group(1)
            out.append(f"<li>{inline_markup(item)}</li>")
            continue
        paragraph.append(line)
    flush_paragraph()
    close_list()
    return "\n".join(out)


def main() -> None:
    ARTICLE_DIR.mkdir(parents=True, exist_ok=True)
    PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(RUN_MANIFEST.read_text(encoding="utf-8"))
    items = []
    bundles: dict[str, list[dict]] = {host["domain"]: [] for host in HOSTS}

    for host_index, host in enumerate(HOSTS):
        host_dir = PUBLISH_DIR / host["domain"]
        host_dir.mkdir(parents=True, exist_ok=True)
        for target_index, _target in enumerate(TARGETS):
            global_index = host_index * 10 + target_index + 1
            markdown, data = article_markdown(host_index, target_index)
            filename = f"{global_index:02d}-{data['slug']}.md"
            path = ARTICLE_DIR / filename
            path.write_text(markdown, encoding="utf-8")
            html_body = markdown_to_html(markdown)
            (host_dir / filename).write_text(markdown, encoding="utf-8")
            (host_dir / filename.replace(".md", ".html")).write_text(html_body, encoding="utf-8")
            source_helper = (
                "<!doctype html><html><head><meta charset=\"utf-8\"><title>Publish source</title></head><body>"
                f"<label>Title source<textarea aria-label=\"Title source\">{html.escape(data['title'])}</textarea></label>"
                f"<label>HTML source<textarea aria-label=\"HTML source\">{html.escape(html.unescape(html_body))}</textarea></label>"
                f"<label>Description source<textarea aria-label=\"Description source\">{html.escape(data['description'])}</textarea></label>"
                "</body></html>"
            )
            (host_dir / filename.replace(".md", ".source.html")).write_text(source_helper, encoding="utf-8")
            bundle_item = {
                "index": global_index,
                "host_index": target_index + 1,
                "file": filename,
                **data,
                "html": html_body,
            }
            bundles[host["domain"]].append(bundle_item)
            old = manifest["items"][global_index - 1]
            items.append({
                **old,
                "title": data["title"],
                "game": "deadlock" if "Deadlock" in data["title"] else "cs2",
                "language": "en",
                "status": "article",
                "output": str(path),
            })

    manifest["items"] = items
    RUN_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (PUBLISH_DIR / "bundles.json").write_text(json.dumps(bundles, ensure_ascii=False, indent=2), encoding="utf-8")

    index_lines = ["# Network T2 Batch Index", ""]
    for host in HOSTS:
        index_lines.extend([f"## {host['domain']}", ""])
        for item in bundles[host["domain"]]:
            index_lines.append(f"{item['host_index']}. [{item['title']}](../../articles/{RUN_ID}/{item['file']}) -> [{item['anchor']}]({item['target_url']})")
        index_lines.append("")
    (PUBLISH_DIR / "ARTICLE_INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(json.dumps({"articles": len(items), "hosts": len(HOSTS), "publish_dir": str(PUBLISH_DIR)}, indent=2))


if __name__ == "__main__":
    main()
