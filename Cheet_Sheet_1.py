from math import *
#Arithmatic operator
print(3+2)
print(3-1)
print(3*2)
print(3/2)
print(3//2)
print(3**2)
print(2%5)
#Assignment operator
num=5
num*=3 #Change it to any arithmatic +,-,//,*,**
print(num)
#Round function with fixed no. of digits after decimal point here 6
print(round(4.785621,6))
#Absolute function 
print(abs(-4.56))
#Floor and Ceil function need to import math
print(floor(4.563))
print(ceil(-4.563))
#Comparison Operator
num1=4
num2=3
print(num1==num2)
print(num1!=num2)
print(num1 >= num2)
#Strings
message="'BD's World"
print(message)
message='"BD'+"'"+'s" World'
print(message)
message="""Jai's Cousine Brother
is my Best-friend's 
nephew."""
print(message)
x,y=3,2
print(x**y)
#Boolean Oparation
x,y=True,False
print(x and not y)
print(not x and y or x)
#If condition evaluates to False
if None or 0 or 0.0 or '' or [] or {} or set():
	#None,0,0.0,empty strings,or empty
	#container types are evaluated to False
	print("Dead code")#Not reached
print(int(3.9))
print(float(3))
s="The youngest pope was 11 years old"
print(s[0])
print(s[1:3])
print(s[-3:-1])
print(s[-3:])
x=s.split()
print(x[-3]+" "+x[-1]+" "+x[2]+"s")
y="   This is lazy\t\n   "
print(y.strip())
print("DrDre".lower())
print("attention".upper())
print("smartphone".startswith("smart"))
print("another".find("other"))
print("cheat".replace("ch","m"))
print('-'.join(["F","B","I"]))
print(len("MyNameisBiplab"))
print("ear" in "earth")
print('Yes')
print("Yes".upper())
print("""Hello Biplab! it's my
pleasure to meet you
in person.Nice to hear you,I'm glad to meet to too""".lower())
print(str(5)=='5')
print('Biplab Das')