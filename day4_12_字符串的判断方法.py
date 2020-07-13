# unicode 字符串
numb_str = "\u00b2"
print(numb_str)

# 1.字符串中只包含数字，则返回true,全角数字

print(numb_str.isdecimal())

# 2.字符串中只包含数字，则返回true，全角数字、（1）、\u00b2

print(numb_str.isdigit())

# 3.字符串中只包含数字，则返回true,全角数字、汉字数字

print(numb_str.isnumeric())


