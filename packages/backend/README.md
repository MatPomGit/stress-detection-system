# Stress Detection Backend

FastAPI-based backend service for real-time stress detection system.

## Features

- **FastAPI REST API** with automatic OpenAPI docs
- **WebSocket** support for real-time stress updates
- **Privacy-first** - all processing local, no external transmission
- **Performance optimized** - <5s response time, <10% CPU usage

## Quick Start

### Prerequisites

- Python 3.10+
- Poetry for dependency management

### Installation

```bash
# Install dependencies
poetry install

# Run development server
poetry run python src/main.py
```

The API will be available at:
- **API**: http://127.0.0.1:8765
- **Docs**: http://127.0.0.1:8765/api/docs
- **WebSocket**: ws://127.0.0.1:8765/ws/stress

## API Endpoints

### Health Check
```bash
GET /api/health
```

### Stress Detection
```bash
# Get current stress score
GET /api/stress/current

# Response
{
  "score": 72,
  "level": "HIGH",
  "confidence": 0.85,
  "timestamp": "2026-02-02T10:30:00",
  "modules": {
    "behavioral": 75,
    "facial": 68,
    "voice": 71
  }
}
```

### Settings
```bash
# Get settings
GET /api/settings

# Update settings
PUT /api/settings
{
  "behavioral_enabled": true,
  "facial_enabled": true,
  "voice_enabled": true,
  "notification_threshold": 70
}
```

### Baseline Calibration
```bash
# Start calibration
POST /api/baseline/start

# Check status
GET /api/baseline/status
```

## Development

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run unit tests only
poetry run pytest tests/unit/

# Run benchmarks
poetry run pytest tests/benchmarks/ -v --benchmark-only

# Run with coverage
poetry run pytest --cov=src --cov-report=html
```

### Code Quality

```bash
# Format code
poetry run black src/ tests/

# Lint code
poetry run ruff src/ tests/

# Type checking
poetry run mypy src/
```

## Benchmarks

Performance targets:
- **API Response Time**: <5 seconds (requirement), <1 second (target)
- **CPU Usage**: <10% average
- **Memory**: <500 MB
- **Throughput**: >50 requests/second

Run benchmarks:
```bash
poetry run pytest tests/benchmarks/ -v --benchmark-only
```

## Project Structure

```
packages/backend/
├── src/
│   ├── main.py              # FastAPI application
│   ├── api/                 # API routes
│   ├── services/            # Business logic
│   ├── modules/             # Stress detection modules
│   ├── ml/                  # ML models & inference
│   ├── database/            # Database models & CRUD
│   └── utils/               # Utilities
├── tests/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── benchmarks/          # Performance benchmarks
├── pyproject.toml           # Poetry configuration
└── README.md                # This file
```

## Environment Variables

Create `.env` file:
```bash
# API Configuration
API_HOST=127.0.0.1
API_PORT=8765

# Database
DATABASE_PATH=~/.local/share/stressdetector/data.db

# Logging
LOG_LEVEL=INFO
```

## License

MIT License - see LICENSE file for details.
