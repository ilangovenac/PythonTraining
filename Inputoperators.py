num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
print(num1+num2)

print('///////////')

result=input('Type the arithmetic expression: ')
print(eval(result))

print('///////////')

#n+=1 # n=n+1
#n-=2 # n=n-2
#n*=4 # n=n*4
#n//=5 # n=n//5

print('///////////')

a,b,c=10,20,30
print(a,b,c,sep='*')
print(a,b,c, end='STOP')

print('////////////')

a,b,c = 10,5.8,'Hi'
print('Value of a:%d'%a)
print('int value:%d,float value:%f,string:%s'%(a,b,c))

print('/////////////')

capital='Chennai'
state='Tamil Nadu'
print('{} is the capital of {}'.format(capital,state))


capital='Chennai'
state='Tamil Nadu'
print('{0} is the capital of {1}'.format(capital,state))

capital='Chennai'
state='Tamil Nadu'
print('{1} is the capital of {0}'.format(capital,state))













