$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$outputDir = Join-Path $projectRoot 'output/articles/20260910-082336'
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$items = @(
    @{ Dest = '01-cs2-cheat-research-order.md'; Source = 'output/articles/CHEATSGAMING-T2-57-20260908/CG-004-cs2-cheat-research-order.md'; Target = 'https://cheatsgaming.com/games/cs2'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/601d8fcb5d5ab4789906b298.png'; Alt = 'Cluster website shown as one evidence source while researching current CS2 tool categories and product claims'; Caption = 'A current website capture can document visible claims, but it cannot prove future compatibility or account outcomes.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/bb7e3f764ea76d2c8e62fab6.jpg'; Alt = 'Cluster CS2 interface screenshot used to separate visible feature labels from broader marketing conclusions'; Caption = 'A real interface image can confirm labels and layout; performance and safety still need separate evidence.' }
    )},
    @{ Dest = '02-deadlock-cheat-research-map.md'; Source = 'output/packages/CHEATSGAMING-T2-57-20260908-DEADLOCK/md/CG-028-deadlock-cheat-research-map.md'; Target = 'https://cheatsgaming.com/games/deadlock'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/047332b84a6d6b180f78af24.gif'; Alt = 'Deadlock Auto-Parry demonstration from the supplied guide showing one narrow automation category in motion'; Caption = 'Auto-Parry is one feature family, not a complete verdict on a Deadlock product.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/79a4acf3465c24536ad2fc25.jpg'; Alt = 'Cluster Deadlock menu screenshot illustrating how aim, visual, movement, and hero features share one product'; Caption = 'The menu supplies a taxonomy to investigate; every category still needs current scope and limitations.' }
    )},
    @{ Dest = '04-melonity-vs-umbrella-update-evidence.md'; Source = 'output/articles/20260908-181502/01-melonity-vs-umbrella-update-evidence.md'; Target = 'https://cheatsgaming.com/games/dota-2/melonity-vs-umbrella-dota-2-cheats'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/ddab88858ed3104f75c0a92b.png'; Alt = 'Melonity and Umbrella comparison artwork from the supplied Dota 2 article used as an editorial reference'; Caption = 'A comparison page is a starting map of claims, not permanent proof that every claim remains current.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/41ba5d7f0b2e46bd1f78e208.png'; Alt = 'Melonity Dota 2 build helper screenshot documenting a visible workflow rather than a safety guarantee'; Caption = 'A workflow screenshot can show what was presented at capture time; maintenance evidence needs dates.' }
    )},
    @{ Dest = '05-dota-2-cheat-trial-evaluation.md'; Source = 'output/articles/20260908-181502/03-dota-2-cheat-trials-seven-day-evaluation.md'; Target = 'https://cheatsgaming.com/games/dota-2/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/313b60a16e6b505b3f1b5e5c.png'; Alt = 'Best Dota 2 cheats article artwork reused to frame a shortlist as the start of a structured evaluation'; Caption = 'A ranking can supply candidates; a consistent evaluation process decides whether any candidate fits.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/855c8b31134551d1edf292ae.png'; Alt = 'Dota 2 item and ability indicator screenshot used to assess clarity and information density during a trial'; Caption = 'Visible information density is testable during a short review window; long-term safety is not.' }
    )},
    @{ Dest = '06-deadlock-risk-layers.md'; Source = 'output/packages/CHEATSGAMING-T2-57-20260908-DEADLOCK/md/CG-038-deadlock-vac-reports-updates-risk-layers.md'; Target = 'https://cheatsgaming.com/games/deadlock/deadlock-cheat-safety-and-vac-protection-explained-why-cheats-are-safe-b297c2f0f2b8'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/bf083e13863e86601ca7b194.png'; Alt = 'Deadlock cheat safety article artwork reused while separating VAC, reports, updates, and product claims'; Caption = 'Safety language should be split into dated, testable claims instead of treated as one permanent status.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/39dcdc185381a1e3d9e7ab79.jpg'; Alt = 'Anti-cheat software layer diagram from the supplied Deadlock article presented as a source claim to audit'; Caption = 'This supplied diagram illustrates one classification; it is not proof of Deadlock detection internals.' }
    )},
    @{ Dest = '07-cs2-skin-changer-screenshot-proof.md'; Source = 'output/articles/CHEATSGAMING-T2-57-20260908/CG-025-cs2-skin-changer-screenshot-proof.md'; Target = 'https://cheatsgaming.com/games/cs2/top-skinchangers-for-cs2-best-skinchangers-33549b88abea'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/6113ad91e4319a3332f33285.png'; Alt = 'MetaSkins menu screenshot from the supplied CS2 skin changer article showing visible cosmetic controls'; Caption = 'The capture can document visible controls and coverage at one moment, but not ownership or future support.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/26a68a2422b13ddf3a4e1d53.jpg'; Alt = 'Sapphire Changer menu screenshot used to compare what a second CS2 cosmetic interface visibly demonstrates'; Caption = 'A second real screenshot helps separate shared interface evidence from product-specific marketing claims.' }
    )},
    @{ Dest = '08-cs2-skin-changer-preview-mismatch.md'; Source = 'output/articles/CHEATSGAMING-T2-57-20260908/CG-026-cs2-skin-changer-preview-mismatch.md'; Target = 'https://cheatsgaming.com/games/cs2/top-skinchangers-for-cs2-best-skinchangers-33549b88abea'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/985466ff278301ee81eede01.png'; Alt = 'Inventory Changer menu screenshot used to examine how catalogue previews can differ from in-match rendering'; Caption = 'A catalogue view is evidence of selection and layout, not a promise that every in-game scene will match.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/0fee6a3446e839cfd9f02c60.png'; Alt = 'TouchSkins menu screenshot from the supplied article showing another cosmetic preview and control layout'; Caption = 'Comparing two interfaces makes preview assumptions visible without claiming that either item is tradable.' }
    )},
    @{ Dest = '09-cost-of-free-cs2-cheats.md'; Source = 'output/articles/CHEATSGAMING-T2-57-20260908/CG-008-cost-of-free-cs2-cheats.md'; Target = 'https://cheatsgaming.com/games/cs2/best-free-cheats-for-cs2-top-free-hacks-for-cs2-dcf35b94fc52'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/601d8fcb5d5ab4789906b298.png'; Alt = 'Cluster website screenshot from the supplied free CS2 cheats article used to inspect a visible offer route'; Caption = 'A visible offer page documents presentation and route; terms and availability must still be rechecked.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/4c8440c116bd2d5030f28a81.png'; Alt = 'Cluster CS2 interface screenshot used to compare product visibility with the hidden costs of unsupported files'; Caption = 'An interface capture can be checked; anonymous downloads often leave maintenance and support unobservable.' }
    )},
    @{ Dest = '10-legit-vs-semi-rage-vs-rage-cs2.md'; Source = 'output/articles/CHEATSGAMING-T2-57-20260908/CG-010-legit-vs-semi-rage-vs-rage-cs2.md'; Target = 'https://cheatsgaming.com/games/cs2/top-5-legit-cheats-for-cs2-best-legit-cs2-hack-5ac352f79364'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/bb7e3f764ea76d2c8e62fab6.jpg'; Alt = 'Cluster CS2 menu screenshot from the supplied legit cheats ranking showing one product interface at capture time'; Caption = 'The screenshot documents visible controls; the word legit remains a community style label, not proof of safety.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/f5184a7077b9f3fe914a8d71.png'; Alt = 'Predator CS2 menu screenshot used to show why the same legit label can cover different product presentations'; Caption = 'Different menus can share the same label, so reviewers need explicit definitions and current evidence.' }
    )},
    @{ Dest = '11-deadlock-parry-window-timing-feints.md'; Source = 'output/packages/CHEATSGAMING-T2-57-20260908-DEADLOCK/md/CG-031-deadlock-parry-window-timing-feints.md'; Target = 'https://cheatsgaming.com/games/deadlock/deadlock-auto-parry-cheat-how-it-works-features-download-3041cefa2924'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/047332b84a6d6b180f78af24.gif'; Alt = 'Animated Deadlock Auto-Parry example from the supplied guide showing one successful defensive response'; Caption = 'A successful clip shows a result, but reviewers should also look for spacing, feints, and unavailable states.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/95f7ec2b145cd6406a190dd7.gif'; Alt = 'Animated Deadlock field-of-view changer example reused to distinguish camera tools from parry automation'; Caption = 'Separate camera presentation from defensive timing; feature proximity in a menu does not merge their jobs.' }
    )},
    @{ Dest = '12-deadlock-cheat-comparison-beyond-aimbot.md'; Source = 'output/packages/CHEATSGAMING-T2-57-20260908-DEADLOCK/md/CG-040-deadlock-cheat-comparison-beyond-aimbot.md'; Target = 'https://cheatsgaming.com/games/deadlock/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e'; Images = @(
        @{ Url = 'https://cheatsgaming.com/media/medium/79a4acf3465c24536ad2fc25.jpg'; Alt = 'Cluster Deadlock menu screenshot from the supplied ranking used to inspect features beyond aimbot labels'; Caption = 'One menu can establish visible categories, while maintenance and support require different evidence.' },
        @{ Url = 'https://cheatsgaming.com/media/medium/c67c99238ac148edb99cdbdf.jpg'; Alt = 'Umbrella Deadlock menu screenshot from the supplied ranking used as a second comparison reference'; Caption = 'A second interface helps compare scope without turning a static screenshot into a permanent winner score.' }
    )}
)

