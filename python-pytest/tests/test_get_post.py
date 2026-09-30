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

    # 5. Display the response information
    print("Response body:", data) # Print the response body