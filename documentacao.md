# Caso de Teste: "Listar Todas as Escolas"

## Descrição
&nbsp;&nbsp;Este teste verifica diretamente uma funcionalidade do sistema, buscar informações sobre todas as escolas cadastradas, para garantir que o sistema esteja funcionando e que as listagens estejam sendo recuperadas e exibidas conforme esperado.

## Objetivo
&nbsp;&nbsp;Verificar se a API retorna corretamente a lista completa de escolas ao ser requisitada.

## Pré-condição
- A aplicação deve estar em execução.
- A API estar funcionando corretamente e disponível para realizar requisições HTTP.
- Existirem escolas cadastradas no banco de dados.
- Ter a biblioteca Python `requests` devidamente instalada no dispositivo. 

## Procedimento de Teste
1. Realizar uma requisição HTTP (`/Get`) para a rota `/institutions`.
2. Validar o conteúdo retornado no corpo da resposta JSON, verificando se os dados da escola correspondem ao registrado no banco de dados.

## Resultado Esperado
- Status HTTP: 200 - OK
- Corpo da resposta:
```json
{
    "id": 306,
    "name": "Faculdade de Tecnologia de São Paulo",
    "students_counts": "14"
}
{
    "id": 307,
    "name": "Faculdade de Tecnologia de Sorocaba (José Crespo Gonzales)",
    "students_counts": "9"
}
{
    "id": 308,
    "name": "Faculdade de Tecnologia de Americana (Ministro Ralph Biasi)",
    "students_counts": "15"
}
```

## Resultado Obtido
- Status HTTP: 200 - OK
- Corpo da resposta:
```json
{
    "id": 306,
    "name": "Faculdade de Tecnologia de São Paulo",
    "students_counts": "14"
}
{
    "id": 307,
    "name": "Faculdade de Tecnologia de Sorocaba (José Crespo Gonzales)",
    "students_counts": "9"
}
{
    "id": 308,
    "name": "Faculdade de Tecnologia de Americana (Ministro Ralph Biasi)",
    "students_counts": "15"
}
```

## Pós-condição
&nbsp;&nbsp;Nenhuma alteração após a execução do teste.