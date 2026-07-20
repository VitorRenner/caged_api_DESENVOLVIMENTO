from database import Base, engine

# Importa os models antes de criar

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso.")