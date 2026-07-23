from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from pandas.errors import ParserError


class BaseCollector(ABC):
    """
    Classe base para todos os coletores do projeto.
    """

    REQUEST_TIMEOUT_SECONDS = 30
    DOWNLOAD_CHUNK_SIZE = 8192

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
        **kwargs: Any,
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
                timeout=self.REQUEST_TIMEOUT_SECONDS,
            )
            response.raise_for_status()

            with Path(caminho_arquivo).open("wb") as arquivo:
                for chunk in response.iter_content(
                    chunk_size=self.DOWNLOAD_CHUNK_SIZE,
                ):
                    if chunk:
                        arquivo.write(chunk)

            return True

        except requests.RequestException as erro:
            raise RuntimeError(f"Erro ao baixar arquivo: {erro}") from erro

    def read_excel(
        self,
        caminho_arquivo: str,
        **kwargs: Any,
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
            raise RuntimeError(f"Erro ao ler o arquivo Excel: {erro}") from erro
