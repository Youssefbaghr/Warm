import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_URLS = [value for key, value in os.environ.items() if key.startswith("API_URL_")]
    PING_INTERVAL = int(os.getenv("PING_INTERVAL", 60))
    RUN_INTERVAL = int(os.getenv("RUN_INTERVAL", 12 * 60))  # 12 hours in minutes
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "warm.log")