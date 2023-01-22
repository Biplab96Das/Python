#List
l=[1,2,3]
print(len(l))
#Adding Element
m,n=[1,2,2],[1,2,4]
m.append(4)#Cann't include directly int print statements
n.insert(2,2)#Cann't print it
print(m)
print(n)
print([1,2,2]+[4])
#Removal of Element
m.remove(2)
n.remove(1)
print(m,n)
#Reversing an element
l.reverse()
print(l)
#Sorting
o=[1,9,-7,0,5,2,6,-1]
o.sort()
print(o)
#Indexing
m=[1,0,2,0,-5,2,0,6,2]
print(m.index(-5))
print(m.index(2,2))#Index of element 0 in m for index>=2
#Stack
stack =[3]
stack.append(42)#Push is append only
print(stack)
print(stack.pop())
print(stack.pop())
#Set
basket={"apple",'eggs',"banna",'orange'}
same =set(['apple','eggs','banna','orange'])
print(basket)
print(same)
#Dictionary
calories={'apple':52,'banna':89,'choco':546}
print(calories['apple']<calories['choco'])
calories['chappu']=74
print(calories['banna']<calories['chappu'])
print('apple' in calories.keys())
print(52 in calories.values())
for k,v in calories.items():
	print(k) if v>500 else None
#Membership Operator
print('eggs' in basket)
print('mashroom' in basket)
#List Comprehension
l=[('Hi'+" "+ x) for x in ['Alice','Bob','Pete']]
print(l)
l2=[x*y for x in range(3) for y in range(3) if x>y]
print(l2)
squares={x**2 for x in {0,2,4} if x<4}