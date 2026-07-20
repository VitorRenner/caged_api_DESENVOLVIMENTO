from typing import TypedDict

import pandas as pd

COLUNAS_OBRIGATORIAS = (
    "competencia",
    "setor",
    "admissoes",
    "demissoes",
    "saldo",
)


class RegistroCaged(TypedDict):
    competencia: str
    setor: str
    admissoes: int
    demissoes: int
    saldo: int


def transformar_caged(
        df: pd.DataFrame,
) -> list[RegistroCaged]:
    """
    Prepara os dados do CAGED para salvar no banco.
    """

    if df.empty:
        return []

    colunas = {
        "competencia": "competencia",
        "setor": "setor",
        "admissoes": "admissoes",
        "demissoes": "demissoes",
        "saldo": "saldo",
    }

    df = df.rename(
        columns={
            antiga: nova
            for antiga, nova in colunas.items()
            if antiga in df.columns
        }
    )

    for coluna in COLUNAS_OBRIGATORIAS:

        if coluna not in df.columns:
            df[coluna] = 0

    for coluna in (
            "admissoes",
            "demissoes",
            "saldo",
    ):

        df[coluna] = (
            pd.to_numeric(
                df[coluna],
                errors="coerce",
            )
            .fillna(0)
            .astype(int)
        )

    df["competencia"] = (
        df["competencia"]
        .astype(str)
        .str[:6]
    )

    df["setor"] = (
        df["setor"]
        .astype(str)
        .str[:100]
    )

    return df[
        list(COLUNAS_OBRIGATORIAS)
    ].to_dict("records")


def validar_dados(
        registros: list[RegistroCaged],
) -> tuple[
    list[RegistroCaged],
    list[dict],
]:
    """
    Separa os registros válidos dos inválidos.
    """

    validos = []
    invalidos = []

    for indice, registro in enumerate(registros):

        erros = []

        if (
                not registro.get("competencia")
                or len(str(registro["competencia"])) != 6
        ):
            erros.append(
                "Competência deve estar no formato YYYYMM."
            )

        if not registro.get("setor"):
            erros.append(
                "Setor não informado."
            )

        for campo in (
                "admissoes",
                "demissoes",
                "saldo",
        ):

            if not isinstance(
                    registro.get(campo),
                    (int, float),
            ):
                erros.append(
                    f"{campo} deve ser numérico."
                )

        if erros:

            registro_invalido = registro.copy()
            registro_invalido["_erros"] = erros
            registro_invalido["_linha"] = indice

            invalidos.append(registro_invalido)

        else:

            validos.append(registro)

    return validos, invalidos