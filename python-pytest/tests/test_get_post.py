import requests

def test_get_post():

    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send a GET request
    response = requests.get(url)
    data = response.json() # Read the response body as JSON

    # 3. Check the HTTP status code
    assert response.status_code == 200 # Check if the status code is 200 (OK)

    # 4. Check the response body content
    assert data["userId"] == 1 # Check if the "userId" field in the response body is 1
    assert data["id"] == 1 # Check if the "id" field in the response body is 1
    assert data["title"] # Check the title and make sure it is not empty
    assert data["body"] # Check the body and make sure it is not empty

def test_get_nonexistent_post():

    # 1. Define the API endpoint for a non-existent post
    url = "https://jsonplaceholder.typicode.com/posts/9999"

    # 2. Send a GET request
    response = requests.get(url)

    # 3. Check the HTTP status code
    assert response.status_code == 404 # Check if the status code is 404 (Not Found)