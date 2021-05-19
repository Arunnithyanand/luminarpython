# Create a child class Bus that will inherit all of the variables and methods of Vehicle class?
# class Vehicle:
#     def details(self,type,maxspeed):
#         self.type=type
#         self.maxspeed=maxspeed
#
#         print("Vehicle type: ",self.type)
#         print("max speed: ",self.maxspeed,"km/hr")
# class Bus(Vehicle):
#     pass
# v=Bus()
# v.details("bus",78)
# print()
# k=Bus()
# k.details("car",85)

# Create a Book class with instance Library_name, book_name, author, pages?
# class Book:
#     def details(self,Library_name,book_name,author,pages):
#         self.library=Library_name
#         self.name=book_name
#         self.author=author
#         self.page=pages
#         print("library name: ",self.library)
#         print("Book name: ",self.name)
#         print("Author: ",self.author)
#         print("No of pages: ",self.page)
# book=Book()
# book.details("A454","WHY WE TOOK THE CAR","A K MAX",345)
# print()

#Create an Animal class using constructor and build a child class for Dog?
# class Animal:
#     def _init_(self,name,type):
#         self.name=name
#         self.type=type
#
#     def print(self):
#         print("Animal name: ",self.name)
#         print("Animal type: ",self.type)
#
# class Dog(Animal):
#     def _init_(self,petname,name,type):
#         super()._init_(name,type)
#         self.petname=petname
#
#     def printval(self):
#         print("Pet name: ",self.petname)
#
#
# b=Dog("Pinky","dog","domestic")
# b.print()
# b.printval()

#What is method overriding give an example using Books class?
# class Book:
#     def details(self,name,pages):
#         self.name=name
#         self.pages=pages
#         print("name: ", self.name)
#         print("Pages: ", self.pages)
#         print("bad")
# class Page(Book):
#     def details(self,name,pages):
#         self.name=name
#         self.pages=pages
#         print("name: ",self.name)
#         print("Pages: ",self.pages)
#         print("good")
# book=Page()
# book.details("Why we took the car",354)

#When is the finally block executed.Explain with example?

# a=10
# b=0
# try:
#     print("ans: ",a/b)
# except:
#     print("exceptional error occurred")
# finally:
#     print("done")

#Write a Python program to find the sequences of one upper case letter followed by lower case letters?
# import re
# r=input("enter the string")
# x='^[A-Z]{1}[a-z]+'
# match=re.fullmatch(x,r)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
# import re
# r=input("enter the string")
# x='^a[a-zA-Z0-9\D]+b$'
# match=re.fullmatch(x,r)
# if match is not None:
#     print("matching")
# else:
#     print("not matching")

# Create an example for three types of inheritance in one program by using Person as main class?
# class Person:
#     def print(self,name):
#         self.name=name
#         print(self.name)
#
#
# class Student:
#     def printval(self,age):
#         self.age=age
#         print(self.age)
#
# # single inheritance #
# class Print(Person):
#     def m(self):
#         print("details:")
#
# # multiple inheritance #
# class Parent(Person,Student):
#     def det(self,job):
#         self.job=job
#         print(self.job)
#
# # multi level inheritance #
# class Employee(Parent):
#     def details(self,salary):
#         self.salary=salary
#         print(self.salary,"Rs")



#     def _str_(self):
#         return self.name
#
# v=Print()
# v.m()
#
# o=Employee()
# o.print("Maneesh")
# o.printval(25)
# o.det("Engineer")
# o.details(50000)
# print()
# print(o)

# Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456

# import re
# r=open("phone","r")
# l=[]
# for i in r:
#     x='^[+][9][1][0-9]{10}'
#     n=re.findall(x,i)
#     if n!=[]:
#         l.append(n)
#         f=open("num","w")
#         f.write(str(l))


import re
f2=open("validreg",'w')
rule="([L][U][M]\d{2}[P][Y]\d{3}$)"
f=open("lumregno","r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        f2.write(number)
        f2.write("\n")