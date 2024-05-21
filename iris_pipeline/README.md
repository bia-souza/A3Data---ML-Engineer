# Iris Classification Pipeline

Este projeto implementa uma pipeline para a classificação de flores Iris utilizando Kedro, Docker e Flask. A pipeline treina um modelo de classificação utilizando Random Forest, salva o modelo e implementa uma API para realizar previsões com o modelo treinado.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Kedro**: Framework para criar pipelines de dados.
- **Scikit-Learn**: Biblioteca para aprendizado de máquina.
- **Joblib**: Biblioteca para serialização de objetos Python.
- **Flask**: Microframework para criar a API.
- **Docker**: Plataforma para containerização.

## Configuração do Ambiente

### Pré-requisitos

- Docker
- Docker Compose

### Passos para Executar a Pipeline

1. **Clonar o Repositório**

   ```sh
   git clone https://github.com/seu_usuario/iris-pipeline.git
   cd iris-pipeline
   ```

2. **Construir e Iniciar os Contêineres Docker**

  ```sh
  docker-compose up --build
  ```

3. **Verificar a Execução da Pipeline**

O Kedro será executado dentro do contêiner e o modelo treinado será salvo em `src/iris_pipeline/model.joblib`.

4. **Verificar a API**

A API Flask será executada no contêiner `iris-api` e estará disponível em `http://localhost:5000`.

## Casos de Teste

### Testar a API com cURL

1. **Caso de Teste 1**

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}"
```

**Resposta Esperada**:

```json
{
  "species": "Iris-setosa"
}
```

2. **Caso de Teste 2**

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"sepal_length\": 6.0, \"sepal_width\": 3.0, \"petal_length\": 4.0, \"petal_width\": 1.5}"
```

**Resposta Esperada**:

```json
{
  "species": "Iris-versicolor"
}
```

3. **Caso de Teste 3**

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"sepal_length\": 7.2, \"sepal_width\": 3.6, \"petal_length\": 6.1, \"petal_width\": 2.5}"
```

**Resposta Esperada**:

```json
{
  "species": "Iris-virginica"
}
```

### Testar a API com Postman

1. **Abrir o Postman**

   Abra o Postman e crie uma nova requisição.

2. **Configurar a Requisição**

   - **Método**: POST
   - **URL**: `http://localhost:5000/predict`
   - **Headers**: `Content-Type: application/json`
   - **Body**:
     ```json
     {
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
     }
     ```

3. **Enviar a Requisição**

   Clique em "Send" para enviar a requisição e verifique a resposta esperada.
