class Student:
    def __init__(self,name,rollno,department):
        self.name=name
        self.rollno=rollno
        self.department=department
    def printval(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
per=Student("arun",6,"MCA")
per.printval()
per=Student("maya",7,"MCA")
per.printval()