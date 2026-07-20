from collectors import BaseCollector

BASE_URL = "https://servicodados.ibge.gov.br/api/v1"
CODIGO_JOINVILLE = 4209102


class IBGECollector(BaseCollector):
    """
    Responsável por coletar dados da API do IBGE.
    """

    def __init__(self) -> None:
        super().__init__(
            base_url=BASE_URL,
        )

    def _buscar_json(
            self,
            url: str,
    ) -> dict:
        """
        Realiza uma requisição GET e retorna o JSON da resposta.
        """

        try:
            response = self.session.get(
                url,
                timeout=30,
            )

            response.raise_for_status()

            return response.json()

        except Exception as erro:
            raise RuntimeError(
                f"Erro ao acessar a API do IBGE: {erro}"
            ) from erro

    def coletar(
            self,
            endpoint: str = "municipios",
    ) -> dict:
        """
        Coleta dados da API do IBGE.
        """

        url = (
            f"{self.base_url}"
            f"/localidades/estados/SC/{endpoint}"
        )

        return self._buscar_json(url)

    def buscar_joinville(self) -> dict:
        """
        Busca as informações de Joinville.
        """

        url = (
            f"{self.base_url}"
            f"/localidades/municipios/{CODIGO_JOINVILLE}"
        )

        return self._buscar_json(url)