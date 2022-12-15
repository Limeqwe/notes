'''
property方法中有四个参数
第一个参数是方法名，调用对象属性时自动触发执行
第二个参数是方法名，调用对象属性时自动触发执行方法
第三个参数是方法名，调用del对象属性时自动触发执行方法
第四个参数是字符串，调用对象属性。doc，此参数是该属性的描述信息
'''
#python 2.x 默认是经典类 使用深度优先遍历
#python 3.x 默认是新式类 使用广度优先遍历
'''
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self,size):
        # print(size)
        self.width,self.height = size
        print('use set_size'+str(self.width)+' '+str(self.height))
    def get_size(self):
        print('use get_size'+str(self.width)+' '+str(self.height))
        return self.width,self.height
    def del_size(self):
        print ("del_size")
    size = property(get_size,set_size,del_size,'日志记录')
'''
'''
class Rectangle1:
    def __init__(self):
        self.width = 0
        self.height = 0
    @property
    def size(self):
        print('use size'+str(self.width)+' '+str(self.height))
        return self.width,self.height
    @size.setter
    def size(self,size):
        self.width,self.height = size
        print('use size'+str(self.width)+' '+str(self.height))
    @size.deleter
    def size(self):
        del self.width,self.height

obj = Rectangle1()
obj.size
obj.size = 15,12
del obj.size
'''

# class  TestIterator:
#     value = 0
#     def __next__(self):
#         self.value += 2
#         if self.value > 10 :
#             raise StopIteration
#         return self.value
#     def __iter__(self):
#         return self
# ti =TestIterator()
# print(list(ti))

def test():
    print("hello")
if __name__ == "__main__": test()