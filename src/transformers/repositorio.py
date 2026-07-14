from sqlalchemy.orm import Session

from database import CagedMovimentacao


def buscar_caged(
        db: Session,
        competencia=None,
        setor=None,
        skip=0,
        limit=100
):

    query = db.query(
        CagedMovimentacao
    )

    if competencia:

        query = query.filter(
            CagedMovimentacao.competencia
            == competencia
        )

    if setor:

        query = query.filter(
            CagedMovimentacao.setor.ilike(
                f"%{setor}%"
            )
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def buscar_por_id(
        db: Session,
        id: int
):

    return (
        db.query(CagedMovimentacao)
        .filter(
            CagedMovimentacao.id == id
        )
        .first()
    )


def contar_registros(
        db: Session
):

    return (
        db.query(
            CagedMovimentacao
        )
        .count()
    )


def upsert_caged(
        db: Session,
        registros: list[dict]
) -> int:

    processados = 0

    for dados in registros:

        existente = (
            db.query(CagedMovimentacao)
            .filter(
                CagedMovimentacao.competencia
                == dados["competencia"],
                CagedMovimentacao.setor
                == dados["setor"]
            )
            .first()
        )

        if existente:

            existente.saldo = dados["saldo"]
            existente.admissoes = dados["admissoes"]
            existente.demissoes = dados["demissoes"]

        else:

            novo = CagedMovimentacao(
                **dados
            )

            db.add(novo)

        processados += 1

    db.commit()

    return processados


def deletar_caged(
        db: Session,
        id: int
):

    registro = buscar_por_id(
        db,
        id
    )

    if not registro:
        return False

    db.delete(registro)

    db.commit()

    return True