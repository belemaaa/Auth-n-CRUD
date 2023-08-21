import requests

with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

endpoint = 'http://127.0.0.1:8000/api/post/3/update/'
headers = {'Authorization': f'Bearer {token}'}

title = input('Enter updated title: ')
content = input('Enter updated content: ')
data = {
    'title': title,
    'content': content
}
response = requests.put(endpoint, json=data, headers=headers)

print(response.json())