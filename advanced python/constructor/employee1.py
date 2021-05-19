class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.salary)
    def __str__(self):
        return self.name+str(self.age)+str(self.salary)

emp=Employee("arun",24,25000)
emp.printval()
print(emp)
