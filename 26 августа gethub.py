import requests

url = "https://dummyjson.com/auth/login"

def test_get_products_with_token():
    login_response = requests.post(
        url,
        json={"username": "emilys", "password": "emilyspass"})

    token = login_response.json()["accessToken"]
    print(token)

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get("https://dummyjson.com/products", headers = headers)

    assert response.status_code == 200
    assert len(response.json()["products"])> 0
