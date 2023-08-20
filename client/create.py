import requests

endpoint = 'http://127.0.0.1:8000/api/post/create/'

data = {
    'title': 'a client side post',
    'content': 'some random content for testing'
}
response = requests.post(endpoint, json=data)

print(response.json())