# AutoContent - File Navigation Guide

**Quick navigation reference for the AutoContent project.**

---

## 📚 Documentation (Start Here)

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | 📖 **START HERE** - Architecture overview and features |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | 📋 Quick reference and statistics |
| [SETUP.md](SETUP.md) | 🚀 Installation and quick start guide |
| [DEVELOPMENT.md](DEVELOPMENT.md) | 💻 Development standards and code patterns |
| [ROADMAP.md](ROADMAP.md) | 🗺️ 5-phase development roadmap |
| [COMPLETION_CHECKLIST.md](COMPLETION_CHECKLIST.md) | ✅ What's complete and what's planned |

---

## 🔧 Backend (Python/FastAPI)

### Main Entry Point
- **[backend/main.py](backend/main.py)** - Application startup

### Core Setup
- **[backend/app/core/app.py](backend/app/core/app.py)** - FastAPI app factory
- **[backend/app/core/database.py](backend/app/core/database.py)** - Database configuration
- **[backend/app/core/config.py](backend/app/core/config.py)** - Settings and environment

### Data Models
- **[backend/app/models/models.py](backend/app/models/models.py)** - SQLAlchemy ORM models (4 tables)

### API Routes
- **[backend/app/api/channels.py](backend/app/api/channels.py)** - Channel CRUD endpoints
- **[backend/app/api/pipeline.py](backend/app/api/pipeline.py)** - Pipeline execution endpoints
- **[backend/app/api/logs.py](backend/app/api/logs.py)** - Log retrieval endpoints
- **[backend/app/api/auth.py](backend/app/api/auth.py)** - OAuth endpoints

### Request/Response Schemas
- **[backend/app/schemas/base.py](backend/app/schemas/base.py)** - All Pydantic schemas

### Business Logic
- **[backend/app/services/channel.py](backend/app/services/channel.py)** - Channel operations
- **[backend/app/services/pipeline.py](backend/app/services/pipeline.py)** - Pipeline execution
- **[backend/app/services/oauth.py](backend/app/services/oauth.py)** - OAuth handling

### Configuration Files
- **[backend/requirements.txt](backend/requirements.txt)** - Python dependencies
- **[backend/.env.example](backend/.env.example)** - Environment variables template
- **[backend/README.md](backend/README.md)** - Backend setup guide

---

## 🎨 Frontend (Angular/TypeScript)

### Main Entry Point
- **[frontend/src/main.ts](frontend/src/main.ts)** - Angular bootstrap
- **[frontend/src/index.html](frontend/src/index.html)** - HTML entry point

### Angular Module
- **[frontend/src/app/app.module.ts](frontend/src/app/app.module.ts)** - Module configuration

### Main Component
- **[frontend/src/app/app.component.ts](frontend/src/app/app.component.ts)** - Root component
- **[frontend/src/app/app.component.html](frontend/src/app/app.component.html)** - Root template
- **[frontend/src/app/app.component.css](frontend/src/app/app.component.css)** - Root styles

### Components
| Component | Purpose |
|-----------|---------|
| [dashboard](frontend/src/app/components/dashboard/) | Main dashboard with tabs |
| [channel-list](frontend/src/app/components/channel-list/) | Display active channels |
| [channel-form](frontend/src/app/components/channel-form/) | Create new channels |
| [pipeline-runner](frontend/src/app/components/pipeline-runner/) | Execute pipelines |
| [logs-viewer](frontend/src/app/components/logs-viewer/) | Real-time log display |

### Services
- **[frontend/src/app/services/channel.service.ts](frontend/src/app/services/channel.service.ts)** - Channel API calls
- **[frontend/src/app/services/pipeline.service.ts](frontend/src/app/services/pipeline.service.ts)** - Pipeline API calls

### Data Types
- **[frontend/src/app/models/types.ts](frontend/src/app/models/types.ts)** - TypeScript interfaces

