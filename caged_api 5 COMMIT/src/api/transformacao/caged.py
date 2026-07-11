import pandas as pd

def transformar_caged(df: pd.DataFrame) -> List[Dict]:
    """
    Transform raw CAGED DataFrame to database format.

    Args:
        df: Raw DataFrame from CAGED files

    Returns:
        List of dictionaries ready for database insertion
    """
    if df.empty:
        return []

    # Expected columns mapping (adjust based on actual data format)
    column_mapping = {
        'competencia': 'competencia',
        'setor': 'setor',
        'admissoes': 'admissoes',
        'demissoes': 'demissoes',
        'saldo': 'saldo'
    }

    # Rename columns if necessary
    for old, new in column_mapping.items():
        if old in df.columns:
            df = df.rename(columns={old: new})

    # Ensure required columns exist
    required = ['competencia', 'setor', 'admissoes', 'demissoes', 'saldo']
    for col in required:
        if col not in df.columns:
            df[col] = 0

    # Convert types
    df['admissoes'] = pd.to_numeric(df['admissoes'], errors='coerce').fillna(0).astype(int)
    df['demissoes'] = pd.to_numeric(df['demissoes'], errors='coerce').fillna(0).astype(int)
    df['saldo'] = pd.to_numeric(df['saldo'], errors='coerce').fillna(0).astype(int)
    df['competencia'] = df['competencia'].astype(str).str[:6]
    df['setor'] = df['setor'].astype(str).str[:100]

    # Convert to list of dicts
    registros = df[required].to_dict('records')

    return registros

def validar_dados(registros: List[Dict]) -> tuple:
    """
    Validate CAGED data before insertion.

    Args:
        registros: List of record dictionaries

    Returns:
        Tuple of (valid_records, invalid_records)
    """
    valid = []
    invalid = []

    for idx, reg in enumerate(registros):
        errors = []

        # Check required fields
        if not reg.get('competencia') or len(str(reg['competencia'])) != 6:
            errors.append("competencia must be 6 characters (YYYYMM)")

        if not reg.get('setor'):
            errors.append("setor is required")

        # Check numeric fields
        for field in ['admissoes', 'demissoes', 'saldo']:
            if not isinstance(reg.get(field), (int, float)):
                errors.append(f"{field} must be numeric")

        if errors:
            reg['_errors'] = errors
            reg['_index'] = idx
            invalid.append(reg)
        else:
            valid.append(reg)

    return valid, invalid

    def transformar_caged(dados):
        return {
            "Município": "Joinville",
            "saldo": saldo
        }
