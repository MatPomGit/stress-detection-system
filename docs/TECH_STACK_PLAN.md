# Technology Stack & Platform Architecture Plan
## Real-Time Stress Detection System

**Version:** 1.0
**Date:** February 2, 2026
**Status:** Planning / Decision Required
**Owner:** Development Team

---

## Table of Contents

1. [Platform Strategy](#1-platform-strategy)
2. [Architecture Overview](#2-architecture-overview)
3. [Backend Technology Stack](#3-backend-technology-stack)
4. [Frontend Technology Stack](#4-frontend-technology-stack)
5. [Communication Layer](#5-communication-layer)
6. [Development Tooling](#6-development-tooling)
7. [Build & Deployment](#7-build--deployment)
8. [Key Technical Decisions](#8-key-technical-decisions)
9. [Implementation Roadmap](#9-implementation-roadmap)
10. [Open Questions](#10-open-questions)

---

## 1. Platform Strategy

### 1.1 Target Platforms (Priority Order)

| Platform | Priority | Rationale | Market Share |
|----------|----------|-----------|--------------|
| **Windows 10/11** | P0 | Largest enterprise market, 65% of dev machines | 65% |
| **macOS 12+** | P0 | Popular in tech/remote work, 30% of dev machines | 30% |
| **Linux (Ubuntu 20.04+)** | P1 | Developer preference, 5% market | 5% |

**Decision**: Cross-platform desktop application (not web, not mobile)

### 1.2 Why Desktop Over Web?

| Factor | Desktop | Web App | Decision |
|--------|---------|---------|----------|
| **OS-level hooks** | ✅ Full access | ❌ Browser sandbox | Desktop wins |
| **Camera/Mic access** | ✅ System APIs | ⚠️ Limited | Desktop wins |
| **Performance** | ✅ Native speed | ⚠️ Browser overhead | Desktop wins |
| **Privacy** | ✅ Truly local | ⚠️ Still needs server | Desktop wins |
| **System monitoring** | ✅ Direct access | ❌ Impossible | Desktop wins |
| **Deployment** | ⚠️ Install required | ✅ Zero install | Web wins |

**Conclusion**: Desktop is the only viable option for privacy-first, system-level monitoring.

### 1.3 Distribution Model

- **Channel**: Direct download from GitHub Releases + website
- **Installer**:
  - Windows: `.exe` (NSIS or Squirrel)
  - macOS: `.dmg` (code-signed, notarized)
  - Linux: `.AppImage` (universal) + `.deb`/`.rpm` (distro-specific)
- **Auto-update**: Electron's `autoUpdater` (Squirrel/electron-updater)
- **Licensing**: MIT (open source)

---

## 2. Architecture Overview

### 2.1 High-Level Architecture Pattern

**Pattern**: **Hybrid Desktop Application** (Electron frontend + Python backend)

```
┌───────────────────────────────────────────────────────────┐
│                    User's Computer (Local)                │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐ │
│  │         Electron Main Process (Node.js)             │ │
│  │  • System tray management                           │ │
│  │  • Window lifecycle                                 │ │
│  │  • Python backend process spawner                   │ │
│  │  • IPC bridge (Renderer ↔ Python)                   │ │
│  └────────────┬────────────────────────────────────────┘ │
│               │                                           │
│               ├──────────────┬────────────────────────┐   │
│               ▼              ▼                        ▼   │
│  ┌──────────────────┐  ┌──────────────┐  ┌──────────────┐│
│  │ Renderer Process │  │ System Tray  │  │ Notification ││
│  │ (React + TS)     │  │    Icon      │  │   Manager    ││
│  │ • Dashboard UI   │  │              │  │              ││
│  │ • Charts         │  └──────────────┘  └──────────────┘│
│  │ • Settings       │                                     │
│  └────────┬─────────┘                                     │
│           │ IPC (electron-ipc)                            │
│           ▼                                               │
│  ┌──────────────────────────────────────────────────────┐│
│  │         Python Backend Service (FastAPI)             ││
│  │  • REST API server (localhost:8765)                  ││
│  │  • WebSocket server (real-time updates)              ││
│  │  • Background workers (threading)                    ││
│  │                                                       ││
│  │  ┌────────────────────────────────────────────────┐ ││
│  │  │         Data Collection Modules                │ ││
│  │  │  • Behavioral (keyboard, mouse, apps)          │ ││
│  │  │  • Facial (MediaPipe, OpenFace)                │ ││
│  │  │  │  Voice (librosa, VAD)                       │ ││
│  │  └────────┬───────────────────────────────────────┘ ││
│  │           ▼                                          ││
│  │  ┌────────────────────────────────────────────────┐ ││
│  │  │         ML Inference Engine                    │ ││
│  │  │  • Feature extraction                          │ ││
│  │  │  • Baseline comparison                         │ ││
│  │  │  • Multi-modal fusion                          │ ││
│  │  └────────┬───────────────────────────────────────┘ ││
│  │           ▼                                          ││
│  │  ┌────────────────────────────────────────────────┐ ││
│  │  │    SQLite Database (AES-256 encrypted)         │ ││
│  │  │  • User profile, baselines, history            │ ││
│  │  └────────────────────────────────────────────────┘ ││
│  └──────────────────────────────────────────────────────┘│
└───────────────────────────────────────────────────────────┘

         │ (One-time, on first launch)
         ▼
┌────────────────────────┐
│  External (Internet)   │
│  • Pre-trained models  │
│  • Software updates    │
└────────────────────────┘
```

### 2.2 Process Architecture

**Multi-process model**:
1. **Electron Main Process** (Node.js) - Orchestrator
   - Spawns Python backend as child process
   - Manages IPC between renderer and Python
   - Handles system tray, notifications

2. **Electron Renderer Process** (Chromium) - UI
   - React app for dashboard
   - Communicates with main process via IPC

3. **Python Backend Process** - Heavy lifting
   - Runs as subprocess (spawned by Electron)
   - Exposes REST API + WebSocket on `localhost:8765`
   - Independent lifecycle (can restart without killing UI)

**Why separate processes?**
- Python crash doesn't kill UI
- UI can show "reconnecting..." if backend fails
- Easier debugging (can test Python API independently)

---

## 3. Backend Technology Stack

### 3.1 Core Stack

| Component | Technology | Version | Rationale |
|-----------|-----------|---------|-----------|
| **Language** | Python | 3.10+ | ML ecosystem, cross-platform |
| **API Framework** | FastAPI | 0.109+ | Async, WebSocket, auto-docs |
| **Web Server** | Uvicorn | 0.27+ | ASGI server for FastAPI |
| **Async Runtime** | asyncio | stdlib | Native Python async |
| **Background Tasks** | Threading | stdlib | For blocking ML inference |

### 3.2 Machine Learning

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **ML Framework** | scikit-learn | 1.3+ | Random Forest, Isolation Forest |
| **Deep Learning** | TensorFlow Lite | 2.13+ | On-device inference (optional) |
| **Computer Vision** | OpenCV | 4.8+ | Video processing |
| **Face Detection** | MediaPipe | 0.10+ | Face mesh (468 landmarks) |
| **Facial AU** | OpenFace (py-feat) | 2.2.0 | Action Unit recognition |
| **Audio Processing** | librosa | 0.10+ | MFCC, pitch extraction |
| **Voice Activity** | webrtcvad | 2.0.10 | Voice activity detection |
| **Audio I/O** | sounddevice | 0.4.6 | Better than PyAudio (cross-platform) |

### 3.3 System Integration

| Platform | Libraries | Purpose |
|----------|-----------|---------|
| **Windows** | pywin32, psutil, pynput | Win32 API, process monitoring, input hooks |
| **macOS** | pyobjc, psutil, pynput | Cocoa, Quartz, input hooks |
| **Linux** | python-xlib, psutil, pynput | X11/Wayland, input hooks |
| **All** | watchdog | File system monitoring |

### 3.4 Data & Security

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Database** | SQLite | 3.40+ | Embedded DB |
| **Encryption** | SQLCipher | 4.5+ | Encrypted SQLite |
| **Crypto** | cryptography | 41.0+ | AES-256, key derivation |
| **Config** | pydantic-settings | 2.0+ | Typed config management |
| **Logging** | loguru | 0.7+ | Structured logging |

### 3.5 Backend Architecture Pattern

**Pattern**: Layered Architecture (Clean Architecture inspired)

```python
src/backend/
├── main.py                    # FastAPI app entry point
├── api/                       # API layer
│   ├── routes/
│   │   ├── stress.py         # GET /api/stress/current
│   │   ├── baseline.py       # POST /api/baseline/calibrate
│   │   ├── settings.py       # GET/PUT /api/settings
│   │   └── history.py        # GET /api/history/{date}
│   └── websocket.py          # WebSocket endpoint
├── services/                  # Business logic
│   ├── stress_monitor.py     # Orchestrates modules
│   ├── baseline_manager.py   # Baseline learning
│   └── alert_manager.py      # Alert decision logic
├── modules/                   # Data collection
│   ├── behavioral/
│   │   ├── keyboard_monitor.py
│   │   ├── mouse_monitor.py
│   │   └── app_monitor.py
│   ├── facial/
│   │   ├── face_detector.py
│   │   ├── au_recognizer.py
│   │   └── eye_tracker.py
│   └── voice/
│       ├── audio_capture.py
│       ├── pitch_analyzer.py
│       └── vad.py
├── ml/                        # ML layer
│   ├── models/               # Saved models
│   ├── inference/
│   │   ├── stress_classifier.py
│   │   ├── anomaly_detector.py
│   │   └── fusion_engine.py
│   └── training/             # Training scripts
├── database/
│   ├── models.py             # SQLAlchemy models
│   ├── crud.py               # Database operations
│   └── migrations/           # Schema migrations (Alembic)
└── utils/
    ├── config.py
    ├── encryption.py
    └── platform_utils.py
```

---

## 4. Frontend Technology Stack

### 4.1 Core Stack

| Component | Technology | Version | Rationale |
|-----------|-----------|---------|-----------|
| **Desktop Framework** | Electron | 28+ | Cross-platform, mature ecosystem |
| **UI Library** | React | 18+ | Component-based, huge ecosystem |
| **Language** | TypeScript | 5.3+ | Type safety, better DX |
| **Build Tool** | Vite | 5+ | Fast HMR, modern bundler |
| **State Management** | Zustand | 4+ | Simpler than Redux, sufficient for this app |
| **API Client** | TanStack Query | 5+ | Data fetching, caching, sync |
| **WebSocket** | Socket.io-client | 4+ | Reliable WebSocket with fallbacks |

### 4.2 UI Components & Styling

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **UI Components** | shadcn/ui | latest | Accessible, customizable (Radix UI) |
| **CSS Framework** | Tailwind CSS | 3+ | Utility-first styling |
| **Charts** | Recharts | 2+ | Composable React charts |
| **Icons** | Lucide React | latest | Modern icon library |
| **Animations** | Framer Motion | 11+ | Smooth UI transitions |

### 4.3 Frontend Architecture Pattern

**Pattern**: Feature-based structure

```
src/frontend/
├── electron/                  # Electron main process
│   ├── main.ts               # Entry point
│   ├── preload.ts            # Context bridge (security)
│   ├── backend-manager.ts    # Python subprocess spawner
│   ├── tray.ts               # System tray
│   └── ipc-handlers.ts       # IPC listeners
├── src/                      # Renderer process (React)
│   ├── main.tsx              # React entry point
│   ├── App.tsx               # Root component
│   ├── features/             # Feature modules
│   │   ├── dashboard/
│   │   │   ├── components/
│   │   │   │   ├── StressGauge.tsx
│   │   │   │   ├── TrendChart.tsx
│   │   │   │   └── QuickStats.tsx
│   │   │   ├── hooks/
│   │   │   │   └── useStressData.ts
│   │   │   └── DashboardPage.tsx
│   │   ├── settings/
│   │   │   ├── components/
│   │   │   ├── SettingsPage.tsx
│   │   │   └── useSettings.ts
│   │   ├── baseline/
│   │   │   └── BaselineCalibrationPage.tsx
│   │   └── history/
│   │       └── HistoryPage.tsx
│   ├── components/           # Shared components
│   │   ├── ui/              # shadcn/ui components
│   │   ├── Layout.tsx
│   │   └── Navigation.tsx
│   ├── lib/                  # Utilities
│   │   ├── api.ts           # API client (axios/fetch)
│   │   ├── websocket.ts     # WebSocket client
│   │   └── utils.ts
│   ├── store/                # Zustand stores
│   │   ├── stressStore.ts
│   │   └── settingsStore.ts
│   └── types/                # TypeScript types
│       ├── stress.ts
│       └── api.ts
├── public/                   # Static assets
└── package.json
```

---

## 5. Communication Layer

### 5.1 Architecture Pattern

**3-Layer Communication**:

```
┌──────────────┐    IPC     ┌──────────────┐   HTTP/WS   ┌──────────────┐
│   Renderer   │ ◄─────────► │ Electron Main│ ◄─────────► │ Python API   │
│   (React)    │  contextBridge │  (Node.js)   │  localhost  │  (FastAPI)   │
└──────────────┘             └──────────────┘             └──────────────┘
```

### 5.2 Communication Protocols

| Layer | Protocol | Use Case | Example |
|-------|----------|----------|---------|
| **Renderer ↔ Main** | IPC (contextBridge) | UI events, file dialogs | `window.electron.openSettings()` |
| **Main ↔ Python** | HTTP REST | Config, history queries | `GET http://localhost:8765/api/stress/current` |
| **Main ↔ Python** | WebSocket | Real-time stress score | `ws://localhost:8765/ws/stress` |

### 5.3 API Design

#### REST Endpoints (FastAPI)

```python
# GET /api/health - Health check
# GET /api/stress/current - Current stress score
# GET /api/stress/history?start=2026-02-01&end=2026-02-02
# POST /api/baseline/start - Start baseline calibration
# GET /api/baseline/status - Calibration progress
# GET /api/settings - Get user settings
# PUT /api/settings - Update settings
# POST /api/modules/behavioral/toggle - Enable/disable module
```

#### WebSocket Events

```typescript
// Server → Client
{
  "event": "stress_update",
  "data": {
    "score": 72,
    "level": "HIGH",
    "confidence": 0.85,
    "timestamp": "2026-02-02T14:30:00Z",
    "modules": {
      "behavioral": 75,
      "facial": 68,
      "voice": 71
    }
  }
}

// Client → Server
{
  "event": "subscribe",
  "data": { "stream": "stress_updates" }
}
```

### 5.4 Python Backend Spawning (Electron Main)

```typescript
// electron/backend-manager.ts
import { spawn } from 'child_process';
import { app } from 'electron';
import path from 'path';

class BackendManager {
  private process: ChildProcess | null = null;

  start() {
    const pythonPath = app.isPackaged
      ? path.join(process.resourcesPath, 'python', 'main.exe')
      : 'python';

    const scriptPath = app.isPackaged
      ? path.join(process.resourcesPath, 'backend', 'main.py')
      : path.join(__dirname, '../../backend/main.py');

    this.process = spawn(pythonPath, [scriptPath], {
      env: { ...process.env, PORT: '8765' }
    });

    this.process.stdout.on('data', (data) => {
      console.log(`[Python] ${data}`);
    });

    this.process.stderr.on('data', (data) => {
      console.error(`[Python Error] ${data}`);
    });
  }

  stop() {
    if (this.process) {
      this.process.kill();
    }
  }
}
```

---

## 6. Development Tooling

### 6.1 Backend Tools

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Poetry** | Dependency management | `pyproject.toml` |
| **pytest** | Testing | `tests/` |
| **black** | Code formatting | 88 char line length |
| **ruff** | Linting | Replaces flake8, isort |
| **mypy** | Type checking | Strict mode |
| **pre-commit** | Git hooks | Run linters before commit |

### 6.2 Frontend Tools

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **pnpm** | Package manager | Faster than npm |
| **Vite** | Build tool | `vite.config.ts` |
| **ESLint** | Linting | Airbnb config |
| **Prettier** | Formatting | 2 spaces, single quotes |
| **TypeScript** | Type checking | Strict mode |
| **Vitest** | Testing | React Testing Library |
| **Playwright** | E2E testing | Cross-platform tests |

### 6.3 Monorepo Structure

**Decision**: Monorepo vs separate repos?

**Recommendation**: **Single monorepo** with workspace structure

```
stress-detection-system/
├── packages/
│   ├── backend/          # Python backend
│   │   ├── pyproject.toml
│   │   └── src/
│   ├── frontend/         # Electron + React
│   │   ├── package.json
│   │   └── src/
│   └── shared/           # Shared types/constants
│       └── types.ts
├── docs/
├── scripts/              # Build scripts
│   ├── build-backend.sh
│   ├── build-frontend.sh
│   └── package.sh       # Create installer
├── .github/
│   └── workflows/
│       └── ci.yml
└── package.json         # Root workspace
```

**Root package.json**:
```json
{
  "private": true,
  "workspaces": ["packages/*"],
  "scripts": {
    "dev:backend": "cd packages/backend && poetry run python main.py",
    "dev:frontend": "cd packages/frontend && pnpm dev",
    "dev": "concurrently \"pnpm dev:backend\" \"pnpm dev:frontend\"",
    "build": "pnpm build:backend && pnpm build:frontend",
    "test": "pnpm test:backend && pnpm test:frontend"
  }
}
```

---

## 7. Build & Deployment

### 7.1 Development Workflow

```bash
# 1. Clone and setup
git clone <repo>
cd stress-detection-system

# 2. Install dependencies
pnpm install           # Installs all workspaces
cd packages/backend && poetry install

# 3. Run in dev mode
pnpm dev              # Starts both backend + frontend
```

### 7.2 Production Build Process

**Backend Packaging**:
- Use **PyInstaller** to bundle Python + dependencies into standalone executable
- Include pre-trained models in bundle
- Result: `backend.exe` (Windows), `backend.app` (macOS), `backend` (Linux)

**Frontend Packaging**:
- Use **electron-builder** to create installers
- Bundle backend executable inside Electron app
- Code signing (macOS: Developer ID, Windows: authenticode)

**Build steps**:
```bash
# 1. Build Python backend
cd packages/backend
poetry run pyinstaller main.spec  # Creates dist/backend

# 2. Build Electron app
cd packages/frontend
pnpm build                        # Vite build
pnpm electron-builder            # Creates installer

# 3. Package includes:
#    - Electron app
#    - Python backend (embedded in resources/)
#    - Pre-trained models
#    - SQLite database schema
```

### 7.3 CI/CD Pipeline

**GitHub Actions workflow**:
```yaml
name: Build & Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - Setup Python, Node, Poetry, pnpm
      - Build backend with PyInstaller
      - Build Electron app with electron-builder
      - Upload .exe installer

  build-macos:
    runs-on: macos-latest
    steps:
      - Same as above
      - Code sign with Developer ID
      - Notarize with Apple
      - Upload .dmg

  build-linux:
    runs-on: ubuntu-latest
    steps:
      - Same as above
      - Upload .AppImage, .deb, .rpm

  release:
    needs: [build-windows, build-macos, build-linux]
    steps:
      - Create GitHub Release
      - Upload all installers
      - Generate release notes
```

---

## 8. Key Technical Decisions

### Decision Matrix

| Decision | Options Considered | Choice | Rationale |
|----------|-------------------|--------|-----------|
| **Desktop Framework** | Electron, Tauri, Qt | **Electron** | Mature, proven, easier React integration |
| **Backend Language** | Python, Rust, Go | **Python** | ML ecosystem, faster development |
| **API Framework** | Flask, FastAPI, Django | **FastAPI** | Async, WebSocket, auto-docs |
| **State Management** | Redux, Zustand, Jotai | **Zustand** | Simpler, sufficient for this app |
| **Build Tool** | Webpack, Vite, Rollup | **Vite** | Faster HMR, modern |
| **Package Manager** | npm, yarn, pnpm | **pnpm** | Faster, disk-efficient |
| **Python Packaging** | pip, conda, poetry | **Poetry** | Modern, lockfile, better DX |
| **Database** | SQLite, PostgreSQL | **SQLite + SQLCipher** | Embedded, no server, encrypted |
| **Testing** | Jest, Vitest | **Vitest** | Native Vite integration |
| **Monorepo** | Yes, No | **Yes** | Easier versioning, shared configs |

### Decision: Why Electron over Tauri?

| Factor | Electron | Tauri | Winner |
|--------|----------|-------|--------|
| Maturity | ✅ 10+ years | ⚠️ 3 years | Electron |
| Ecosystem | ✅ Huge | ⚠️ Growing | Electron |
| Bundle size | ❌ 150 MB | ✅ 15 MB | Tauri |
| Memory | ❌ Heavy | ✅ Light | Tauri |
| Development speed | ✅ Fast | ⚠️ Learning curve | Electron |
| Python integration | ✅ Easy subprocess | ✅ Easy | Tie |
| Risk | ✅ Low | ⚠️ Medium | Electron |

**Verdict**: Electron for v1.0, consider Tauri for v2.0 rewrite if bundle size becomes issue.

---

## 9. Implementation Roadmap

### Phase 1: Foundation (Week 1-2)

**Backend**:
- [ ] Set up Poetry project structure
- [ ] Create FastAPI skeleton with health endpoint
- [ ] Set up SQLite database with SQLAlchemy models
- [ ] Implement basic logging (loguru)

**Frontend**:
- [ ] Set up Electron + Vite + React + TypeScript
- [ ] Configure IPC bridge (preload script)
- [ ] Create basic system tray + main window
- [ ] Set up Zustand store

**Integration**:
- [ ] Backend spawning from Electron main process
- [ ] Health check endpoint integration
- [ ] WebSocket connection test

### Phase 2: Behavioral Module (Week 3-5)

**Backend**:
- [ ] Keyboard monitoring (pynput)
- [ ] Mouse monitoring
- [ ] Application tracking (psutil)
- [ ] Idle time detection
- [ ] Basic feature extraction

**Frontend**:
- [ ] Dashboard page scaffold
- [ ] Real-time stats display
- [ ] Settings page for module toggles

### Phase 3: ML & Baseline (Week 6-8)

**Backend**:
- [ ] Baseline learning algorithm
- [ ] Anomaly detection (Isolation Forest)
- [ ] Stress classifier (Random Forest)
- [ ] Multi-modal fusion engine

**Frontend**:
- [ ] Baseline calibration wizard
- [ ] Stress gauge visualization
- [ ] Trend charts (Recharts)

### Phase 4: Facial & Voice (Week 9-12)

**Backend**:
- [ ] MediaPipe face detection
- [ ] OpenFace AU recognition
- [ ] Audio capture (sounddevice)
- [ ] Voice feature extraction (librosa)

**Frontend**:
- [ ] Video call detection UI
- [ ] Module status indicators

### Phase 5: Polish & Package (Week 13-14)

**Backend**:
- [ ] PyInstaller build config
- [ ] Pre-trained model bundling

**Frontend**:
- [ ] electron-builder config
- [ ] Auto-updater integration
- [ ] Code signing setup

**CI/CD**:
- [ ] GitHub Actions workflows
- [ ] Automated releases

---

## 10. Open Questions

### Questions Requiring Decision

1. **Backend Packaging**: PyInstaller vs Nuitka for Python bundling?
   - PyInstaller: Easier, more compatible
   - Nuitka: Faster runtime, smaller bundle

2. **API Security**: How to secure localhost API from malicious apps on user's machine?
   - Option A: Random token on startup (shared via file)
   - Option B: No auth (assume localhost is safe)
   - **Recommendation**: Random token for defense-in-depth

3. **Crash Reporting**: Should we use Sentry or similar?
   - Pros: Better bug reports
   - Cons: Privacy concerns (send crash data?)
   - **Recommendation**: Optional, opt-in only

4. **ML Model Updates**: How to ship model updates without full app update?
   - Option A: Separate download on startup
   - Option B: Bundle in app (larger download)
   - **Recommendation**: Bundle in app for simplicity

5. **Database Location**: Where to store SQLite file?
   - Windows: `%APPDATA%/StressDetector/data.db`
   - macOS: `~/Library/Application Support/StressDetector/data.db`
   - Linux: `~/.local/share/stressdetector/data.db`

6. **Feature Flags**: Do we need feature flag system for gradual rollout?
   - **Recommendation**: Not for v1.0, add in v1.1

---

## Next Steps

### Immediate Actions

1. **Review this document** with team for alignment
2. **Create `pyproject.toml`** for backend with Poetry
3. **Create `package.json`** for frontend with pnpm workspace
4. **Set up project structure** (monorepo with packages/)
5. **Prototype IPC communication** (Electron ↔ Python)
6. **Create ADR** (Architecture Decision Record) for major choices

### Deliverables

- [ ] Updated `requirements.txt` → `pyproject.toml`
- [ ] New `packages/frontend/package.json`
- [ ] Root `package.json` with workspaces
- [ ] `electron/main.ts` with backend spawning
- [ ] `backend/main.py` with FastAPI + WebSocket
- [ ] Initial CI/CD pipeline

---

**Status**: Awaiting stakeholder approval to proceed with implementation.
