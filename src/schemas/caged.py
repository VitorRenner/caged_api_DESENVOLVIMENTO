from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CagedBase(BaseModel):
    """
    Campos base do registro CAGED.
    """

    competencia: str
    setor: str
    admissoes: int
    demissoes: int
    saldo: int


class CagedCreate(CagedBase):
    """
    Schema para criação de registros.
    """

    pass


class CagedBulkCreate(BaseModel):
    """
    Schema para criação de múltiplos registros.
    """

    registros: list[CagedCreate]


class CagedResponse(CagedBase):
    """
    Schema de resposta da API.
    """

    id: int
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
