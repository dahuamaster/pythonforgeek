from urllib import request
from urllib import parse

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    # "Referer": "http://www.infoq.com",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
dict = {
    'name': 'value'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
url = 'http://httpbin.org/post'
req = request.Request(
    url,
    data=data,
    headers=headers,
    method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
