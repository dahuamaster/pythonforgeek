# while 遍历

# num=5
# while True:
#     print('a')
#     num=num+1
#     if num>10:
#         break
import time
num=5
while True:
    num=num+1
    if num==10:
        continue
    print(num)
    time.sleep(1)
