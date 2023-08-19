import requests

endpoint = 'http://127.0.0.1:8000/api/login/'
username = input('Username: ')
password = input('Password: ')

response = requests.post(endpoint, json={
    'username': username,
    'password': password
})

print(response.json())