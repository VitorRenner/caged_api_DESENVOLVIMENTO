import logging
import sys

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def configurar_logging(
    nivel: int = logging.INFO,
) -> None:
    """
    Configura o sistema de logs da aplicação.
    """

    logging.basicConfig(
        level=nivel,
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT,
        stream=sys.stdout,
        force=True,
    )
