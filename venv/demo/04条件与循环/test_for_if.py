# for if 遍历元组

zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
               u'巨蟹座',u'狮子座',u'室女座',u'天秤座',u'天蝎座',u'射手座')
zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
               (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
(month,day) = (2,15)
#用户输入月份和日期
int_month = int(input('请输入月份:'))
int_day = int(input('请输入日期:'))

for x in range(len(zodiac_days)):
    if zodiac_days[x] >= (int_month,int_day):
        print(zodiac_name[x])
        break
    elif int_month == 12 and int_day > 23:
        print(zodiac_name[0])
        break