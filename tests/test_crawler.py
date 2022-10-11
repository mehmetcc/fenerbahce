

from bs4 import BeautifulSoup
from fenerbahce.crawler import Crawler

import pytest

def test_get_soup_valid():
    url = "https://google.com"
    crawler = Crawler()
    soup = crawler.get_soup(url)

    assert type(soup) is BeautifulSoup
    assert soup.text is not None


def test_get_soup_invalid():
    url = "anan://asald.im"
    crawler = Crawler()

    with pytest.raises(Exception):
        crawler.get_soup(url)
