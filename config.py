import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres@localhost:5432/chat_db")
    ENV: str = os.getenv("ENV", "dev")

settings = Settings()
