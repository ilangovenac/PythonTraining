#Square numeric pattern

#1

side=int(input( 'Enter side value: '))
row=1
while row<=side:
    if row%2==0:
        col=1
        while col<=side:
            print('0',end=' ')
            col+=1
    else:
        col=1
        while col<=side:
            print('1',end=' ')
            col+=1
    print()
    row+=1
    
#2

side=int(input('Enter side value: '))
row=1
while row<=side:
    col=1
    while col<=side:
        if col%2==0:
            print('1',end=' ')
        else:
            print('0',end=' ')
        col+=1
    print()
    row+=1

#3

side=int(input('Enter an odd side value: '))
row=1
center=side//2+1
while row<=side:
    col=1
    while col<=side:
        if col==center and row==center:
            print('0',end=' ')
        else:
            print('1',end=' ')
        col+=1
    print()
    row+=1

#4

side=int(input('Enter side value: '))
row=1
while row<=side:
    if row==1 or row==side:
        print('0',end=' ')
        col=2
        while col<side:
            print('1',end=' ')
            col+=1
        print('0',end=' ')
    else:
        print('1',end=' ')
        col=2
        while col<side:
            print('0',end=' ')
            col+=1
        print('1',end=' ')
    
    print()
    row+=1

#5

row=1
while row<=5:
    col=row
    while col<=5-1:
        print(col,end=' ')
        col+=1
    col=1
    while col<=row:
        print('5',end=' ')
        col+=1
    print()
    row+=1

#6

n=int(input('Enter range: '))
row=1
while row<=(n*2)-1:
    while row<=n:
        col=1
        while col<=row:
            print(col,end=' ')
            col+=1
        col=row-1
        while col>=1:
            print(col,end=' ')
            col-=1
        print()
        row+=1
        
    while row>n and row<=(n*2)-1:
        s=n-(row-n)
        col=1
        while col<=s:
            print(col,end=' ')
            col+=1
        col=s-1
        while col>=1:
            print(col,end=' ')
            col-=1
        print()
        row+=1