import requests

def test_get_all_posts():

    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Send a GET request
    response = requests.get(url)

    # 3. Read the response body as JSON
    data = response.json()

    # 4. Assert the response status code
    assert response.status_code == 200

    # 5. Assert the response body is a list
    assert isinstance(data, list)

    # 6. Assert the list is not empty
    assert data

    # 7. Assert the first post contains the expected fields
    assert "userId" in data[0]
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]