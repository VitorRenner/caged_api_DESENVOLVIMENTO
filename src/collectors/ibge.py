import pandas as pd

from collectors import BaseCollector

class IBGECollector(BaseCollector):
    """
    Collector for IBGE (Brazilian Institute of Geography and Statistics) data.
    """

    def __init__(self):
        super().__init__(base_url="https://servicodados.ibge.gov.br/api/v1")

    def coletar(self, endpoint: str = "municipios") -> dict:
        """
        Collect data from IBGE API.

        Args:
            endpoint: API endpoint to query

        Returns:
            JSON response as dictionary
        """
        url = f"{self.base_url}/localidades/estados/SC/{endpoint}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error collecting IBGE data: {e}")
            return {}

    def get_joinville_info(self) -> dict:
        """Get specific information about Joinville"""
        # Joinville municipality code: 4209102
        url = f"{self.base_url}/localidades/municipios/4209102"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return {"nome": "Joinville", "id": 4209102}