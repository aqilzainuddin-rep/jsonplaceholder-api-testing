import requests

def test_delete_post():
    
    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Send a DELETE request
    response = requests.delete(url)

    # 3. Assert the response status code
    assert response.status_code == 200

    # 4. Assert the response body is empty
    assert response.text == "{}"