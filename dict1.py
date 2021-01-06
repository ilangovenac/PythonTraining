#Homework problem
#To find salary per month
l=[]
for x in range(1,5):
    print('Enter no. of hours for Week %d'%x,end=' ')
    h=int(input())
    l.append(h)
sal=0
i=1
for x in l:
    if x<45:
        print('LOW WORK IN WEEK %d'%i)
        sal+=(x*100)
    elif x>60:
        sal+=6750#45*100+(60-45)*150
    else:
        sal+=4500+(x-45)*150
    i+=1
print('Total salary for the month:',sal)

#dict datatype


d={'ilango':90,'kumar':95,'ravi':85,'raj':85}
print(type(d))
print(d)

#Accessing a dict
d={1000:'Ilango',1001:'Ravi',1002:'Kumar',1003:'Raj',1004:'Rohit'}
print(d[1003])#printing value by specifying keys
d[1004]='Shankar'  #dict is mutable, values can be changed
d[2000]='Tamil' #creates a new key-value pair
print(d.get(1000))
print(d.get(1500))
print(d.get(1500,'Not Available'))
print(d[1500])

#Removal from dict
d={1000:'Ilango',1001:'Ravi',1002:'Kumar',1003:'Raj',1004:'Rohit'}
print(d.pop(1001))#Shows the item removed from dict
print(d)#dict without item after pop()
print(d.popitem())#removes an item randomly
print(d)#dict after item removed using d.popitem()
del d[1000]#deletes the item from dict
print(d)
d.clear()#clears all the items from dict
print(d)
del d #deletes the whole dict from memory
print(d)#shows as d not defined; as dict is deleted

#Accessing keys in dict
d={1000:'Ilango',1001:'Ravi',1002:'Kumar',1003:'Raj',1004:'Rohit'}
print(d.keys())#function keys used to print keys of dict
print(type(d.keys()))
#keys are of tuple data type, as they are immutable

#For getting keys separately
for x in d.keys():
    print(x)

#Accessing values in dict
d={1000:'Ilango',1001:'Ravi',1002:'Kumar',1003:'Raj',1004:'Rohit'}
print(d.values())#function values() used to print values of dict
print(type(d.values()))

#For getting values separately
for x in d.values():
    print(x)
    
#Accessing items in a dictd={1000:'Ilango',1001:'Ravi',1002:'Kumar',1003:'Raj',1004:'Rohit'}
print(d.items())#function items() used to print items of dict
print(type(d.items()))

#For getting items separately
for x in d.items():
    print(x)


    


