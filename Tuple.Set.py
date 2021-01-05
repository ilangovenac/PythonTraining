t1=(10,20,20,'hi',30,40,50)
t2=(10,20,20,'hi',30,40,50)
print(t1)
print(id(t1))
print(id(t2))
t1=(10,20,20,30,40,50)
print(id(t1))
print(id(t2))

t2=(10)
print(t2)
t2=(10,)
print(t2)

#Tuple packing and unpacking
a,b,c,d=10,20,30,40
t=a,b,c,d#tuple packing
print(t)
p,q,r,s=t#tuple unpacking
print(p,q,r,s)


#Command line input for tuple
t= eval(input("Enter values : "))
print(t) 

#Functions in tuple
t=(10,20,20,30,40,50)
print(t.count(20))
print(len(t))
print(t.index(40))
print(min(t))
print(max(t))
print(sum(t))
t1=sorted(t)
print(t1)
t1=sorted(t,reverse=True)
print(t1)

#Set Datatype
lst=[10,20,20,'hi',40]
s=set(lst)
print(s)

#Empty set creation
s={}
print(s)
print(type(s))
s=set()
print(type(s))

#Set functions
s1={10,20,30,40,50,60,70,80}
s1.remove(30)
print(s1)
s1.discard(40)
print(s1)
s1.discard(200)
print(s1)
s1.remove(100)
print(s1)

#Wenn diagram functions
s1={10,20,30,40,50,60}
s2={40,50,60,70,90}
print(s1 | s2)#union
print(s1 & s2)#intersection
print(s1-s2)
print(s2-s1)
print(s1^s2)
print((s1|s2)-(s1&s2))









