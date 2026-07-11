from src.api.database.conexao import SessionLocal
from src.api.database import repositorio


from src.api.database.conexao import SessionLocal
from src.api.database import repositorio

db = SessionLocal()

print("Total de registros:")

print(
    repositorio.contar_registros(db)
)