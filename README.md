# AutoContent - Modular Content Automation Platform

## Overview

AutoContent is a comprehensive, modular platform for automating content creation, transformation, and publishing across social media platforms. Built with Angular frontend and FastAPI backend, designed to scale from MVP to a full SaaS platform.

### Key Features
- 🎯 **Modular Architecture**: Independent, reusable modules
- 🔄 **Multi-Mode Support**: Curated, Avatar, and Ads content generation
- 📱 **Social Media Integration**: YouTube, TikTok, Instagram (expandable)
- ⚡ **Real-time Processing**: FFmpeg, Whisper, TTS integration
- 📊 **Analytics & Monitoring**: Built-in logging and performance tracking
- 🚀 **Scalable Design**: From single-user MVP to SaaS platform

## Project Structure

```
autocontent/
├── backend/                 # Python FastAPI backend
│   ├── app/                # Application code
│   │   ├── core/          # Config, database, setup
│   │   ├── api/           # Route handlers
│   │   ├── models/        # SQLAlchemy ORM models
│   │   ├── schemas/       # Pydantic validation schemas
│   │   ├── services/      # Business logic
│   │   └── utils/         # Helper functions
│   ├── requirements.txt    # Python dependencies
│   └── main.py           # Application entry point
│
├── frontend/               # Angular frontend
│   ├── src/
│   │   ├── app/          # Angular components
│   │   │   ├── components/   # Reusable UI components
│   │   │   ├── services/     # API services
│   │   │   └── models/       # TypeScript interfaces
│   │   └── styles.css    # Global styles
│   ├── angular.json      # Angular CLI config
│   └── package.json      # NPM dependencies
│
├── modules/              # Modular processing units
│   ├── trend_miner/     # Content discovery
│   ├── downloader/      # Video downloading
│   ├── clipper/         # Video clipping
│   ├── script_generator/# Title/description generation
│   ├── voice/           # TTS and voice processing
│   ├── avatar/          # Avatar-based content (Phase 3)
│   ├── composer/        # Video composition
│   ├── uploader/        # Platform uploading
│   └── ads/            # Ad-specific processing
│
├── pipeline/            # Pipeline orchestration
│   ├── strategies/      # Strategy pattern implementations
│   └── workers/         # Background workers
│
├── storage/             # Data and artifact storage
├── auth/                # Authentication layer
├── analytics/           # Metrics and insights
├── scheduler/           # Task scheduling
│
├── docker-compose.yml   # Docker orchestration
├── Dockerfile.backend   # Backend container
├── Dockerfile.frontend  # Frontend container
└── README.md           # This file
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.10+ (for local development)
- Node.js 20+ (for frontend development)
- FFmpeg

### Using Docker Compose

```bash
# Clone repository
git clone <repo-url>
cd autocontent

# Create environment file
cp .env.example .env
# Edit .env with your credentials

# Start all services
docker-compose up -d

# Services running on:
# Frontend: http://localhost:4200
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Development

**Backend:**
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

## API Endpoints (Phase 1)

### Channels
```
POST   /api/v1/channels              Create channel
GET    /api/v1/channels              List channels
GET    /api/v1/channels/{id}         Get channel
PATCH  /api/v1/channels/{id}         Update channel
DELETE /api/v1/channels/{id}         Delete channel
```

### Pipeline
```
POST   /api/v1/pipeline/run          Run pipeline
GET    /api/v1/pipeline/{id}         Get pipeline status
```

### Logs
```
GET    /api/v1/logs/{pipeline_id}    Get execution logs
```

### Authentication
```
POST   /api/v1/auth/youtube/init          Start YouTube OAuth
GET    /api/v1/auth/youtube/callback      OAuth callback
```

## Development Phases

### Phase 1 ✅ (Current)
- Basic UI with channel management
- Simple pipeline execution
- OAuth foundation
- Phase 1 endpoints implemented
- Real-time log viewer
 - Local developer environment bootstrap (scripts/bootstrap.sh)
 - Backend virtualenv and Python dependencies installed (`backend/.venv`, `requirements.txt`)
 - Frontend dependencies installed and lockfile committed (`frontend/package-lock.json`)
 - FFmpeg installed and verified for media processing

### Phase 2 🔄
- Scheduler for automated runs
- Multi-channel management
- Ads mode implementation
- Database metrics tracking
- Enhanced dashboard with charts

### Phase 3 (Planned)
- Feedback loops from metrics
- Content scoring algorithm
- A/B testing framework
- Smart recommendations
- Avatar mode expansion

