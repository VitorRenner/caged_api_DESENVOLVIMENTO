import logging

from apscheduler.schedulers.background import BackgroundScheduler

from services import atualizar_caged

logger = logging.getLogger(__name__)

SCHEDULER_INTERVAL_SECONDS = 30

scheduler = BackgroundScheduler()


def iniciar_scheduler() -> None:
    """
    Inicia o scheduler caso ele ainda não esteja rodando.
    """

    if scheduler.running:
        logger.info(
            "O scheduler já está em execução."
        )
        return

    try:
        scheduler.add_job(
            atualizar_caged,
            trigger="interval",
            seconds=SCHEDULER_INTERVAL_SECONDS,
            id="atualizacao_caged",
            name="Atualização automática do CAGED",
            replace_existing=True,
        )

        scheduler.start()

        logger.info(
            "Scheduler iniciado com sucesso."
        )

    except Exception:
        logger.exception(
            "Erro ao iniciar o scheduler."
        )
        raise


def parar_scheduler() -> None:
    """
    Encerra o scheduler.
    """

    if not scheduler.running:
        logger.info(
            "O scheduler já está parado."
        )
        return

    try:
        scheduler.shutdown(
            wait=False,
        )

        logger.info(
            "Scheduler encerrado com sucesso."
        )

    except Exception:
        logger.exception(
            "Erro ao encerrar o scheduler."
        )
        raise