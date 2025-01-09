from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"massage": "call /search or /wiki"}


def test_read_wiki():
    response = client.get("/wiki/taiwan")
    assert response.status_code == 200
    assert response.json() == {
        "massage": "Taiwan, officially the Republic of China (ROC), is a country in East Asia."
    }
