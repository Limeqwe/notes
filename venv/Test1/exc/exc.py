                            #异常
'''
常用异常
Exception             所有异常的超类
AttributeError        引用属性或给它赋值失败时引发
OSError               操作系统不能执行指定任务时引发，有多个子类
IndexError            使用序列中不存在的索引时引发，为LookupError子类
KeyError              使用映射中不存在的键时引发，为LookupError子类
NameError             找不到名称(变量)时引发
SyntaxError           代码不正确时引发
TypeError             将内置操作或函数用于类型不正确的对象时引发
ValueError            非法参数时引发
ZeroDivisionError     在除法或求模运算的第二个参数为零时引发
1. raise AttributeError raise 为抛出异常的关键字
2. 创建异常类  需直接或间接地继承Exception
'''

'''
try:
    x = int(input("Put the first number: "))
    y = int(input("Put the Second number: "))
    print (x / y)
except ZeroDivisionError:
    print('The second number can\'t be zero!' )
'''

'''
try:
    1 / 0
except ZeroDivisionError:
    raise ValueError from ZeroDivisionError  提供自己的异常上下文
    raise ValueError from None  使用None来禁用上下文
'''

'''
def faulty():
    raise Exception('Someting is wrong')
def ignore_exception():
    faulty()
def hadle_exception():
    try:
        faulty()
    except :
        print('Exception handled')
ignore_exception()
'''

                                #警告
'''
from warnings import warn
warn('just a warnning')
'''

'''
from warnings import warn
from warnings import filterwarnings
filterwarnings('ignore')
warn("Anyone out there?")
filterwarnings('error')
warn("Something is very wrong!")
'''

                                #DB API 异常
'''
StandardError      所有异常的超类
InterfaceError     与接口相关的错误
DatabaseError      与数据库相关的错误
DataError          数据相关
OperationalError   数据库操作内部的错误
IntegrityError     关系完整性遭到破坏
ProgramingError    用户变成错误 如未找到数据库表
NotSupportedError  请求不支持的功能
'''