import os

import uvicorn

from database import Base, engine
from transformers import app

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))


def initialize_database() -> None:
    """
    Cria todas as tabelas definidas nos modelos do SQLAlchemy,
    caso ainda não existam.
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    initialize_database()

    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
    )