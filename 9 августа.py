import requests

BASE_URL = "https://dummyjson.com"

# 1. Тест успешного логина
def test_successful_login():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "michaelw",
        "password": "michaelwpass"
    })
    assert response.status_code == 200, "❌ Логин не удался"
    data = response.json()
    assert "accessToken" in data, "❌ Токен не получен"
    assert "refreshToken" in data, "❌ Refresh токен не получен"
    print("✅ Тест 1: Успешный логин работает")

# 2. Тест неудачного логина
def test_failed_login():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "michaelw",
        "password": "wrongpassword"
    })
    assert response.status_code == 400, "❌ Сервер должен вернуть 400"
    print("✅ Тест 2: Неудачный логин обработан правильно")

# 3. Тест доступа без токена
def test_access_without_token():
    response = requests.get(f"{BASE_URL}/auth/me")
    assert response.status_code == 401, "❌ Доступ разрешён без токена"
    print("✅ Тест 3: Доступ без токена запрещён")

# 4. Тест доступа с токеном
def test_access_with_token():
    login_response = requests.post(f"{BASE_URL}/auth/login", json={
        "username": "michaelw",
        "password": "michaelwpass"
    })
    token = login_response.json()["accessToken"]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
    assert response.status_code == 200, "❌ Доступ с токеном не работает"
    data = response.json()
    assert data["username"] == "michaelw", "❌ Данные пользователя не совпадают"
    print("✅ Тест 4: Доступ с токеном работает")

def test_michael_login():
        ...
