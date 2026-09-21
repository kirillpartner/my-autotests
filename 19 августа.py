import requests


def test_pikachu_exists():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"

    response = requests.get(url)

    assert response.status_code == 200, f"❌ Ошибка: {response.status_code}"

    data = response.json()

    assert data["name"] == "pikachu", f"❌ Ожидали pikachu, а пришёл {data['name']}"