# AutoContent Backend

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create .env file:
```bash
cp .env.example .env
```

3. Initialize database:
```bash
python -c "from app.core.database import init_db; init_db()"
```

4. Run server:
```bash
uvicorn main:app --reload
```

API available at: http://localhost:8000
API Docs: http://localhost:8000/docs

## API Endpoints (Phase 1)

### Channels
- `POST /api/v1/channels` - Create channel
- `GET /api/v1/channels` - List all channels
- `GET /api/v1/channels/{id}` - Get channel details
- `PATCH /api/v1/channels/{id}` - Update channel
- `DELETE /api/v1/channels/{id}` - Delete channel

### Pipeline
- `POST /api/v1/pipeline/run` - Run content pipeline
- `GET /api/v1/pipeline/{id}` - Get pipeline status

### Logs
- `GET /api/v1/logs/{pipeline_id}` - Get pipeline logs

### Auth
- `POST /api/v1/auth/youtube/init` - Initialize YouTube OAuth
- `POST /api/v1/auth/youtube/callback` - Handle OAuth callback

## Architecture

```
app/
├── core/           # Config, database, app setup
├── api/            # Route handlers
├── models/         # SQLAlchemy ORM models
├── schemas/        # Pydantic request/response schemas
├── services/       # Business logic
└── utils/          # Helper functions
```

## Phase Roadmap

- **Phase 1**: Basic UI, OAuth, simple pipeline
- **Phase 2**: Scheduler, multi-channel, ads mode
- **Phase 3**: ML feedback, scoring, recommendations
- **Phase 4**: Creator profiles, feed
- **Phase 5**: SaaS, billing, multi-tenant
