a=[1,2,3]
#使用lambda 必须转化为list
# filter是筛选出符合函数规则的数据
print(list(filter(lambda x:x>2,a)))

#map是按照函数规则修改每个值
print(list(map(lambda x:x+1,a)))
b=[4,5,6]
print(list(map(lambda x,y:x+y,a,b)))