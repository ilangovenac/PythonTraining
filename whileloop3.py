#Reverse a number, Sum of digits and Number of digits

#num=input('Enter a number: ')
#count=0
#reverse=''
#digitsum=0
#i=len(num)-1
#while i>=0:
#    reverse+=num[i]
#    digitsum+=int(num[i])
#    count+=1
#    i-=1
#print('Reverse of the number:',reverse)
#print('Number of digits:',count)
#print('Sum of digits:',digitsum)
#if reverse==num:
#    print('Palindrome')
#else:
#    print('Not palindrome')

#num=num2=int(input('Enter a number: '))
#reverse=0
#digitsum=0
#count=0
#while num>0:
#    digitsum+=num%10
#    count+=1
#    reverse=reverse*10+num%10
#    num//=10
#print('Reverse of number:',reverse)
#print('Number of digits:',count)
#print('Sum of digits:',digitsum)
#if num2==reverse:
#    print('Palindrome')
#else:
#    print('Not palindrome')

#ARMSTRONG NUMBER

#num=num2=int(input('Enter a number: '))
#total=0
#while num>0:
#        digit=num%10
#        total+=digit**3
#        num//=10
#if num2==total:
#    print('Armstrong number')
#else:
#    print('Not Armstrong number')
    
#Printing a Fibonacci series
n1=-1
n2=1
range=int(input('Enter range of Fibonacci series: '))
while range>0:
    sum=n1+n2
    print(sum,end=' ')
    n1=n2
    n2=sum
    range-=1

    
    
    
    
    
    
    
    
    
    
    
    
    
