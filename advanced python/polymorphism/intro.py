# polymorphism............many forms
# overloading..........same method name different signature/different parameteres
# overriding ..........same method same parameteres/child class method will work
# over loading
class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)
per=Student()
per.show(3,4)

#over riding

class Parent:
    def properties(self):
        print("10 lack rs,2 car")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")
c=Child()
c.marry()