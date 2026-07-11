from src.api.database.conexao import engine, Base

from src.api.database.models import CagedMovimentacao

# Importa os models antes de criar
from src.api.database.models import CagedMovimentacao

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso.")