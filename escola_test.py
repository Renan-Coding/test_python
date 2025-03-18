import requests

# URL e Token
base_url = 'url_da_api_passada'
token = 'token_passado'

endpoint = f'{base_url}/escolas/1'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

def GetEscolaByID():
    response = requests.get(endpoint, headers=headers)

    # Verifica se o status code é 200 OK
    assert response.status_code == 200, f"Esperado status 200, obtido {response.status_code}"

    # Verifica o conteúdo retornado pela API
    escola = response.json()
    assert escola["id"] == 1, f"Esperado id=1, obtido {escola['id']}"
    assert "nome" in escola, "Campo 'nome' não encontrado na resposta"

    print("Teste executado com sucesso. Dados da escola:", escola)

if __name__ == "__main__":
    endpoint = f"{base_url}/escolas/1"
    GetEscolaByID()