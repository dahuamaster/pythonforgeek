# 类的继承，类的多态(父类定义的方法，子类可以覆盖)，查询类的类型及继承关系
# 猫科动物 -》猫
class Monstor:
    '定义怪物类'

    def __init__(self, hp=200):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')


class Animals(Monstor):
    '普通怪物'

    def __init__(self, hp=10):
        # self.hp=hp
        super().__init__(hp)


class Boss(Monstor):
    'Boss类怪物'

    def whoami(self):
        print('我是怪物我怕谁')


a1 = Monstor(200)
print(a1.hp)
print(a1.run())

a2 = Animals(20)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
print(a3.hp)
print(a3.whoami())  # 子类和父类的同一个方法会产生覆盖

print('a1类型 %s' % type(a1))
print('a2类型 %s' % type(a2))
print('a2类型 %s' % type(a2))

print(isinstance(a2, Monstor))
