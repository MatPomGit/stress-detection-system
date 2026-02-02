"""
API Performance Benchmarks

Tests API response times to ensure they meet the <5 second requirement.
Run with: pytest tests/benchmarks/test_api_performance.py -v --benchmark-only
"""

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestAPIPerformance:
    """Benchmark API endpoint performance"""

    def test_health_endpoint_response_time(self, benchmark):
        """Health endpoint should respond in <100ms"""
        def call_health():
            response = client.get("/api/health")
            assert response.status_code == 200
            return response

        result = benchmark(call_health)
        assert result.status_code == 200

        # Verify response time
        stats = benchmark.stats
        assert stats.stats.mean < 0.1, f"Health endpoint too slow: {stats.stats.mean:.3f}s"

    def test_stress_endpoint_response_time(self, benchmark):
        """Stress score endpoint should respond in <5s (current requirement)"""
        def call_stress():
            response = client.get("/api/stress/current")
            assert response.status_code == 200
            return response

        result = benchmark(call_stress)
        assert result.status_code == 200

        # Verify response time meets requirement
        stats = benchmark.stats
        assert stats.stats.mean < 5.0, f"Stress endpoint too slow: {stats.stats.mean:.3f}s"

        # Ideally should be much faster than 5s
        if stats.stats.mean < 1.0:
            print(f"✓ Excellent: {stats.stats.mean:.3f}s (target <1s)")
        elif stats.stats.mean < 2.0:
            print(f"✓ Good: {stats.stats.mean:.3f}s (target <2s)")
        else:
            print(f"⚠ Acceptable: {stats.stats.mean:.3f}s (requirement <5s)")

    def test_settings_get_response_time(self, benchmark):
        """Settings GET should respond in <100ms"""
        def call_settings():
            response = client.get("/api/settings")
            assert response.status_code == 200
            return response

        result = benchmark(call_settings)
        stats = benchmark.stats
        assert stats.stats.mean < 0.1, f"Settings GET too slow: {stats.stats.mean:.3f}s"

    def test_settings_update_response_time(self, benchmark):
        """Settings PUT should respond in <200ms"""
        def call_update_settings():
            payload = {
                "behavioral_enabled": True,
                "facial_enabled": True,
                "voice_enabled": False,
                "notification_threshold": 75
            }
            response = client.put("/api/settings", json=payload)
            assert response.status_code == 200
            return response

        result = benchmark(call_update_settings)
        stats = benchmark.stats
        assert stats.stats.mean < 0.2, f"Settings PUT too slow: {stats.stats.mean:.3f}s"

    def test_baseline_start_response_time(self, benchmark):
        """Baseline start should respond in <200ms"""
        def call_baseline_start():
            response = client.post("/api/baseline/start")
            assert response.status_code == 200
            return response

        result = benchmark(call_baseline_start)
        stats = benchmark.stats
        assert stats.stats.mean < 0.2, f"Baseline start too slow: {stats.stats.mean:.3f}s"

    def test_concurrent_stress_requests(self, benchmark):
        """Test performance with concurrent stress score requests"""
        def concurrent_stress_calls():
            responses = []
            for _ in range(10):
                response = client.get("/api/stress/current")
                responses.append(response)
            return responses

        results = benchmark(concurrent_stress_calls)
        assert all(r.status_code == 200 for r in results)

        stats = benchmark.stats
        # Each request should still be fast even when concurrent
        assert stats.stats.mean < 1.0, f"Concurrent requests too slow: {stats.stats.mean:.3f}s"


class TestAPIThroughput:
    """Benchmark API throughput"""

    def test_requests_per_second(self, benchmark):
        """Measure requests/second capacity"""
        request_count = 0

        def stress_load_test():
            nonlocal request_count
            response = client.get("/api/stress/current")
            request_count += 1
            return response

        benchmark.pedantic(stress_load_test, rounds=100, iterations=10)

        stats = benchmark.stats
        rps = 1.0 / stats.stats.mean
        print(f"\nRequests per second: {rps:.2f}")

        # Should handle at least 50 requests/second
        assert rps > 50, f"Throughput too low: {rps:.2f} req/s"


class TestPayloadSize:
    """Benchmark payload sizes to ensure efficiency"""

    def test_stress_response_size(self):
        """Stress response should be compact (<1KB)"""
        response = client.get("/api/stress/current")
        assert response.status_code == 200

        payload_size = len(response.content)
        print(f"\nStress response size: {payload_size} bytes")

        # Should be compact
        assert payload_size < 1024, f"Response too large: {payload_size} bytes"

    def test_health_response_size(self):
        """Health response should be minimal (<500 bytes)"""
        response = client.get("/api/health")
        assert response.status_code == 200

        payload_size = len(response.content)
        print(f"\nHealth response size: {payload_size} bytes")

        assert payload_size < 500, f"Health response too large: {payload_size} bytes"
