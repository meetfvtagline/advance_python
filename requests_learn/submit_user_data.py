# import requests

# payloads={
#     'name':'john',
#     'age':23,
#     'city':'New York'
# }



# response = requests.get("https://postman-echo.com/get", data=payloads)
# print("Status Code:",response.status_code)
# print("url:",response.url)
# print("Content:",response.text)

import requests

# Server URL (live fake API)
url = "https://dummyjson.com/users/add"

# User data to send
user_data = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 25,
    "email": "john.doe@example.com"
}

# Send POST request
response = requests.post(url, json=user_data)

# Print response status code
print("Status Code:", response.status_code)

# Print response data
print("Response Data:", response.json())
