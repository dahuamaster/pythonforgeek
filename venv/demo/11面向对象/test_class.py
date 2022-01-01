# 面向过程
# user1={'name':'tom','hp':100}
# user2={'name':'jerry','hp':80}
#
# def print_role(role):
#     print('name is %s,hp is %s'%(role[name],role[hp]))
# print(user1)

# 定义一个类，增加一个方法，增加一个属性
class Player:  # 定义一个类
    def __init__(self, name, hp, occu):

        self.name = name  # 变量称作属性
       # self.__name = name # 变量前增加2个下划线，变量不会被访问，不会被修改
        self.hp = hp
        self.occ = occu

    def print_role(self):  # 定义一个方法
        print('%s: %s %s' % (self.name, self.hp, self.occ))

    def updateName(self, newname):
        self.name = newname


class Monstor:
    # 定义怪物
    pass


user1 = Player('tom', 100, 'war')  # 类的实例化
user2 = Player('jerry', 80, 'master')
user1.print_role()
user2.print_role()
user1.updateName('wilson')

user1.print_role()
user2.print_role()
