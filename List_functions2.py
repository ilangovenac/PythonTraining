#Sorting names and time
names=['kumar','ravi','bala','dina']
time=[13,11,16,10.3]
for i in range(len(time)):
    for j in range(i,len(time)):
        if time[i]>time[j]:
            time[i],time[j]=time[j],time[i]
            names[i],names[j]=names[j],names[i]
for i in range(len(time)):
    print(names[i]+'-',time[i])

#Sorting list
lst=[23,12,45,35,11]
lst1=['ravi','kumar','abc','xyz']
lst.sort(reverse=True)
lst1.sort(reverse=True)
print(lst)
print(lst1)

#List aliasing and cloning
lst1=[20,33,55]
lst2=lst1 #List aliasing
lst3=lst1[:] #List cloning
print(id(lst1))
print(id(lst2))
print(id(lst3))

#Operators
lst1=[20,33,55]
lst2=[10,33,55]
lst3=['hi','hello']
lst4=['abc','xyz']
print(lst1!=lst2)
print(lst2<lst1)
print(lst1 is lst2)
print(lst4<lst3)

#Membership operator and clear() function
lst=[34,23,54,'hi','the']
print(34 in lst)
print('old' in lst)
print('hi' in lst)
lst.clear()
print(lst)

#List comprehension
lst1=[x for x in range(10)]
print(lst1)

lst2=[x for x in lst1 if x%2==0]
print(lst2)

lst=['hi','how','are','you']
lst3=[lst[2] for x in lst]
print(lst3)



