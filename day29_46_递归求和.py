# 定义一个函数sum_number,能够接收一个num的整数参数
# 计算1+2+...num


def sum_number(num):
    # 1.出口
    if num == 1:
        return 1
    # 2.数字的累加num+（1...num-1）,假设sum_能够正确处理1...num-1
    temp = sum_number(num - 1)
    return num + temp


result = sum_number(100)
print(result)



