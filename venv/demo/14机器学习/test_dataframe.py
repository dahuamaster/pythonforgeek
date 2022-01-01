from pandas import Series, DataFrame
import pandas as pd
from numpy import nan as NA


data = {'city': ['beijing', 'shanghai', 'hangzhou'],
        'year': [2018, 1987, 2020],
        'pop': [1.2, 2.3, 4.3]}

frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
print(frame)
print(frame2)
print(frame2['city'])
print(frame2.year)
frame2['new'] = 100
print(frame2)
frame2['cap'] = frame2.city == 'beijing'
print(frame2)

pop = {'beijing': {2008: 1.6, 2009: 2.0},
       'shanghai': {2008: 1.8, 2009: 3.9}}
frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)

obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj5)

data = Series([1, NA, 2])
print(data.dropna())
