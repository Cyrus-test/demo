def messure():
    print("测试开始。。。")
    print("测试结束。。。")
    temp = 25
    wess = 35

    # 元组可以包含多个数据，因此可以使用元组让函数一次返回多个值，如果函数返回的类型是元组，小括号可以省略
    return temp, wess


result = messure()

print(result)

