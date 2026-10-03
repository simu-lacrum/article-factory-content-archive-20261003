$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$runId = '20260910-084742'
$articleDir = Join-Path $projectRoot "output/articles/$runId"
$promptDir = Join-Path $projectRoot "output/prompts/$runId"
$evidenceDir = Join-Path $projectRoot "output/evidence/$runId"
$taskDir = Join-Path $projectRoot "output/codex_tasks/$runId"
$manifestPath = Join-Path $projectRoot "output/runs/$runId.json"

New-Item -ItemType Directory -Force -Path $articleDir, $promptDir, $evidenceDir, $taskDir | Out-Null

$items = @(
    @{ Id=1; Platform='Substack'; Slug='status-produkta-ne-garantiya'; Title='Статус продукта — не гарантия: как читать каталог игровых инструментов'; Game='multi'; Primary='статус игрового инструмента'; Target='https://cluster.center/ru'; File='01-status-produkta-ne-garantiya.md'; Intent='status-label evidence literacy'; Source='ru.md' },
    @{ Id=2; Platform='Substack'; Slug='hud-v-cs2-informacionnaya-plotnost'; Title='HUD в CS2: как оценить полезность информации на экране'; Game='cs2'; Primary='HUD в CS2'; Target='https://cluster.center/ru/cs2'; File='02-hud-v-cs2-informacionnaya-plotnost.md'; Intent='visual information-density audit'; Source='cs2.md' },
    @{ Id=3; Platform='Substack'; Slug='deadlock-glubina-podderzhki-geroev'; Title='Deadlock и глубина поддержки героев: что на самом деле значит Combo'; Game='deadlock'; Primary='поддержка героев Deadlock'; Target='https://cluster.center/ru/deadlock'; File='03-deadlock-glubina-podderzhki-geroev.md'; Intent='hero coverage analysis'; Source='deadlock.md' },
    @{ Id=4; Platform='Notion'; Slug='edinyy-akkaunt-test-i-podderzhka'; Title='Единый аккаунт, тест и поддержка: как проверить путь пользователя'; Game='multi'; Primary='тест игрового инструмента'; Target='https://cluster.center/ru'; File='04-edinyy-akkaunt-test-i-podderzhka.md'; Intent='account and trial journey audit'; Source='ru.md' },
    @{ Id=5; Platform='Notion'; Slug='cs2-external-sovmestimost'; Title='CS2 External и совместимость: экранный режим, Windows и разрешение'; Game='cs2'; Primary='CS2 External совместимость'; Target='https://cluster.center/ru/cs2'; File='05-cs2-external-sovmestimost.md'; Intent='compatibility matrix explainer'; Source='cs2.md' },
    @{ Id=6; Platform='Notion'; Slug='auto-parry-zaderzhka-i-dokazatelstva'; Title='Auto Parry и задержка: почему один ролик не доказывает стабильность'; Game='deadlock'; Primary='Auto Parry и задержка'; Target='https://cluster.center/ru/deadlock'; File='06-auto-parry-zaderzhka-i-dokazatelstva.md'; Intent='latency and demo evidence audit'; Source='deadlock.md' },
    @{ Id=7; Platform='GitBook'; Slug='dokumentaciya-igrovogo-servisa'; Title='Документация игрового сервиса: минимальный стандарт доверия'; Game='multi'; Primary='документация игрового сервиса'; Target='https://cluster.center/ru'; File='07-dokumentaciya-igrovogo-servisa.md'; Intent='documentation quality checklist'; Source='ru.md' },
    @{ Id=8; Platform='GitBook'; Slug='slovar-funkciy-cs2'; Title='Aimbot, TriggerBot, ESP и HUD: словарь функций CS2'; Game='cs2'; Primary='функции CS2'; Target='https://cluster.center/ru/cs2'; File='08-slovar-funkciy-cs2.md'; Intent='feature taxonomy and evidence types'; Source='cs2.md' },
    @{ Id=9; Platform='GitBook'; Slug='slovar-funkciy-deadlock'; Title='Combo, Auto Parry и Souls Aimbot: словарь функций Deadlock'; Game='deadlock'; Primary='функции Deadlock'; Target='https://cluster.center/ru/deadlock'; File='09-slovar-funkciy-deadlock.md'; Intent='feature taxonomy without operational guidance'; Source='deadlock.md' },
    @{ Id=10; Platform='GitHub'; Slug='publichnyy-changelog-i-status-page'; Title='Публичный changelog и статусная страница: как документировать обновления'; Game='multi'; Primary='публичный changelog'; Target='https://cluster.center/ru'; File='10-publichnyy-changelog-i-status-page.md'; Intent='open documentation specification'; Source='ru.md' },
    @{ Id=11; Platform='GitHub'; Slug='posle-obnovleniya-cs2-chto-proveryat'; Title='После обновления CS2: как проверять версию, видео и known issues'; Game='cs2'; Primary='обновление CS2 и совместимость'; Target='https://cluster.center/ru/cs2'; File='11-posle-obnovleniya-cs2-chto-proveryat.md'; Intent='post-update verification checklist'; Source='cs2.md' },
    @{ Id=12; Platform='GitHub'; Slug='matrica-podderzhki-geroev-deadlock'; Title='Матрица поддержки героев Deadlock: как показывать реальное покрытие'; Game='deadlock'; Primary='матрица поддержки героев Deadlock'; Target='https://cluster.center/ru/deadlock'; File='12-matrica-podderzhki-geroev-deadlock.md'; Intent='maintainer documentation design'; Source='deadlock.md' },
    @{ Id=13; Platform='JustPasteMe'; Slug='besplatnyy-test-12-voprosov'; Title='Бесплатный тест игрового инструмента: 12 вопросов до регистрации'; Game='multi'; Primary='бесплатный тест игрового инструмента'; Target='https://cluster.center/ru'; File='13-besplatnyy-test-12-voprosov.md'; Intent='trial evaluation questionnaire'; Source='ru.md' },
    @{ Id=14; Platform='JustPasteMe'; Slug='kak-razbirat-demo-cs2'; Title='Как разбирать демо CS2-инструмента: что видео доказывает, а что нет'; Game='cs2'; Primary='демо CS2-инструмента'; Target='https://cluster.center/ru/cs2'; File='14-kak-razbirat-demo-cs2.md'; Intent='video evidence literacy'; Source='cs2.md' },
    @{ Id=15; Platform='JustPasteMe'; Slug='demo-deadlock-bez-haypa'; Title='Демо Deadlock без хайпа: как проверять заявленные функции'; Game='deadlock'; Primary='демо Deadlock'; Target='https://cluster.center/ru/deadlock'; File='15-demo-deadlock-bez-haypa.md'; Intent='feature-specific demo audit'; Source='deadlock.md' }
)

