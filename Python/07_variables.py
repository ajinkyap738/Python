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
