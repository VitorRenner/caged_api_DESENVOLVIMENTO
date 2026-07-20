from apscheduler.schedulers.background import BackgroundScheduler

from services import atualizar_caged

scheduler = BackgroundScheduler()


def iniciar_scheduler() -> None:
    """
    Inicia o scheduler caso ele ainda não esteja rodando.
    """

    if scheduler.running:
        return

    scheduler.add_job(
        atualizar_caged,
        trigger="interval",
        seconds=30,
        id="atualizacao_caged",
        replace_existing=True,
    )

    scheduler.start()

    print("✅ Scheduler iniciado.")


def parar_scheduler() -> None:
    """
    Encerra o scheduler.
    """

    if not scheduler.running:
        return

    scheduler.shutdown(wait=False)

    print("🛑 Scheduler encerrado.")