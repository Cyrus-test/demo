class Tool(object):
    # 1.使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("剪刀")
tool3 = Tool("锤子")

tool3.count = 99
print("计数是：%d " % Tool.count)
