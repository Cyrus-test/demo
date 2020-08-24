# 私有属性 就是对象 不希望公开的属性

# 私有方法 就是对象 不系统公开的对象


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __sercrit(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d " % (self.name, self.age))


xiaomei = Women("小美")

# 私有属性，在外界不能够被直接访问
print(xiaomei.age)
# 私有属性不能在外界被调用
xiaomei.__sercrit()
