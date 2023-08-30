# coding=UTF-8
"""
Author: trickerer (https://github.com/trickerer, https://github.com/trickerer01)
"""
#########################################
#
#

import sys
from asyncio import run as run_async, sleep, as_completed, Future
from re import compile as re_compile
from urllib.parse import urlparse

from aiohttp_socks import ProxyConnector, ProxyType

from defs import (
    Log, PROXY_DEFAULT_STR, NM_SITE_PAGE_REQUEST_BASE, RN_SITE_PAGE_REQUEST_BASE, RV_SITE_PAGE_REQUEST_BASE, RX_SITE_PAGE_REQUEST_BASE
)
from fetch_html import fetch_html


async def fetch_nm() -> str:
    nm_page_entry_href_re = re_compile(r'^/video/(\d+)/[^/]+?$')
    a_html = await fetch_html(NM_SITE_PAGE_REQUEST_BASE % ('', 1))
    assert a_html
    maxid = nm_page_entry_href_re.search(str(a_html.find('a', href=nm_page_entry_href_re).get('href'))).group(1)
    return f'NM: {maxid}'


async def fetch_rn() -> str:
    use_proxy = True
    rn_page_entry_class_re = re_compile(r'^thumb shm-thumb.+?$')
    rn_page_entry_href_re = re_compile(r'^/post/view/(\d+)$')
    pp = urlparse(PROXY_DEFAULT_STR)
    ptype = ProxyType.SOCKS5 if pp.scheme in {'socks5', 'socks5h'} else ProxyType.HTTP
    connector = ProxyConnector(proxy_type=ptype, host=pp.hostname, port=pp.port) if use_proxy else None
    a_html = await fetch_html(RN_SITE_PAGE_REQUEST_BASE, connector=connector)
    assert a_html
    maxid = rn_page_entry_href_re.search(str(a_html.find('a', class_=rn_page_entry_class_re).get('href'))).group(1)
    return f'RN: {maxid}'


async def fetch_rv() -> str:
    rv_page_entry_class_re = re_compile('^th js-open-popup$')
    rv_page_entry_href_re = re_compile(r'^.+/(\d+)/.+?$')
    a_html = await fetch_html(RV_SITE_PAGE_REQUEST_BASE % ('', 1), tries=999999,
                              headers={'Referer': RV_SITE_PAGE_REQUEST_BASE % ('', 1),
                                       'X-fancyBox': 'true', 'X-Requested-With': 'XMLHttpRequest'},
                              cookies={'kt_rt_popAccess': '1', 'kt_tcookie': '1'})
    assert a_html
    maxid = rv_page_entry_href_re.search(str(a_html.find('a', class_=rv_page_entry_class_re).get('href'))).group(1)
    return f'RV: {maxid}'


async def fetch_rx() -> str:
    a_html = await fetch_html(RX_SITE_PAGE_REQUEST_BASE)
    assert a_html
    maxid = str(a_html.find('post').get('id'))
    return f'RX: {maxid}'


async def main() -> None:
    if '--silent' not in sys.argv:
        input(f'\n{"#" * 47}\n# MAKE SURE REQUIRED PROXIES / UNBLOCKERS ARE ENABLED! #\n{"#" * 47}\nPress <Enter> to continue...\n')

    aresults = (fetch_nm(), fetch_rn(), fetch_rv(), fetch_rx())
    f_strings = dict()

    for cr in as_completed(aresults):  # type: Future[str]
        s = await cr
        f_strings[s[:2]] = s

    Log('\n'.join(f_strings[k] for k in ('NM', 'RN', 'RV', 'RX')))


async def run_main() -> None:
    await main()
    await sleep(0.5)


if __name__ == '__main__':
    assert sys.version_info >= (3, 7), 'Minimum python version required is 3.7!'
    run_async(run_main())
    Log('')
    exit(0)

#
#
#########################################
