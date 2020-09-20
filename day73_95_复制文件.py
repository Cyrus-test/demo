# 1.打开文件
file_read = open("READER")
file_write = open("READER【复制】", "w")

# 2.读写文件
test = file_read.read()
print(test)
test_fuzhi = file_write.write(test)

# 3.关闭文件
file_read.close()
file_write.close()