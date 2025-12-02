#Identity Operators (is, is not)
#

a=3
b=2

c=a

print(a is b)  #False

print(a is c)  #True

print(id(a))
print(id(b))
print(id(c))

#is not :

print(a is not b)  #True
print(a is not c)  #False