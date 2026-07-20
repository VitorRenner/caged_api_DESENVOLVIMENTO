from sqlalchemy.orm import Session

from database import CagedMovimentacao


def buscar_caged(
        db: Session,
        competencia: str | None = None,
        setor: str | None = None,
        skip: int = 0,
        limit: int = 100,
) -> list[CagedMovimentacao]:
    """
    Busca os registros do CAGED com filtros opcionais.
    """

    query = db.query(CagedMovimentacao)

    if competencia:
        query = query.filter(
            CagedMovimentacao.competencia == competencia
        )

    if setor:
        query = query.filter(
            CagedMovimentacao.setor.ilike(f"%{setor}%")
        )

    return query.offset(skip).limit(limit).all()


def buscar_por_id(
        db: Session,
        registro_id: int,
) -> CagedMovimentacao | None:
    """
    Busca um registro pelo ID.
    """

    return (
        db.query(CagedMovimentacao)
        .filter(CagedMovimentacao.id == registro_id)
        .first()
    )


def contar_registros(
        db: Session,
) -> int:
    """
    Retorna a quantidade de registros cadastrados.
    """

    return db.query(CagedMovimentacao).count()


def upsert_caged(
        db: Session,
        registros: list[dict],
) -> int:
    """
    Cria novos registros ou atualiza os existentes.
    """

    processados = 0

    try:
        for dados in registros:

            registro = (
                db.query(CagedMovimentacao)
                .filter(
                    CagedMovimentacao.competencia == dados["competencia"],
                    CagedMovimentacao.setor == dados["setor"],
                    )
                .first()
            )

            if registro:
                registro.saldo = dados["saldo"]
                registro.admissoes = dados["admissoes"]
                registro.demissoes = dados["demissoes"]
            else:
                db.add(CagedMovimentacao(**dados))

            processados += 1

        db.commit()
        return processados

    except Exception:
        db.rollback()
        raise


def deletar_caged(
        db: Session,
        registro_id: int,
) -> bool:
    """
    Remove um registro pelo ID.
    """

    registro = buscar_por_id(db, registro_id)

    if registro is None:
        return False

    db.delete(registro)
    db.commit()

    return True