import requests

def test_get_posts_by_user():

    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Define the query parameters
    params={
        "userId": 1
    }

    # 3. Send a GET request with query parameters
    response = requests.get(url, params=params)

    # 4. Read response body as JSON
    data = response.json()

    # 5. Assert that the response status code is 200
    assert response.status_code == 200

    # 6. Assert the response is a list
    assert isinstance(data, list)

    # 7. Assert the response is not empty
    assert data

    # 8. Assert each post has the correct userId
    for post in data:
        assert post["userId"] == params["userId"]

def test_get_posts_by_nonexistent_user():

    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Define a nonexistent userId
    params = {
        "userId": 9999
    }

    # 3. Send a GET request with query parameters
    response = requests.get(url, params=params)

    # 4. Read the response body as JSON
    data = response.json()

    # 5. Assert that the response status code is 200
    assert response.status_code == 200

    # 6. Assert the response body is an empty list
    assert data == []