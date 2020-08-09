def demo(num, list):

    num = 100
    list = [1, 2, 3]

    print("函数开始执行。。。")
    print(num)
    print(list)
    print("函数执行结束")
# 只要针对参数进行赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用
gl_num =2
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)