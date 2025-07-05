import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}

def test_read_item_success():
    # First, add an item to test retrieval
    item_data = {"name": "Laptop", "description": "A gaming laptop", "price": 999.99}
    post_response = client.post("/items/", json=item_data)
    assert post_response.status_code == 200

    # Retrieve the added item
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json() == item_data

def test_read_item_not_found():
    response = client.get("/items/999")  # Assuming no item at this index
    assert response.status_code == 200
    assert response.json() == {"error": "Item not found"}

def test_create_item():
    item_data = {"name": "Tablet", "description": "A lightweight tablet", "price": 199.99}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item added successfully",
        "item": item_data,
    }
