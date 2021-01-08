#Homework
l=[1,3,5,7,9]
print('Given digits:',l) 
l=[]
i=1
while i<=9:
    j=1
    while j<=9:
        s=(i*10)+j
        l.append(s)
        j+=2
    i+=2
print('All possible 2-digit numbers:')
for x in l:
    print(x,end=' ')
    
#Homework using dict
l=[1,3,5,7,9]
print('Given digits:',l)
d={}
for x in l:
    d[x]=l
out=[]
length=len(l)

for key,value in d.items():
    for x in range(length): 
        s=(key*10)+value[x]
        out.append(s)
 
print('Possible two digit numbers:\n',out)


#Functions

def name(x): #x-> formal parameter
    print('Hi',x)

def welcome():
    print('Welcome to Python')

name('Ilango')#actual parameter
welcome()

#return statement
def multiply(a,b):
    return a*b

def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a//b
    
    return add,sub,mul,div
    
def sub(a,b):
    sub=a-b
    
print(multiply(2,10))
print(calc(2,10))
print(sub(2,10))

print(type(sub(2,10)))
print(type(multiply(2,10)))
print(type(calc(2,10)))

#Types of arguments
#Positional arguments
def add(a,b):
    print(b,a)
add('Ilango','Hi')

#Keyword arguments

def add(c,b,a):
    print(a,b)
    print(c)

#add(2,a=10,b=20)
add(a=10,b=20,2)

#Default arguments
def msg(name='Customer',item='Electronics'):
    print('Dear',name,',Product:',item)
    #print(a)

msg('Ilango','Laptop')
msg()
#msg(10,'Ilango','Laptop')

#Variable length argumentsdef add(*n):
    sum=0
    for x in n:
        sum+=x
    return sum

print(add(10))
print(add(10,20,30))

def numalpha(**kywrd):
   for num,alpha in kywrd.items():
        print(num,'->',alpha)
numalpha(one=1,two=2,three=3)

#Global and local constants
lightstatus = 'OFF'
def day():
    print('Day Light status:',lightstatus)
def night():
    lightstatus='ON'
    print('Night Light status:',lightstatus)
    print('No person at home, Light status:',globals()['lightstatus'])

day()
night()


























