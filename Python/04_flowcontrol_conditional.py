"""
1. Conditional statement
if
if-else
elif


2. Iteration statement
for 
while

3. Transfer statement 
break
continue
"""

# Case1: If condition

a=10
if a>20:
    print("True condition")
else:
    print("False condition")  

# O/P False condition
print("==============================")

# Case2:  Condition we can passed by boolean values as well True,1 or False,0
if True:
    print("True condition")
else:
    print("False condition")    
# True condition
print("==============================")
# Case3:  Indentation is required in "if condtion" not provided then act as a normal code
if 1:
    print("If block condtion part")
    print("2nd statement of if block")
print("Normal code outside the if block") 

'''' O/P
If block condtion part
2nd statement of if block
Normal code outside the if block
'''
print("==============================")
# Case 4: We can write the condition in the one line with multiple statement is present then {} if not given the it act as the normal code 

print("if block") if 10>20 else print("else block")
print("if block") if 10<20 else print("else block")
{print("if1 block"),print("if2 block")} if 10<20 else {print("else1 block") ,print("else1 block")}


''' O/P
else block
if block
if1 block
if2 block
'''
print("==============================")

# elif conditional statement here else block is optional


a=100
if a==10:
    print("ajinkya")
elif (a==100):
    print("pawar")
elif a==109:
    print("swaraj")
else:
    print("ajju") 
#O/P pawar









    