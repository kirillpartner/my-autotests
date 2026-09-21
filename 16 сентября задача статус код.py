import requests

response = requests.get("https://dummyjson.com/users/1")

assert response.status_code == 200