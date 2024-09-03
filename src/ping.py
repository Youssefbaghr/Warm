import asyncio
import aiohttp
import logging
from typing import List, Dict
from src.config import Config

logger = logging.getLogger(__name__)

async def ping_api(session: aiohttp.ClientSession, url: str) -> Dict[str, any]:
    start_time = asyncio.get_event_loop().time()
    try:
        async with session.get(url, timeout=30) as response:
            elapsed_time = asyncio.get_event_loop().time() - start_time
            return {
                "url": url,
                "status_code": response.status,
                "response_time": elapsed_time,
                "success": response.status == 200
            }
    except aiohttp.ClientError as e:
        elapsed_time = asyncio.get_event_loop().time() - start_time
        logger.error(f"Error pinging {url}: {str(e)}")
        return {
            "url": url,
            "status_code": None,
            "response_time": elapsed_time,
            "success": False,
            "error": str(e)
        }

async def ping_all_apis() -> None:
    urls = Config.API_URLS
    if not urls:
        logger.warning("No API URLs found in configuration.")
        return

    logger.info(f"Pinging {len(urls)} API URLs.")
    async with aiohttp.ClientSession() as session:
        tasks = [ping_api(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for result in results:
        if result["success"]:
            logger.info(f"Successfully pinged {result['url']} in {result['response_time']:.2f} seconds")
        else:
            logger.error(f"Failed to ping {result['url']}: {result.get('error', f'Status code {result['status_code']}')})")