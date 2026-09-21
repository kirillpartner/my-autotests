import requests

api_key = "71e6f4ee805836a5cce23ec67762e9b8"
cities_input = input("Введи города через запятую: ")

# Разделяем строку по запятым и убираем лишние пробелы
cities = [city.strip() for city in cities_input.split(",")]

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        feels = data['main']['feels_like']
        print(f'{city}:Ощущается как {feels}C')
        temp = data['main']['temp']
        print(f"🌡️ {city}: {temp}°C")
    else:
        print(f"❌ {city}: город не найден")