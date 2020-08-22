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

    def dark(self):
        # 1. 针对子类特有的需求，编写代码
        print("我是神狗，叫的就是响")
        # 2. 使用super（）.调用原本在父类中的方法
        # super().dark()
        # super在python2.0中没有这个方法，可以使用父类名.方法()来创建
        Dag.dark(self)
        # 注意：如果出现子类调用方法，会出现递归调用，----死循环！
        XiaoTianQuan.dark(self)
        # 3. 其他需求
        print("#^&*&*&*$@")



xtq = XiaoTianQuan()
xtq.dark()