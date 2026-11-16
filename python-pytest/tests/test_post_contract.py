# Import the requests library to make HTTP requests
import requests

def test_post_contract():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert isinstance(data, dict)
    assert set(data) == {"id", "userId", "title", "body"}  # Check that the response contains the expected keys
    assert type(data["id"]) is int
    assert type(data["userId"]) is int
    assert isinstance(data["title"], str) and data["title"].strip()
    assert isinstance(data["body"], str) and data["body"].strip()