import requests
url = "https://reqres.in/api/login"
api_key = "free_user_3HaGYlsFSlsp7fJbMT9ELUOxS9H"
headers = {"x-api-key": api_key,
           "User-Agent": "reqres-qa-tests/1.0"}

data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"}
response = requests.post(url, json=data, headers=headers)
if response.status_code in [200, 201]:
    token = response.json()["token"]
    print(f"✔ Логин успешен! Токен: {token}")
else:
    print(f"❌ Ошибка: {response.status_code}")
    print("Ответ сервера:", response.text)




