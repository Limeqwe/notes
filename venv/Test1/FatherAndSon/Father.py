class A:
    age = 12
    name = 'A'
    def test(self):
        print("from A")
class B(A):
    def test(self):
        print("from B")
class C(A):
    def test(self):
        print("from C")
class D(B,C):
    def test(self):
        print("from D")
#类和对象获取的一些方法
    # obj = D()
    # print(obj.test())
    # # issubclass 确定一个类是否是另一个类的子类
    # print(issubclass(B,A))
    # # __bases__ 获取其基类
    # print(D.__bases__)
    # #确定对象是否是特定类的实例
    # d = D()
    # print(isinstance(d,D))
    # #获取对象是属于哪个类
    # print(d.__class__)
#接口查询 hasattr 查询方法是否存在 getattr(tc,'talk',None) 检查属性是否存在 setattr用于设置对象的属性
#__dict__ 查看对象中存储的所有值
# print(A.__bases__)