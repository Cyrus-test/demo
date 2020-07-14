# 要求：顺序并且居中对齐输出以下内容

poem = ["登黄鹤楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem :

    # print("|%s|" % poem_str.center(10)," ") # 居中对齐
    # print("|%s|" % poem_str.ljust(10), " ") # 靠左对齐
    print("|%s|" % poem_str.rjust(10), " ") # 靠右对齐