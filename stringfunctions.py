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