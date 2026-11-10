# Requests sends HTTP calls and exposes their responses.
import requests


def test_get_existing_post():
    # 1. Identify the endpoint with its full URL.
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Check the HTTP status before decoding JSON.
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"]
    assert data["body"]


def test_get_missing_post():
    # 1. Identify the endpoint with its full URL.
    url = "https://jsonplaceholder.typicode.com/posts/999999"

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Check the HTTP status before decoding JSON.
    assert response.status_code == 404

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data == {}