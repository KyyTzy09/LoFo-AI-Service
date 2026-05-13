from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    app_name: str = ""
    env: str = ""

    secret_token: str = "LoFo-AI-API"
    gemini_api_key: str = ""
    openai_api_key: str = ""
    openai_temperature: float = 0.6

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()