class Person:                       #supeclass
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):                  #derived class/sub class/child class
    def print(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)
per=Person()
per.setval("arun",24,"male")
st=Student()
st.print("mca","sdit")
st.setval("bijoy",24,"male")
st.printval()



#single inheritance