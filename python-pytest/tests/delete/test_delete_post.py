# Requests sends HTTP calls and exposes their responses.
import requests

def test_delete_post():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.delete(url, timeout=10)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data == {}