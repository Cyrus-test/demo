def messure():
    print("测试开始。。。")
    print("测试结束。。。")
    temp = 25
    wess = 35

    # 元组可以包含多个数据，因此可以使用元组让函数一次返回多个值，如果函数返回的类型是元组，小括号可以省略
    return temp, wess

# 元组
result = messure()

print(result)
# 需要单独的处理温度和湿度--不方便
print(result[0])
print(result[1])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素，可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组中的个数保持一致

gl_temp, gl_wess = messure()

print(gl_temp)
print(gl_wess)


