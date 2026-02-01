#!/usr/bin/env python3
"""
Real-Time Stress Detection System - FastAPI Backend

This is the backend API service that provides stress detection endpoints.

Privacy Notice:
- All processing happens locally on your device
- No data is transmitted to external servers
- Only feature data (not content) is stored, encrypted with AES-256
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from pydantic import BaseModel

# Configure loguru
logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add("logs/stress_backend.log", rotation="10 MB", retention="7 days")

# Initialize FastAPI app
app = FastAPI(
    title="Stress Detection API",
    version="0.1.0",
    description="Local API for real-time stress detection system",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS middleware for Electron frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:*", "http://127.0.0.1:*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic Models
class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: datetime


class StressScore(BaseModel):
    score: int
    level: str
    confidence: float
    timestamp: datetime
    modules: dict[str, Optional[int]]


class Settings(BaseModel):
    behavioral_enabled: bool = True
    facial_enabled: bool = True
    voice_enabled: bool = True
    notification_threshold: int = 70


# Global state (will be replaced with proper services)
current_stress_score = 0
settings = Settings()


# API Routes
@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        version="0.1.0",
        timestamp=datetime.now()
    )


@app.get("/api/stress/current", response_model=StressScore)
async def get_current_stress():
    """Get current stress score"""
    # Mock data for now - will be replaced with actual ML inference
    return StressScore(
        score=72,
        level="HIGH",
        confidence=0.85,
        timestamp=datetime.now(),
        modules={
            "behavioral": 75,
            "facial": 68,
            "voice": 71
        }
    )


@app.get("/api/settings", response_model=Settings)
async def get_settings():
    """Get user settings"""
    return settings


@app.put("/api/settings", response_model=Settings)
async def update_settings(new_settings: Settings):
    """Update user settings"""
    global settings
    settings = new_settings
    logger.info(f"Settings updated: {settings}")
    return settings


@app.post("/api/baseline/start")
async def start_baseline_calibration():
    """Start baseline calibration process"""
    logger.info("Starting baseline calibration...")
    return {
        "status": "started",
        "estimated_days": 5,
        "message": "Baseline calibration started. Use the app normally for 5 days."
    }


@app.get("/api/baseline/status")
async def get_baseline_status():
    """Get baseline calibration status"""
    return {
        "status": "in_progress",
        "progress": 40,  # 0-100
        "days_completed": 2,
        "days_remaining": 3
    }


# WebSocket for real-time updates
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket client connected. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"WebSocket client disconnected. Total: {len(self.active_connections)}")

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting to client: {e}")


manager = ConnectionManager()


@app.websocket("/ws/stress")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time stress updates"""
    await manager.connect(websocket)
    try:
        while True:
            # Send stress update every 30 seconds
            import asyncio
            await asyncio.sleep(30)

            stress_data = {
                "event": "stress_update",
                "data": {
                    "score": 72,
                    "level": "HIGH",
                    "confidence": 0.85,
                    "timestamp": datetime.now().isoformat(),
                    "modules": {
                        "behavioral": 75,
                        "facial": 68,
                        "voice": 71
                    }
                }
            }
            await websocket.send_json(stress_data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        manager.disconnect(websocket)


@app.on_event("startup")
async def startup_event():
    """Run on app startup"""
    logger.info("=" * 60)
    logger.info("Real-Time Stress Detection Backend v0.1.0")
    logger.info("Privacy-First | Multi-Modal | Local Processing")
    logger.info("API Docs: http://127.0.0.1:8765/api/docs")
    logger.info("=" * 60)


@app.on_event("shutdown")
async def shutdown_event():
    """Run on app shutdown"""
    logger.info("Shutting down Stress Detection Backend...")


def main():
    """Main entry point"""
    # Create logs directory
    Path("logs").mkdir(exist_ok=True)

    # Run server
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8765,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()
