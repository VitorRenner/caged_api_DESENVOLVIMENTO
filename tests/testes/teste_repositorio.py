from database import SessionLocal
from database import repositorio


from database import SessionLocal
from database import repositorio

db = SessionLocal()

print("Total de registros:")

print(
    repositorio.contar_registros(db)
)