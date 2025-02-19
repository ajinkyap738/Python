''''
Numbers = int float  = 10,20,30   10.2, 11.3
String = str    = "Ajinkya"    'Pawar'
Boolean = bool  = True False 1,0

'''
# Dynamically typed language no need to specify the type of variables
eid=11  #int
ename="ajinkya"  #String
esal=10000.76  # Float

# Print the variables
print(eid)
print(ename)
print(esal)

""" O/P
11
ajinkya
10000.76
"""
print("===================================")

#Check the type of the variable by using type function

print(type(eid))
print(type(ename))
print(type(esal))

""" O/P
<class 'int'>
<class 'str'>
<class 'float'>
"""
print("===================================")

# How to write the code in singleline of code
a,b,c=10,20,30
print(a)
print(b)
print(c)
print(a+b+c)
"""O/P
10
20
30
60
"""
print("===================================")

#How to assign on value to three variables

a=b=c=10
print(a+b+c)
#30
print("===================================")

##Concatinations happened with same type of data only
print(10+20)

#print(20+"Ajinkya") #TypeError: unsupported operand type(s) 
print(10+True)

print("===================================")
## Re-assigning the variables

a=10
print(a)
a=1000
print(a)
""" O/P
10
1000
"""
print("===================================")

## Swappig the data
a,b=11,22
a,b=b,a
print(a)
print(b)
""" O/P
22
11
"""
print("===================================")


##Delete the variable once use
a=10000
print(a)
del a
#print(a)
"""" O/P
NameError: name 'a' 
"""

print("===================================")

## Print the data
eid,ename,esal=111,"Ajinkya",111111
print("Emp eid is=",eid)
print("Emp ename is=",ename)
print("Emp esal is=",esal)
print(eid,ename,esal)
("===================================")





