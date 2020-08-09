class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


tom = Cat()
tom.name = "TOM"
tom.drink()
tom.eat()
print(tom)
# 再创建一个猫对象

lazy_cat = Cat()
lazy_cat.name = "大懒喵"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)