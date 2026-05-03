# AutoContent - Complete Setup & Development Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Quick Start with Docker](#quick-start-with-docker)
3. [Local Development Setup](#local-development-setup)
4. [API Documentation](#api-documentation)
5. [Development Workflow](#development-workflow)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required
- Docker & Docker Compose
- Git

### For Local Development
- Python 3.10+
- Node.js 20+
- npm or yarn

### Optional (for full functionality)
- FFmpeg
- OpenAI Whisper
- Coqui TTS

## Quick Start with Docker

### 1. Setup Environment

```bash
# Clone the repository
git clone <repo-url>
cd autocontent

# Create environment file
cp .env.example .env

# Edit .env with your credentials (YouTube OAuth, etc.)
nano .env
```

### 2. Build and Run

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# Check service status
docker-compose ps
```

### 3. Access Services

- **Frontend**: http://localhost:4200
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **API Schema**: http://localhost:8000/openapi.json

### 4. Initialize Database

```bash
# The database is created automatically on first run
# Check logs if there are issues
docker-compose logs backend
```

## Local Development Setup

### Backend (Python)

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
cp .env.example .env
nano .env

# 6. Initialize database
python -c "from app.core.database import init_db; init_db()"

# 7. Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Backend will be available at http://localhost:8000
```

### Frontend (Angular)

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm start

# Frontend will be available at http://localhost:4200
```

### Full Stack Development

In separate terminals:

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

## API Documentation

### Interactive API Docs
Visit http://localhost:8000/docs (Swagger UI)

### Base URL
```
http://localhost:8000/api/v1
```

### Common Operations

#### Create Channel
```bash
curl -X POST http://localhost:8000/api/v1/channels \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My YouTube Channel",
    "platform": "youtube",
    "mode": "curated"
  }'
```

#### List Channels
```bash
curl http://localhost:8000/api/v1/channels
```

#### Run Pipeline
```bash
curl -X POST http://localhost:8000/api/v1/pipeline/run \
  -H "Content-Type: application/json" \
  -d '{
    "channel_id": 1,
    "mode": "curated",
    "content_keyword": "technology"
  }'
```

#### Get Pipeline Status
```bash
curl http://localhost:8000/api/v1/pipeline/1
```

#### Get Pipeline Logs
```bash
curl http://localhost:8000/api/v1/logs/1
```

## Development Workflow

### 1. Creating a New Module

```
modules/
└── my_module/
    ├── __init__.py
    ├── module.py           # Core logic
    └── tests.py            # Tests
```

### 2. Adding API Endpoints

1. Create schema in `backend/app/schemas/`
2. Create model in `backend/app/models/` (if needed)
3. Create service in `backend/app/services/`
4. Create routes in `backend/app/api/`

### 3. Adding UI Components

```
frontend/src/app/
└── components/
    └── my-component/
        ├── my-component.component.ts
        ├── my-component.component.html
        └── my-component.component.css
```

### 4. Code Quality

```bash
# Backend linting (TODO)
cd backend
pylint app/

# Frontend linting
cd frontend
npm run lint
```

## Troubleshooting

### Docker Issues

**Services not starting:**
```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild images
docker-compose build --no-cache

# Reset everything
docker-compose down -v
docker-compose up --build
```

**Port already in use:**
```bash
# Change ports in docker-compose.yml
ports:
  - "8001:8000"  # Backend
  - "4201:4200"  # Frontend
```

### Backend Issues

**Database locked:**
```bash
# Remove SQLite database and reinit
rm backend/autocontent.db
cd backend
python -c "from app.core.database import init_db; init_db()"
```

**Module not found:**
```bash
# Ensure Python path includes project root
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Frontend Issues

**Dependencies issues:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Port already in use:**
```bash
# Run on different port
ng serve --port 4201
```

## Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for production setup instructions.

## Contributing

1. Create feature branch: `git checkout -b feature/my-feature`
2. Make changes following code style
3. Test locally
4. Commit: `git commit -m "Add my feature"`
5. Push: `git push origin feature/my-feature`
6. Create Pull Request

## Support

For issues:
1. Check [Troubleshooting](#troubleshooting) section
2. Review logs: `docker-compose logs`
3. Open GitHub issue with details

## Next Steps

- Review [README.md](README.md) for architecture overview
- Explore Phase 1 implementation
- Check module documentation in respective folders
- Set up IDE (VSCode recommended)
- Configure pre-commit hooks (TODO)

---

**Need help?** Check the documentation in each module or open an issue on GitHub.
