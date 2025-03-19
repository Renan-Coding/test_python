import os
import requests
import pytest
import dotenv
from unittest.mock import patch, Mock

# Carrega as variáveis definidas no arquivo .env
dotenv.load_dotenv()

# URL base e token importados do .env
base_url = os.getenv("API_KEY").strip()
token = os.getenv("SECRET_KEY").strip()

# Cabeçalhos da requisição com autenticação Bearer
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

def get_institutions():
    endpoint = f"{base_url}/institutions/"
    try:
        response = requests.get(endpoint, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        raise e

class TestInstitutionsAPI:
    
    def test_listar_escolas_sucesso(self):
        response = get_institutions()
        
        # Verifica se o status code é 200 (OK)
        assert response.status_code == 200
        
        # Verifica se a resposta é um JSON válido
        data = response.json()
        assert isinstance(data, list) or isinstance(data, dict)
    
    def test_autenticacao_valida(self): 
        # Testa se os headers de autenticação estão corretos
        response = get_institutions()
        assert response.status_code != 401, "Falha na autenticação"
    
    @patch('requests.get')
    def test_erro_conexao(self, mock_get): # Testa o comportamento quando há erro de conexão
        # Configura o mock para simular um erro de conexão
        mock_get.side_effect = requests.exceptions.ConnectionError("Erro de conexão simulado")
        
        # Verifica se a exceção é levantada corretamente
        with pytest.raises(requests.exceptions.ConnectionError):
            get_institutions()
    
    @patch('requests.get')
    def test_resposta_404(self, mock_get): # Testa o comportamento quando o endpoint não existe
        # Configura o mock para retornar status code 404
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        response = get_institutions()
        assert response.status_code == 404
    
    @patch('requests.get')
    def test_resposta_invalida(self, mock_get): # Testa o comportamento quando a resposta não é um JSON válido
        # Configura o mock para retornar uma resposta inválida
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = requests.exceptions.JSONDecodeError("Invalid JSON", "", 0)
        mock_get.return_value = mock_response
        
        response = get_institutions()
        with pytest.raises(requests.exceptions.JSONDecodeError):
            response.json()

# Para executar os testes manualmente (sem o pytest)
if __name__ == "__main__":
    test = TestInstitutionsAPI()
    try:
        test.test_listar_escolas_sucesso()
        print("Teste de listagem de escolas passou com sucesso!")
    except AssertionError as e:
        print(f"Teste falhou: {e}")
    
    try:
        test.test_autenticacao_valida()
        print("Teste de autenticação passou com sucesso!")
    except AssertionError as e:
        print(f"Teste falhou: {e}")