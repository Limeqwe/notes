import hashlib

str = 'this is a test'

hl = hashlib.md5()
print (type(hl))
print (hl.hexdigest())
