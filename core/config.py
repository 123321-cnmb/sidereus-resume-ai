from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MY_REAL_API_KEY: str
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    MAX_TOKEN_LIMIT: int = 15000

    class Config:
        env_file = ".env"

settings = Settings()