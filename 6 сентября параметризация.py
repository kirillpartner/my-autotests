import pytest
import requests

BASE_URL = "https://dummyjson.com"

@pytest.fixture
def token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys", "password": "emilyspass"}
    )
    return response.json()["accessToken"]


@pytest.mark.parametrize("username,password",[
    ("emilys", "emilyspass"),
    ("michaelw", "michaelwpass"),

])
def test_login_success(username, password):
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": username, "password": password}
    )
    assert response.status_code == 200




