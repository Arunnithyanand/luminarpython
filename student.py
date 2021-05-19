class Student:
    def __init__(self,name,rollno,department):
        self.name=name
        self.rollno=rollno
        self.department=department
    def printval(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
    def __str__(self):
        return self.name+str(self.rollno)+str(self.department)
st=Student("arun",21,"mca")
st.printval()
print()
