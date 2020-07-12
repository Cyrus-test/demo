xiaoming_dict = {"name" : "小明",
                 "age" : 12,}

# 1.统计键值对的数量
print(len(xiaoming_dict))

# 2.合并字典
temp_dict = {"height" : 1.75,
             "name" : "laowang"}
# 注意：如果被合并的字典已包含存在的键值对，会覆盖原有键值对
xiaoming_dict.update(temp_dict)

print(xiaoming_dict)

# 3.清空字典
xiaoming_dict.clear()
print(xiaoming_dict)

