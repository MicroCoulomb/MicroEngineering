$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

docker build -t microprelegal $repoRoot
try {
    docker rm -f microprelegal | Out-Null
} catch {
}
docker run -d --name microprelegal -p 8000:8000 microprelegal
