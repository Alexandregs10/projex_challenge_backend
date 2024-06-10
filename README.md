# Desafio Estágio de Desenvolvimento Projex Consulting 2024.

## Dependências

- Python 3.10 ou superior
- PIP (Preferred Installer Program)
- FastAPI

## Preparação de ambiente

Instale as dependências em [requirements](requirements.txt) com:

```sh
pip install -r requirements.txt
```

Rode o projeto com:

```sh
py run.py
```
# Para testar a API use o Postman, ThunderClient ou qualquer outra ferramenta para fazer chamadas de API.

# Endpoints para teste
GET http://127.0.0.1:8000/cat_question/gato/{id}

GET http://127.0.0.1:8000/cat_question/gato

GET http://127.0.0.1:8000/cat_question/gatos-mais-velhos

GET http://127.0.0.1:8000/cat_question/buscar-gatos
Parâmetros no body:
{
    "nome": "Tom"
}

GET http://127.0.0.1:8000/cat_question/buscar-raca
Parâmetros no body:
{
    "raca": "Persa"
}
    
