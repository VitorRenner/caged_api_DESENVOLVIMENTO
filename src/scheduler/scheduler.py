from apscheduler.schedulers.background import BackgroundScheduler

from services import atualizar_caged

scheduler = BackgroundScheduler()


def iniciar_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            atualizar_caged,
            trigger="interval",
            seconds=30,
            id="atualizacao_caged",
            replace_existing=True,
        )

        scheduler.start()

        print("✅ Scheduler iniciado.")


def parar_scheduler():
    if scheduler.running:
        scheduler.shutdown(wait=False)
        print("🛑 Scheduler encerrado.")