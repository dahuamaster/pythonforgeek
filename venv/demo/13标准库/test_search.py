# match 精准匹配，search 搜索模糊匹配
import re
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print('匹配数字',p.match('aaa2019-06-10aaaa'))
print('匹配数字',p.search('aaa2019-06-10aaaa'))
