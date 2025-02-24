'''
Number : int 10,20 ,  float 10.20, 20.30
String : str : "Ajinkya", 'Pawar'
Boolean : bool : True False

There are two differeent types of variables in the python
1. Local variable= The variable which are inside the function as well as fuction arg 
2. Global variable= Declare outside the function


'''
### Local variables
# We can write the function by using def keywaords
def disp1():
    name="Pawar" # name which is declare inside the fuction
    print("0-arg function",name)
def disp2(name):#name is as fuction args
    print("1-arg function ",name)

disp1()
disp2("Ajinkya")
""" O/P

0-arg function Pawar
1-arg function  Ajinkya
"""
print("==================================================")

###Global variables

name="Pune" # Global variable
def a1():
    print("Global variable is ",name)
a1()
'''' O/P
Global variable is  Pune
'''
print("==================================================")

# local and global variable having same name the priority goes to local variables
a,b=10,20
def aj(a,b):
    print(a+b) #local variables
    print(globals()['a']+globals()['b'])
aj(100,200)

""" O/P priority goes to local variable if want to use golabal global variables the use globals functions
300
30
"""
print("==================================================")
"""
Function argumnets are 
1. default arguments
2.Required argument
3. Keyword argument
4. var argiment

"""

def defaultargs(eid=100,ename="ajinkya"):
    print(eid,ename)

defaultargs() # if we not provided the values then it used default values
defaultargs(10) #if we provided the the single value then it will changes the that values only and remaining as it is
defaultargs(111,"Pawar") # If we passed all the values then it will print passed values not default values
''' O/P
100 ajinkya
10 ajinkya
111 Pawar
'''
print("==================================================")

## Function Return statement 
def r1():
    print("Good morning")
    return 10
    return 20 #it taking only first return values & default rutern value is none
x=r1()
print(x)
""""
Good morning
10
"""
print("==================================================")
""""
Once we are usig the same outer function variables inner function then we can not declare local var 
"""
def Outer():
    name="Ajinkya"
    def Inner():
        #print(name)
        name="Pawar"
        print("Inner function",name)
    print(name)
    Inner()
    print(name)
Outer()
'''
Ajinkya
Inner function Pawar
Ajinkya
'''
print("==================================================")

def Outer():
    name="outer"   # non local
    def Inner1():
        name="inner1"
        print("inner1 function :",name)
    def Inner2():
        nonlocal name
        name="inner2"
        print("inner2 function :",name)
    def Inner3():
        global name
        name="inner3"
        print("inner3 function :",name)
    #Outer function code
    print(name) #outer
    Inner1()    
    print(name) #outer
    Inner2()
    print(name) #inner2
    Inner3()
    print(name) #inner2
Outer()
print(name)
'''' O/P
outer
inner1 function : inner1
outer
inner2 function : inner2
inner2
inner3 function : inner3
inner2
inner3
'''
print("==================================================")
