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
    # 如果子类中，重写了父类的方法，在使用此类对象调用子类方法时，会调用子类的方法，覆盖父类
    def dark(self):
        print("我是神狗，叫的就是响")


xtq = XiaoTianQuan()
xtq.dark()