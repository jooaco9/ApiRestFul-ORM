from fastapi.testclient import TestClient
from api import app

# Generamos el test de cliente
client = TestClient(app)

# Test del endpoint GET /categories
def test_read_categories():
    response = client.get("/categories/")
    print(response.json())

    assert response.status_code == 200
    assert len(response.json()) > 0
