"""Async web scraping."""
import asyncio
import logging
from pathlib import Path
from typing import List

import aiohttp
from yarl import URL

log = logging.getLogger(__name__)


async def download_web_page(url: URL) -> bytes:
    log.info(f"Begin downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            log.info(f"Finished downloading {url}")
            return content


async def write_to_file(output_dir: Path, url: URL, content: bytes) -> None:
    """Write file to unique(ish) name built from url."""
    url_name = [p for p in url.parts if p][-1]
    filename = f"{url.host.replace('.', '')}-{url_name}.html"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    with open(str(output_path), "wb") as html_file:
        log.info(f"Begin writing to {output_path}")
        html_file.write(content)
        log.info(f"Finished writing to {output_path}")


async def scrape_html(output_dir: Path, url: URL) -> None:
    content = await download_web_page(url)
    await write_to_file(output_dir, url, content)


async def scrape_all(output_dir: Path, urls: List[URL]) -> None:
    """Given a list of URLs, fetch and write out the html to file."""
    tasks = [asyncio.create_task(scrape_html(output_dir, url)) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
