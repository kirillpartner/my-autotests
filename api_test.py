import requests
BASE_URL = "https://dummyjson.com"

def test_successful_login():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "emilys",
        "password": "emilyspass"
    })
    assert response.status_code == 200, '❌ Логин не удался'

    data = response.json()
    assert "accessToken" in data, "❌ Нет accessToken"
    assert "refreshToken" in data, "❌ Нет refreshToken"

    print("✔ Тест1: Успешный логин работает")

def test_failed_login():
    response = requests.post(f"{BASE_URL}/auth/login",json={
            "username": "emilys",
            "password": "wrongpassword"
        })
    assert response.status_code == 400, "❌сервер должен вернуть 400"
    print("✔ Тест 2: Неудачный логин обработан правильно")
def test_access_without_token():
    response = requests.get(f"{BASE_URL}/auth/me")
    assert response.status_code == 401, "❌ Доступ разрешен без токена"
    print(" ✔ тест 3: Доуступ без токена запрещен")
def test_access_with_token():
    login_response = requests.post(f"{BASE_URL}/auth/login",json={
        "username": "emilys",
        "password": "emilyspass"
    })
    token = login_response.json()["accessToken"]
    headers = {"Authorization":f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
    assert response.status_code == 200, "❌Данные пользователя не совпадают"
    print("✔ Тест 4: Доступ с токеном работает")

if __name__ == "__main__":
    print("🚀 ЗАПУСК АВТОТЕСТОВ")
    print("=" * 40)
    test_successful_login()
    test_failed_login()
    test_access_without_token()
    test_access_with_token()
    print("✔ Все автотесты пройдены!")
