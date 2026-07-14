from sqlalchemy import text

from database import engine


def testar_conexao():
    """
    Faz um teste simples para verificar
    se o PostgreSQL está respondendo.
    """

    try:
        with engine.connect() as conexao:
            conexao.execute(text("SELECT 1"))

        print("Conexão com o banco realizada com sucesso.")

    except Exception as erro:
        print("Erro ao conectar com o banco:")
        print(erro)


if __name__ == "__main__":
    testar_conexao()