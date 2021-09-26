import pytest

from aioresponses import aioresponses
from yarl import URL

from async_web_scraper.fetch import (
    download_web_page, write_to_file, scrape_all
)


@pytest.mark.asyncio
@pytest.mark.parametrize("status,body,expected", [
    (200, "test", b"test"),
])
async def test_download_web_page(status, body, expected):
    with aioresponses() as mocked:
        url = URL("https://www.example.com")
        mocked.get(url, status=status, body=body)
        content = await download_web_page(url)
        assert content == expected


@pytest.mark.asyncio
async def test_write_to_file(tmp_path):
    p = tmp_path / "wwwexamplecom-hello.html"
    url = URL("https://www.example.com/hello")
    content = b'test'
    await write_to_file(tmp_path, url, content)
    assert p.read_bytes() == content
    assert len(list(tmp_path.iterdir())) == 1


@pytest.mark.asyncio
async def test_scrape_all(tmp_path):
    mocked_responses = [
        (URL("https://www.example.com/foo"), 200, b'foo'),
        (URL("https://www.example.com/bar"), 200, b'bar'),
        (URL("https://www.example.com/baz"), 200, b'baz'),
    ]
    with aioresponses() as mocked:
        for url, status, body in mocked_responses:
            mocked.get(url, status=status, body=body)

        await scrape_all(tmp_path, [mr[0] for mr in mocked_responses])

    assert len(list(tmp_path.iterdir())) == 3
    assert (tmp_path / "wwwexamplecom-foo.html").read_bytes() == b'foo'
    assert (tmp_path / "wwwexamplecom-bar.html").read_bytes() == b'bar'
    assert (tmp_path / "wwwexamplecom-baz.html").read_bytes() == b'baz'
