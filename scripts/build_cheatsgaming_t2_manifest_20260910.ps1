$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$runId = '20260910-082336'
$articleDir = Join-Path $projectRoot "output/articles/$runId"
$promptDir = Join-Path $projectRoot "output/prompts/$runId"
$evidenceDir = Join-Path $projectRoot "output/evidence/$runId"
$taskDir = Join-Path $projectRoot "output/codex_tasks/$runId"
$manifestPath = Join-Path $projectRoot "output/runs/$runId.json"

New-Item -ItemType Directory -Force -Path $promptDir, $evidenceDir, $taskDir | Out-Null

$items = @(
    @{ Id=1; Slug='cs2-cheat-research-order'; Title='CS2 Cheat Research: Check Claims in the Right Order'; Game='cs2'; Primary='CS2 cheat research'; Target='https://cheatsgaming.com/games/cs2'; File='01-cs2-cheat-research-order.md'; Intent='research workflow'; Source='knowledge/agent_memory/sources/target-urls/cs2.md' },
    @{ Id=2; Slug='deadlock-cheat-research-map'; Title='Deadlock Cheat Research: Four Feature Families'; Game='deadlock'; Primary='Deadlock cheat research'; Target='https://cheatsgaming.com/games/deadlock'; File='02-deadlock-cheat-research-map.md'; Intent='feature taxonomy'; Source='knowledge/agent_memory/sources/target-urls/deadlock.md' },
    @{ Id=3; Slug='dota-2-cheat-categories'; Title='Dota 2 Cheat Categories: Scripts, Visuals, and Utility'; Game='dota2'; Primary='Dota 2 cheat categories'; Target='https://cheatsgaming.com/games/dota-2'; File='03-dota-2-cheat-categories.md'; Intent='feature taxonomy'; Source='knowledge/agent_memory/sources/target-urls/dota-2.md' },
    @{ Id=4; Slug='melonity-vs-umbrella-update-evidence'; Title='Melonity or Umbrella After a Patch? Audit the Proof'; Game='dota2'; Primary='Melonity vs Umbrella updates'; Target='https://cheatsgaming.com/games/dota-2/melonity-vs-umbrella-dota-2-cheats'; File='04-melonity-vs-umbrella-update-evidence.md'; Intent='comparison and freshness audit'; Source='knowledge/agent_memory/sources/target-urls/melonity-vs-umbrella-dota-2-cheats.md' },
    @{ Id=5; Slug='dota-2-cheat-trial-evaluation'; Title='Dota 2 Cheat Trials: What Seven Days Can Prove'; Game='dota2'; Primary='Dota 2 cheat trials'; Target='https://cheatsgaming.com/games/dota-2/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6'; File='05-dota-2-cheat-trial-evaluation.md'; Intent='pre-purchase evaluation'; Source='knowledge/agent_memory/sources/target-urls/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6.md' },
    @{ Id=6; Slug='deadlock-risk-layers'; Title='Deadlock Risk Layers: VAC, Reports, and Updates'; Game='deadlock'; Primary='Deadlock risk layers'; Target='https://cheatsgaming.com/games/deadlock/deadlock-cheat-safety-and-vac-protection-explained-why-cheats-are-safe-b297c2f0f2b8'; File='06-deadlock-risk-layers.md'; Intent='risk evidence literacy'; Source='knowledge/agent_memory/sources/target-urls/deadlock-cheat-safety-and-vac-protection-explained-why-cheats-are-safe-b297c2f0f2b8.md' },
    @{ Id=7; Slug='cs2-skin-changer-screenshot-proof'; Title='CS2 Skin Changer Screenshots: What They Prove'; Game='cs2'; Primary='CS2 skin changer screenshot'; Target='https://cheatsgaming.com/games/cs2/top-skinchangers-for-cs2-best-skinchangers-33549b88abea'; File='07-cs2-skin-changer-screenshot-proof.md'; Intent='visual evidence audit'; Source='knowledge/agent_memory/sources/target-urls/top-skinchangers-for-cs2-best-skinchangers-33549b88abea.md' },
    @{ Id=8; Slug='cs2-skin-changer-preview-mismatch'; Title='CS2 Skin Changer Preview Mismatch Explained'; Game='cs2'; Primary='CS2 skin changer preview mismatch'; Target='https://cheatsgaming.com/games/cs2/top-skinchangers-for-cs2-best-skinchangers-33549b88abea'; File='08-cs2-skin-changer-preview-mismatch.md'; Intent='preview troubleshooting'; Source='knowledge/agent_memory/sources/target-urls/top-skinchangers-for-cs2-best-skinchangers-33549b88abea.md' },
    @{ Id=9; Slug='cost-of-free-cs2-cheats'; Title='The Real Cost of Free CS2 Cheats'; Game='cs2'; Primary='cost of free CS2 cheats'; Target='https://cheatsgaming.com/games/cs2/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52'; File='09-cost-of-free-cs2-cheats.md'; Intent='risk-aware cost analysis'; Source='knowledge/agent_memory/sources/target-urls/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52.md' },
    @{ Id=10; Slug='legit-vs-semi-rage-vs-rage-cs2'; Title='Legit vs Semi-Rage vs Rage in CS2'; Game='cs2'; Primary='legit vs semi-rage vs rage'; Target='https://cheatsgaming.com/games/cs2/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364'; File='10-legit-vs-semi-rage-vs-rage-cs2.md'; Intent='terminology explainer'; Source='knowledge/agent_memory/sources/target-urls/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364.md' },
    @{ Id=11; Slug='deadlock-parry-window-timing-feints'; Title='Deadlock Parry Window: Timing and Feints Explained'; Game='deadlock'; Primary='Deadlock parry window'; Target='https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924'; File='11-deadlock-parry-window-timing-feints.md'; Intent='combat mechanic explainer'; Source='knowledge/agent_memory/sources/target-urls/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924.md' },
    @{ Id=12; Slug='deadlock-cheat-comparison-beyond-aimbot'; Title='Deadlock Cheat Comparison Beyond Aimbot'; Game='deadlock'; Primary='Deadlock cheat comparison'; Target='https://cheatsgaming.com/games/deadlock/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e'; File='12-deadlock-cheat-comparison-beyond-aimbot.md'; Intent='persona-led comparison'; Source='knowledge/agent_memory/sources/target-urls/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e.md' }
)

