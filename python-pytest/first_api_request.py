import requests

# 1. Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# 2. Send a GET request
response = requests.get(url)

# 3. Check the HTTP status code
if response.status_code == 200:

    # 4. Read the response body as JSON
    data = response.json()

    # 5. Read a response header
    content_type = response.headers.get("content-type")

    # 6. Print the response information
    print("Status code:", response.status_code)
    print("Content-Type:", content_type)
    print("Response body:", data)

else:
    print("Request failed.")
    print("Status code:", response.status_code)
