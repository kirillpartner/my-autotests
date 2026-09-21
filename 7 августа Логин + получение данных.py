import requests
import time
#1. Логинимся и получаем токен
login_url = "https://reqres.in/api/login"
login_data = {
    "email": "eve.holt@reqres.in",
    "password": "бред сивой кобылы"
}
api_key = "free_user_3HaGYlsFSlsp7fJbMT9ELUOxS9H"
headers = {"x-api-key": api_key}
login_response = requests.post(login_url, json=login_data, headers=headers)
assert login_response.status_code == 200, "❌ Ошибка логина"
token = login_response.json()["token"]
print(f"✔ Логин успешен! Токен:{token}")

#2 Используем токен для получения данных пользователя
user_url = "https://reqres.in/api/users/3"
headers["authorization"] = f"Bearer {token}" #Добавляем токен в заголовок
start_time = time.time()

user_response = requests = requests.get(user_url, headers=headers)

end_time = time.time()

print(f"🕐 Время получения данных: {end_time - start_time:.3f} секунд")

assert user_response.status_code == 200, "❌ Не удалось получить данные"
user_data = user_response.json()
print("✔ Данные получены", user_data)

#3. Проверяем, что данные соответсвуют ожидаемым

expected_user = {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver"
}
assert user_data["data"]["email"] == expected_user["email"], "❌ Email не совпадает"
assert user_data["data"]["first_name"] == expected_user["first_name"], "❌ Имя не совпадает"
assert user_data["data"]["last_name"] == expected_user["last_name"], "❌ Фамилия не совпадет"
print("✔ Все проверки пройдены! Тест успешен.")
