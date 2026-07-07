from abc import ABC, abstractmethod

import pandas as pd
import requests

class BaseCollector(ABC):

    def __init__(
            self,
            base_url: str
    ):

        self.base_url = base_url

        self.session = requests.Session()

    @abstractmethod
    def coletar(
            self,
            **kwargs
    ):
        pass

    def download_file(
            self,
            url: str,
            save_path: str
    ) -> bool:

        try:

            response = self.session.get(
                url,
                stream=True,
                timeout=30
            )

            response.raise_for_status()

            with open(
                    save_path,
                    "wb"
            ) as arquivo:

                for chunk in response.iter_content(
                        chunk_size=8192
                ):
                    arquivo.write(chunk)

            return True

        except Exception as erro:

            raise Exception(
                f"Erro ao baixar arquivo: {erro}"
            )

    def read_excel(
            self,
            file_path: str,
            **kwargs
    ) -> pd.DataFrame:

        try:

            return pd.read_excel(
                file_path,
                **kwargs
            )

        except Exception as erro:

            print(
                f"Erro ao ler Excel: {erro}"
            )

            return pd.DataFrame()
