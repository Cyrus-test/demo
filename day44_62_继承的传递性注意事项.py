class Animal:
    def eat(self):
        print("吃饭了")

    def drink(self):
        print("喝可乐了")

    def run(self):
        print("跑一跑")

    def sleep(self):
        print("睡一睡")

class Dag(Animal):
    # 子类用于父类所有的属性和方法
    def dark(self):
        print("汪汪汪")

class XiaoTianQuan(Dag):
    def fly(self):
        print("飞行了")

class Cat(Animal):
    def catch(self):
        print("抓老鼠")

xtq = XiaoTianQuan()
xtq.dark()
xtq.catch()

