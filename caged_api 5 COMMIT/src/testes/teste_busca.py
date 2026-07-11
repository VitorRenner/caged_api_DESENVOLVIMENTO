from src.api.database.conexao import SessionLocal
from src.api.database.repositorio import buscar_caged

db = SessionLocal()

registros = buscar_caged(db)

for registro in registros:
    print(
        registro.to_dict()
    )