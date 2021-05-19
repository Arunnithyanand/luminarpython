class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Employee():
    def __init__(self,name,empid,age,place):
        super().__init__(name,age)
        self.empid=empid
        self.place=place
    def print(self):
        print(self.empid)
        print(self.place)
cr=Employee("arun","acb",24,"kochi")
cr.printval()
cr.print()