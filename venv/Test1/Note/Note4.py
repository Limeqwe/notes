# 模块
#dir 查明模块包含哪些东西
import copy
# print (dir(copy))
print([n for n in dir(copy) if not n.startswith('_')])