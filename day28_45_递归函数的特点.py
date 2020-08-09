def number(num):

    print(num)
    # 递归函数的出口，当参数满足某个条件时，不在执行参数
    if num == 1:
        # return 执行以后下面的代码不会再执行 
        return
    # 自己调用自己
    number(num - 1)

number(3)