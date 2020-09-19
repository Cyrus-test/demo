# 打开文件
file = open("READER")

#
while True:
    test = file.readline()
    # 判断是否读取到内存
    if not test:
        break
    print(test)

file.close()