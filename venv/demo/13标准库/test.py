# https://docs.python.org/zh-cn/3/library/index.html
# 1.文字处理的re

import re

# 正则表达式
# . 元字符，匹配除了换行的任意字符
# ^ 开头， 匹配字符串的开头
# $ 结尾，匹配字符串尾或者在字符串尾的换行符的前一个字符 jpg$
# * 匹配前面字符出现0-N次
# + 匹配前面字符出现1-N次
# ？对它前面的正则式匹配0到1次重复
# {m} 对其之前的正则式指定匹配 m 个重复
# {m,n} 对正则式进行 m 到 n 次匹配，在 m 和 n 之间取尽量多
# []  用于表示一个字符集合。在一个集合中,字符可以单独列出，比如 [amk] 匹配 'a'， 'm'， 或者 'k'
# | A|B， A 和 B 可以是任意正则表达式，创建一个正则表达式，匹配 A 或者 B. 任意个正则表达式可以用 '|' 连接

# 转义字符
# \d  匹配数字 [0-9]+
# \D  匹配不包含数字
# \s  匹配字符串 [a-z]
# ()  (2018)-(03)-(04).group 正则分组概念
# ^$  这一行是空行
# .*? 不使用贪婪模式


p = re.compile('ca{4,6}t')
print(p.match('caaaat'))

# p = re.compile('...')  #写法1
p = re.compile('.{3}')  #写法2
print('匹配三个字符',p.match('bat'))
print('匹配三个字符',p.match('cat'))

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print('匹配数字',p.match('2019-06-10'))
print('匹配数字',p.match('2019-06-10').group())
print('匹配数字',p.match('2019-06-10').group(1))
print('匹配数字',p.match('2019-06-10').group(2))
print('匹配数字',p.match('2019-06-10').group(3))
print('匹配数字',p.match('2019-06-10').groups())

year,month,day = p.match('2019-06-10').groups()
print(year,month,day)