function New-RealImageBlock {
    param([int]$Index, [hashtable]$Image, [string]$Target)
    $slot = '{0:D2}' -f $Index
    return @"
<!-- IMAGE_SLOT_$slot
Type: real screenshot
Generated sequence index: none; real screenshots do not consume the generated sequence
Style branch: none; real screenshot
Model: not applicable
Placement: embedded at this editorial breakpoint
Purpose: document a visible element from the supplied target article without fabricating UI
Source URL: $($Image.Url)
Source article: $Target
Retrieval date: 2026-09-10
Suggested filename: source-screenshot-$slot.webp
Alt text: $($Image.Alt)
Caption: $($Image.Caption)
Rights and accuracy guardrail: reuse the supplied publisher asset as-is; crop only if the platform requires it, preserve labels, and do not imply independent testing.
-->

![$($Image.Alt)]($($Image.Url))

*$($Image.Caption)*
"@
}

foreach ($item in $items) {
    $sourcePath = Join-Path $projectRoot $item.Source
    $destinationPath = Join-Path $outputDir $item.Dest
    $content = [System.IO.File]::ReadAllText($sourcePath, [System.Text.Encoding]::UTF8)

    $content = [regex]::Replace($content, '(?s)<!-- IMAGE_SLOT_\d+.*?-->', '')
    $content = [regex]::Replace($content, '(?s)<!-- INTERNAL_LINK_SUGGESTIONS.*?-->', '')
    $content = $content.Replace('2026-09-08', '2026-09-10')
    $content = $content.Replace('September 8, 2026', 'September 10, 2026')

    if ($item.Dest -eq '04-melonity-vs-umbrella-update-evidence.md') {
        $content = $content.Replace('The official [Melonity Dota 2 page](https://melonity.gg/en)', 'The official Melonity Dota 2 page')
        $content = $content.Replace('Use Melonity’s live [dota 2 cheats](https://melonity.gg/en) page as a current product snapshot, then cross-check any feature claim against its newest dated update.', 'Use the current [Melonity vs Umbrella Dota 2 comparison](https://cheatsgaming.com/games/dota-2/melonity-vs-umbrella-dota-2-cheats) to collect the advertised claims, then cross-check each one against dated first-party material.')
    }

    if ($item.Dest -eq '05-dota-2-cheat-trial-evaluation.md') {
        $content = $content.Replace('Melonity’s current eligibility and plan language should be checked on its official [dota 2 cheats](https://melonity.gg/en) page because trial terms can change.', 'Before using any shortlist, read the claims in this [best Dota 2 cheats guide](https://cheatsgaming.com/games/dota-2/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6), then confirm current eligibility and terms on the provider’s official page because offers can change.')
    }

    if ($content -notmatch '(?m)^target_url:') {
        $targetLine = "target_url: `"$($item.Target)`""
        $content = [regex]::Replace($content, '(?m)^(language:\s*"?en"?\s*)$', { param($match) $match.Groups[1].Value + "`r`n" + $targetLine }, 1)
    }

    $firstImage = New-RealImageBlock -Index 1 -Image $item.Images[0] -Target $item.Target
    $secondImage = New-RealImageBlock -Index 2 -Image $item.Images[1] -Target $item.Target
    $content = [regex]::Replace($content, '(?m)^(# .+)$', { param($match) $match.Groups[1].Value + "`r`n`r`n" + $firstImage }, 1)
    $content = [regex]::Replace($content, '(?m)^## FAQ\s*$', "$secondImage`r`n`r`n## FAQ", 1)

    [System.IO.File]::WriteAllText($destinationPath, $content, [System.Text.UTF8Encoding]::new($false))
}

Write-Output "Staged $($items.Count) articles in $outputDir"
