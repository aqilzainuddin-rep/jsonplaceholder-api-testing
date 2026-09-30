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

    # 5. Display the response information for debugging purposes
    print("Status code:", response.status_code) # Print the status code
    print("Response body:", data) # Print the response body 