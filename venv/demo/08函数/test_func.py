# def func (a,b,c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
# func(1,2,3)
#
# # 统计参数个数
# def howlong(first,*other):
#     print(1+len(other))
# howlong('eat','dirk',213,12312)

# var1 =123
# def func():
#     #默认变量在函数体内，关键字global全局变量
#     global var1
#     var1 = 456
#     print(var1)
# func()
# print(var1)

# 迭代器  iter next
# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

#
# for i in range(10,20,2):
#     print(i)

# 我觉得这样会好理解很多，碰到yield后，暂停，再次调用next（）时，从上次的位置开始执行
# yield的主要用途是需要一个数据时，才产生一个，而不是把数据线一次性存入内存；相对于把数据提前定义成列表来使用，要极为节省系统资源。
# 一般访问生成器要使用next方法，也可以使用list方法一次性讲将所有值读取出来，但是一次性读取出来就和列表一样了，失去自身的优势。
def frange(start, stop, step):
    print('starting')
    x = start
    while x < stop:
        yield x
        # print(x)
        x += step


i = frange(1, 10, 0.5)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# for i in frange(10,20,0.5):
#     print(i)
