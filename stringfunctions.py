#finding location and no of times of a substring
sen=input('Enter a sentence: ')
sub=input('Enter substring to be searched: ')
count=0
index=-1
length=len(sen)
while True:
    value=sen.find(sub,index+1,length)
    if value==-1:
        print('''Substring '{}' is not present'''.format(sub))
        break
    index=value
    print('Substring is present at:',value)
    count+=1
print('''No. of times '{}' present is:'''.format(sub),count)

#using count() function
sen=input('Enter a sentence: ')
sub=input('Enter substring to be searched: ')
print('No of times present: ',sen.count(sub))

#Replace functions1='Tom'
s2=s1.replace('m','g')
print(s2)
s1='It is wrong'
s2=s1.replace('wrong','fine')
print(s2)

#str function list
s='welcome to python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s.startswith('python'))
print(s.endswith('python'))
print(s.isalpha())
print(s.isdigit())
print(s.isupper())
print(s.islower())
print(s.isspace())

#Program to alternatively merge two strings
s1=input('Enter 1st string: ')
s2=input('Enter 2nd string: ')
comb=''
if len(s1)<len(s2):
    for i in range(len(s1)):
        comb=comb+s1[i]+s2[i]
        i+=1
    for x in range(i,len(s2)):
        comb+=s2[x]
        x+=1
    print('Merged string is:',comb)
else:
    for i in range(len(s2)):
        comb=comb+s1[i]+s2[i]
        i+=1
    for x in range(i,len(s1)):
        comb+=s1[x]
        x+=1
    print('Merged string is:',comb)    


