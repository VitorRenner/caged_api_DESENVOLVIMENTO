import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from core.settings import settings

logger = logging.getLogger(__name__)

logger.info("Inicializando conexão com o banco de dados.")

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

Base = declarative_base()


def get_db() -> Session:
    """
    Cria uma sessão do banco de dados para a requisição
    e garante seu fechamento ao final do uso.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()