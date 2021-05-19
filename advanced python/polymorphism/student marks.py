class Student:
    def __init__(self,name,rollno,department,marks):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.marks=marks

    def printval(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("department",self.department)
        print("marks",self.marks)
    def __str__(self):
        return self.name
lst=[]
f = open("studentmark", 'r')
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    rollno=data[1]
    department=data[2]
    marks=data[3]
    obj=Student(name,rollno,department,marks)
    lst.append(obj)
    mark=[]
for obj in lst:
    if(obj.marks==max(marks)):
        print(obj.name,obj.rollno,obj.department,obj.marks)
