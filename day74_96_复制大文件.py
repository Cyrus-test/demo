# 1.打开文件
file_read = open("READER")
file_write = open("READER【复制】", "w")

# 2.读写文件
while True:
    # 读取一行的内容
    test = file_read.readline()
    # 判断是否读取到内容
    if not test:
        break
    file_write.write(test)


# 3.关闭文件
file_read.close()
file_write.close()