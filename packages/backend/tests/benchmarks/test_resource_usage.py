"""
Resource Usage Benchmarks

Tests CPU and memory usage to ensure they meet requirements:
- CPU usage: <10% average
- Memory footprint: <500 MB

Run with: pytest tests/benchmarks/test_resource_usage.py -v --benchmark-only
"""

import pytest
import psutil
import time
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestResourceUsage:
    """Benchmark CPU and memory usage"""

    def test_idle_cpu_usage(self):
        """Test CPU usage when backend is idle"""
        process = psutil.Process()

        # Warm up
        for _ in range(5):
            client.get("/api/health")

        # Measure CPU usage over 5 seconds
        cpu_samples = []
        for _ in range(10):
            cpu_percent = process.cpu_percent(interval=0.5)
            cpu_samples.append(cpu_percent)

        avg_cpu = sum(cpu_samples) / len(cpu_samples)
        max_cpu = max(cpu_samples)

        print(f"\nIdle CPU Usage:")
        print(f"  Average: {avg_cpu:.2f}%")
        print(f"  Maximum: {max_cpu:.2f}%")

        # Should use minimal CPU when idle
        assert avg_cpu < 5.0, f"Idle CPU too high: {avg_cpu:.2f}%"

    def test_load_cpu_usage(self):
        """Test CPU usage under load"""
        process = psutil.Process()

        cpu_samples = []

        def simulate_load():
            # Simulate 30 seconds of API calls
            for _ in range(30):
                client.get("/api/stress/current")
                time.sleep(1)
                cpu_percent = process.cpu_percent(interval=0.1)
                cpu_samples.append(cpu_percent)

        simulate_load()

        avg_cpu = sum(cpu_samples) / len(cpu_samples)
        max_cpu = max(cpu_samples)

        print(f"\nLoad CPU Usage:")
        print(f"  Average: {avg_cpu:.2f}%")
        print(f"  Maximum: {max_cpu:.2f}%")

        # Requirement: <10% average
        assert avg_cpu < 10.0, f"Average CPU too high: {avg_cpu:.2f}%"

        # Max spikes acceptable, but not sustained
        if max_cpu > 20.0:
            print(f"  ⚠ Warning: Max CPU spike {max_cpu:.2f}%")

    def test_memory_footprint(self):
        """Test memory usage"""
        process = psutil.Process()

        # Warm up
        for _ in range(10):
            client.get("/api/stress/current")

        # Get memory info
        mem_info = process.memory_info()
        mem_mb = mem_info.rss / 1024 / 1024  # Convert to MB

        print(f"\nMemory Footprint:")
        print(f"  RSS: {mem_mb:.2f} MB")

        # Requirement: <500 MB
        assert mem_mb < 500.0, f"Memory usage too high: {mem_mb:.2f} MB"

        # Ideally should be much lower for FastAPI skeleton
        if mem_mb < 100:
            print(f"  ✓ Excellent: <100 MB")
        elif mem_mb < 200:
            print(f"  ✓ Good: <200 MB")
        else:
            print(f"  ⚠ Acceptable: {mem_mb:.2f} MB (requirement <500 MB)")

    def test_memory_leak(self):
        """Test for memory leaks over sustained load"""
        process = psutil.Process()

        # Baseline memory
        initial_mem = process.memory_info().rss / 1024 / 1024

        # Run 100 requests and check memory growth
        for _ in range(100):
            client.get("/api/stress/current")

        final_mem = process.memory_info().rss / 1024 / 1024
        mem_growth = final_mem - initial_mem

        print(f"\nMemory Leak Test:")
        print(f"  Initial: {initial_mem:.2f} MB")
        print(f"  Final: {final_mem:.2f} MB")
        print(f"  Growth: {mem_growth:.2f} MB")

        # Should not grow significantly
        assert mem_growth < 50.0, f"Possible memory leak: {mem_growth:.2f} MB growth"


class TestStartupPerformance:
    """Benchmark startup time"""

    def test_api_startup_time(self):
        """Measure time to first successful response"""
        import subprocess
        import requests
        import time

        # Note: This is a simplified test. In real scenario, we'd spawn
        # a separate process and measure startup time.

        start_time = time.time()

        # API should respond quickly
        max_attempts = 10
        for attempt in range(max_attempts):
            try:
                response = client.get("/api/health")
                if response.status_code == 200:
                    startup_time = time.time() - start_time
                    print(f"\nAPI Ready in: {startup_time:.3f}s")
                    assert startup_time < 5.0, f"Startup too slow: {startup_time:.3f}s"
                    return
            except Exception:
                time.sleep(0.5)

        pytest.fail("API failed to start")
