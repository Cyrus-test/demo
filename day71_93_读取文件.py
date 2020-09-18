# 1.打开文件（注意：文件名是区分大小写的！！！）
file = open("READER.txt")

# 2.读取文件内容
text = file.read()
print(text)

# 3.关闭文件
file.close()