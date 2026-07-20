from database import SessionLocal, repositorio

db = SessionLocal()

print("Total de registros:")

print(
    repositorio.contar_registros(db)
)