# BACKLOG - CAGED API

## Objetivo

Este documento registra a evolução técnica do projeto CAGED API.

O objetivo é organizar as funcionalidades, melhorias e decisões arquitetônicas adotadas durante o desenvolvimento, permitindo acompanhar a evolução do sistema de forma semelhante ao fluxo de trabalho de equipes profissionais de engenharia de software.

---

# Histórico de Desenvolvimento

## Sessão 01

### Concluído

- Estruturação inicial do projeto.
- Configuração do ambiente Python.
- Configuração do PostgreSQL.
- Integração inicial com FastAPI.
- Organização inicial da estrutura de diretórios.

---

## Sessão 02

### Concluído

- Organização da arquitetura em camadas.
- Separação entre Routers, Database, Collectors, Services e Transformers.
- Ajustes na inicialização da aplicação.
- Padronização da estrutura do projeto.

---

## Sessão 03

### Concluído

- Configuração da conexão com o banco de dados.
- Criação dos Models.
- Implementação do Repository.
- Primeiros testes de persistência dos dados.

---

## Sessão 04

### Concluído

- Implementação da API REST.
- Desenvolvimento do CRUD do CAGED.
- Integração com Swagger/OpenAPI.
- Ajustes nos endpoints e respostas HTTP.

---

## Sessão 05

### Concluído

- Implementação da estrutura BaseCollector.
- Criação do CagedCollector.
- Criação do IBGECollector.
- Organização da camada de coleta de dados.

---

## Sessão 06

### Concluído

- Implementação dos Transformers.
- Estruturação do pipeline de transformação.
- Validação dos registros.
- Preparação dos dados para persistência no banco.

---

## Sessão 07 (20/07/2026)

### Concluído

- Auditoria completa da arquitetura do projeto.
- Revisão técnica dos principais arquivos.
- Refatoração e padronização do código.
- Revisão dos Routers.
- Revisão dos Collectors.
- Revisão dos Transformers.
- Revisão do Repository.
- Revisão dos Models.
- Revisão dos Services.
- Padronização das responsabilidades entre as camadas.
- Definição da estratégia de evolução do projeto.
- Criação do BACKLOG.md.

### Decisões arquitetônicas

- O projeto deixa de ser tratado como um projeto universitário e passa a ser desenvolvido como um ecossistema profissional.
- Todas as decisões técnicas deverão possuir justificativa arquitetônica.
- Novas tecnologias serão adotadas apenas quando resolverem um problema real do projeto.
- O desenvolvimento seguirá uma evolução incremental, semelhante ao fluxo utilizado em equipes profissionais.

---

# Backlog Atual

## Prioridade P0 (Versão 1.0)

- [ ] Implementar coleta oficial dos dados do CAGED.
- [ ] Implementar download automático dos arquivos.
- [ ] Processar os arquivos oficiais.
- [ ] Integrar Collector → Transformer → Repository.
- [ ] Finalizar o fluxo automático do Scheduler.
- [ ] Validar todo o pipeline de atualização.
- [ ] Concluir a integração prática com o IBGE.
- [ ] Revisar configurações da aplicação.

---

## Prioridade P1

- [ ] Melhorar tratamento de erros.
- [ ] Melhorar documentação técnica.
- [ ] Revisar desempenho das consultas.
- [ ] Revisar tratamento de exceções da API.

---

## Prioridade P2

- [ ] Implementar testes unitários.
- [ ] Implementar testes de integração.
- [ ] Configurar Docker.
- [ ] Configurar Docker Compose.
- [ ] Implementar GitHub Actions.
- [ ] Implementar Alembic.
- [ ] Adicionar Logging estruturado.
- [ ] Implementar Health Check.
- [ ] Configurar Observabilidade.
- [ ] Planejar Deploy.

---

# Objetivo Final

Construir um ecossistema de engenharia de software que represente um sistema profissional, aplicando boas práticas de arquitetura, qualidade de código e escalabilidade, servindo como portfólio para oportunidades em empresas nacionais e internacionais.

# Changelog

| Data | Versão | Descrição |
|------|---------|-----------|
| 20/07/2026 | v0.1 | Conclusão da primeira auditoria arquitetônica. |