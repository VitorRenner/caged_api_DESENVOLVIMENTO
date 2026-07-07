from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from src.api.banco.conexao import get_db
from src.api.banco import repositorio

router = APIRouter()


# Pydantic Models for request/response
class CagedCreate(BaseModel):
    competencia: str = Field(..., min_length=6, max_length=6, description="Format: YYYYMM")
    saldo: int
    admissoes: int
    demissoes: int
    setor: str = Field(..., max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "competencia": "202401",
                "saldo": 150,
                "admissoes": 500,
                "demissoes": 350,
                "setor": "Tecnologia da Informação"
            }
        }


class CagedResponse(BaseModel):
    id: int
    competencia: str
    saldo: int
    admissoes: int
    demissoes: int
    setor: str
    atualizado_em: Optional[str]

    class Config:
        from_attributes = True


class CagedBulkCreate(BaseModel):
    registros: List[CagedCreate]


@router.get("/", response_model=List[CagedResponse])
def listar_caged(
        competencia: Optional[str] = Query(None, description="Filter by YYYYMM"),
        setor: Optional[str] = Query(None, description="Filter by sector"),
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=1000),
        db: Session = Depends(get_db)
):
    """
    List all CAGED records with optional filtering.
    """
    registros = repositorio.buscar_caged(db, competencia, setor, skip, limit)
    return [r.to_dict() for r in registros]


@router.get("/{id}", response_model=CagedResponse)
def buscar_caged_id(id: int, db: Session = Depends(get_db)):
    """
    Get single CAGED record by ID.
    """
    registro = repositorio.buscar_por_id(db, id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return registro.to_dict()


@router.post(
    "/",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def criar_caged(data: CagedCreate, db: Session = Depends(get_db)):
    """
    Create single CAGED record.
    """
    registro = [data.model_dump()]
    count = repositorio.upsert_caged(db, registro)
    return {"message": "Registro criado/atualizado", "count": count}


@router.post(
    "/bulk",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def criar_bulk_caged(data: CagedBulkCreate, db: Session = Depends(get_db)):
    """
    Create/update multiple CAGED records at once.
    """
    registros = [r.model_dump() for r in data.registros]
    count = repositorio.upsert_caged(db, registros)
    return {"message": f"{count} registros processados", "count": count}


@router.delete("/{id}")
def deletar_caged(id: int, db: Session = Depends(get_db)):
    """
    Delete CAGED record by ID.
    """
    success = repositorio.deletar_caged(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return {"message": "Registro deletado com sucesso"}


@router.get("/stats/resumo")
def estatisticas(db: Session = Depends(get_db)):
    """
    Get summary statistics.
    """
    total = repositorio.contar_registros(db)
    return {
        "total_registros": total,
        "endpoints_disponiveis": [
            "GET /caged/",
            "GET /caged/{id}",
            "POST /caged/",
            "POST /caged/bulk",
            "DELETE /caged/{id}"
        ]
    }