try :
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s " % result)
else:
    print("尝试成功")
finally:
    print("不管上面执行的怎么样，都会执行这个命令")

print("-" * 50)