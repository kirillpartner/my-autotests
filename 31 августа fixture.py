import pytest
import requests

BASE_URL = "https://dummyjson.com"

@pytest.fixture
def token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys", "password": "emilyspass"})
    return response.json()["accessToken"]

def test_auth_me(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)

    assert response.status_code == 200
    assert response.json()["username"] == "emilys"

def test_products_with_token(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/products", headers=headers)

    assert response.status_code == 200
    assert len(response.json()["products"]) > 0