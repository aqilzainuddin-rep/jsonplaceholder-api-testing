# Import the requests library to make HTTP requests
import requests

def test_replace_post():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # A dictionary maps JSON field names to values.
    payload = {
        "id": 1,
        "title": "Replacement title",
        "body": "Replacement body",
        "userId": 1
    }

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.put(url, timeout=10, json=payload)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data == payload