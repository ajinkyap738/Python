""""
String is immutable in nature
declare by using "" and ''

"""
s1="ajinkya"
print(s1)
s2='Pawar'
print(s2)
'''
ajinkya
Pawar
'''
print("=============================================")
s="ajinkya" # 7 char
print(s[2]) #provide the values of index 2
print(s[2:5]) #print char in the index format and excluded the last index value
print(s[0:6:2])  # print char in the index format and by incrementing the value of 2
#print(s[10]) #IndexError: string index out of range

''' O/P
i
ink
aik
'''
print("=============================================")

s="ajinkya" # 7 char -7,-6,-5,-4,-3,-2,-1
print(s[-2]) #y
print(s[-5:-1]) #inky
print(s[:-1]) # ajinky
print(s[:]) #ajinkya

print("=============================================")

"""
len() = to find the legth of string
strip()= to remove the white space from the string
lstrip()=  to remove the white space/any repeated char from the string
"""
s="   ajinkya   "
print(len(s)) #13
print(s.strip())#ajinkya
print(len(s.strip()))#7
'''
13
ajinkya
7
'''
print("=============================================")


s1="@@@@@Ajinkya$$$$$"
print(len(s1))
print(s1.lstrip("@"))
print(s1.rstrip("$"))
print(s1.rstrip("$").lstrip("@"))
print(len(s1.rstrip("$").lstrip("@")))
'''
Ajinkya$$$$$
@@@@@Ajinkya
Ajinkya
7
'''
print("=============================================")

''' 
id() print the memory address
is, is not : memory compare: return boolean
==, != : data compare : return boolean
in, not in : check data available or not : return boolean

'''
name1="ajinkya"
name2="pawar"
name3="ajinkya"
print(id(name1))
print(id(name2))
print(id(name3))
print("-------")
print(name1 is name2) #memory comapre false
print(name1 is name3) # true
print("-------")
print(name1 is not name2) #true
print(name1 is not name3) #false
print("-------")
print(name1 == name2) #Data compare false
print(name1 == name3) # true
print("-------")
print(name1 != name2) #true
print(name1 != name3) #false
print("-------")
print("ink" in name1) #check provided string present or not true
print("ink" in name2) #false
print("ink" in name3) # true
print("-------")
print("ink" not in name1) #check negative scenario provided string present or not false
print("ink" not in name2) #true
print("ink" not in name3) # false
print("-------")
print("========================================")

""""
Concatition =adding the data
replication = replica of same type of data

"""
s1="ajinkya"
s2="pawar"
s3=s1+s2
print(s3) #ajinkyapawar

ss= s1*3 + s2*2 #is called as replication 
print(ss) #ajinkyaajinkyaajinkyapawarpawar 
print("========================================")
"""
Relational operator > < >= <= = !=

"""

print("ajinkya">"aj") #true
print("ajinkya"<"aj") #Flase
print("ajinkya">="aj") #True
print("ajinkya"<="aj") # False
print("ajinkya"=="aj") #False
print("ajinkya"!="aj") #True

print("========================================")

text="hi ajinkya pawar here"
print("upper =>",text.upper()) #uppercase format
print("lower =>",text.lower()) #lowercase format
print("capitalize =>",text.capitalize()) # starting string with capital letter
print("join =>","+".join(text.split())) # join the string by using join fuction
print("Replace =>",text.replace("ajinkya","swaraj")) #replace the keyword from the string old to new by using replace function
''' O/P
upper => HI AJINKYA PAWAR HERE
lower => hi ajinkya pawar here
capitalize => Hi ajinkya pawar here
join => hi+ajinkya+pawar+here
Replace => hi swaraj pawar here
'''

print("========================================")
text1="hi split check.in here there"

print(text1.split())
print(text1.split("."))
#enumarate function-to get the data in index format
str1="ajju"
print(tuple(enumerate(str1))) # Check the output 
print(list(enumerate(str1)))
'''

['hi', 'split', 'check.in', 'here', 'there']
['hi split check', 'in here there']
((0, 'a'), (1, 'j'), (2, 'j'), (3, 'u'))
[(0, 'a'), (1, 'j'), (2, 'j'), (3, 'u')]
'''
print("========================================")

#Check the count of string

a1="pawarpawar"
print(a1.count('p')) #count of p in the string is showing 2
print(a1.count('pawar')) #Count of wod pawar showing 2
print(a1.count("p",0,8)) # count of p inside the index 0 to 8 is 2

print("========================================")

#Check startswith() and endswith() function

a2="check ajinkya pawar is here"
print(a2.endswith("here"))
print(a2.endswith("ajinkya",0,13))
print(a2.startswith("check"))
print(a2.endswith("ajinkya",5,12))
''''
True
True
True
False
'''
print("========================================")
# find () gives + and - optput

a3="welcome to python"
print(a3.find("python")) # if condition is true then return output as +ve
print(a3.find("ajinkya")) # If condition is false then return output as -ve

print(a3.index("python"))
print(a3.index("c",0,8))
a4="WelCome To Python"
print(a3.swapcase())

#Check alphanumeric or not
# isalnum()=check string and digit
# isalpha()=check alphabate only
# is digit()=check numeric/digit value 

print(a4.isalnum()) #false
aa4="ajinkyapawar"
print(aa4.isalpha()) #true
a5="1234"
print(a5.isdigit()) # true

print("========================================")
"""
islower()= check the string in lowercase or not
isupper()= check the string in uppercase or not
isspace()= check the string conatins space or not
"""
q1="pawar"
print(q1.islower()) # true
q2="AJINKYA"
print(q2.isupper()) #true
q3=" "
print(q3.isspace()) #true
print("========================================")
#get the count of iterated char in string without count function
e1="ajinkya"
print(e1.count("a")) #2
count=0
for x in s1:
    if x=='a':
        count=count+1
print(count)
print("========================================")

z1="ajinkya pawar swaraj pawar supriya pawar"
print(z1.count("pawar")) # will get direct count
w1=z1.split() #split the string by space
count=0
for x in w1: #iterate the splited string
    if x=="pawar":
        count=count+1;
print(count)
'''
3
3
'''
print("========================================")
aj=input("Enter a string: ")
words=aj.split()
print(words)
words.sort()
for x in words:
    print(x)
print('-----------')
# reverse the sort list
words.sort(reverse=True)
for x in words:
    print(x)
""""
Enter a string: ajju apawar
['ajju', 'apawar']
ajju
apawar
apawar
ajju
"""
print("========================================")

