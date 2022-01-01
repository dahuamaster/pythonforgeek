
# IndentationError: unexpected indent
# i=j

# SyntaxError: unmatched ')'
# print())

# IndexError: string index out of range
# a='123'
# print(a[3])

# KeyError: 'c'
# d = {'a': 1 ,'b': 2}
# print(d['c'])

# ValueError: invalid literal for int() with base 10: 'y'
# year = int (input('input year:'))

# try:
#     year = int (input('input year:'))
# except ValueError:
#     print('年份要输入数字')

# a=123
# try:
#     a.append()
# except AttributeError:
#     print('int 不能添加')

# except (ValueError,AttributeError,KeyError)

# try:
#     print(1/'a')
# except Exception as e:
#     print('  %s' %e)

# 自定义异常
# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')
# finally:
#
try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()



# try
#     open('name.txt')
# except print('yy')
