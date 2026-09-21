import requests

#1 Адрес для создания пользователя
url = "https://jsonplaceholder.typicode.com/users"
#Данные нового пользователя
new_user = {
    "name": "Том круз",
    "username": "Tom.kruz",
    "email": "Tom@example.com"
}
#3 Отправялем POST-запрос
response=requests.post(url,json=new_user)
#4 Проверяем статус
assert response.status_code == 201, "Пользователь не создан"
#5 Получаем ответ
user_data = response.json()
print("✔ Пользователь создан:",user_data)
#6 Проверяем, что id есть
assert "id" in user_data, "❌ Нет id в ответе"
print(f"✔ID нового пользователя: {user_data['id']}")
#7 Проверяем, что данные совпадают
assert user_data["name"] == new_user["name"], ">❌Имя не совпадает"
assert user_data["username"] == new_user["username"], "❌ Username не совпадает"
assert user_data["email"] == new_user["email"], "❌Email не совпадает"

print("✔Все проверки пройдены! Тест успешен.")