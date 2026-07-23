# Importa os modelos para registrá-los no SQLAlchemy.
from src.database import models  # noqa: F401
from src.database.conexao import Base, engine

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso.")
