from src.api.banco.conexao import SessionLocal
from src.api.banco import repositorio


from src.api.banco.conexao import SessionLocal
from src.api.banco import repositorio

db = SessionLocal()

print("Total de registros:")

print(
    repositorio.contar_registros(db)
)