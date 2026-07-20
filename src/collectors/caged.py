import logging
import os

import pandas as pd

from collectors import BaseCollector

BASE_URL = "https://portaldatransparencia.gov.br"
CODIGO_JOINVILLE = 4209102

logger = logging.getLogger(__name__)


class CagedCollector(BaseCollector):
    """
    Responsável por coletar os dados do CAGED.
    """

    def __init__(self) -> None:
        super().__init__(
            base_url=BASE_URL,
        )

        self.download_folder = os.path.join(
            "data",
            "caged",
        )

        os.makedirs(
            self.download_folder,
            exist_ok=True,
        )

    def coletar(
            self,
            ano: int = 2024,
            mes: int = 1,
    ) -> pd.DataFrame:
        """
        Coleta os dados do CAGED.
        """

        if not 1 <= mes <= 12:
            raise ValueError("O mês deve estar entre 1 e 12.")

        logger.info(
            "Coletando dados do CAGED - %02d/%d",
            mes,
            ano,
        )

        # Aqui ficará a lógica de download do CAGED.
        return pd.DataFrame(
            columns=[
                "competencia",
                "municipio",
                "setor",
                "admissoes",
                "demissoes",
                "saldo",
            ]
        )

    def processar_arquivo_local(
            self,
            caminho_arquivo: str,
            codigo_municipio: int = CODIGO_JOINVILLE,
    ) -> pd.DataFrame:
        """
        Lê um arquivo local e retorna os dados do município informado.
        """

        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(
                f"Arquivo não encontrado: {caminho_arquivo}"
            )

        df = self.read_excel(caminho_arquivo)

        if not df.empty and "municipio" in df.columns:
            df = df[
                df["municipio"] == codigo_municipio
                ]

        return df