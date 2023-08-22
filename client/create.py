import requests

with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

endpoint = 'http://127.0.0.1:8000/api/post/create/'
headers = {
    'Authorization': f'Bearer {token}'
}
title = input('title: ')
content = input('content: ')
data = {
    "title": title,
    "content": content
}
response = requests.post(endpoint, json=data, headers=headers)
print(token)
print(response.json())