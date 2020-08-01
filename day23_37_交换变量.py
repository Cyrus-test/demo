a = 8
b = 100

# # 使用一个变量，解法1：
# c = a
# a = b
# b = c
# print(a)
# print(b)
#
# # 不使用变量，解法2：
#
# a = a + b
# b = a - b
# a = a - b
#
# print(a)
# print(b)

# 使用python，解法3
a, b = b, a
print(a)
print(b)


