# 使用多个键值对，存储描述一个物体的相关信息，描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历

card_list = [
    {"name": "张三",
     "age": "16",
     "qq": "12314"},
    {"name": "老王",
     "age": "23",
     "qq": "100"}
]

for car_info in card_list :
    print(car_info)