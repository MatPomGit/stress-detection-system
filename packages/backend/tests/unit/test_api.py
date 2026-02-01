"""
Unit tests for API endpoints
"""

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for /api/health endpoint"""

    def test_health_check_returns_200(self):
        """Health check should return 200 OK"""
        response = client.get("/api/health")
        assert response.status_code == 200

    def test_health_check_returns_correct_schema(self):
        """Health check should return expected schema"""
        response = client.get("/api/health")
        data = response.json()

        assert "status" in data
        assert "version" in data
        assert "timestamp" in data
        assert data["status"] == "healthy"
        assert data["version"] == "0.1.0"


class TestStressEndpoint:
    """Tests for /api/stress/* endpoints"""

    def test_get_current_stress_returns_200(self):
        """Stress endpoint should return 200 OK"""
        response = client.get("/api/stress/current")
        assert response.status_code == 200

    def test_get_current_stress_returns_valid_schema(self):
        """Stress endpoint should return valid stress score schema"""
        response = client.get("/api/stress/current")
        data = response.json()

        assert "score" in data
        assert "level" in data
        assert "confidence" in data
        assert "timestamp" in data
        assert "modules" in data

        # Validate types
        assert isinstance(data["score"], int)
        assert isinstance(data["level"], str)
        assert isinstance(data["confidence"], float)
        assert isinstance(data["modules"], dict)

    def test_stress_score_in_valid_range(self):
        """Stress score should be 0-100"""
        response = client.get("/api/stress/current")
        data = response.json()

        assert 0 <= data["score"] <= 100

    def test_stress_level_is_valid(self):
        """Stress level should be one of: LOW, MEDIUM, HIGH, CRITICAL"""
        response = client.get("/api/stress/current")
        data = response.json()

        valid_levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        assert data["level"] in valid_levels

    def test_confidence_in_valid_range(self):
        """Confidence should be 0.0-1.0"""
        response = client.get("/api/stress/current")
        data = response.json()

        assert 0.0 <= data["confidence"] <= 1.0


class TestSettingsEndpoint:
    """Tests for /api/settings endpoint"""

    def test_get_settings_returns_200(self):
        """Settings GET should return 200 OK"""
        response = client.get("/api/settings")
        assert response.status_code == 200

    def test_get_settings_returns_valid_schema(self):
        """Settings should return expected schema"""
        response = client.get("/api/settings")
        data = response.json()

        assert "behavioral_enabled" in data
        assert "facial_enabled" in data
        assert "voice_enabled" in data
        assert "notification_threshold" in data

    def test_update_settings_returns_200(self):
        """Settings PUT should return 200 OK"""
        payload = {
            "behavioral_enabled": True,
            "facial_enabled": False,
            "voice_enabled": True,
            "notification_threshold": 80
        }
        response = client.put("/api/settings", json=payload)
        assert response.status_code == 200

    def test_update_settings_persists(self):
        """Settings should persist after update"""
        # Update settings
        payload = {
            "behavioral_enabled": False,
            "facial_enabled": True,
            "voice_enabled": False,
            "notification_threshold": 65
        }
        client.put("/api/settings", json=payload)

        # Verify settings persisted
        response = client.get("/api/settings")
        data = response.json()

        assert data["behavioral_enabled"] == False
        assert data["facial_enabled"] == True
        assert data["voice_enabled"] == False
        assert data["notification_threshold"] == 65


class TestBaselineEndpoint:
    """Tests for /api/baseline/* endpoints"""

    def test_start_baseline_returns_200(self):
        """Baseline start should return 200 OK"""
        response = client.post("/api/baseline/start")
        assert response.status_code == 200

    def test_baseline_status_returns_200(self):
        """Baseline status should return 200 OK"""
        response = client.get("/api/baseline/status")
        assert response.status_code == 200

    def test_baseline_status_schema(self):
        """Baseline status should return progress information"""
        response = client.get("/api/baseline/status")
        data = response.json()

        assert "status" in data
        assert "progress" in data
        assert 0 <= data["progress"] <= 100


class TestAPIDocumentation:
    """Tests for API documentation endpoints"""

    def test_openapi_docs_accessible(self):
        """OpenAPI docs should be accessible"""
        response = client.get("/api/docs")
        assert response.status_code == 200

    def test_openapi_json_valid(self):
        """OpenAPI JSON schema should be valid"""
        response = client.get("/openapi.json")
        assert response.status_code == 200

        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert "paths" in data
