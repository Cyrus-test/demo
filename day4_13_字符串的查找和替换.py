hello_str = "hello world"

# 1.判断是否以制定的字符串开始
print(hello_str.startswith("Hello"))
# 2.判断是否以制定的字符串结束
print(hello_str.endswith("ld"))
# 3.查找制定的字符串
# index如果制定的字符串不存在，会报错
# find如果制定的字符串不存在，会返回-1
print(hello_str.find("wor234"))
# 4.替换字符串
# replace方法执行完不会修改原有字符串的内容，会返回一个新的字符串
print(hello_str.replace("world", "python"))

print(hello_str)
