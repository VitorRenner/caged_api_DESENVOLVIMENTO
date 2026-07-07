from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import caged, ibge
from src.api.scheduler.scheduler import (
    iniciar_scheduler,
    parar_scheduler,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Executa ações quando a API inicia e quando é encerrada.
    """
    iniciar_scheduler()
    yield
    parar_scheduler()


app = FastAPI(
    title="CAGED API - Joinville",
    description="API para dados de emprego e desemprego de Joinville/SC",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS - Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://seudominio.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(caged.router, prefix="/caged", tags=["CAGED"])
app.include_router(ibge.router, prefix="/ibge", tags=["IBGE"])


@app.get("/")
def root():
    return {
        "message": "CAGED API - Joinville",
        "docs": "/docs",
        "endpoints": {
            "caged": "/caged",
            "ibge": "/ibge",
        },
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
