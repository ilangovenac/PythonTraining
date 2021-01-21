#Operator overloading in of same class
class deposit:
    def __init__(self,money):
        self.money=money

    def __add__(self,partner):
        return self.money + partner.money

        
father=deposit(1000)
mother=deposit(1500)
print('Total deposit: ',father+mother)

#Operator overloading for different classes
class cash:
    def __init__(self,cash):
        self.cash=cash
    
    def __add__(self,other):
        return self.cash+user2.amount

class cheque:
    def __init__(self,amount):
        self.amount=amount
    
    def __add__(self,other):
        return user1.cash+self.amount

user1=cash(1000)
user2=cheque(2000)
print('Total_1: ',user1+user2)
print('Total_2: ',user2+user1)

#Method overloading
class number:
    def addition(self,*no):
        for i in no:
            print(i,end=' ')
c=number()
c.addition(10,20)
c.addition(10,20,30)

#Method Overiding
class parent:
	def activity(self):
		print("Walking")
		
class Child(parent):
	def activity(self):
		print("Playing basketball")
		#super().activity()
c = Child()
c.activity()

#Constructor overriding

class parent:
    def __init__(self):
        print('Parent Constructor')

class Child(parent):
    def __init__(self):
        print('Child constructor')

c = Child()

#Abstraction
from abc import *
class human(ABC):
    @abstractmethod
    def hobby(self):
        pass

class children(human):
    def hobby(self):
        print('Playing')
class adult(human):
    def hobby(self):
        print('Reading')

user1=children()
user1.hobby()
user2=adult()
user2.hobby()

#usage of globals()[*string*]
from abc import *
class human(ABC):
    @abstractmethod
    def hobby(self):
        pass

class children(human):
    def hobby(self):
        print('Playing')
class adult(human):
    def hobby(self):
        print('Reading')

name=input('Enter class name (children/adult): ')
classname=globals()[name]
user1=classname()
user1.hobby()
    