#Finding maximum number in a listlst=[13,61,90,81,16]
max=lst[0]
for x in lst:
    if x>max:
        max=x
print('Maximum number:',max)

#Program to remove duplicates
lst=[10,20,30,10,40]
for x in lst:
    if lst.count(x)>1:
        lst.remove(x)
print('Corrected list:',lst)

#Finding words greater than n
lst=['hi','hello','how','ilango','in']
n=int(input('Enter limit for length: '))
for x in lst:
    if len(x)>n:
        print(x)

#Finding common numberlst1=[10,20,30,70,50,40]
lst2=[18,20,50,25,6]
for x in lst1:
    for j in lst2:
        if x==j:
            print(x)
#Sequence
sen=input('Enter a sequence: ')
out=''
i=0
while i<len(sen):
    j=ord(sen[i])
    out+=sen[i]
    out+=chr(j+int(sen[i+1]))
    i+=2
print(out)

#Reversing a sentence
sen=input('Enter a sentence: ')
lst=sen.split()
#print(lst)
revlst=[]
i=len(lst)-1
while i>=0:
    revlst.append(lst[i])
    i-=1
#print(revlst)
out=' '.join(revlst)
print(out)

#Adding substring to existing strings in a list
sen=input('Enter the terms: ')
lst=sen.split()
lst1=[]
i=0
while i<len(lst):
    lst1.append(lst[i]+'day')
    i+=1
out=' '.join(lst1)
print(out)
