$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$targetDir = Join-Path $projectRoot 'output/articles/20260910-082336'
$replacements = [ordered]@{
    'вЂњ' = '“'
    'вЂќ' = '”'
    'вЂ™' = '’'
    'вЂ”' = '—'
    'вЂ“' = '–'
}

Get-ChildItem -LiteralPath $targetDir -Filter '*.md' -File | ForEach-Object {
    $text = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $updated = $text
    foreach ($entry in $replacements.GetEnumerator()) {
        $updated = $updated.Replace($entry.Key, $entry.Value)
    }
    if ($updated -ne $text) {
        [System.IO.File]::WriteAllText($_.FullName, $updated, [System.Text.UTF8Encoding]::new($false))
        Write-Output "Fixed $($_.Name)"
    }
}
