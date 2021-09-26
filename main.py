import asyncio
import logging
import time

from pathlib import Path
from typing import List

from yarl import URL

from async_web_scraper.fetch import scrape_all

log = logging.getLogger(__name__)


async def main(urls: List[URL]) -> None:
    output_dir = Path(__file__).parent / "output"
    await scrape_all(output_dir, urls)


def configure_logging():
    """Some basic log config."""
    logging.basicConfig(format="%(asctime)s - %(levelname)s: %(message)s",
                        filename="async_web_scraper.log",
                        filemode="w",
                        level=logging.INFO)


if __name__ == "__main__":
    configure_logging()
    search_urls = []
    start = time.perf_counter()
    asyncio.run(main([URL(url) for url in search_urls]))
    elapsed = time.perf_counter() - start
    log.info(f"total time: {elapsed:0.2f}")
