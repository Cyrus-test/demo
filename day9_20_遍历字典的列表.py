studen = [
    {"name": "阿土"},
    {"name": "小美"}
]

findname = "小123"

for stu_dict in studen:
    print(stu_dict)
    if stu_dict["name"] == findname:
        print("找到了 %s" % findname)
        # 如果已经已经找到，应该直接退出循环，而不再循环后续元素
        break
    else:
        print("很抱歉，没有找到 %s" % findname)



else:
# 如果希望在搜索列表的时，所有的字典检查之后，都没有发现所寻找的目标，还希望有一个统一的提示！
    print("很抱歉，没有找到 %s" % findname)


print("循环结束")