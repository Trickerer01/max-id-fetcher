# coding=UTF-8
"""
Author: trickerer (https://github.com/trickerer, https://github.com/trickerer01)
"""
#########################################
#
#

from asyncio import sleep
from random import uniform as frand
from typing import Optional
from urllib.parse import urlparse

from aiohttp import ClientSession, http_parser
from bs4 import BeautifulSoup

from defs import CONNECT_RETRIES_PAGE, Log, DEFAULT_HEADERS


async def fetch_html(url: str, *, connector=None, tries=None, headers=None, cookies=None) -> Optional[BeautifulSoup]:
    # very basic, minimum validation
    tries = tries or CONNECT_RETRIES_PAGE

    r = None
    retries = 0
    async with ClientSession(connector=connector) as s:
        s.headers.update(DEFAULT_HEADERS.copy())
        if headers is not None:
            s.headers.update(headers.copy())
        if cookies is not None:
            s.cookie_jar.update_cookies(cookies.copy(), http_parser.URL(urlparse(url).netloc))
        while retries < tries:
            try:
                async with await s.request('GET', url, timeout=10) as r:
                    r.raise_for_status()
                    content = await r.read()
                    return BeautifulSoup(content, 'html.parser')
            except (KeyboardInterrupt,):
                assert False
            except (Exception,):
                if r and str(r.url).find('404.') != -1:
                    Log('ERROR: 404')
                    assert False
                retries += 1
                await sleep(frand(1.0, 7.0))
                continue

    if retries >= tries:
        errmsg = f'Unable to connect. Aborting {url}'
        Log(errmsg, True)
    elif r is None:
        Log('ERROR: Failed to receive any data', True)

    return None

#
#
#########################################
