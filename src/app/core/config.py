from pydantic import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = (
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"
    )
    APP_TITLE: str = "Top-N Post Recs API"
    APP_VERSION: str = "0.1.0"

    class Config:
        env_file = ".env"

settings = Settings()

