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





#Random module
import random
l=[]
for x in range(4):
    r=random.randint(0,9)
    l.append(r)
    
print(l) 
#lambda
odd_even=lambda n: print('Even') if n%2==0 else print('Odd')
n=int(input('Enter a number: '))
odd_even(n)
