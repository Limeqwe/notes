# a = input('a = ') # 输入的值默认是str
# print(type(a))
# import string

#repr() 函数将对象转化为供解释器读取的形式。
# dict = { 'a':1,'b':2,'c':3,'d':4,'e':5}
# print(dict)
# print(repr(dict))

#形如r"c:\news" 由r开头引起的字符串就是申明了后面引号里的东西是原始字符串
#file = open('c:\\news')
#file = open(r'c:\news')

# lst = [i for i in range(10)]
# print(lst)
# print(lst[::3])
# print(lst[::-3])
# print(lst[1:4:2])
# lst1 = list('hello')
# print(lst('hello'))

# b={"I":2,'love':1,'China!':0}
# print(' '.join(b))
# print('-'.join(b))

# lst = ['We','Qw','qr','qr','We']
# print(lst.count("qr"))
# print(lst.index("We"))

# lst = [i*2 for i in range(10)]
# print(lst)
# insert(index,)
# lst1 = lst.insert(3,'insertNum')
# lst2 = lst.insert(0,'insertNum')
# print(str(lst))

#pop() 删除一个元素 ，默认是最后一个元素
# 不可变类型为Number、string、tuple 不可变数据类型的值变化，地址也会变.
# 可变类型为: List dict set 可变数据类型变量中的值变化，地址不会变.

# dict = {'a':12,'b':28,'c':37,'d':11}
# print(dict.items())
# dict2 = sorted(dict.items(),key = lambda x:x[1])
# print(dict2)

# name = '小明'
# age = 12.134
# print("name is {name} and the age is {age:.1f}".format(name=name,age=age))

# seq = [1,2,3,4,5,6]
# seq = [str(i) for i in seq]
# print('+'.join(seq))

# d = {'title': 'Python Web Site','url': 'http://www.python.org','spam':0}
# print(d.items())

# d = {}
# d.setdefault('name','N/A')
# print(d)
# d['name'] = 'Gumby'
# print(d)
# d.setdefault('name','N/A')
# print(d)

# *的返回值是一个列表(不论个数) *args是打包元组 *kwargs是打包成列表
# name = 'Albus Percival Wulric Brian Dumbldeore'
# first,*middle,last = name.split(' ')
# print(middle)

# 可以使用global来获取全部变量 例如:有一个名为parameter的全局变量，那么在combine(parameter)函数内部访问全局变量时，因为与参数重名，必须使用globals()['parameter']
# def cimbine(parameter):
#     print parameter+globals()['parameter']


# eval 会计算字符串形式的Python表达式，并返回结果的值。

#   exec语句不会返回任何对象。而eval会返回表达式的值。 函数exec主要用于动态地创建代码字符串。 使用exec可以有效的防止因为变量和内置函数名相同而覆盖的问题
# from math import sqrt
# scope = {}
# exec('sqrt=1',scope)
#sqprt(4)