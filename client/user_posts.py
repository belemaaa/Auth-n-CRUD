import requests

with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

endpoint = 'http://127.0.0.1:8000/api/post/user/'
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(endpoint, headers=headers)

print(response.json())