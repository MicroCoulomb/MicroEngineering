$ErrorActionPreference = "Stop"

try {
    docker rm -f microprelegal | Out-Null
} catch {
}
