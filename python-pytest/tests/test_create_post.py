import requests

def test_create_post():
    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Define the request body
    payload = {
        "title": "QA Automation Test",
        "body": "Learning API automation with Python",
        "userId": 1
    }

    # 3. Send a POST request
    response = requests.post(url, json=payload)
    data = response.json() # Read the response body as JSON

    # 4. Assertions to verify the response
    assert response.status_code == 201 # Check if the status code is 201 (Created)
    assert data['id'] == 101 # Check if the id in the response is 101
    assert data['title'] == payload['title'] # Check if the title in the response matches the request
    assert data['body'] == payload['body'] # Check if the body in the response matches the request
    assert data['userId'] == payload['userId'] # Check if the userId in the response matches the request