from functools import reduce

# 第一个元素1，初始值1，根据lambda表达是和列表操作 （（（1+2）+3）+4）
print(reduce(lambda x, y: x + y, [2, 3, 4], 1))
