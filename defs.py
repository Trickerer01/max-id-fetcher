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
    'aHR0cHM6Ly9ydWxlMzR2aWRlby5jb20vc2VhcmNoLz9tb2RlPWFzeW5jJmZ1bmN0aW9uPWdldF9ibG9jayZibG9ja19pZD1jdXN0b21fbGlzdF92aWRlb3NfdmlkZW9zX2xpc3'
    'Rfc2VhcmNoJnE9JXMmc29ydF9ieT1wb3N0X2RhdGUmZnJvbV92aWRlb3M9JWQ=').decode()
RX_SITE_PAGE_REQUEST_BASE = (
    f'{b64decode("aHR0cHM6Ly9hcGkucnVsZTM0Lnh4eC8=").decode()}index.php?page=dapi&s=post&q=index&limit=1')

USER_AGENT = 'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0'
DEFAULT_HEADERS = {'User-Agent': USER_AGENT}
PROXY_DEFAULT_STR = 'socks5://127.0.0.1:222'

CONNECT_RETRIES_PAGE = 5
CONNECT_RETRIES_ITEM = 10

Log = print

#
#
#########################################
