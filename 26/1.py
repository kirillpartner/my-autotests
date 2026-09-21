import requests
def test_pokeapi_status():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    assert response.status_code == 200

def test_first_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    data = response.json()
    assert data["results"][0]["name"] == "bulbasaur"