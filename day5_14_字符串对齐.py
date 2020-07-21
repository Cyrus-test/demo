# 要求：顺序并且居中对齐输出以下内容
# 假如，以下是从网络上抓取的
poem = ["\t\n登黄鹤楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem :

    # print("|%s|" % poem_str.center(10)," ") # 居中对齐
    # print("|%s|" % poem_str.ljust(10), " ") # 靠左对齐
    # print("|%s|" % poem_str.rjust(10), " ") # 靠右对齐

    # 先使用strip方法去除字符串中的空白字符
    print("|%s|" % poem_str.strip().center(10) , " ")