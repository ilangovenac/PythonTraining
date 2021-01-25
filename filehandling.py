#file handling
file=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt','w')

print(file.name)
print(file.mode)#w-write,r-read
print(file.readable())#To check readability
print(file.writable())#To check writability
print(file.close())#Check if file closed

file.close()
print(file.close())

#file writing
file=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt','w')

file.write('Hi\nHow are you')

file.close()

#file writing using list
file=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt','w')
lst=['hi\n','how are you']
file.writelines(lst)

file.close()

#file reading
file=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt','r')

data=file.read()
print(data)

#file preset or not
import os
a = os.path.isfile('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt')

if a:
    print('File Present')
else:
    print('File Not present')

#linecount,wordcount,charcount
import os
a = os.path.isfile('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt')

if a:
    print('File Present')
    file=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\sample.txt','r')
    linecount=wordcount=lettercount=0
    for x in file:
        print(x)
        linecount+=1
        w=x.split()
        wordcount+=len(w)
        lettercount+=len(x)
    
else:
    print('File Not present')

print('Linecount: ',linecount)
print('Wordcount: ',wordcount)
print('Character count: ',lettercount) 

#Binary data handling
input=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\kobe.jpg','rb')
output=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\Medical\\bryant.jpg','wb')

img=input.read()

out=output.write(img)

#CSV data handling
import csv

w=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\location.csv','w',newline='')
location=csv.writer(w)
location.writerow(['SNo','City','State'])
count=int(input('Enter number of locations: '))
for x in range(count):
    SNo=input('Enter SNo: ')
    city=input('Enter city: ')
    state=input('Enter state: ')
    location.writerow([SNo,city,state])

#Reading csv
import csv

w=open('C:\\Users\\Ilangoven\\Documents\\PyTraining\\location.csv','r',newline='')
#w= open("location.csv", "r",newline='')
r = csv.reader(w)  #reader object 
output = list(r)
for x in output:
    for y in x:
        print(y, end = ' ')
    print()
    
#Regex example
import re

mobnumtemplate=re.compile('(0|91)?[6-9][0-9]{9}')
usermobnum=input('Enter mob number: ')
check=mobnumtemplate.search('User mobile number'+usermobnum)
print(check)




