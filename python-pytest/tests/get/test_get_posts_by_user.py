# Import the requests library to make HTTP requests
import requests

def test_filter_valid_user():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # Let request parameters be a dictionary
    params = {"userId": '1'}

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10, params=params)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10  # Assuming userId 1 has 10 posts in the placeholder API
    assert all(post["userId"] == 1 for post in data)  # Check that all posts belong to userId 1

def test_filter_non_existing_user():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # Let request parameters be a dictionary
    params = {"userId": '9999'}  # Assuming userId 9999 does not exist

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10, params=params)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data == []  # Expecting an empty list for a non-existing userId

def test_filter_invalid_user():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # Let request parameters be a dictionary
    params = {"userId": 'john'}  # Invalid userId format

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10, params=params)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data == []  # Expecting an empty list for an invalid userId format


def test_filter_empty_user():
    # 1. Endpoint URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # Let request parameters be a dictionary
    params = {"userId": ''} # Empty userId

    # 2. Send the request. The timeout bounds socket waits.
    response = requests.get(url, timeout=10, params=params)

    # 3. Check status code of the response
    assert response.status_code == 200

    # 4. Decode the response and check what the server returned.
    data = response.json()
    assert data == []  # Expecting an empty list for an empty userId