### Styling
- **[frontend/src/styles.css](frontend/src/styles.css)** - Global styles

### Configuration Files
- **[frontend/package.json](frontend/package.json)** - NPM dependencies
- **[frontend/angular.json](frontend/angular.json)** - Angular CLI configuration
- **[frontend/tsconfig.json](frontend/tsconfig.json)** - TypeScript configuration
- **[frontend/README.md](frontend/README.md)** - Frontend setup guide

---

## 🔄 Pipeline & Strategy Pattern

### Strategy Pattern Implementation
- **[pipeline/strategies/content_strategy.py](pipeline/strategies/content_strategy.py)**
  - Abstract ContentStrategy
  - CuratedStrategy (implemented)
  - AvatarStrategy (Phase 3)
  - AdsStrategy (Phase 2)
  - StrategyFactory

---

## 📦 Processing Modules

### Core Modules (with mock implementations ready for real integration)

| Module | File | Purpose |
|--------|------|---------|
| **Trend Miner** | [modules/trend_miner/trend_miner.py](modules/trend_miner/trend_miner.py) | Content discovery |
| **Downloader** | [modules/downloader/downloader.py](modules/downloader/downloader.py) | Video downloading |
| **Clipper** | [modules/clipper/clipper.py](modules/clipper/clipper.py) | Video clipping |
| **Script Generator** | [modules/script_generator/script_generator.py](modules/script_generator/script_generator.py) | Title/description gen |
| **Voice** | [modules/voice/voice_engine.py](modules/voice/voice_engine.py) | Text-to-speech |
| **Composer** | [modules/composer/composer.py](modules/composer/composer.py) | Video composition |
| **Uploader** | [modules/uploader/uploader.py](modules/uploader/uploader.py) | Platform publishing |
| **Avatar** | [modules/avatar/avatar_generator.py](modules/avatar/avatar_generator.py) | Avatar generation (Phase 3) |
| **Ads** | [modules/ads/ads_generator.py](modules/ads/ads_generator.py) | Ad generation (Phase 2) |

### Storage
- **[storage/storage.py](storage/storage.py)** - File storage management

---

## 🚀 Future Development (Placeholders)

### Phase 2+ Features
- **[scheduler/scheduler.py](scheduler/scheduler.py)** - Automated scheduling (Phase 2)
- **[analytics/analytics.py](analytics/analytics.py)** - Analytics engine (Phase 3)
- **[auth/saas_auth.py](auth/saas_auth.py)** - SaaS authentication (Phase 5)

---

## 🐳 Docker & DevOps

| File | Purpose |
|------|---------|
| [Dockerfile.backend](Dockerfile.backend) | Backend container definition |
| [Dockerfile.frontend](Dockerfile.frontend) | Frontend container definition |
| [docker-compose.yml](docker-compose.yml) | Service orchestration |
| [nginx.conf](nginx.conf) | Nginx configuration for frontend |

---

## 📋 Configuration Files

| File | Purpose |
|------|---------|
| [.env.example](.env.example) | Environment variables template |
| [.gitignore](.gitignore) | Git ignore patterns |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Development guidelines |

---

## 🎯 Quick Navigation by Task

### I want to...

