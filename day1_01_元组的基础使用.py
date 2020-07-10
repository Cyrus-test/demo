# 元组与列表不同，元组的元素不能修改
# 元组用（）来定义
# 创建空元组 info_tuple = ()
# 元组中包含一个元素时，需要在元素后面加一个，号

info_tuple = ("zhangsan", 20, 1.87, 20, 20)

# 1.取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，系统知道该数据在元组中的索引
print(info_tuple.index(20))

# 2.统计计数
print(info_tuple.count(20))

# 3.统计元组中元素的个数
print(len(info_tuple))

# 4.元组的遍历
for my_info in info_tuple:
    # 使用格式字符串拼接 myinfo 这个变量很不方便，因为元组中通常报错的数据类型是不同的
    print(my_info)




