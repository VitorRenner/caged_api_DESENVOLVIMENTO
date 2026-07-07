import os
import uvicorn

from src.api.app import app
from src.api.banco.conexao import Base, engine

def init_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_database()

    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
    )