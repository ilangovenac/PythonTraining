#Reversing a number with int input
n=int(input('Enter an integer: '))
total=0
r=len(str(n))
for x in range(r):
    total=total*10 + n%10
    n//=10
print('Reverse of number:',total)

#Patterns
#1
for row in range(1,6):
    for col in range(1,6):
        print(chr(96+row),end=' ')
        row+=1
    print()
    
#2
for row in range(1,6):
    k=5
    for col in range(1,row):
        print(k,end=' ')
        k-=1
    for col in range(1,7-row):
        print(6-row,end=' ')
    print()
    
#3
for row in range(1,6):
    k=row
    for col in range(1,7-k):
        print(k,end=' ')
        k+=1
    k=row
    for col in range(1,k):
        print(k-col,end=' ')
        col+=1
    print()

#4
for row in range(1,6):
    k=row
    for col in range(1,k):
        print(k,end=' ')
        k-=1
    for col in range(1,(7-row)):
        print(col,end=' ')
    print()
        