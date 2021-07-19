import requests
from requests.api import head

def client():
    token_h = 'Token be08c0ae011b5390290d1b3028f5e25575687ef5'
    # credentials = {'username':'root', 'password':'go9511455'}

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/admin', headers=headers)

    print('status code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()