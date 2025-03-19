# Caso de Teste: "Listar Instituições"

## Objetivo
Garantir que a função se comporte corretamente em cada situação, validando tanto respostas de sucesso quanto de erro. Este conjunto de testes validar a integração com a API de instituições. Os testes cobrem os seguintes cenários:
- Listagem bem-sucedida das instituições com resposta HTTP 200 e JSON válido.
- Verificação dos cabeçalhos de autenticação para garantir que o token seja utilizado corretamente.
- Comportamento esperado quando ocorre um erro de conexão, simulando a exceção ConnectionError.
- Retorno de status HTTP 404 para endpoints inexistentes.
- Tratamento correto de uma resposta com JSON malformado, que deve levantar um JSONDecodeError.


## Pré-condições
- A API deve estar em execução e acessível no endereço configurado pela variável `API_KEY` no arquivo `.env`.
- Deve existir pelo menos uma instituição cadastrada para o cenário de listagem com sucesso.
- A variável `SECRET_KEY` do arquivo `.env` deve conter um token de acesso válido.
- As bibliotecas `requests`, `pytest` e `dotenv` devem estar instaladas.

## Procedimento de Teste

**OBS:** Utilizar o comando `python -m pytest mock.py` no terminal para realizar o teste.

### 1. Listagem com Sucesso
- **Resultado Esperado:**
  - Status HTTP: 200 (OK).
  - Resposta: JSON válido contendo a lista ou objeto com as instituições.
- **Resultado Obtido:**
  - Status HTTP: 200 (OK).
  - Resposta: JSON válido confirmado como um objeto.
  - Teste executado com sucesso, validando que a API retorna corretamente as instituições cadastradas.

### 2. Verificação de Autenticação
- **Resultado Esperado:**
  - Status HTTP: Diferente de 401, indicando que o token de autenticação é válido e está sendo utilizado corretamente.
- **Resultado Obtido:**
  - Status HTTP: Diferente de 401.
  - Token de autenticação Bearer enviado corretamente nos cabeçalhos.
  - Teste confirmou que as credenciais estão funcionando adequadamente para acesso à API.

### 3. Erro de Conexão
- **Resultado Esperado:**
  - A exceção requests.exceptions.ConnectionError deve ser levantada quando o erro de conexão ocorrer.
- **Resultado Obtido:**
  - Exceção devidamente levantada conforme simulação.
  - O mock foi configurado para simular corretamente o erro de conexão.
  - O método get_institutions propagou adequadamente a exceção sem tratá-la internamente.

### 4. Resposta com Endpoint Inexistente (404)
- **Resultado Esperado:**
  - Status HTTP: 404.
- **Resultado Obtido:**
  - Status HTTP: 404.
  - A função `get_institutions` retornou corretamente o objeto de resposta com status 404.
  - O mock foi configurado corretamente para simular um endpoint inexistente.

### 5. Resposta com JSON Inválido
- **Resultado Esperado:**
  - Na tentativa de converter a resposta para JSON, deve ser levantada a exceção requests.exceptions.JSONDecodeError.
- **Resultado Obtido:**
  - A exceção requests.exceptions.JSONDecodeError foi levantada conforme esperado.
  - O mock foi configurado corretamente para simular uma resposta com JSON inválido.
  - A função `get_institutions` retornou o objeto de resposta sem tentar processar o JSON internamente.

## Pós-condição
Após a execução dos testes, nenhum dado é alterado ou persistido, os testes são realizados de forma isolada.