#### Run the project
👉 [SETUP.md - Quick Start with Docker](SETUP.md#quick-start-with-docker)

#### Understand the architecture
👉 [README.md - Architecture Base](README.md#arquitetura-base)

#### See what's been done
👉 [COMPLETION_CHECKLIST.md](COMPLETION_CHECKLIST.md)

#### Understand Phase 1
👉 [README.md - Phase 1](README.md#fase-1--mvp-funcional)

#### See future phases
👉 [ROADMAP.md](ROADMAP.md)

#### Learn the code standards
👉 [DEVELOPMENT.md](DEVELOPMENT.md)

#### Add a new API endpoint
👉 [DEVELOPMENT.md - Adding API Endpoints](DEVELOPMENT.md#2-adding-api-endpoints)

#### Add a new component
👉 [DEVELOPMENT.md - Adding UI Components](DEVELOPMENT.md#3-adding-ui-components)

#### Create a new module
👉 [DEVELOPMENT.md - Creating a New Module](DEVELOPMENT.md#1-creating-a-new-module)

#### Troubleshoot issues
👉 [SETUP.md - Troubleshooting](SETUP.md#troubleshooting)

#### Understand the API
👉 [README.md - API Endpoints](README.md#fase-1--mvp-funcional) or visit http://localhost:8000/docs

---

## 📂 Complete Directory Structure

```
autocontent/
├── 📖 README.md                    # Project overview
├── 📖 SETUP.md                     # Setup instructions
├── 📖 DEVELOPMENT.md               # Development guide
├── 📖 ROADMAP.md                   # 5-phase roadmap
├── 📖 PROJECT_SUMMARY.md           # Quick reference
├── 📖 COMPLETION_CHECKLIST.md      # Status checklist
├── 📖 INDEX.md                     # This file
├── 📄 .env.example
├── 📄 .gitignore
│
├── 🐍 backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   └── app/
│       ├── core/
│       │   ├── app.py
│       │   ├── database.py
│       │   └── config.py
│       ├── api/
│       │   ├── channels.py
│       │   ├── pipeline.py
│       │   ├── logs.py
│       │   └── auth.py
│       ├── models/
│       │   └── models.py
│       ├── schemas/
│       │   └── base.py
│       ├── services/
│       │   ├── channel.py
│       │   ├── pipeline.py
│       │   └── oauth.py
│       └── utils/
│
├── 🎨 frontend/
│   ├── package.json
│   ├── angular.json
│   ├── tsconfig.json
│   ├── README.md
│   └── src/
│       ├── main.ts
│       ├── index.html
│       ├── styles.css
│       └── app/
│           ├── app.module.ts
│           ├── app.component.ts
│           ├── app.component.html
│           ├── app.component.css
│           ├── components/
│           │   ├── dashboard/
│           │   ├── channel-list/
│           │   ├── channel-form/
│           │   ├── pipeline-runner/
│           │   └── logs-viewer/
│           ├── services/
│           │   ├── channel.service.ts
│           │   └── pipeline.service.ts
│           └── models/
│               └── types.ts
│
├── 🔄 pipeline/
│   └── strategies/
│       └── content_strategy.py
│
├── 📦 modules/
│   ├── trend_miner/
│   ├── downloader/
│   ├── clipper/
│   ├── script_generator/
│   ├── voice/
│   ├── avatar/
│   ├── composer/
│   ├── uploader/
│   └── ads/
│
├── 💾 storage/
├── 🔐 auth/
├── 📊 analytics/
├── ⏰ scheduler/
│
├── 🐳 docker-compose.yml
├── 🐳 Dockerfile.backend
├── 🐳 Dockerfile.frontend
├── 🐳 nginx.conf
│
└── .github/
    └── copilot-instructions.md
```

---

## 🚀 Getting Started Checklist

- [ ] Read [README.md](README.md)
- [ ] Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- [ ] Follow [SETUP.md](SETUP.md)
- [ ] Review [DEVELOPMENT.md](DEVELOPMENT.md)
- [ ] Run `docker-compose up -d`
- [ ] Test frontend: http://localhost:4200
- [ ] Test backend: http://localhost:8000
- [ ] Check API docs: http://localhost:8000/docs
- [ ] Explore code structure
- [ ] Start Phase 2 development

---

## 📞 Need Help?

1. Check the relevant documentation above
2. Review code patterns in DEVELOPMENT.md
3. Check [Troubleshooting section](SETUP.md#troubleshooting)
4. Look at similar implementations in the codebase
5. Open a GitHub issue

---

**Last Updated**: May 3, 2026
**Version**: 0.1.0 (Phase 1 Complete)
**Project Status**: ✅ Ready for development

Happy coding! 🚀
