from pydantic import BaseModel, Field
from typing import Optional, List
from model.tecnica import Tecnica

from schemas import ComentarioSchema

class TecnicaSchema(BaseModel):
    """ Define como uma nova Tecnica a ser inserida deve ser representada
    """
    nome: str = "Chave reta"
    descricao: str = "Chave reta na montada"
    nivel: str = "Iniciante"
    video: str = "https://youtu.be/TEV76y9ijHQ?si=rB_qrRT4KaI-lQP2"

class TecnicaPathSchema(BaseModel):
    id: int = Field(..., description="Tecnica id", json_schema_extra={"deprecated":True, "example": 1})

class TecnicaBodySchema(BaseModel):
    nome: Optional[str] = Field(..., min_length=2, max_lengh=140, description="Nome da tecnica")
    descricao: Optional[str] = Field(..., min_length=2, max_length=4000, description="Descricao da Tecnica")
    nivel: Optional[str] = Field(..., min_length=2, max_length=30, description="Iniciante")
    video: Optional[str] = Field(..., min_length=4, description="Youtube video URL")

class TecnicaBuscaSchemaPorTermo(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base em um termo no nome da Tecnica.
    """
    nome: str = "reta"

class TecnicaBuscaSchemaPorNome(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base o nome da Tecnica.
    """
    nome: str = "Chave Reta"

class TecnicaBuscaSchemaPorID(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID da Tecnica.
    """
    id: int = 1

class ListagemTecnicasSchema(BaseModel):
    """ Define como uma listagem de tecnicas será devolvida.
    """
    tecnicas:List[TecnicaSchema]


def apresenta_tecnicas(tecnicas: List[Tecnica]):
    """ Devolve uma representação da tecnica seguindo o schema definido em
        TecnicaViewSchema.
    """
    result = []
    for tecnica in tecnicas:
        result.append({
            "id": tecnica.id,
            "nome": tecnica.nome,
            "descricao": tecnica.descricao,
            "nivel": tecnica.nivel,
            "video": tecnica.video,
        })

    return {"tecnicas": result}


class TecnicaViewSchema(BaseModel):
    """ Define como um tecnica será devolvida: tecnica + comentários.
    """
    id: int = 1
    nome: str = "Chave Reta"
    descricao: str = "Chave reta na montada"
    nivel: str = "Iniciante"
    video: str = "https://youtu.be/TEV76y9ijHQ?si=rB_qrRT4KaI-lQP2"
    total_comentarios: int = 1
    comentarios:List[ComentarioSchema]


class TecnicaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    nome: str

def apresenta_tecnica(tecnica: Tecnica):
    """ Devolve uma representação da tecnica seguindo o schema definido em
        TecnicaViewSchema.
    """
    return {
        "id": tecnica.id,
        "nome": tecnica.nome,
        "descricao": tecnica.descricao,
        "nivel": tecnica.nivel,
        "video": tecnica.video,
        "total_comentarios": len(tecnica.comentarios),
        "comentarios": [{"texto": c.texto} for c in tecnica.comentarios]
    }