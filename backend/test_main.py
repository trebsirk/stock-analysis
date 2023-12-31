from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_stock():
    response = client.get("/stock/AAPL")
    assert response.status_code == 200
    #assert response.json() == {"Hello": "World"}