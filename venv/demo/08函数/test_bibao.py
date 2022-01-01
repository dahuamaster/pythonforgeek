def func():
    a=1
    b=2
    return a+b

def sum(a):
    def add(b):
        #外部函数被内部函数引用的话叫闭包
        return a+b
    return add

num2=sum(2)
print(num2(4))

# 计数器
def counter(FIRST=0):
    cnt = [FIRST]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

num1 =counter()
print(num1())
print(num1())
print(num1())

# a*x+b=y
def a_line(a,b):
    # def arg_y(x):
    #     return a*x+b
    # return arg_y
    return lambda x:a*x+b

line1 =a_line(3,5)
print(line1(10))