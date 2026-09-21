import requests
BASE_URL = "https://dummyjson.com"

def get_first_product():
    print("1️⃣ Логинимся...")
    login_data = {
        "username": "emilys",
        "password": "emilyspass"
    }
    login_response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    token = login_response.json()["accessToken"]
    print("🔑 Токен:", token)
    print(" 2 Токен получен")

    headers = {"Authorization": f"Bearer {token}"}
    products_response = requests.get(f"{BASE_URL}/products", headers=headers)

    assert products_response.status_code == 200
    products = products_response.json()["products"]
    assert len(products)> 0

    first_product=products[0]
    print(f"✔ Название перовго товара: {first_product['title']}")
if __name__ == "__main__":
    get_first_product()
    print("🔁 Код запущен")


