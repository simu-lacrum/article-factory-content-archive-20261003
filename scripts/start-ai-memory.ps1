param(
    [string]$ContainerName = "ai-memory",
    [string]$Image = "akitaonrails/ai-memory:latest",
    [int]$Port = 49374
)

$ErrorActionPreference = "Stop"

Write-Host "Checking Docker daemon..."
docker version --format "{{.Server.Version}}" | Out-Null

$existing = docker ps -a --filter "name=^/$ContainerName$" --format "{{.Names}}"
if ($existing -eq $ContainerName) {
    $running = docker ps --filter "name=^/$ContainerName$" --format "{{.Names}}"
    if ($running -eq $ContainerName) {
        Write-Host "$ContainerName is already running on http://127.0.0.1:$Port"
        exit 0
    }
    Write-Host "Starting existing $ContainerName container..."
    docker start $ContainerName | Out-Null
    Write-Host "$ContainerName started on http://127.0.0.1:$Port"
    exit 0
}

Write-Host "Pulling $Image..."
docker pull $Image

Write-Host "Starting $ContainerName in zero-LLM mode..."
docker run -d `
    --name $ContainerName `
    --restart unless-stopped `
    -p "127.0.0.1:$Port`:49374" `
    -v ai-memory-data:/data `
    $Image | Out-Null

Write-Host "$ContainerName started on http://127.0.0.1:$Port"
Write-Host "Zero-LLM mode still supports local wiki and FTS search. Add provider env vars later if needed."
