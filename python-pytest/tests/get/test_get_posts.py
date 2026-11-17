# Import the requests library to make HTTP requests
import requests

def test_get_all_posts():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Send the request. Timeout bounds socket waits.
    response = requests.get(url, timeout=10)

    # 3. Assert the response status code
    assert response.status_code == 200

    # 4. Decode the JSON response & assert the response received from server
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100  # Assuming there are 100 posts in the response
    assert {post['id'] for post in data} == set(range(1, 101))  # Check if IDs are from 1 to 100
