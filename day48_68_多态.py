class Dag(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTianQuan(Dag):
    def game(self):
        print("%s 飞到天上去玩耍" % self.name)

class Persion(object):
    def __init__(self, name):
        self.name = name

    def persion_with_dag_play(self, dog):
        print("%s 和 %s 一起快乐的玩耍" % (self.name, dog.name))


# 1.创建一个狗对象
# wangcai = Dag("旺财")
wangcai = XiaoTianQuan("飞天旺财")
# 2.创建一个小明的对象
xiaoming = Persion("小明")
# 3.让小明调用和狗玩耍的方法
xiaoming.persion_with_dag_play(wangcai)

