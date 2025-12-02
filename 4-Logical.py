#Logical Operators (and, or, not)

'''
and :
T and T = T
T and F = F
F and F = F
F and T = F

OR :
T and T = T
T and F = T
F and F = T
F and T = T

not :
not(True)=False
not(False)=True

'''

#Examples of and & or
a=56
b=13

print((a>b) and (a!=b))  #True

print((a==b) and (a!=b))  #False

print((a==b) or (a>b))  #True

print((a>b) and (a!=b))  #False


#Examples of not
a=67
b=89

print(not(a>b)) #not(F) = True
print(not(a==b)) #not(F) = True
print(not(a!=b)) #not(T) = False




