import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN", "")
    PHONE_NUMBER_ID: str = os.getenv("PHONE_NUMBER_ID", "")
    VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN", "verify_me")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    WHATSAPP_API_URL = "https://graph.facebook.com/v18.0"

settings = Settings()