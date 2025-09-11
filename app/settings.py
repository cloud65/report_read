from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    admin_secret: str = "123456789"

    class Config:
        env_file = ".env"


settings = Settings()
