class Persion():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s，我的体重是 %.2f " % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("每锻炼一次，体重减少至 %.2f" % self.weight)

    def eat(self):
        self.weight += 1
        print("每吃一次，体重增加到%.2f" % self.weight)


xiaoming = Persion("小明", 75.0)
xiaoming.run()
xiaoming.eat()

print(xiaoming)

xiaomei = Persion("小美", 40.0)
xiaomei.run()
xiaomei.eat()
print(xiaomei)