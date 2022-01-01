from pandas import Series,DataFrame
import pandas as pd

obj=Series([4,5,6,-7])
print(obj)
print(obj.index)
print(obj.values)

# {'a':1,'b':2,'c':3}

obj2=Series([4,5,6,-7],index=['d','b','c','a'])
print(obj2)
print(obj2['c'])
obj2['c']=8
print(obj2['c'])

sdata = {'beijing':35000,'shanghai':71000}
obj3=Series(sdata)
print(obj3)
obj3.index=['bj','sh']
print(obj3)


