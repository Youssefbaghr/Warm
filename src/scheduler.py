import asyncio
import schedule
import time
from concurrent.futures import ThreadPoolExecutor
from src.ping import ping_all_apis
from src.config import Config

def run_ping_all_apis():
    """Run the ping_all_apis coroutine in an event loop."""
    asyncio.run(ping_all_apis())

def start_scheduler(test_mode=False):
    """Start the scheduler to run the ping function at specified intervals."""
    schedule.every(Config.RUN_INTERVAL).minutes.do(run_ping_all_apis)
    
    # Run once immediately on startup
    run_ping_all_apis()
    
    if test_mode:
        # Run the scheduler for a limited number of iterations in test mode
        for _ in range(3):
            run_scheduler()
    else:
        # Run the scheduler indefinitely in normal mode
        while True:
            run_scheduler()

def run_scheduler():
    """Run the scheduler once."""
    schedule.run_pending()
    time.sleep(1)