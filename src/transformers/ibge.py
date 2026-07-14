import pandas as pd

def transformar_municipios(data: List[Dict]) -> pd.DataFrame:
    """
    Transform IBGE municipalities data to DataFrame.

    Args:
        data: JSON response from IBGE API

    Returns:
        Processed DataFrame
    """
    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)
    return df

def extrair_joinville(data: List[Dict]) -> Dict:
    """
    Extract Joinville data from municipalities list.

    Args:
        data: List of municipalities

    Returns:
        Joinville data dictionary or empty dict
    """
    for municipio in data:
        if municipio.get('nome', '').lower() == 'joinville':
            return municipio
    return {}