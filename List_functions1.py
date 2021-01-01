lst1=list['a','abc',10,20,20,15.3]
lst2=list['a','abc',10,20,20,15.3]
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

#Functions

#split()
sen='how are you'
lst=sen.split()
print(lst)
lst=sen.split('are')
print(lst)

#count
lst=[10,20,'hi',2.3,'hi']
print(lst.count(20))
print(lst.count('hi'))
print(lst.count(30))

#index
lst=[10,20,'hi',2.3,'hi']
print(lst.index(20))
print(lst.index('hi'))
print(lst.index(30))

#append
lst1=[10,20,'hi',2.3,'hi']
lst2=[0,1]
lst1.append(10)
lst1.append('hello')
lst1.append(lst2)
print(lst1)

#insert
lst=[10,20,'hi',2.3]
lst.insert(3,5)
print(lst)
lst.insert(-10,4)
lst.insert(-5,3)
lst.insert(10,50)
lst.insert(9,60)
print(lst)
print(lst.insert(0,5))

#extend
lst1=[10,20,30]
lst2=['a','b','c']
lst3=lst1+lst2
lst1.extend(lst2)
print(lst1)
print(lst3)

#remove
lst=[10,20,30,'a','b','c']
lst.remove(20)
print(lst)
lst.remove(50)
print(lst)

#pop
lst=[10,20,30,'a','b','c']
lst.pop()
print(lst)
lst.pop(2)
print(lst)
lst.pop(-1)
print(lst)

#reverse
lst=['a','b','c']
lst.reverse()
print(lst)
























