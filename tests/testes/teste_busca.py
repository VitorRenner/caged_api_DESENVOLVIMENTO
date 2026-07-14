from database import SessionLocal
from database import buscar_caged

db = SessionLocal()

registros = buscar_caged(db)

for registro in registros:
    print(
        registro.to_dict()
    )