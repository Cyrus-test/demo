class GamePlay(object):
    # 1.记录第一个被创建的对象
    instance = None

    # 2.记录是否执行过初始化动作
    shuxing = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2.如果为空，调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1.判断是否执行过初始化动作
        if GamePlay.shuxing:
            return
        # 2.如果没有执行过，在执行初始化动作
        print("初始化属性")

        # 3.修改类属性的标记
        GamePlay.shuxing = True


play1 = GamePlay()
print(play1)
play2= GamePlay()
print(play2)