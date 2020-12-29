#Reversing a string
name=input('Enter name: ')
length=len(name)
for x in range(length-1,-1,-1):
    print(name[x],end=' ')

#Pattern using string
#1
name=input('Enter a name: ')
length=len(name)
for row in range(length):
    for col in range(length):
        print(name[col],end=' ')
    print()
    length-=1

#2
name=input('Enter a name: ')
length=len(name)
for row in range(length):
    for col in range(0,length-(row+1)):
        print('-',end=' ')
    for col in range(row+1):
        print(name[col],end=' ')
    print()
    
#in function
name='Ilango'
letter='g'
if letter in name:
    print('Present')
else:
    print('Not present')
    
sentence='Welcome to Tamil Nadu'
word='Tamil'
if word in sentence:
    print('Present')
else:
    print('Not present')

sentence='Welcome to Tamil Nadu'
if 'Tamil' in sentence:
    print('Present')
else:
    print('Not present')

sentence='Welcome to Tamil Nadu'.upper()
word='tamil'.upper()
if word in sentence:
    print('Present')
else:
    print('Not present')

#swapcase
name='kUMAr'
name=name.swapcase()
print(name)

#find and rfind
name='Ravi Kumar'
#     0123456789
print(name.find('a'))

name='Ravi Kumar'
#     0123456789
print(name.rfind('a'))

name='Ravi Kumar'
#     0123456789
print(name.find('a',2,9))


#strip function
sen=input('Enter a sentence: ')
print(sen.strip())

print(sen.rstrip())
print(sen.lstrip())

#index

sen='Welcome to Python'
print(sen.find('hi'))
print(sen.index('hi'))

    
    
    