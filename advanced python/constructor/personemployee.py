class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def setval1(self,name,empid):
        self.name=name
        self.empid=empid
        print(self.name)
        print(self.empid)
per=Person()
per.setval("arun",24,"male")
per.printval()
st=Employee()
st.setval("amal",24,"male")
st.printval()
st.setval1("bijoy",24)
