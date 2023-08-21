import requests

with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

endpoint = 'http://127.0.0.1:8000/api/post/create/'
headers = {
    'Authorization': f'Bearer {token}'
}
data = {
    'title': 'a new client side post',
    'content': 'some random content for testing purposes'
}
response = requests.post(endpoint, json=data, headers=headers)
print(token)
print(response.json())