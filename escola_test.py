import requests

# URL e Token
base_url = 'url_da_api_passada'
token = 'token_passado'

endpoint = f'{base_url}/escolas/1'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}