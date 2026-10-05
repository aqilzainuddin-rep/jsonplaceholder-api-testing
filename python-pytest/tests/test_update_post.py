import requests

def test_update_post():

    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Define the update request body/payload
    payload = {
        "id": 1,
        "title": "Updated QA Automation Test",
        "body": "Updated using a PUT request",
        "userId": 1
    }

    # 3. Send a PUT request to update the post
    response = requests.put(url, json=payload)

    # 4. Read the response body as JSON
    data = response.json()

    # 5. Check the HTTP status code
    assert response.status_code == 200 # Check if the status code is 200 (OK)

    # 6. Check the response body content
    assert data['id'] == payload['id'] # Check if the "id" field in the response body matches the payload
    assert data['title'] == payload['title'] # Check if the "title" field in the response body matches the payload
    assert data['body'] == payload['body'] # Check if the "body" field in the response body matches the payload
    assert data['userId'] == payload['userId'] # Check if the "userId" field in the response body matches the payload