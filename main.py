import asyncio
import logging
import time

from pathlib import Path
from typing import List

from googlesearch import search
from yarl import URL

from async_web_scraper.fetch import scrape_all

log = logging.getLogger(__name__)


async def main(urls: List[URL]) -> None:
    output_dir = Path(__file__).parent / "output"
    await scrape_all(output_dir, urls)


def configure_logging() -> None:
    """Some basic log config."""
    logging.basicConfig(format="%(asctime)s - %(levelname)s: %(message)s",
                        filename="async_web_scraper.log",
                        filemode="w",
                        level=logging.INFO)


if __name__ == "__main__":
    configure_logging()
    search_urls = search("how to data engineering", stop=5)
    start = time.perf_counter()
    asyncio.run(main([URL(url) for url in search_urls if url]))
    elapsed = time.perf_counter() - start
    log.info(f"total time: {elapsed:0.2f}")
