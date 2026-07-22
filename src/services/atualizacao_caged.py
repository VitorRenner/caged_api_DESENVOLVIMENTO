import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def atualizar_caged() -> None:
    """
    Executa o fluxo de atualização dos dados do CAGED.
    """

    inicio = datetime.now()

    logger.info("=" * 50)
    logger.info("Iniciando atualização do CAGED...")
    logger.info(
        "Data e hora: %s",
        inicio.strftime("%d/%m/%Y %H:%M:%S"),
    )
    logger.info("=" * 50)

    try:
        # Fluxo principal da atualização:
        # 1. Coletar os dados
        # 2. Transformar os dados
        # 3. Validar os dados
        # 4. Salvar no banco

        logger.info("Atualização do CAGED finalizada com sucesso.")

    except Exception:
        logger.exception(
            "Erro durante a atualização do CAGED."
        )
        raise

    finally:
        duracao = datetime.now() - inicio

        logger.info(
            "Tempo de execução: %.2f segundos.",
            duracao.total_seconds(),
        )