def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))

    # 1. 定义一个数据变量
    result = "hello"
    print("函数要返回数据的内存地址是 %d " % id(result))
    # 2. 将字符串变量返回，返回的是数据的引用，而不是数据本身
    return result

a = 10

# 数据的地址是本质就是一个数字
print("a 变量保存数据的内存地址是 %d " % id(a))

# 2.调用test函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
# 注意：如果函数有返回值，但是没有定义变量的接收
# 程序不会报错，但是无法获取返回结果

r = test(a)

print("%s 内存地址是 %d " % (r, id(r)))
