# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# print (zodiac[2:4])
# print (zodiac[-1])
year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])
print('狗' in chinese_zodiac)
print(chinese_zodiac*3)
print(chinese_zodiac+"12321")
