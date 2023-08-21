import requests

with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

endpoint = 'http://127.0.0.1:8000/api/post/3/delete/'
headers = {'Authorization': f'Bearer {token}'}

pk = int(input('enter the id of the resource you wish to delete: '))
try:
    pk = pk
except pk is None:
    print(f'{pk} is not a valid id')    

if pk:
    endpoint = f'http://127.0.0.1:8000/api/post/{pk}/delete'
    response = requests.delete(endpoint, headers=headers)

    print(response.status_code, response.status_code==204)