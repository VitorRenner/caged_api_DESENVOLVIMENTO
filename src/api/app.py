from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import caged, ibge
app = FastAPI(
    title="CAGED API - Joinville",
    description="API para dados de emprego e desemprego de Joinville/SC",
    version="1.0.0"
)

# CORS - Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
            "ibge": "/ibge"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}