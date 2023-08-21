import requests

pk = int(input('enter the id of the resource you wish to delete: '))

endpoint = f'http://127.0.0.1:8000/api/post/{pk}/delete'
response = requests.delete(endpoint)

print(response.status_code, response.status_code==204)