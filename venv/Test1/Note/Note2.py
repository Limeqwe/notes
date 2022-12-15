# data  =  12
# def test1():
    # print(globals()['data'])
# test1()
# def test2():
#     global data
#     data = 24
# test2()
# print(data)

#map()是python的内置函数 叫映射函数() Input: map(function,iterables) Output 一个可迭代对象
# data = [[1,2],[3,4]]
# A=map(lambda x:x[0],data)
# print(type(A))
# for i in A :
    # print(i)

#filter(function,iterable)
# Demo_lists = [i for i in range(8)]
#
# Demo = filter(lambda x:x>2,Demo_lists)
# print(type(Demo))
# for i in Demo:
#     print(i)

#reduce函数先从列表（或序列）中取出2个元素执行指定函数，并将输出结果与第3个元素传入函数，输出结果再与第4个元素传入函数，…，以此类推，直到列表每个元素都取完。
#reduce函数相比于for函数会更慢 reduce(function,iterable)
# from functools import reduce
# a=[1,2,3,4,5]
# def add(x,y): return x + y
# print(reduce(add,a))

#多态（在python中协议通常指的是规范行为的规则，协议指定实现哪种方法以及这些方法应该做什么） 继承 封装 “云雀”为“鸟类”的子类，而“鸟类”为“云雀”的超类
#在表示复数的时候Python通常约定使用单数将首字母大写如,Bird和Lark

#python没有为私有属性提供直接的支持 而是要求程序员知道在什么情况下从外部修改属性是安全的
#要让方法或者属性成为私有的 在名称前用两个下划线

#需要注意的是，在派生类的构造函数中要明确调用其父类的构造函数。如果不显示调用，基类的构造函数不会被执行。这点和 C++、Java 不同。在 C++ 和 Java 中，基类的构造函数在创建派生类时是自动调用的
 # def __inaccessible(self):
class Secretive:
    def __inaccessible(self):
        print("Bet u cant see")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()
s = Secretive()
# s.__inaccessible()  私有类型 不可访问
s.accessible()
# s._Secretive__inaccessible() 可以通过此方法调用类里面的私有方法
