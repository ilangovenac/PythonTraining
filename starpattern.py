#Basic pattern
row=1
while row<=5:
    col1=1
    while col1<=5:
        print('-',end=' ')
        col1+=1
    col2=1
    while col2<=5:
        print('*',end=' ')
        col2+=1
    print()
    row+=1

print('//////////')

#Variation 1
row=1
while row<=5:
    col=5
    while col>row:
        print('-',end=' ')
        col-=1
    col2=1
    while col2<=row:
        print('*',end=' ')
        col2+=1
    print()
    row+=1

print('//////////')

#Variation 2
row=1 
while row<=5:
    col=1
    while col<row:
        print('-',end=' ')
        col+=1
    col2=1
    while col2<=6-row:
        print('*', end=' ')
        col2+=1
    print()
    row+=1    

print('//////////')
    
#Variation 3
row=1
while row<=5:
    col=1
    while col<=6-row:
        print('*',end=' ')
        col+=1
    col2=1
    while col2<row:
        print('-',end=' ')
        col2+=1
    print()
    row+=1

print('//////////')

#Variation 4   
row=1
while row<=5:
    col=1
    while col<=row:
        print('*',end=' ')
        col+=1
    col2=5
    while col2>row:
        print('-',end=' ')
        col2-=1
    print()
    row+=1   

print('//////////')
   
#Combination of pattern

#Half diamond
row=1
while row<=5:
    col=5
    while col>=row:
        print('*',end=' ')
        col-=1
    col2=1
    while col2<row:
        print('-',end=' ')
        col2+=1
    col3=1
    while col3<row:
        print('-',end=' ')
        col3+=1
    col4=5
    while col4>=row:
        print('*',end=' ')
        col4-=1
    print()
    row+=1

print('//////////')

#Full diamond
row=1
while row<=5:
    col=5
    while col>=row:
        print('*',end=' ')
        col-=1
    i=1
    while i<=2:
        col2=1
        while col2<row:
            print('-',end=' ')
            col2+=1
        i+=1
    col4=5
    while col4>=row:
        print('*',end=' ')
        col4-=1
    print()
    row+=1
    
row=1
while row<=5:
    col=1
    while col<=row:
        print('*',end=' ')
        col+=1
    i=1
    while i<=2:
        col2=5
        while col2>row:
            print('-',end=' ')
            col2-=1
        i+=1
    col3=1
    while col3<=row:
        print('*',end=' ')
        col3+=1
    print()
    row+=1
 
print('//////////')

#Hollow square
side=int(input('Enter side of square: '))
row=1
while row<=side:
    if row==1 or row==side:
        col=1
        while col<=side:
            print('*',end=' ')
            col+=1
    if row>1 and row<side:
       print('*',end=' ')
       col=1
       while col<=(side-2):
        print(' ',end=' ')
        col+=1
       print('*',end=' ')
    print()
    row+=1

#Hollow square with diagnol
side=int(input('Enter side of square: '))
row=1
while row<=side:
    if row==1 or row==side:
        col=1
        while col<=side:
            print('*',end=' ')
            col+=1
    if row>1 and row<side:
       print('*',end=' ')
       col=2
       while col<side:
        if col==row:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        col+=1
       print('*',end=' ')
    print()
    row+=1

#Solid Rhombus
side=int(input('Enter a side of Rhombus: '))
row=1
while row<=side:
    col=5
    while col>row:
        print(' ',end=' ')
        col-=1
    col2=1
    while col2<=side:
        print('*',end=' ')
        col2+=1
    print()
    row+=1
    
#Hollow Rhombus
side=int(input('Enter side of Rhombus: '))
row=1
while row<=side:
    col=5
    while col>row:
        print(' ',end=' ')
        col-=1
    if row==1 or row==side:
        col=1
        while col<=side:
            print('x',end=' ')
            col+=1
    else:
        print('x',end=' ')
        col=2
        while col<side:
            print(' ',end=' ')
            col+=1
        print('x',end=' ')
    print()
    row+=1
    
#Pyramid Star Pattern
height=int(input('Enter height of triangle: '))
row=1
while row<=height:
    col=height
    while col>row:
        print(' ',end=' ')
        col-=1
    col=1
    while col<=row:
        print('*',end=' ')
        col+=1
    i=row-1
    while i>0:
        print('*',end=' ')
        i-=1
    col=height
    while col>row:
        print(' ',end=' ')
        col-=1
    print()
    row+=1














