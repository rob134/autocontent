# AutoContent Development Guide

## Architecture Overview

### Clean Code Principles
- **Single Responsibility**: Each module has one reason to change
- **DRY**: Don't Repeat Yourself
- **SOLID Principles**: Applied throughout
- **Type Safety**: Use type hints everywhere

### Design Patterns Used

#### 1. Strategy Pattern (Pipeline)
Different content generation modes:
```python
class ContentStrategy(ABC):
    async def generate(self, **kwargs): pass

class CuratedStrategy(ContentStrategy): ...
class AvatarStrategy(ContentStrategy): ...
class AdsStrategy(ContentStrategy): ...
```

#### 2. Factory Pattern
```python
strategy = StrategyFactory.get_strategy("curated")
```

#### 3. Service Pattern
Business logic separation:
```python
class ChannelService:
    def create_channel(self, ...): ...
    def list_channels(self): ...
```

#### 4. Dependency Injection
```python
@router.get("/")
def get_channels(db: Session = Depends(get_db)):
    ...
```

## File Structure Best Practices

### Backend
```
backend/
├── app/
│   ├── core/           # Application setup & config
│   │   ├── __init__.py
│   │   ├── app.py      # FastAPI app factory
│   │   ├── config.py   # Settings
│   │   └── database.py # DB setup
│   ├── api/            # Route handlers
│   │   ├── channels.py
│   │   ├── pipeline.py
│   │   └── ...
│   ├── models/         # SQLAlchemy ORM
│   │   └── models.py
│   ├── schemas/        # Pydantic validation
│   │   └── base.py
│   ├── services/       # Business logic
│   │   ├── channel.py
│   │   ├── pipeline.py
│   │   └── ...
│   └── utils/          # Helpers
├── main.py             # Entry point
├── requirements.txt
└── README.md
```

### Frontend
```
frontend/
├── src/
│   ├── app/
│   │   ├── app.module.ts
│   │   ├── components/
│   │   │   ├── dashboard/
│   │   │   ├── channel-list/
│   │   │   └── ...
│   │   ├── services/
│   │   │   ├── channel.service.ts
│   │   │   └── pipeline.service.ts
│   │   └── models/
│   │       └── types.ts
│   ├── main.ts
│   ├── index.html
│   └── styles.css
├── angular.json
├── package.json
└── README.md
```

## Coding Standards

### Python (Backend)

**Type Hints**
```python
from typing import Optional, List, Dict, Any

async def create_channel(
    db: Session,
    name: str,
    platform: str
) -> Channel:
    ...
```

**Error Handling**
```python
try:
    # Do something
except ValueError as e:
    logger.error(f"Invalid value: {str(e)}")
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")
    raise HTTPException(status_code=500, detail="Internal error")
```

**Async/Await**
```python
async def process_video(url: str) -> str:
    result = await download_video(url)
    return result
```

### TypeScript (Frontend)

**Type Safety**
```typescript
interface Channel {
  id: number;
  name: string;
  platform: string;
}

channels: Channel[] = [];
```

**RxJS Observables**
```typescript
listChannels(): Observable<Channel[]> {
  return this.http.get<Channel[]>(this.apiUrl);
}

// Usage
this.channelService.listChannels().subscribe(
  (channels) => this.channels = channels,
  (error) => console.error(error)
);
```

## Testing Strategy

### Backend (pytest)
```python
import pytest
from fastapi.testclient import TestClient

def test_create_channel(client: TestClient):
    response = client.post(
        "/api/v1/channels",
        json={"name": "Test", "platform": "youtube"}
    )
    assert response.status_code == 200
```

### Frontend (Jasmine)
```typescript
describe('ChannelService', () => {
  it('should get channels', () => {
    service.listChannels().subscribe(channels => {
      expect(channels.length).toBe(1);
    });
  });
});
```

## Database Migrations

### Using Alembic (Future)
```bash
# Create migration
alembic revision --autogenerate -m "Add field to channel"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Logging Strategy

### Backend
```python
import logging

logger = logging.getLogger(__name__)

logger.info("Channel created successfully")
logger.warning("Low disk space")
logger.error("Failed to upload video", exc_info=True)
```

### Frontend
```typescript
export class LoggerService {
  log(message: string): void {
    console.log(`[${new Date().toISOString()}] ${message}`);
  }
}
```

## Performance Considerations

### Database
- Add indexes for frequently queried fields
- Use pagination for large result sets
- Implement caching strategies

### API
- Implement rate limiting
- Compress responses
- Use pagination
- Add request validation early

### Frontend
- Lazy load components
- Use Change Detection strategy (OnPush)
- Implement virtual scrolling for large lists
- Optimize bundle size

## Security Best Practices

### Backend
- Validate all inputs with Pydantic
- Use HTTPS in production
- Implement CSRF protection
- Sanitize database queries (SQLAlchemy handles this)
- Rate limit endpoints
- Add request timeout

### Frontend
- Never store secrets in code
- Sanitize user input
- Implement CORS correctly
- Use secure headers
- Validate API responses

### Tokens & Secrets
- Always encrypt stored tokens
- Use environment variables
- Rotate keys regularly
- Never commit secrets

## Module Development Checklist

When creating a new module:

- [ ] Create module directory with `__init__.py`
- [ ] Implement core functionality
- [ ] Add type hints
- [ ] Write docstrings
- [ ] Add error handling
- [ ] Add logging
- [ ] Create unit tests
- [ ] Update README
- [ ] Add to imports
- [ ] Document API endpoints (if backend)
- [ ] Create UI component (if frontend)

## Common Patterns

### Async Service
```python
class MyService:
    async def do_work(self) -> Result:
        data = await fetch_data()
        processed = await process_data(data)
        return Result(processed)
```

### API Endpoint
```python
@router.post("/action")
async def perform_action(
    request: ActionRequest,
    db: Session = Depends(get_db)
) -> ActionResponse:
    service = MyService(db)
    result = await service.do_action(request)
    return result
```

### Component Service
```typescript
@Injectable()
export class MyService {
  constructor(private http: HttpClient) {}

  doAction(data: Data): Observable<Result> {
    return this.http.post<Result>(`${this.apiUrl}/action`, data);
  }
}
```

## Deployment Phases

### Phase 1 (Current)
- Docker local development
- SQLite database
- Basic API
- Simple UI

### Phase 2-5 (Future)
- PostgreSQL migration
- Redis caching
- Load balancing
- Auto-scaling
- Microservices
- Multi-tenant support

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Angular Documentation](https://angular.io/docs)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Pydantic Validation](https://docs.pydantic.dev/)
- [Docker Best Practices](https://docs.docker.com/)

## Support & Questions

1. Check module README files
2. Review existing code patterns
3. Consult architecture documentation
4. Open GitHub discussion

---

**Remember**: Write code for humans first, computers second.
