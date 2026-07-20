from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
import requests


class BaseCollector(ABC):
    """
    Classe base para todos os coletores do projeto.
    """

    def __init__(
            self,
            base_url: str,
    ) -> None:
        """
        Inicializa o coletor.
        """
        self.base_url = base_url
        self.session = requests.Session()

    @abstractmethod
    def coletar(
            self,
            **kwargs,
    ) -> Any:
        """
        Método que deve ser implementado pelos coletores.
        """
        raise NotImplementedError

    def download_file(
            self,
            url: str,
            caminho_arquivo: str,
    ) -> bool:
        """
        Faz o download de um arquivo.
        """
        try:
            response = self.session.get(
                url,
                stream=True,
                timeout=30,
            )

            response.raise_for_status()

            with open(
                    caminho_arquivo,
                    "wb",
            ) as arquivo:

                for chunk in response.iter_content(
                        chunk_size=8192,
                ):
                    if chunk:
                        arquivo.write(chunk)

            return True

        except Exception as erro:
            raise RuntimeError(
                f"Erro ao baixar arquivo: {erro}"
            ) from erro

    def read_excel(
            self,
            caminho_arquivo: str,
            **kwargs,
    ) -> pd.DataFrame:
        """
        Lê um arquivo Excel.
        """
        try:
            return pd.read_excel(
                caminho_arquivo,
                **kwargs,
            )

        except Exception as erro:
            raise RuntimeError(
                f"Erro ao ler o arquivo Excel: {erro}"
            ) from erro