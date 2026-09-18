from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_quote():
    response = client.post(
        "/quotes",
        params={
            "unit_price": 100,
            "quantity": 3,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 300