$manifestItems = @()
$indexLines = @('# CheatsGaming T2 Article Index', '')
$taskLines = @('# Codex Article Task', '', 'Write and verify exactly 12 English T2 articles for the supplied CheatsGaming targets. Use one contextual target link per article, two real source images, answer-first GEO structure, non-operational risk-aware wording, SEO front matter, and FAQ. Product mapping: CS2/Deadlock to cluster.center; Dota 2 to Melonity.', '', '## Articles', '')

foreach ($item in $items) {
    $promptPath = Join-Path $promptDir (('{0:D2}-{1}.md' -f $item.Id, $item.Slug))
    $evidencePath = Join-Path $evidenceDir (('{0:D2}-{1}.json' -f $item.Id, $item.Slug))
    $outputPath = Join-Path $articleDir $item.File

    $prompt = @"
# $($item.Title)

- Page type: Blog post
- Search intent: $($item.Intent)
- Primary keyword: $($item.Primary)
- Contextual target: $($item.Target)
- Required product mapping: $(if ($item.Game -eq 'dota2') { 'Melonity' } else { 'cluster.center' })
- Required structure: SEO front matter, one H1, answer-first introduction, question-led H2s, practical checks, two real images from the supplied target pages, conclusion, and 4-7 FAQ items.
- Safety boundary: explain terminology, evidence, comparison, and risk only; do not provide anti-cheat bypass, evasion, injection, concealment, or implementation instructions.
- Uniqueness boundary: do not paraphrase the destination or reuse its ranking order; provide a distinct $($item.Intent) job.
"@
    [System.IO.File]::WriteAllText($promptPath, $prompt, [System.Text.UTF8Encoding]::new($false))

    $evidenceSources = @(
        @{ source = $item.Target; role = 'live target page, canonical destination, and supplied editorial media' },
        @{ source = $item.Source; role = 'materialized target-page text and image references' },
        @{ source = 'knowledge/agent_memory/products/product-map.md'; role = 'mandatory product mapping and supported high-level claims' },
        @{ source = 'knowledge/agent_memory/rules/article-visual-prompt-guide.md'; role = 'real screenshot accuracy, alt text, and placement requirements' }
    )
    if ($item.Id -eq 6) {
        $evidenceSources += @{ source = 'https://forums.playdeadlock.com/threads/09-26-2024-update.33015/'; role = 'dated official Deadlock anti-cheat and reporting context' }
        $evidenceSources += @{ source = 'https://help.steampowered.com/en/faqs/view/571A-97DA-70E9-FF74'; role = 'official Valve Anti-Cheat terminology' }
    }
    if ($item.Id -eq 11) {
        $evidenceSources += @{ source = 'https://forums.playdeadlock.com/threads/04-10-2026-update.125825/'; role = 'dated official parry behavior context' }
    }
    if ($item.Id -eq 4 -or $item.Id -eq 5) {
        $evidenceSources += @{ source = 'https://melonity.gg/en'; role = 'current first-party Melonity product and trial wording checked 2026-09-10' }
        $evidenceSources += @{ source = 'https://uc.zone/en/dota2'; role = 'current first-party Umbrella product and trial wording checked 2026-09-10' }
    }

    $evidenceObject = @{ evidence = $evidenceSources; target = $item.Target; intent = $item.Intent; checked_at = '2026-09-10T08:23:36+03:00' }
    [System.IO.File]::WriteAllText($evidencePath, ($evidenceObject | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))

    $manifestItems += [ordered]@{
        topic_id = $item.Id
        title = $item.Title
        game = $item.Game
        language = 'en'
        status = 'article'
        output = $outputPath
        prompt = $promptPath
        evidence = $evidencePath
        llm_error = $null
    }
    $indexLines += ('{0}. [{1}]({2})' -f $item.Id, $item.Title, $outputPath)
    $taskLines += ('### {0}. {1}' -f $item.Id, $item.Title), '', ('- Prompt: `{0}`' -f $promptPath), ('- Evidence: `{0}`' -f $evidencePath), ('- Target: `{0}`' -f $outputPath), ''
}

$manifest = [ordered]@{
    created_at = $runId
    spec = [ordered]@{
        raw = 'Create exactly 12 original English T2 articles for 12 supplied link placements across 11 live CheatsGaming targets; publish two per platform across Substack, Notion, GitBook, GitHub, JustPasteMe, and Rentry.'
        count = 12
        language = 'en'
        game = 'mixed'
        style = 'Direct, practical, conversational, answer-first, evidence-led, gamer-aware'
        volume = '1500+ words'
        ad_mode = 'native'
    }
    llm_provider = 'none'
    model = $null
    items = $manifestItems
}

[System.IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 10), [System.Text.UTF8Encoding]::new($false))
[System.IO.File]::WriteAllLines((Join-Path $taskDir 'ARTICLE_INDEX.md'), $indexLines, [System.Text.UTF8Encoding]::new($false))
[System.IO.File]::WriteAllLines((Join-Path $taskDir 'TASK.md'), $taskLines, [System.Text.UTF8Encoding]::new($false))

Write-Output "Built manifest and evidence for $($items.Count) articles"
