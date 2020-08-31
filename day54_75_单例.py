class GamePlay(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2.如果为空，调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

play1 = GamePlay()
print(play1)
play2= GamePlay()
print(play2)