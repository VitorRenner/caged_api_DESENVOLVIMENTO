from typing import TypedDict

import pandas as pd

COLUNAS_OBRIGATORIAS = (
    "competencia",
    "setor",
    "admissoes",
    "demissoes",
    "saldo",
)

MAPEAMENTO_COLUNAS = {
    "competencia": "competencia",
    "setor": "setor",
    "admissoes": "admissoes",
    "demissoes": "demissoes",
    "saldo": "saldo",
}


class RegistroCaged(TypedDict):
    """
    Estrutura esperada de um registro do CAGED.
    """

    competencia: str
    setor: str
    admissoes: int
    demissoes: int
    saldo: int


def transformar_caged(
    df: pd.DataFrame,
) -> list[RegistroCaged]:
    """
    Padroniza os dados do CAGED para persistência no banco.
    """

    if df.empty:
        return []

    df = df.rename(
        columns={
            antiga: nova
            for antiga, nova in MAPEAMENTO_COLUNAS.items()
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

    df["competencia"] = df["competencia"].astype(str).str[:6]

    df["setor"] = df["setor"].astype(str).str[:100]

    return df[list(COLUNAS_OBRIGATORIAS)].to_dict(orient="records")


def validar_dados(
    registros: list[RegistroCaged],
) -> tuple[
    list[RegistroCaged],
    list[dict],
]:
    """
    Valida registros antes da gravação no banco.
    """

    registros_validos = []
    registros_invalidos = []

    for indice, registro in enumerate(registros):
        erros = []

        competencia = str(registro["competencia"])

        if len(competencia) != 6 or not competencia.isdigit():
            erros.append("Competência deve estar no formato YYYYMM.")

        if not registro.get("setor"):
            erros.append("Setor não informado.")

        for campo in (
            "admissoes",
            "demissoes",
            "saldo",
        ):
            valor = registro.get(campo)

            if not isinstance(valor, int):
                erros.append(f"{campo} deve ser numérico.")
                continue

            if valor < 0:
                erros.append(f"{campo} não pode ser negativo.")

        if erros:
            registro_invalido = registro.copy()

            registro_invalido["_erros"] = erros
            registro_invalido["_linha"] = indice

            registros_invalidos.append(registro_invalido)

        else:
            registros_validos.append(registro)

    return (
        registros_validos,
        registros_invalidos,
    )