$manifestItems = @()
$indexLines = @('# Cluster RU T2 Article Index', '')
$taskLines = @('# Codex Article Task', '', 'Write and verify exactly 15 original Russian T2 articles: three for each non-Rentry platform and five distinct intents for each Cluster RU target. Use one contextual target link, two real target-page images, answer-first GEO structure, non-operational risk-aware wording, SEO front matter, and FAQ.', '', '## Articles', '')

foreach ($item in $items) {
    $promptPath = Join-Path $promptDir (('{0:D2}-{1}.md' -f $item.Id, $item.Slug))
    $evidencePath = Join-Path $evidenceDir (('{0:D2}-{1}.json' -f $item.Id, $item.Slug))
    $outputPath = Join-Path $articleDir $item.File
    $prompt = @"
# $($item.Title)

- Destination platform: $($item.Platform)
- Page type: Blog post / T2 editorial resource
- Search intent: $($item.Intent)
- Primary keyword: $($item.Primary)
- Contextual target: $($item.Target)
- Required structure: SEO front matter, one H1, answer-first introduction, question-led H2s, practical checks, two real images from the supplied target page, conclusion, and 4-7 FAQ items.
- Safety boundary: explain terminology, evidence, comparison, compatibility, and risk only; do not provide anti-cheat bypass, evasion, injection, concealment, or implementation instructions.
- Uniqueness boundary: do not paraphrase the destination, reuse its sales copy, or repeat the 2026-09-09 published Cluster articles; solve the distinct $($item.Intent) job.
"@
    [System.IO.File]::WriteAllText($promptPath, $prompt, [System.Text.UTF8Encoding]::new($false))

    $evidenceObject = [ordered]@{
        evidence = @(
            @{ source = $item.Target; role = 'live target page and supplied editorial media' },
            @{ source = "knowledge/agent_memory/sources/cluster-ru-t2-15-20260910-links/$($item.Source)"; role = 'materialized target-page text and image references' },
            @{ source = 'knowledge/agent_memory/products/product-map.md'; role = 'mandatory CS2 and Deadlock product mapping' },
            @{ source = 'knowledge/agent_memory/rules/article-visual-prompt-guide.md'; role = 'real screenshot accuracy, alt text, and placement requirements' },
            @{ source = 'published/articles.csv'; role = 'duplicate prevention for existing Cluster Substack articles' }
        )
        target = $item.Target
        platform = $item.Platform
        intent = $item.Intent
        checked_at = '2026-09-10T08:47:42+03:00'
    }
    [System.IO.File]::WriteAllText($evidencePath, ($evidenceObject | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))

    $manifestItems += [ordered]@{
        topic_id = $item.Id
        title = $item.Title
        game = $item.Game
        language = 'ru'
        status = 'article'
        output = $outputPath
        prompt = $promptPath
        evidence = $evidencePath
        llm_error = $null
    }
    $indexLines += ('{0}. [{1}]({2}) — {3}' -f $item.Id, $item.Title, $outputPath, $item.Platform)
    $taskLines += ('### {0}. {1}' -f $item.Id, $item.Title), '', ('- Platform: `{0}`' -f $item.Platform), ('- Prompt: `{0}`' -f $promptPath), ('- Evidence: `{0}`' -f $evidencePath), ('- Target: `{0}`' -f $outputPath), ''
}

$manifest = [ordered]@{
    created_at = $runId
    spec = [ordered]@{
        raw = 'Create exactly 15 original Russian T2 articles: one for each pairing of three Cluster RU targets and five platforms, excluding Rentry.'
        count = 15
        language = 'ru'
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

$publication = [ordered]@{
    created_at = '2026-09-10'
    status = 'articles_in_progress'
    excluded_platforms = @('Rentry')
    platforms = [ordered]@{
        Substack = @(1,2,3)
        Notion = @(4,5,6)
        GitBook = @(7,8,9)
        GitHub = @(10,11,12)
        JustPasteMe = @(13,14,15)
    }
    targets = [ordered]@{
        'https://cluster.center/ru' = @(1,4,7,10,13)
        'https://cluster.center/ru/cs2' = @(2,5,8,11,14)
        'https://cluster.center/ru/deadlock' = @(3,6,9,12,15)
    }
}
[System.IO.File]::WriteAllText((Join-Path $projectRoot 'output/cluster-ru-t2-publication-manifest-20260910.json'), ($publication | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))

Write-Output "Built custom Cluster RU manifest for $($items.Count) articles"
