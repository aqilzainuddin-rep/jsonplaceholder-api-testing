# Requests sends HTTP calls and exposes their responses.
import requests

def test_patch_post():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # A dictionary maps JSON field names to values.
    payload = {
        "title": "Patched title"
    }

    # Read the original fields to verify that PATCH leaves them intact.
    original = requests.get(url, timeout=10)
    assert original.status_code == 200
    before = original.json()

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.patch(url, timeout=10, json=payload)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["userId"] == before["userId"]
    # PATCH preserves the body already stored for post 1.
    assert data["body"] == before["body"]