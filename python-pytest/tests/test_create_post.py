import requests

def test_create_post():
    # 1. Identify the endpoint with its full URL.
    url = "https://jsonplaceholder.typicode.com/posts"
    # A dictionary maps JSON field names to values.
    payload = {
        "title": "QA Automation Test",
        "body": "Learning API automation",
        "userId": 1
    }

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.post(url, timeout=10, json=payload)

    # 3. Check the HTTP status before decoding JSON.
    assert response.status_code == 201

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert type(data["id"]) is int
    assert data["id"] > 100
    for field, expected_value in payload.items():
        assert data[field] == expected_value