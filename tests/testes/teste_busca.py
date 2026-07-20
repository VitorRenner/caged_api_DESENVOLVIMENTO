from database import SessionLocal, buscar_caged

db = SessionLocal()

registros = buscar_caged(db)

for registro in registros:
    print(
        registro.to_dict()
    )