<#
Run backend locally (Windows PowerShell).
Creates a virtual environment at `backend/.venv`, installs requirements, and runs uvicorn.

Usage:
  .\scripts\run_local_backend.ps1
#>

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found in PATH. Install Python 3.10+ first." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path backend/.venv)) {
    Write-Host "Creating virtualenv..." -ForegroundColor Cyan
    python -m venv backend/.venv
}

$activate = "backend/.venv/Scripts/Activate.ps1"
if (Test-Path $activate) {
    Write-Host "Activating venv and installing requirements..." -ForegroundColor Cyan
    & $activate; pip install --upgrade pip; pip install -r backend/requirements.txt
    Write-Host "Starting uvicorn..." -ForegroundColor Cyan
    & $activate; uvicorn main:app --reload --port 8000
} else {
    Write-Host "Activation script not found at $activate" -ForegroundColor Red
    exit 1
}
