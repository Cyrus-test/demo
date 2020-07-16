
# len 可以统计元素的个数
srr = "qwertyuiopasdfghjklzxcvbnm"

str = max(srr)
str1 = min(srr)
print(str)
print(str1)

number = [1, 2, 4, 8, 11, 54]

num = max(number)
print(num)

mum1 = min(number)
print(mum1)

# 字典进行对比的时候，只对比键值对的key
t_dict = {"a": "z", "b": "y", "c": "x"}
t = max(t_dict)
t1 = min(t_dict)
print(t)
print(t1)

# cmp（比较） 在python3.x中已经取消


print("1" < "2")

print("1" > "2")
print("================")
print([1, 1, 1] < [2, 2, 2] )

print((1, 1, 1) < (2, 2, 2) )

print({"a": "z"} < {"b": "y"})
