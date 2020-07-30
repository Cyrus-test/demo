# 注意：在开发时，应该把模块中的所有全局变量定义在函数上方，就可以保证所有的函数都能够正常的访问到每一个全局变量

num = 10

# 再定义一个全局变量
title = "黑马程序员"

def demo():

    print("%d" % num)
    print("%s" % title)
    print("%s" % name)

demo()

name = "xiaoming"

# 代码结构示意图：
# 1.shebang
#
# 2.import模块
#
# 3.全局变量
#
# 4.函数定义
#
# 5.执行代码