### Phase 4 (Planned)
- Creator profile system
- Public feed interface
- Creator rankings
- Profile customization

### Phase 5 (Planned)
- Full SaaS platform
- User authentication system
- Subscription tiers (free, pro)
- Usage limits enforcement
- Billing integration
- Multi-tenant support
- Microservices architecture

## Module Descriptions

### Trend Miner
Discovers trending content through API calls and web scraping.
- Input: Keywords, platforms
- Output: Trending videos/content list

### Downloader
Fetches source videos from various platforms.
- Input: URL
- Output: Downloaded video file

### Clipper
Generates short video clips from longer content.
- Input: Video file, duration
- Output: Clipped video segments

### Script Generator
Creates titles and descriptions using templates and AI.
- Input: Content, keywords
- Output: Title, description, tags

### Voice
Text-to-speech conversion with multiple engine support.
- Input: Script text, voice settings
- Output: Audio file

### Avatar
AI-powered avatar video generation (Phase 3).
- Input: Script, avatar model
- Output: Avatar video

### Composer
Combines video, audio, and effects into final product.
- Input: Video, audio, effects
- Output: Composed video file

### Uploader
Publishes content to social media platforms.
- Input: Video, metadata, platform
- Output: Upload confirmation

### Ads
Ad-specific processing pipeline (Phase 2).
- Input: Product catalog, CTA
- Output: Ad video with call-to-action

## Database Schema

### Channels
```sql
CREATE TABLE channels (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  platform VARCHAR(50),
  platform_channel_id VARCHAR(255) UNIQUE,
  oauth_token TEXT,
  mode VARCHAR(20),
  is_active BOOLEAN,
  created_at DATETIME
);
```

### Pipelines
```sql
CREATE TABLE pipelines (
  id INTEGER PRIMARY KEY,
  channel_id INTEGER FK,
  status VARCHAR(50),
  mode VARCHAR(20),
  content_keyword VARCHAR(255),
  generated_title VARCHAR(500),
  generated_description TEXT,
  output_video_path VARCHAR(500),
  error_message TEXT,
  created_at DATETIME
);
```

### Logs
```sql
CREATE TABLE pipeline_logs (
  id INTEGER PRIMARY KEY,
  pipeline_id INTEGER FK,
  level VARCHAR(20),
  message TEXT,
  step VARCHAR(100),
  created_at DATETIME
);
```

## Security Considerations

- ✅ Use official APIs only (no browser automation)
- ✅ Encrypt stored tokens
- ✅ Implement rate limiting
- ✅ Add request validation
- ✅ Audit logging for sensitive operations
- ✅ CORS configuration
- ✅ Environment variable for secrets

## Performance Optimization

- Async processing for I/O operations
- Database connection pooling
- Caching strategy for frequently accessed data
- Queue system for background jobs (Phase 2+)
- CDN for static assets (Phase 4+)

## Testing

```bash
# Backend tests (TODO)
cd backend
pytest

# Frontend tests (TODO)
cd frontend
npm test
```

## Deployment

### Docker Registry
```bash
docker build -t autocontent/backend -f Dockerfile.backend .
docker build -t autocontent/frontend -f Dockerfile.frontend .
docker push autocontent/backend
docker push autocontent/frontend
```

### Cloud Deployment (Phase 5)
- AWS ECS, Kubernetes, or similar
- Database migration to PostgreSQL
- Redis for session/cache management
- CDN for static assets
- Load balancing

## Contributing

1. Follow the modular architecture
2. Add tests for new features
3. Keep components decoupled
4. Document your changes
5. Use clear commit messages

## License

MIT License

## Support

For issues and questions, please open an GitHub issue or contact the development team.

---

**Version**: 0.1.0 (Phase 1)  
**Version**: 0.1.1 (Phase 1)
**Last Updated**: May 17 2026

## Recent Changes

- Added `scripts/bootstrap.sh` to automate system/package setup, create backend virtualenv, install Python and Node dependencies, copy `.env` examples, and create `storage`/`temp` directories. (Committed)
- Created placeholder `.env` files at project root and `backend/.env` from examples (kept uncommitted by design — `.env` is gitignored). (Generated)
- Installed backend Python dependencies into `backend/.venv` and ran `npm install` in `frontend` (local dev setup completed). (Executed locally)
- Committed `frontend/package-lock.json` to pin frontend dependency versions for reproducible installs. (Committed)

These commits and local setup actions complete additional Phase 1 developer-experience tasks: environment bootstrap, dependency locking, and initial system dependency verification (FFmpeg).
