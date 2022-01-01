from urllib import request
from urllib import parse
# url = 'http://www.baidu.com'
# response = request.urlopen(url,timeout=1)
# print(response.read().decode('utf-8'))

data = bytes(parse.urlencode({'world': 'hello'}), encoding='utf8')
url = 'http://httpbin.org/post'
response2 = request.urlopen(url, data=data, timeout=1)
print(response2.read().decode('utf-8'))
