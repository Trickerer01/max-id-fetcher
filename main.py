# coding=UTF-8
"""
Author: trickerer (https://github.com/trickerer, https://github.com/trickerer01)
"""
#########################################
#
#

from asyncio import run as run_async, sleep, as_completed
from re import compile as re_compile, search as re_search
from sys import argv

from defs import (
    Log, PROXY_DEFAULT_STR, NM_SITE_PAGE_REQUEST_BASE, RN_SITE_PAGE_REQUEST_BASE, RV_SITE_PAGE_REQUEST_BASE, RX_SITE_PAGE_REQUEST_BASE
)
from fetch_html import fetch_html


async def fetch_nm() -> str:
    nm_page_entry_href_re = re_compile(r'^/video/(\d+)/[^/]+?$')
    a_html = await fetch_html(NM_SITE_PAGE_REQUEST_BASE % ('', 1))
    assert a_html
    maxid = re_search(nm_page_entry_href_re, str(a_html.find('a', href=nm_page_entry_href_re).get('href'))).group(1)
    return f'NM: {maxid}'


async def fetch_rn() -> str:
    rn_page_entry_class_re = re_compile(r'^thumb shm-thumb.+?$')
    rn_page_entry_href_re = re_compile(r'^/post/view/(\d+)$')
    a_html = await fetch_html(RN_SITE_PAGE_REQUEST_BASE, proxy=PROXY_DEFAULT_STR)
    assert a_html
    maxid = re_search(rn_page_entry_href_re, str(a_html.find('a', class_=rn_page_entry_class_re).get('href'))).group(1)
    return f'RN: {maxid}'


async def fetch_rv() -> str:
    rv_page_entry_class_re = re_compile('^th js-open-popup$')
    rv_page_entry_href_re = re_compile(r'^.+/(\d+)/.+?$')
    a_html = await fetch_html(RV_SITE_PAGE_REQUEST_BASE % ('', 1))
    assert a_html
    maxid = re_search(rv_page_entry_href_re, str(a_html.find('a', class_=rv_page_entry_class_re).get('href'))).group(1)
    return f'RV: {maxid}'


async def fetch_rx() -> str:
    a_html = await fetch_html(RX_SITE_PAGE_REQUEST_BASE)
    assert a_html
    maxid = str(a_html.find('post').get('id'))
    return f'RX: {maxid}'


async def main() -> None:
    if '--silent' not in argv:
        input(f'\n{"#" * 47}\n# MAKE SURE REQUIRED PROXIES / UNBLOCKERS ARE ENABLED! #\n{"#" * 47}\nPress <Enter> to continue...\n')

    aresults = [fetch_nm(), fetch_rn(), fetch_rv(), fetch_rx()]
    f_strings = {}

    for cr in as_completed(aresults):
        s = await cr
        f_strings[s[:2]] = s

    Log('\n'.join(f_strings[k] for k in ['NM', 'RN', 'RV', 'RX']))


async def run_main() -> None:
    await main()
    await sleep(0.5)


if __name__ == '__main__':
    run_async(run_main())
    Log('')
    exit(0)

#
#
#########################################
