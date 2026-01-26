from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import Dict, List
load_dotenv(override=True)
class Settings(BaseSettings):
    LLM_API_KEY : str
    LLM_CHAT_MODEL : str
    LLM_BASE_URL : str
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"
        env_file_encoding = "utf-8"
settings = Settings()