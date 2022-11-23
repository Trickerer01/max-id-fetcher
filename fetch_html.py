# coding=UTF-8
"""
Author: trickerer (https://github.com/trickerer, https://github.com/trickerer01)
"""
#########################################
#
#

from typing import Optional

from aiohttp import ClientSession
from bs4 import BeautifulSoup

from defs import CONNECT_RETRIES_PAGE, Log, DEFAULT_HEADERS


async def fetch_html(url: str, proxy=None, tries=None) -> Optional[BeautifulSoup]:
    # very basic, minimum validation
    tries = tries or CONNECT_RETRIES_PAGE

    r = None
    retries = 0
    async with ClientSession() as s:
        s.headers.update(DEFAULT_HEADERS.copy())
        while retries < tries:
            try:
                async with s.request('GET', url, timeout=5, proxy=proxy) as r:
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
