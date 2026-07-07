Dia 1 - 16/06/2026: Início da estrutura do novo projeto
# Apagamos os arquivos corrompidos antigos do início do projeto. Nele, haviam x problemas:

# Ficamos 10 dias tentando fazer  o projeto com configurações erradas , estrutura e arquitetura erradas, sem pluggins e
biblioteca e sem o .venv e uv da raíz do projeto finalizado

-Então fizemos tudo do zero. Novo projeto, novas configurações. Tudo zerado.
- 
-  Enfrentamos estes desafios no novo projeto:

-> Erro de finalização das configurações para início da estrutura e arquitetura do projeto. 

-> Falta de algumas bibliotecas instaladas na IDE (Intellij) e pluggins para o começo da estrutura do projeto.

-> Arquivos corrompidos, dificultando o início da API.

-> Pip e .venv (crucial para a instalação das bibliotecas) faltando.


No final do dia, conseguimos configurar todo o ambiente de trabalho, estrutura e arquitetura dos dados. 

# 17/06/2026

- Códigos base da estrtura inicial do projeto finalizados, com o auxílio deferramentas de Inteligência Artificial
- para estudo, vídeoaulas e PDF para a base de dados inicial da API. 
- Parte da documentação foi feita no dia. 

# 18/06/2026

- Finalização das documentações do dia, início dos testes. Agora vamos falar sobre o objetivo até a próxima reunião:

1. Dentro do arquivo: src/api/coleta/caged.py, vamos usar, dentro desse arquivo com início, os métodos:

-> CRUD ( CREATE, READ, UPDATE, DELETE) -> (CRIAR, LER, ATUALIZAR, E DELETAR)

Observação: Outro método de tratamento de dados que usaremos é o ETL (Extrair, Transformar e carregar, do inglês)

- Este tipo de prática será muito útil para chamarmos a requisição HTTP, buscando da URL do site oficial do caged. 
- O primeiro passo é apenas buscar. Depois disso vamos para:
- 1. Extraír os dados do site/api. (Esses dados ficarão salvos temporáriamente na memória RAM local)
- 2. Após a extração, usaremos o banco, fazendo conexão com ele, de início, localmente. Aí passamos os dados que estavam
- 3. Salvos na memória secundária para o banco (para disco local)
- 4. Agora que os dados já estão localmente no banco, precisamos definir tabelas para padronizar os dados estraidos.
- 5. Fazer de fato, o backend (python e cia) ligar -se por completo com  o banco. 
- 6. Executar o ETL de fato. Quando funcionar, ele irá atualizar automaticamente o site, com backend com banco. Basta 
um F5, e tudo atualiza.

22/06/2026
Na semana passada, conectamos, em tese, a API com python e fastapi com o banco. Sofremos algumas alterações nos nomes e 
endereços, então demorou um pouco mais do que o esperado. Agora, por final, o banco está conectado com a API, e agora 
mesmo, estamos criando tabelas para já começar a popular o banco como teste, e a API funcionar.


23/06/2026

Projeto em andamento:

-> API inicial funcionando 

-> Banco 100% conectado

-> Site local para visualizar dados armazenados finalizado e já atualizado automáticamente

-> Tabelas saem da API e chegam ao banco automáticamente e corretamente

-> Reestruturação da arquitetura do projeto em andamento para uma API  mais rápida e efetiva

-> Testes unitários finalizados.


