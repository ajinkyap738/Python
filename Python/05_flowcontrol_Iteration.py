"""
Iteration statement
 1. for 
    for temp-var in iteration-data
        print(temp-var)
 2. while 

in the range function last value if excluded
range(10) = 0,1,2.....,9
range(4,10)= 4,5.....9
range(4,10,3)= 4,7  (increment by 3 untils 9 because last value is excluded)
range(10,4,-3)= 10,7 (decrement by 3 untils 3 because last value is excluded)
range(-10,-5)= -10,-9,-8,-7,-6
range(-10,-5,2)= -10,-8,-6
range(-5,-10,-2)= -5,-7,-9




"""
for x in range(10):
    print("ajinkya",x)
""" O/P
ajinkya 0
ajinkya 1
ajinkya 2
ajinkya 3
ajinkya 4
ajinkya 5
ajinkya 6
ajinkya 7
ajinkya 8
ajinkya 9
"""     
print("============================================")
for x in range(4,10):
    print("pawar",x)  
""" O/P
pawar 4
pawar 5
pawar 6
pawar 7
pawar 8
pawar 9

"""
print("============================================")
for x in range(4,10,3):
    print("aj",x)  
""" O/P

aj 4
aj 7
"""
print("============================================")
for x in range(10,1,-1):
    print("power",x)  
""" O/P
power 10
power 9
power 8
power 7
power 6
power 5
power 4
power 3
power 2
"""
print("============================================")
#print the list data by using the for loop
l=[10,20,30]
for x in l:
    print(x)
""" O/P
10
20
30
"""
print("============================================")
# print the tuple data by using for loop
t=(40,50,60)
for x in t:
    print(x)
""" O/P
40
50
60
"""    
print("============================================")

# for loop with else block 
#Case1: if for loop execution working fine then only else block will executed

for x in range(10):
    print(x)
else:
    print("normal execution of for loop") 

""" O/P
0
1
2
3
4
5
6
7
8
9
normal execution of for loop
"""

print("============================================")
#Case2: if for loop execution interrupted then else block will not executed

for x in range(10):
    if x==3:
        break
    print(x)
else:
    print("Noraml execution of for loop")
""" O/P
0
1
2
"""
print("============================================")

#Case3: if for loop execution interrupted by exception then else block will not executed

for x in range(10):
    print(x)
   # print(10/0)
else:
    print("Noraml execution of for loop")

""" O/P
0
ZeroDivisionError: division by zero

"""
print("============================================")

# Case4: by shutdown the 
import os
for x in range(10):
    print(x)
    # os._exit(0)
else:
    print("Noraml execution of for loop")

print("============================================")

""" While loop is used for the iterations

in the three cases else block will not execute 

case1: break
case2: exception
case3: exit(0)
"""

a=0
while a<10:
    print("Ajinkya while loop")
    a=a+1
else:
    print("normal block else block")
''' O/P
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
Ajinkya while loop
normal block

'''
print("============================================")
