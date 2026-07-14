from database import engine, Base

from database import CagedMovimentacao

# Importa os models antes de criar
from database import CagedMovimentacao

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso.")