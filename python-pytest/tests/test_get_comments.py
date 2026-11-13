import requests

def test_get_comments():
    # 1. Identify the endpoint with its full URL.
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Check the HTTP status before decoding JSON.
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5
    assert all(comment["postId"] == 1 for comment in data)
    assert all(comment["email"] for comment in data)