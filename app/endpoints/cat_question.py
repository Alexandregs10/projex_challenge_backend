from fastapi import APIRouter, Body, HTTPException
from app.models.cat_question import lista_gatos, datas_nascimento
from pydantic import BaseModel

router = APIRouter()

class nome(BaseModel):
    nome: str

class raca(BaseModel):
    raca: str


# Método que recebe um ID e retorna os dados do gato e sua data de nascimento
@router.get("/gato/{id}")
def get_gato_por_id(id: int):
    try:
        gato = next((gato for gato in lista_gatos if gato.id == id), None)
        data_nascimento = next((d['data_nascimento'] for d in datas_nascimento if d['id'] == id), None)
        return {
            'id': gato.id,
            'nome': gato.nome,
            'raca': gato.raca,
            'idade': gato.idade,
            'data_nascimento': data_nascimento.strftime('%Y-%m-%d')
        }
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")
    
# Método que retorna a lista de gatos sem data de nascimento e sem idade
@router.get("/gato")
def get_gatos():
    """_summary_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    try:
        gatos_sem_data_nascimento = []
        for gato in lista_gatos:
            if not any(d['id'] == gato.id for d in datas_nascimento):
                gatos_sem_data_nascimento.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca
                })
        return gatos_sem_data_nascimento
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Método que retorna uma lista de todos os gatos mais velhos com a mesma idade
@router.get("/gatos-mais-velhos")
def get_gatos_mais_velhos():
    try:
        # Encontra a idade máxima entre todos os gatos
        idade_maxima = max(gato.idade for gato in lista_gatos)
        
        # Lista para armazenar todos os gatos mais velhos com a mesma idade máxima
        gatos_mais_velhos = []
        for gato in lista_gatos:
            if gato.idade == idade_maxima:
                # Encontra a data de nascimento do gato
                data_nascimento_gato = next((d['data_nascimento'] for d in datas_nascimento if d['id'] == gato.id), None)
                
                # Adiciona o gato à lista com sua data de nascimento
                gatos_mais_velhos.append({
                    'id': gato.id,
                    'nome': gato.nome,
                    'raca': gato.raca,
                    'idade': gato.idade,
                    'data_nascimento': data_nascimento_gato.strftime('%Y-%m-%d')
                })
        
        return gatos_mais_velhos
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")

# Método que busca gatos por um termo de busca no nome
@router.post("/buscar-gatos")
def buscar_gatos_por_nome(nome: nome):
    try:
        # Utilizando list comprehension diretamente na lista de gatos
        gatos_encontrados = [
            { 
                'id': gato.id,
                'nome': gato.nome,
                'raca': gato.raca,
                'idade': gato.idade,
                'data_nascimento': [d['data_nascimento'] for d in datas_nascimento if d['id'] == gato.id]
            } 
            for gato in lista_gatos 
            if nome.nome.lower() in gato.nome.lower()
        ]   
        return {'gatos_encontrados': gatos_encontrados}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
        
# Método que busca gatos por raça
@router.post("/buscar-raca")
def buscar_gatos_por_raca(raca: raca):
    try:
        gatos_encontrados = [
            { 
                'id': gato.id,
                'nome': gato.nome,
                'raca': gato.raca,
                'idade': gato.idade,
                'data_nascimento': [d['data_nascimento'] for d in datas_nascimento if d['id'] == gato.id]
            } 
            for gato in lista_gatos 
            if raca.raca.lower() in gato.raca.lower()
        ]   
        return {'gatos_encontrados': gatos_encontrados}
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error")