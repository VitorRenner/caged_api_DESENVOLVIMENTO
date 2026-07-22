from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configurações globais da aplicação.
    """

    API_TITLE: str = "CAGED API - Joinville"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = (
        "API para dados do CAGED e IBGE."
    )

    DATABASE_URL: str

    CAGED_BASE_URL: str = (
        "https://portaldatransparencia.gov.br"
    )

    IBGE_BASE_URL: str = (
        "https://servicodados.ibge.gov.br/api/v1"
    )

    SCHEDULER_INTERVAL_SECONDS: int = 30

    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()