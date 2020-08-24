class Gun:
    def __init__(self, model):
        # 1.抢的型号
        self.model = model
        # 2.子弹的数量
        self.buttle_count = 0

    def add_buttle(self, count):
        self.buttle_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.buttle_count <= 0:
            print("%s 没有子弹了。。。" % self.model)
            return
        # 2.发射子弹,-1
        self.buttle_count -= 1

        # 3.提示发射成功
        print("%s 突突突。。。%d" % (self.model, self.buttle_count))

class Soldier:
    def __init__(self, name):
        # 1.士兵的名字
        self.name = name
        # 2.新兵没有抢
        self.gun = None

    def fir(self):
        # 1.判断一下士兵是否有枪
        if self.gun is None:
            print("[%s] 还没有枪。。。" % self.name)
            return

        # 2.高喊口号
        print("冲啊！！！")

        # 3.让枪装填子弹
        self.gun.add_buttle(50)
        # 4.让枪发射子弹
        self.gun.shoot()
# 1.创建抢对象
ak47 = Gun("AK47")

# ak47.add_buttle(50)
#
# ak47.shoot()

# 2.创建士兵

xusando = Soldier("许三多")

# xusando.gun = ak47
xusando.fir()
print(xusando.gun)
