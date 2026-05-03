# AutoContent - Modular Content Automation Platform

**Project Type**: Full-stack web application (Python FastAPI + Angular)

**Overview**: Modular platform for automating content creation, transformation, and publishing across social media. Designed for phased development from MVP (Phase 1) to SaaS platform (Phase 5).

## Development Guidelines

### Architecture Principles
- **Modularity**: Each feature lives in isolated, reusable modules
- **Strategy Pattern**: Support multiple content generation modes (curated, avatar, ads)
- **Clean Code**: Clear separation of concerns across layers
- **Extensibility**: New modules/strategies can be added without modifying core

### Tech Stack
- **Frontend**: Angular
- **Backend**: FastAPI (Python 3.10+)
- **Database**: SQLite → PostgreSQL
- **Container**: Docker + Docker Compose
- **Processing**: FFmpeg, Whisper (OpenAI), TTS (Coqui/local)

### Backend Structure
```
backend/
├── app/
│   ├── core/           # Config, database setup, constants
│   ├── api/            # Route handlers
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas (validation)
│   ├── services/       # Business logic
│   └── utils/          # Helpers
└── migrations/         # Alembic database migrations
```

### Frontend Structure
```
frontend/
├── src/
│   ├── app/
│   │   ├── components/      # Reusable components
│   │   ├── services/        # API services
│   │   ├── models/          # TypeScript interfaces
│   │   └── pages/           # Page components
│   └── assets/
```

### Module Organization
Each module (trend_miner, clipper, composer, etc.) should:
- Have clear input/output contracts
- Implement logging
- Support async operations
- Handle errors gracefully

### API Design
- RESTful endpoints with versioning (/api/v1)
- Request/Response validation via Pydantic schemas
- Clear error responses with meaningful messages
- Authentication headers for protected routes

### Database Patterns
- Use SQLAlchemy ORM for database operations
- Version migrations with Alembic
- Add indexes for performance-critical queries
- Keep schema normalized for scalability

### Code Quality
- Type hints throughout (Python 3.10+)
- Async/await for I/O operations
- Meaningful variable/function names
- Error handling at component boundaries

## Phase Overview

**Phase 1 (MVP)**: Basic UI, OAuth integration, simple pipeline execution
**Phase 2**: Scheduler, multi-channel support, ads mode, metrics dashboard
**Phase 3**: Feedback loops, A/B testing, content scoring, smart recommendations
**Phase 4**: Creator profiles, feed system, public pages
**Phase 5**: Full SaaS with billing, multi-tenant support, microservices

## Running Locally

```bash
docker-compose up -d
# Backend: http://localhost:8000
# Frontend: http://localhost:4200
# API Docs: http://localhost:8000/docs
```

## Important Security Considerations
- Use official APIs only (no browser automation)
- Never store plaintext tokens
- Implement request validation
- Add audit logging for critical operations
- Rate limit API endpoints
