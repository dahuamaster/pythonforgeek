#从1到10 所有偶数的平方

alist = []
for i in range(1,11):
    if (i % 2 ==0):
        alist.append(i*i)
print(alist)

# 推导式写法
blist = [i*i for i in range(1,11) if(i % 2)==0]
print(blist)

