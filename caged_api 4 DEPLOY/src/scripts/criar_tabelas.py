from src.api.banco.conexao import engine, Base

from src.api.banco.models import CagedMovimentacao

# Importa os models antes de criar
from src.api.banco.models import CagedMovimentacao

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso.")