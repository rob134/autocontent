# AutoContent Frontend

Angular-based UI for the AutoContent platform.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm start
```

Frontend available at: http://localhost:4200

## Components

- **Dashboard**: Main UI component organizing all features
- **Channel List**: Display connected social media channels
- **Channel Form**: Create new channels
- **Pipeline Runner**: Execute content generation pipeline
- **Logs Viewer**: Real-time pipeline execution logs

## Architecture

```
src/
├── app/
│   ├── components/      # Reusable UI components
│   ├── services/        # API communication services
│   ├── models/          # TypeScript interfaces
│   └── app.module.ts    # Module configuration
└── styles.css           # Global styles
```

## Services

- `ChannelService`: Manage channels via API
- `PipelineService`: Execute and monitor pipelines

## Features (Phase 1)

- ✅ Create channels
- ✅ List active channels
- ✅ Run content pipeline
- ✅ View real-time logs
- ⏳ OAuth integration (UI placeholder)
- ⏳ Multi-language support
