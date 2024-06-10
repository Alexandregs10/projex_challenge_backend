# Desafio Estágio de Desenvolvimento Projex Consulting 2024.

## Dependências

- Python 3.10 ou superior
- PIP (Preferred Installer Program)
- FastAPI
- Pydantic

## Preparação de ambiente

Instale as dependências em [requirements](requirements.txt) com:

```sh
pip install -r requirements.txt
```

Rode o projeto com:

```sh
py run.py
```
## Para testar a API use o Postman, ThunderClient ou qualquer outra ferramenta para fazer chamadas de API.

## Endpoints para teste
GET http://127.0.0.1:8000/cat_question/gato/{id}

GET http://127.0.0.1:8000/cat_question/gato

GET http://127.0.0.1:8000/cat_question/gatos-mais-velhos

GET http://127.0.0.1:8000/cat_question/buscar-gatos
#### Parâmetros no body em /buscar-gatos:
![image](https://github.com/Alexandregs10/projex_challenge_backend/assets/122055722/1c28301b-b287-4ae4-97f3-b0d69ad73fb2)

GET http://127.0.0.1:8000/cat_question/buscar-raca
#### Parâmetros no body em /buscar-raca:
![image](https://github.com/Alexandregs10/projex_challenge_backend/assets/122055722/0c716ccc-b2a9-4327-b33b-9afaec8f9e86)

    
