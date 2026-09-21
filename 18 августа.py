import requests

response = requests.get("https://api.sampleapis.com/movies")

print(response.status_code)
print(response.text[:500])