from fastapi import APIRouter

from database import get_db

router = APIRouter()

@router.get("/")
def ibge_root():
    return {"message": "IBGE endpoints - Implementar conforme necessidade"}

@router.get("/municipios")
def listar_municipios():
    """Placeholder for IBGE municipalities data"""
    return {
        "municipios": [
            {"id": 4209102, "nome": "Joinville", "estado": "SC"}
        ]
    }