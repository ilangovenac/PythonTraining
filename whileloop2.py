#Program to find number of words in a sentence

#text=input('Enter sentence: ')
#length=len(text)
#i=0
#space=0
#while i<length:
#    if text[i]==' ':
#        space+=1
#    i+=1
#if text[length-1]==' ':
#    space-=1
#    print('No of words: ',space+1)
#else:
#    print('No of words in sentence:',space+1)

#Program to find number of words in a sentence using ASCII values
#text=input('Enter sentence: ')
#i=0
#wordcount=1
#while i<len(text)-1:
#    if text[i]==' ':
#        if text[i+1]>'a' or text[i+1]<'z':
#            wordcount+=1
#    i+=1
#print('Numbers of words in text:',wordcount)

#i=1
#while i<=5:
#    if i==4:
#        i+=1
#        continue
#    print(i,end=' ')
#    i+=1
#else:
#    print('\nApplied filter for given range')

#i=1
#while i<=10:
#    if i==6:
#        i+=1
#        break
#    print(i,end=' ')
#    i+=1
#else:
#    print('\nApplied filter for given range')  

#///////////////
    
#maxrange=int(input('Enter maximum of range: '))
#total=0
#i=1    
#while i<=maxrange:
#        total+=i
#        i+=1
#print('Total of numbers in range:',total)
#print('Average of numbers in range:',total/maxrange)

#//////////////////////

#Program to find HCF of two numbers


limit=n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
if n1>n2:
    limit=n2
while limit>=1:
    if n1%limit==0 and n2%limit==0:
        break
    limit-=1
print('HCF of two numbers:',limit)











    
    
    
    
    
    
    