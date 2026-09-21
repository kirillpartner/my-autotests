import requests

def test_put_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.put(url, json={
        "id":1,
        "title": "Новый заголовок",
        "body": "Новый текст",
        "userId":1
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Новый заголовок"

def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/post/1"
    response = requests.delete(url)

    assert response.status_code == 200
    assert response.json() == {}

