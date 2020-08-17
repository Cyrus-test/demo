class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "TOM"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名（）创建对象的时候，会自动调用初始化方法__int__
tom = Cat("Tom")

print(tom.name)

lazy_cat =Cat("大懒喵")
print(lazy_cat.name)
