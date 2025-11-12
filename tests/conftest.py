"""Pytest configuration and shared fixtures for PyAndroid tests."""

import pytest
import logging


@pytest.fixture(autouse=True)
def configure_logging():
    """Configure logging for tests."""
    # Reduce log output during tests
    logging.getLogger("PyAndroid").setLevel(logging.WARNING)


@pytest.fixture
def mock_kivy_available(monkeypatch):
    """Mock Kivy availability for testing GUI features."""
    # This fixture can be used in tests that need to mock Kivy
    pass
