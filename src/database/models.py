from typing import Any

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.sql import func

from database import Base


class CagedMovimentacao(Base):
    """
    Modelo da tabela que armazena as movimentações do CAGED.
    """

    __tablename__ = "caged_movimentacao"

    __table_args__ = (
        UniqueConstraint(
            "competencia",
            "setor",
            name="uq_competencia_setor",
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    competencia = Column(
        String(6),
        nullable=False,
        index=True,
    )

    setor = Column(
        String(100),
        nullable=False,
        index=True,
    )

    admissoes = Column(
        Integer,
        nullable=False,
        default=0,
    )

    demissoes = Column(
        Integer,
        nullable=False,
        default=0,
    )

    saldo = Column(
        Integer,
        nullable=False,
        default=0,
    )

    atualizado_em = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    def to_dict(self) -> dict[str, Any]:
        """
        Converte o modelo para um dicionário.
        """

        return {
            "id": self.id,
            "competencia": self.competencia,
            "setor": self.setor,
            "admissoes": self.admissoes,
            "demissoes": self.demissoes,
            "saldo": self.saldo,
            "atualizado_em": (
                self.atualizado_em.isoformat()
                if self.atualizado_em
                else None
            ),
        }