from src.api.app import app

from src.api.banco.conexao import engine, Base

# Garante que as tabelas existam
Base.metadata.create_all(bind=engine)

def init_database():
    """Create all tables if they don't exist"""
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()

    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))

    print(f"Starting server at http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)