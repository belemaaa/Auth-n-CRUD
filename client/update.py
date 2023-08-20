import requests

endpoint = 'http://127.0.0.1:8000/api/post/1/update/'
title = input('Enter updated title: ')
content = input('Enter updated content: ')

data = {
    'title': title,
    'content': content
}
response = requests.put(endpoint, json=data)

print(response.json())