from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CSV-CTI"
    SECRET_KEY: str = "your-secret-key"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/dbname"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
