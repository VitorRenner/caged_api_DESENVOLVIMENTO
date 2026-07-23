import logging
from datetime import datetime
from time import perf_counter

logger = logging.getLogger(__name__)

LOG_SEPARATOR = "=" * 50


def atualizar_caged() -> None:
    """
    Executa o fluxo completo de atualização dos dados do CAGED.
    """

    inicio = datetime.now()
    inicio_execucao = perf_counter()

    logger.info(LOG_SEPARATOR)
    logger.info("Iniciando atualização do CAGED...")
    logger.info(
        "Data e hora: %s",
        inicio.strftime("%d/%m/%Y %H:%M:%S"),
    )
    logger.info(LOG_SEPARATOR)

    try:
        # Fluxo da atualização:
        # - Coletar os dados
        # - Transformar os dados
        # - Validar os dados
        # - Persistir no banco de dados

        logger.info("Atualização do CAGED finalizada com sucesso.")

    except Exception:
        logger.exception("Erro durante a atualização do CAGED.")
        raise

    finally:
        duracao = perf_counter() - inicio_execucao

        logger.info(
            "Tempo de execução: %.2f segundos.",
            duracao,
        )
