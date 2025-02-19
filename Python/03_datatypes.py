
#Input function= Only in string format
# act as string concatinations

num1=input("Enter first number: ")
num2=input("Enter second number: ")
add = num1+num2
print("Addition is :",add)

''' O/P
Enter first number: 10
Enter second number: 20
Addition is : 1020

'''
print("===================================")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
add = num1+num2
print("Addition is :",add)

"""" O/P
Enter first number: 11
Enter second number: 22
Addition is : 33.0
"""
print("===================================")

eid=int(input("Enter eid:"))
ename=str(input("Enter ename: "))
esal=str(input("Enter esal: "))

print("eid is :",eid)
print("ename is :",ename)
print("esal is :",esal)
print("===================================")

"""" O/P
Enter eid:10
Enter ename: Ajinkya
Enter esal: 100000
eid is : 10
ename is : Ajinkya
esal is : 100000
"""
##formating data by using the % and {}
'''
int= %d
float= %g for %f
string= %s
'''
eid=int(input("Enter eid:"))
ename=str(input("Enter ename: "))
esal=float(input("Enter esal: "))
# By using the %
print("Emp id=%d Emp name=%s Emp sal=%g"%(eid,ename,esal))

"""" O/P
Enter eid:11
Enter ename: Ajinkya
Enter esal: 100000.2
Emp id=11 Emp name=Ajinkya Emp sal=100000
"""
print("===================================")

# By using the {} format function
print("Emp id={} Emp name={} Emp sal={}".format(eid,ename,esal))

""" O/P
Enter eid:11
Enter ename: Pawar
Enter esal: 10000.2
Emp id=11 Emp name=Pawar Emp sal=10000.2
"""
print("===================================")
