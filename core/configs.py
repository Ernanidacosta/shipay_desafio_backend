from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Configurações gerais da aplicação
    """

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'sqlite+aiosqlite:///database.db'

    class Config:
        case_sensitive = True


settings: Settings = Settings()
