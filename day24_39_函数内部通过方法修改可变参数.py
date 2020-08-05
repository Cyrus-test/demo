# =赋值语句，不会影响全局变量
def demo(num):
    # num =[4, 5, 6]
    print("函数开始执行")
    num.append(9)
    print(num)
    print("函数执行结束")

gl_num =[1, 2, 3]
demo(gl_num)
print(gl_num)
