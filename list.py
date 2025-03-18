import os
import requests  # Importa a biblioteca requests para fazer chamadas HTTP
import dotenv

# Carrega as variáveis definidas no arquivo .env
dotenv.load_dotenv()

# URL base e token importados do .env
base_url = os.getenv("API_KEY").strip()
token = os.getenv("SECRET_KEY").strip()

# Cabeçalhos da requisição com autenticação Bearer
headers = {
    'Authorization': f'Bearer {token}',  # Define o token de autenticação no formato Bearer
    'Content-Type': 'application/json'   # Define o tipo de conteúdo como JSON
}

def listar_escolas():
    endpoint = f"{base_url}/institutions/"  # Define o endpoint para listar escolas
    
    # Fazendo a requisição GET para o endpoint
    try:
        # Envia uma requisição GET para a API com os cabeçalhos de autenticação
        response = requests.get(endpoint, headers=headers)

        # Verifica se a resposta foi bem-sucedida (status code 200)
        if response.status_code == 200:
            try:
                # Tenta converter a resposta para JSON
                institutions = response.json()
                print("Lista de escolas:", institutions)
            except requests.exceptions.JSONDecodeError:
                # Caso a resposta não seja um JSON válido
                print("Erro: A resposta não contém um JSON válido.")
        elif response.status_code == 404:
            # Caso o endpoint não exista
            print("Erro: Endpoint não encontrado (404). Verifique a URL.")
        elif response.status_code == 401:
            # Caso o token de autenticação seja inválido
            print("Erro: Token inválido ou expirado (401).")
        else:
            # Para outros códigos de status HTTP
            print(f"Erro inesperado: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        # Captura erros de conexão com a API
        print(f"Erro ao conectar à API: {e}")

if __name__ == "__main__":
    # Executa a função de listar escolas quando o script é executado diretamente
    listar_escolas()