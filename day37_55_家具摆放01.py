class HomeItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占用面积 %.2F" % (self.name, self.area)


bed = HomeItem("席梦思", 4)
chest = HomeItem("衣柜", 5)
table = HomeItem("餐桌", 2)

print(bed)
print(chest)
print(table)
