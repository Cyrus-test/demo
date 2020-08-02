# 在python中，列表变量调用 += 本质上是调用 exte 方法，不会改变全局变量
def demo(num, num_list):
    print("函数的开始")
    num += num
    # num_list = num_list + num_list
    # 列表变量使用+=不会做相加再赋值操作，本质上是再调用 extend 方法
    num_list += num_list
    # num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数结束")

gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)

