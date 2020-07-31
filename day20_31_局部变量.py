# 局部变量 是在函数内部定义的变量，只能在函数内部使用
def demo1():
    num = 10
    # 1.出生：执行了下方的代码之后，才会被创建
    # 2.死亡：函数执行完成之后
    print("在demo1中的局部变量是 %d" % num)

    # 定义一个局部变量

def demo2():
    print(num)

demo1()
demo2()

