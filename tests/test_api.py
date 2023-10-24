from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get(
        "/health-check",
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["status"] == "ok"


def test_echo_user() -> None:
    response = client.get(
        "/user/jojo",
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "jojo"
