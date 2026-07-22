from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
import requests
from pandas.errors import ParserError


class BaseCollector(ABC):
    """
    Classe base para todos os coletores do projeto.
    """

    DEFAULT_TIMEOUT = 30

    def __init__(
            self,
            base_url: str,
            session: requests.Session | None = None,
    ) -> None:
        """
        Inicializa o coletor.
        """
        self.base_url = base_url
        self.session = session or requests.Session()

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
                timeout=self.DEFAULT_TIMEOUT,
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

        except requests.RequestException as erro:
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

        except (
                FileNotFoundError,
                PermissionError,
                ValueError,
                ParserError,
        ) as erro:
            raise RuntimeError(
                f"Erro ao ler o arquivo Excel: {erro}"
            ) from erro