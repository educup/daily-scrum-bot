from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    mongo_db_server: str
    logging_level: int

    class Config:
        env_file = ".env"


settings = Settings()


def get_settings():
    return settings
