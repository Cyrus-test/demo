class A:
    def test1(self):
        print("wo ui 1")


class B:
    def test2(self):
        print("wo ui 2")

# 继承A和B，在类后面添加A类和B类即可
class C(A, B):
    pass


# 创建子类对象
c = C()
c.test1()