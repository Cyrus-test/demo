class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.drink()
tom.eat()

print(tom)

addr = id(tom)
# %d 是打印10进制的操作符
# %x 是打印16进制的操作符
print("%x" % addr)

