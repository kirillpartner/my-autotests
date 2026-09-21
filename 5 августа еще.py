import requests

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
        "title": "Иван",
        "body": "Привет, я Иван",
        "userId": 1
    }
)

# Проверки
assert response.status_code == 201
data = response.json()
assert data["title"] == "Иван"
assert data["id"] == 101

print("✅ Тест пройден!")