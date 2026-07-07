# CAGED API - Joinville

API para gerenciamento de dados do CAGED (Cadastro Geral de Empregados e Desempregados) para a cidade de Joinville/SC.

## Setup

1. Instale as dependências:
```bash
pip install -r requirements.txt

Documento após Versão 1 da Arquitetura estrutural do projeto:

Projeto CAGED API

Como instalar:

uv sync

Como criar tabelas:

uv run -m src.scripts.criar_tabelas

Como iniciar a API:

uv run uvicorn src.api.app:app --reload

Swagger:

http://127.0.0.1:8000/docs