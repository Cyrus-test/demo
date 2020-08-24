class A:
    def test1(self):
        print("A--wo ui 1")
    def test2(self):
        print("A--wo ui 2")


class B:
    def test1(self):
        print("B--wo ui 1")
    def test2(self):
        print("B--wo ui 2")

# 继承A和B，在类后面添加A类和B类即可
class C(B, A):
    pass


# 创建子类对象
c = C()
c.test1()
c.test2()
# 确定C类对象调用的方法的顺序

print(C.__mro__)

