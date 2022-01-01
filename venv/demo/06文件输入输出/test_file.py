# open read readline seek write colse

# file1 = open('name.txt','w')
# file1.write('诸葛亮')
# file1.close()
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt','a')
# file3.write('刘备')
# file3.close()

# file4 = open('name.txt')
# print(file4.readline())
#
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('======')

#文件的偏移
file6 = open('name.txt')
print(file6.tell())
file6.read(1)
# file6.seek(0)
# file6.read(1)
# file6.read(2)

