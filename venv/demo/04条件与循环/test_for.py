# for 循环遍历序列
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

for x in chinese_zodiac:
    print(x)
for i in range(1,13):
    print(i)

for year in range(2010,2022):
    print('%s 年的生肖是 %s' %(year,chinese_zodiac[year % 12]))