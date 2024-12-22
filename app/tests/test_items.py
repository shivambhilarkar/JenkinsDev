import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Sample API"}

def test_create_item():
    item_data = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 10.99
    }
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 201
    assert response.json()["name"] == item_data["name"]
    assert response.json()["id"] == 1

def test_get_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item():
    # First create an item
    item_data = {
        "name": "Test Item 2",
        "description": "Test Description 2",
        "price": 20.99
    }
    create_response = client.post("/api/v1/items/", json=item_data)
    item_id = create_response.json()["id"]

    # Then get the item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == item_data["name"]

def test_get_nonexistent_item():
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404 