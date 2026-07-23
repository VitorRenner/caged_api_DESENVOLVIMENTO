from typing import Any

import pandas as pd


def transformar_municipios(
    dados: list[dict[str, Any]],
) -> pd.DataFrame:
    """
    Converte dados de municípios do IBGE para DataFrame.
    """

    if not dados:
        return pd.DataFrame()

    return pd.DataFrame(dados)


def buscar_municipio(
    dados: list[dict[str, Any]],
    nome: str = "Joinville",
) -> dict[str, Any] | None:
    """
    Busca um município pelo nome informado.
    """

    nome_normalizado = nome.strip().lower()

    for municipio in dados:
        nome_municipio = municipio.get("nome", "").strip().lower()

        if nome_municipio == nome_normalizado:
            return municipio

    return None
