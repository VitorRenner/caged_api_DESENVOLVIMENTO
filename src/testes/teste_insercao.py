from src.api.banco.conexao import SessionLocal
from src.api.banco.models import CagedMovimentacao

db = SessionLocal()

registro = CagedMovimentacao(
    competencia="202601",
    saldo=100,
    admissoes=150,
    demissoes=50,
    setor="Tecnologia"
)

db.add(registro)

db.commit()

print("Registro inserido com sucesso.")
