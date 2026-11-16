# Import the requests library to make HTTP requests
import requests

def test_get_existing_post():
    # 1. Endpoint URL for getting all posts
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send the request. Timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Assert the response status code
    assert response.status_code == 200

    # 4. Decode the JSON response & assert the response received from server
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"]
    assert data["body"]

def test_get_missing_post():
    # 1. Endpoint URL for getting a non-existing post
    url = "https://jsonplaceholder.typicode.com/posts/9999"

    # 2. Send the request. Timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Assert the response status code
    assert response.status_code == 404

    # 4. Decode the JSON response & assert the response received from server
    data = response.json()
    assert data == {}
