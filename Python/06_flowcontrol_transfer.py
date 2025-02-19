"""
Transfer statement 
1. break=it stops the execution, it should be inside the loop block outside the loop showing the SyntaxError 
2. continue= it skip the perticular iteration

"""
for x in range(10):
    if x==4:
        break
    print(x)

''' O/P
0
1
2
3
'''
print("==================================================")

for x in range(10):
    if x==4:
        continue
    print(x)
''' O/P
0
1
2
3
5
6
7
8
9
'''
