# Caso de Teste: "Obter Escola por ID"

## Descrição
&nbsp;&nbsp;Este teste verifica diretamente uma funcionalidade do sistema: buscar informações específicas sobre uma escola cadastrada, para garantir que o sistema esteja funcionando e que as informações estejam sendo recuperadas e exibidas conforme esperado.

## Objetivo
&nbsp;&nbsp;Verificar se a API retorna corretamente os dados de uma escola específica ao ser requisitada pelo seu ID.

## Pré-condição
- A aplicação deve estar em execução.
- A API estar funcionando corretamente e disponível para realizar requisições HTTP.
- Existir uma escola cadastrada no banco de dados com o ID sendo conhecido (ex: ID = 2).

## Procedimento de Teste
1. Realizar uma requisição HTTP (`/Get`) para a rota `/escolas/{id}`.
2. Validar o conteúdo retornado no corpo da resposta JSON, verificando se os dados da escola correspondem ao registrado no banco de dados.
