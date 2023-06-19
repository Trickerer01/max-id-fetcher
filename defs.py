# coding=UTF-8
"""
Author: trickerer (https://github.com/trickerer, https://github.com/trickerer01)
"""
#########################################
#
#

from base64 import b64decode

# Params required: (str, int). Ex. NM_SITE_PAGE_REQUEST_BASE % ('', 1)
NM_SITE_PAGE_REQUEST_BASE = b64decode(
    'aHR0cHM6Ly93d3cubmF1Z2h0eW1hY2hpbmltYS5jb20vc2VhcmNoL3ZpZGVvcz9vPW1yJnNlYXJjaF9xdWVyeT0lcyZwYWdlPSVk').decode()
RN_SITE_PAGE_REQUEST_BASE = f'{b64decode("aHR0cHM6Ly9ydWxlMzRoZW50YWkubmV0Lw==").decode()}post/list/order%253Did_desc/1'
# Params required: (str, int). Ex. RV_SITE_PAGE_REQUEST_BASE % ('', 1)
RV_SITE_PAGE_REQUEST_BASE = b64decode(
    'aHR0cHM6Ly9ydWxlMzR2aWRlby5wYXJ0eS9zZWFyY2gvP21vZGU9YXN5bmMmZnVuY3Rpb249Z2V0X2Jsb2NrJmJsb2NrX2lkPWN1c3RvbV9saXN0X3ZpZGVvc192aWRlb3Nf'
    'bGlzdF9zZWFyY2gmcT0lcyZzb3J0X2J5PXBvc3RfZGF0ZSZmcm9tX3ZpZGVvcz0lZA==').decode()
RX_SITE_PAGE_REQUEST_BASE = (
    f'{b64decode("aHR0cHM6Ly9hcGkucnVsZTM0Lnh4eC8=").decode()}index.php?page=dapi&s=post&q=index&limit=1')

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Goanna/6.2 Firefox/102.0 PaleMoon/32.2.0'
DEFAULT_HEADERS = {'User-Agent': USER_AGENT}
PROXY_DEFAULT_STR = 'socks5://127.0.0.1:222'

CONNECT_RETRIES_PAGE = 5
CONNECT_RETRIES_ITEM = 10

Log = print

#
#
#########################################
