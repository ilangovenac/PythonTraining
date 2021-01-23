#Encapsulation
class parent:
    a=100#public
    _b=200#protected
    __c=300#private
    def test(self):
        print(parent.a)
        print(parent._b)
        print(parent.__c)

#t=parent()
#t.test()
print(parent.a)
print(parent._b)
print(parent.__c)

#Exception handling
try:
    no1=int(input('Enter 1st number: '))
    no2=int(input('Enter 2nd number: '))
    print(no1/no2)
    
except (ZeroDivisionError,ValueError):
    print('Check input values and type')

finally:
    print('finally block')

print('End of program')

#Nested exception handling
try:
    no1=int(input('Enter 1st number: '))
    no2=int(input('Enter 2nd number: '))
    try:
        print(no1/no2)
    except (ZeroDivisionError,ValueError):
        print('Check input values & types')
    finally:
        print('Division exception handled')

except ValueError:
    print('Check input datatype')

finally:
    print('End of exception')

#Userdefined expection
class NotevenException(Exception):
    def __init__(self,msg):
        self.message=msg
        print(self.message)

try:
    a=int(input('Enter a even number: '))
    if (a%2!=0):
        raise NotevenException('Input not even number')

except (NotevenException):
    print('Checking for default and user defined exception')


