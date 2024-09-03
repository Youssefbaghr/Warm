import os
import logging
from dotenv import load_dotenv
from src.ping import ping_all_apis
from src.scheduler import start_scheduler
from src.config import Config

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(Config.LOG_FILE)
        ]
    )
    return logging.getLogger(__name__)

def load_urls_from_env():
    return [value for key, value in os.environ.items() if key.startswith("API_URL_")]

def main():
    load_dotenv()
    logger = setup_logging()
    logger.info("Starting Warm - API Warming Service")

    try:
        urls = load_urls_from_env()
        if not urls:
            logger.warning("No API URLs found in environment variables.")
            return

        logger.info(f"Loaded {len(urls)} URLs. Ping interval set to {Config.PING_INTERVAL} minutes.")
        start_scheduler(test_mode=False)  # Run in normal mode
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()