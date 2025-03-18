import requests  # Importa a biblioteca requests para fazer chamadas HTTP

# URL base e token fornecidos
base_url = 'https://two025-1a-t13-es05-api2.onrender.com/api/v1'
token = 'g5-d07b7448e0e79b485cef47e88add553218'

# Cabeçalhos da requisição com autenticação Bearer
headers = {
    'Authorization': f'Bearer {token}',  # Define o token de autenticação no formato Bearer
    'Content-Type': 'application/json'   # Define o tipo de conteúdo como JSON
}
