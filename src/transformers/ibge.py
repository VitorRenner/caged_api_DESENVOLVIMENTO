from typing import Any

import pandas as pd


def transformar_municipios(
        dados: list[dict[str, Any]],
) -> pd.DataFrame:
    """
    Converte os dados da API do IBGE para um DataFrame.
    """

    if not dados:
        return pd.DataFrame()

    return pd.DataFrame(dados)


def buscar_municipio(
        dados: list[dict[str, Any]],
        nome: str = "Joinville",
) -> dict[str, Any] | None:
    """
    Procura um município pelo nome.
    """

    nome = nome.strip().lower()

    for municipio in dados:

        if (
                municipio.get("nome", "")
                        .strip()
                        .lower()
                == nome
        ):
            return municipio

    return None