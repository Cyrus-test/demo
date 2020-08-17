class HomeItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占用面积 %.2F" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        # Python 能够自动将一对括号内部的代码连接到一起
        return ("户型：%s\n总面积: %.2f\n【剩余面积:%.2f】\n家具列表:%s" %
                (self.house_type, self.area,
                 self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加的家具: %s" % item)


# 1.创建家具
bed = HomeItem("席梦思", 4)
chest = HomeItem("衣柜", 5)
table = HomeItem("餐桌", 2)

print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)




