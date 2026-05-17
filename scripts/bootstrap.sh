#!/usr/bin/env bash
set -euo pipefail

# Bootstrap script for AutoContent (Linux Debian/Ubuntu)
# Run as: bash scripts/bootstrap.sh

echo "== AutoContent bootstrap starting =="

# 1) Install system packages (requires sudo)
sudo apt-get update
sudo apt-get install -y git curl build-essential ffmpeg python3 python3-venv python3-pip ca-certificates

# 2) Install Node.js 18 (if not present)
if ! command -v node >/dev/null 2>&1 || [ "$(node -v | cut -d. -f1 | tr -d v)" -lt 18 ]; then
  echo "Installing Node.js 18.x via NodeSource..."
  curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
  sudo apt-get install -y nodejs
fi

# 3) Optional: Docker
if ! command -v docker >/dev/null 2>&1; then
  echo "Docker not found. Installing docker.io and docker-compose..."
  sudo apt-get install -y docker.io docker-compose
  sudo systemctl enable --now docker
  echo "You may need to logout/login for docker group changes to take effect."
fi

# 4) Copy env examples if missing
ROOT="$(pwd)"
[ -f .env ] || cp .env.example .env && echo "Created .env from .env.example"
[ -f backend/.env ] || cp backend/.env.example backend/.env && echo "Created backend/.env from example"

# 5) Create storage dirs
mkdir -p storage temp
chmod -R u+rw storage temp

PYTHON_BIN="$(command -v python3.10 || command -v python3)"

# 6) Backend: venv and pip install
cd backend
"$PYTHON_BIN" -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi
deactivate
cd "$ROOT"

# 7) Frontend: npm install
if [ -d frontend ]; then
  cd frontend
  npm install
  cd "$ROOT"
fi

echo "== Bootstrap finished =="
echo "Next steps: edit .env and backend/.env with your credentials, then run:"
echo "  backend: source backend/.venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir ."
echo "  frontend: cd frontend && npm run start"
echo "Or run with Docker: docker-compose up --build"
