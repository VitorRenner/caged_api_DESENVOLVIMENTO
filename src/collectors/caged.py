import os

import pandas as pd

from src.api.coleta.base import BaseCollector

class CagedCollector(BaseCollector):

    def __init__(self):

        super().__init__(
            base_url="https://portaldatransparencia.gov.br"
        )

        self.download_folder = "data/caged"

        os.makedirs(
            self.download_folder,
            exist_ok=True
        )

    def coletar(
            self,
            ano: int = 2024,
            mes: int = 1
    ) -> pd.DataFrame:

        print(
            f"Coletando dados CAGED {ano}/{mes:02d}"
        )

        return pd.DataFrame(
            columns=[
                "competencia",
                "municipio",
                "setor",
                "admissoes",
                "demissoes",
                "saldo"
            ]
        )

    def processar_arquivo_local(
            self,
            file_path: str
    ) -> pd.DataFrame:

        if not os.path.exists(
                file_path
        ):

            raise FileNotFoundError(
                f"Arquivo não encontrado: {file_path}"
            )

        df = self.read_excel(
            file_path
        )

        if (
                not df.empty
                and "municipio" in df.columns
        ):
            df = df[
                df["municipio"] == 4209102
                ]

        return df