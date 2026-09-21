import requests

url = "http://127.0.0.1:5000/users"
new_user = {"name": "Том Круз", "email": "tom@example.com"}

response = requests.post(url, json=new_user)
print("Статус:", response.status_code)
print("Ответ:", response.json())