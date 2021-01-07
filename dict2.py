#Homework
name='anandham'
d={}
for x in name:
    d[x]=d.get(x,0)+1
#print(d)
l=[]
print('Occurences:')
for letter,count in d.items():
    print(letter,'-',count,'times')
    l.append(count)
l.sort()
countmax=l[-1]
for letter,count in d.items():
    if count==countmax:
        print(letter,'has occured maximum times(%d)'%count)
        
#interchanging key and values in dict
d={1000:'Ilango',1001:'Ravi',1002:'Kumar'}
print(d)
d={values:keys for keys,values in d.items()}
print(d)

#Sorting of keys and values in a dict
d={1244:'Ilango',1433:'Kumar',1001:'Raj',1992:'Ravi'}

for x in sorted(d.keys()):
    print(x)
for x in sorted(d.values()):
    print(x)
for x in sorted(d.items()):
    print(x)


#Binary selection
l=[12,23,34,45,56,67,87,88]
l.sort()
num = int(input('Enter number to search: ' ))
min = 0 
max = len(l)-1

while min<=max:
    avg = (min+max)//2	
    if num==l[avg]: 
        print('Number is present at:',avg)
        break
    elif num>l[avg]:  
        min = avg + 1
    else:
        max = avg - 1	
else:
    print('Number not present')

#Bubble sort
l=[12,9,45,33,39,22,50]
print('Before sorting: ',l)
i=1
while i<len(l):
	j= 0
	while j<len(l)-i:		
		if l[j]>l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
		j+=1
	i+=1
	
print('After sorting:',l)

#Insertion sort
l=[12,9,45,33,39,22,50]
print('Before sorting:',l)
length=len(l)-1
for x in range(length):
    for i in range(x,length):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print('Sorted order:',l)


#update() function in dict
d1={1000:'Ilango',1001:'Raj'}
d2={1002:'Kumar',1003:'Dina'}
d3={1005:'Ravi'}
d={}
print(d)
d.update(d1)#update() takes only one argument
print(d)
d.update(d2)
print(d)
d.update(d3)
print(d)
d4={1000:'James'}#to change value of a key 
d.update(d4)
print(d)





