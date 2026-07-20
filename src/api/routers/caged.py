
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import get_db, repositorio

router = APIRouter()


class CagedCreate(BaseModel):
    competencia: str = Field(
        ...,
        min_length=6,
        max_length=6,
        description="Competência no formato YYYYMM",
    )
    saldo: int
    admissoes: int
    demissoes: int
    setor: str = Field(
        ...,
        max_length=100,
        description="Nome do setor",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "competencia": "202401",
                "saldo": 150,
                "admissoes": 500,
                "demissoes": 350,
                "setor": "Tecnologia da Informação",
            }
        }


class CagedResponse(BaseModel):
    id: int
    competencia: str
    saldo: int
    admissoes: int
    demissoes: int
    setor: str
    atualizado_em: str | None

    class Config:
        from_attributes = True


class CagedBulkCreate(BaseModel):
    registros: list[CagedCreate]


@router.get("/", response_model=list[CagedResponse])
def listar_caged(
        competencia: str | None = Query(
            None,
            description="Competência no formato YYYYMM",
        ),
        setor: str | None = Query(
            None,
            description="Nome do setor",
        ),
        skip: int = Query(
            0,
            ge=0,
            description="Quantidade de registros para pular",
        ),
        limit: int = Query(
            100,
            ge=1,
            le=1000,
            description="Quantidade máxima de registros",
        ),
        db: Session = Depends(get_db),
):
    registros = repositorio.buscar_caged(
        db,
        competencia,
        setor,
        skip,
        limit,
    )

    return [registro.to_dict() for registro in registros]


@router.get(
    "/{registro_id}",
    response_model=CagedResponse,
)
def buscar_caged_id(
        registro_id: int,
        db: Session = Depends(get_db),
):
    registro = repositorio.buscar_por_id(db, registro_id)

    if registro is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro não encontrado.",
        )

    return registro.to_dict()


@router.post(
    "/",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
)
def criar_caged(
        dados: CagedCreate,
        db: Session = Depends(get_db),
):
    quantidade = repositorio.upsert_caged(
        db,
        [dados.model_dump()],
    )

    return {
        "message": "Registro criado/atualizado com sucesso.",
        "count": quantidade,
    }


@router.post(
    "/bulk",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
)
def criar_bulk_caged(
        dados: CagedBulkCreate,
        db: Session = Depends(get_db),
):
    registros = [
        registro.model_dump()
        for registro in dados.registros
    ]

    quantidade = repositorio.upsert_caged(
        db,
        registros,
    )

    return {
        "message": f"{quantidade} registros processados.",
        "count": quantidade,
    }


@router.delete("/{registro_id}")
def deletar_caged(
        registro_id: int,
        db: Session = Depends(get_db),
):
    sucesso = repositorio.deletar_caged(
        db,
        registro_id,
    )

    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro não encontrado.",
        )

    return {
        "message": "Registro deletado com sucesso."
    }


@router.get("/stats/resumo")
def estatisticas(
        db: Session = Depends(get_db),
):
    total = repositorio.contar_registros(db)

    return {
        "total_registros": total,
        "endpoints_disponiveis": [
            "GET /caged/",
            "GET /caged/{id}",
            "POST /caged/",
            "POST /caged/bulk",
            "DELETE /caged/{id}",
        ],
    }