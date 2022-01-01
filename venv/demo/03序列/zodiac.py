# 元组内容不可变更，列表可变更，元组大小比较，
# (4)<(5)=true;(4)>(5)=false;
# (1,20)<(2,19)=true;(1,20)>(2,19)=false

zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
               u'巨蟹座',u'狮子座',u'室女座',u'天秤座',u'天蝎座',u'射手座')
zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
               (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
(month,day) = (2,15)
# 过滤器
# >>> a=(1,2,3,4,5,6,7)
# >>> a=(1,2,3,4,5,6,7)
# >>> b=4
# >>> filter(lambda x:x<b,a) #取出a中小于4的元素
# <filter object at 0x11041e610>
# >>> list(filter(lambda x: x<b,a)) #取出a中小于4的元素
# [1, 2, 3]
# >>> len (list(filter(lambda x: x<b,a))) #取出列表中元素的个数
# 3
zodiac_day = filter(lambda x : x<=(month,day),zodiac_days)
zodiac_len = len(list(zodiac_day))%12 #转化成列表
print(zodiac_name[zodiac_len])
