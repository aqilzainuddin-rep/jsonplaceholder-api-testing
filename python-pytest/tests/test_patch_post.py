import requests

def test_patch_post():
    
    # 1. Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # 2. Define only the field we want to update
    payload = {
        "title": "Patched QA Automation Test"
    }

    # 3. Send a PATCH request
    response = requests.patch(url, json=payload)
    
    # 4. Read response body as JSON
    data = response.json()

    # 5. Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # 6. Assert that the title has been updated correctly
    assert data["title"] == payload["title"]