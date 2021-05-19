class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
class Student(Person):
    def __init__(self,name,rollno,mark,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
cr=Student(2,34,"arun",25)
cr.printval()
cr.print()