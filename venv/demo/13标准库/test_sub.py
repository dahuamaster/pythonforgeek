# 字符串替换

import re
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print('匹配数字',p.match('aaa2019-06-10aaaa'))
print('匹配数字',p.search('aaa2019-06-10aaaa'))

phone = '123-456-789 # 这是一个电话号码'
p2 =re.sub(r'#.*$','',phone)
print(p2)

p3 =re.sub(r'\D','',p2)
print(p3)