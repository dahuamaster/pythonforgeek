# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input('请用户输入出生年份'))
print(year % 12)
if (chinese_zodiac[year % 12] =='狗'):
    print('你是属狗的哈。。。。。。')
else:
    print(chinese_zodiac[year % 12])



