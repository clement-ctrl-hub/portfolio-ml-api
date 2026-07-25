import os

import httpx
import pytest


pytestmark = pytest.mark.integration

API_BASE_URL = os.getenv("API_BASE_URL")

if not API_BASE_URL:
    pytest.skip(
        "La variable API_BASE_URL n'est pas définie.",
        allow_module_level=True,
    )


def test_health_production():
    response = httpx.get(
        f"{API_BASE_URL}/health",
        timeout=30.0,
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "model_loaded": True,
    }


def test_prediction_production():
    payload = {
        "MedInc": 8.3,
        "HouseAge": 41,
        "AveRooms": 6.9,
        "AveBedrms": 1.0,
        "Population": 322,
        "AveOccup": 2.5,
        "Latitude": 37.88,
        "Longitude": -122.23,
    }

    response = httpx.post(
        f"{API_BASE_URL}/predict",
        json=payload,
        timeout=30.0,
    )

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert isinstance(result["prediction"], float)