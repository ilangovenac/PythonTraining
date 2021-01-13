#Object Oriented Programming System
class library:
    '''library class about materials in a library'''
    def __init__(self,a,b,c='Tamil,Eng,French'):
        self.count=a
        self.totalprice=b
        self.languages=c

book=library(5,2000,'Tamil&English')
magazine=library(6,2000,'Tamil&English')
newspaper=library(4,500)

print(book.languages)
print(magazine.count)
print(newspaper.languages)

#Construction evidence
class library:
    '''library class about materials in a library'''
    def __init__(self):
        print('Initiation')

book=library()
magazine=library()
newspaper=library()

#Class specific attribute
class library:
    '''library class about materials in a library'''
    location='Chennai'
    materialType='paperback'
    def __init__(self,a,b,c='Tamil,Eng,French'):
        self.count=a
        self.totalprice=b
        self.languages=c

book=library(5,2000,'Tamil&English')
magazine=library(6,2000,'Tamil&English')
newspaper=library(4,500)

print(library.location)
print(library.materialType)
book.materialType='eBook'
print(book.materialType)
print(magazine.materialType)

#Functions on objects 
class library:
    '''library class about materials in a library'''

    def lend(self,noOfbooks):
        print('STATUS:',noOfbooks,'books on lend')

books=library()
books.lend(2)

#Object attributes using class
class library:
    '''library class about materials in a library'''

    def __init__(self):
        self.instock=6

books=library()
print('No of books in stock:',books.instock)

#Instance method
class library:
    '''library class about materials in a library'''

    def __init__(self,a,b,c):
        self.available=a
        self.onlend=b
        self.author=c
    def status(self):
        print('Author:',self.author)
        print('Available:',self.available)
        print('Copies on lend:',self.onlend)


LearnPython=library(10,3,'ABC')
LearnPython.status()

#Class method
class library:
    '''library class about materials in a library'''
    openTime='(Open Time:9AM TO 5PM. Except Sundays)'
    @classmethod
    def checkStatus(cls,query):
        if query!='Sunday':
            print('Open')
        print(cls.openTime)
  
library.checkStatus('Tuesday')

#Staticmethod
class words:
    '''library class about materials in a library'''
    @staticmethod
    def concatenate(word1,word2):
        print(word1+word2)

words.concatenate('washing','machine')






















