import requests

def test_get_post():

    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send a GET request
    response = requests.get(url)

    # 3. Check the HTTP status code
    assert response.status_code == 200 # Check if the status code is 200 (OK)