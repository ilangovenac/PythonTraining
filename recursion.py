#Homework
import random
def guess(comp):
    user=[]
    j=1
    for x in range(len(comp)):
        i=int(input('Enter digit%d: '%j))
        user.append(i)
        j+=1
        
    flag=[]
    for i in range(len(comp)):
        flag.append('X')
        
    if user!=comp:
        for x in range(len(comp)):
            if user[x]==comp[x]:
                flag[x]='C'
            elif user[x] in comp:
                flag[x]='P'
        print(flag)
        guess(comp)
     
    
    else:
        print('RIGHT!! The number is:',user)

comp=[]
for x in range(4):
    r=random.randint(0,9)
    comp.append(r)
guess(comp)

#reverse a number
s=0
def reverse(n):
    global s
    if n>0:
        r=n%10
        s=s*10+r
        n//=10
        reverse(n)
    return s

num=int(input('Enter a number: '))
rev=reverse(num)
print('Reverse of number:',rev)

#Palindrome check for string
def reverse(name):
    if len(name)==1 or len(name)==0:
        print('Palindrome')
    elif name[0]!=name[-1]:
        print('Not Palindrome')
    else:
        reverse(name[1:-1])

word=input('Enter a string: ')
reverse(word)

#Reversing a sentence and palindrome check
rlst=[]
def reverse(lst):
    global rlst
    if len(lst)>=1:
        rlst.append(lst[-1])
        reverse(lst[:-1])
    
    return rlst

sentence=input('Enter a sentence: ')
l=[]
l=sentence.split()
revsentence=' '.join(reverse(l))
if sentence==revsentence:
    print('Sentence is Palindrome')
else:
    print('Reverse sentence:',revsentence)
    print('Sentence not palindrome')

#Fibonacci series
def fibo(n):
    if n<=0:
        print('Invalid range. Provide 1 or above')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

n=int(input('Enter range: '))

print('Fibonacci series: ')
for x in range(1,n+1):
    print(fibo(x),end=' ')

#GCD using recursion
div=[]
d=1
def gcd(a,b):
    global d,div
    lim=a if a<b else b
    if d<=lim:
        if a%d==0 and b%d==0:
            div.append(d)
            d+=1
            gcd(a,b)
        else: 
            d+=1
            gcd(a,b)
    
    div.sort()
    return div[-1]

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
print('GCD of two numbers: ',gcd(a,b))






#lambda
odd_even=lambda n: print('Even') if n%2==0 else print('Odd')
n=int(input('Enter a number: '))
odd_even(n)

#filter
def even(l):
    if l%2==0:
        return True
    else:
        return False

l=[1,2,3,4,5]
even=list(filter(even,l))
print(even)

#filter using lambda
l=[1,2,3,4,5]
even=list(filter(lambda x:x%2==0,l))
print(even)

#map()
def km(m):
    return int(m*1.6)

mile=[3,4,5,5]
k=list(map(km,mile))
print(k)

#map() with lambda
mile=[3,4,5,5]
k=list(map(lambda x:int(x*1.6),mile))
print(k)

#reduce()
from functools import reduce
l=[1,2,3,4] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 







#Random module
import random
l=[]
for x in range(4):
    r=random.randint(0,9)
    l.append(r)
    
print(l) 
