<#
Bootstrap script for Windows development setup.
It checks for Docker, Python and Node, and runs install steps when available.

Usage: Open an elevated PowerShell and run:
  .\scripts\bootstrap.ps1

This script does NOT install Docker Desktop automatically. It will show
instructions and, if possible, run dependency installs with `winget`.
#>

function Check-Command($cmd) {
    $null -ne (Get-Command $cmd -ErrorAction SilentlyContinue)
}

Write-Host "Starting bootstrap checks..." -ForegroundColor Cyan

$hasDocker = Check-Command "docker"
$hasDockerCompose = Check-Command "docker-compose" -or Check-Command "docker"
$hasPython = Check-Command "python"
$hasNode = Check-Command "node"

if (-not $hasDocker) {
    Write-Host "Docker not found. Please install Docker Desktop:" -ForegroundColor Yellow
    Write-Host "https://www.docker.com/get-started"
} else {
    Write-Host "Docker detected." -ForegroundColor Green
}

if (-not $hasPython) {
    Write-Host "Python not found. Install Python 3.10+ (from Microsoft Store or https://www.python.org/downloads/)." -ForegroundColor Yellow
} else {
    Write-Host "Python detected." -ForegroundColor Green
}

if (-not $hasNode) {
    Write-Host "Node.js not found. Install Node 20+ from https://nodejs.org/ or use https://winget.run to install." -ForegroundColor Yellow
} else {
    Write-Host "Node detected." -ForegroundColor Green
}

Write-Host "\nCreating required directories: storage, temp" -ForegroundColor Cyan
New-Item -ItemType Directory -Path ./storage -Force | Out-Null
New-Item -ItemType Directory -Path ./temp -Force | Out-Null

Write-Host "\nCopying .env examples if .env files missing" -ForegroundColor Cyan
if (-not (Test-Path .env) -and (Test-Path .env.example)) {
    Copy-Item .env.example .env -Force
    Write-Host "Created .env from .env.example" -ForegroundColor Green
}
if (-not (Test-Path backend/.env) -and (Test-Path backend/.env.example)) {
    Copy-Item backend/.env.example backend/.env -Force
    Write-Host "Created backend/.env from backend/.env.example" -ForegroundColor Green
}

if ($hasPython) {
    Write-Host "\nSetting up Python virtualenv and installing backend dependencies" -ForegroundColor Cyan
    python -m venv backend/.venv
    $activate = "backend/.venv/Scripts/Activate.ps1"
    if (Test-Path $activate) {
        Write-Host "Activating virtualenv and installing requirements..." -ForegroundColor Cyan
        & $activate; pip install --upgrade pip; pip install -r backend/requirements.txt
    } else {
        Write-Host "Could not find virtualenv activation script at $activate" -ForegroundColor Yellow
    }
}

if ($hasNode) {
    Write-Host "\nInstalling frontend dependencies (npm install)" -ForegroundColor Cyan
    Push-Location frontend
    npm install
    Pop-Location
}

if ($hasDocker -or $hasDockerCompose) {
    Write-Host "\nStarting Docker Compose services..." -ForegroundColor Cyan
    try {
        docker compose up -d
    } catch {
        docker-compose up -d
    }
    Write-Host "Docker Compose command executed. Check containers with: docker ps" -ForegroundColor Green
} else {
    Write-Host "\nDocker not available. You can run services locally instead." -ForegroundColor Yellow
    Write-Host "To run backend locally (after venv):" -ForegroundColor Cyan
    Write-Host "  backend/.venv\\Scripts\\Activate.ps1; uvicorn main:app --reload --port 8000" -ForegroundColor White
    Write-Host "To run frontend locally:" -ForegroundColor Cyan
    Write-Host "  cd frontend; npm start" -ForegroundColor White
}

Write-Host "\nBootstrap complete. Review output above for any errors." -ForegroundColor Green
