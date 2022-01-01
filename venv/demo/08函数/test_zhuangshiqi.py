# 闭包专递的是变量，装饰器传递的是函数
import time
# print(time.time())
# time.sleep(3)

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('函数运行了%s 秒' % (stop_time - start_time))
    return wrapper()


@timer
def i_can_sleep():
    time.sleep(3)

# start_time =time.time()
# timer(i_can_sleep)
# stop_time =time.time()
# print('函数运行了%s 秒'%(stop_time-start_time))

# 2个数的累加和
def new_tips(argv):
    def tips(func):
        def nei(a,b):
            print('start %s %s'%(argv,func.__name__))
            func(a,b)
            print('stop')
        return nei
    return tips

@new_tips('add_mod')
def add(a,b):
    print(a+b)

@new_tips('sub_mod')
def sub(a,b):
    print(a-b)

print(add(4,5))
print(sub(4,5))