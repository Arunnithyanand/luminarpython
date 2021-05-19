#multilevel inheritence

class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Child(Person):
    def print(self,empid,post):
        self.empid=empid
        self.post=post
        print(self.empid)
        print(self.post)
class Parent(Person):
    def info(self,salary,experience):
        self.salary=salary
        self.experience=experience
        print(self.salary)
        print(self.experience)
class Student(Child):
    def det(self,std,sub):
        self.std=std
        self.sub=sub
        print(self.std)
        print(self.sub)
per=Person()
per.details("Anu",23,"Female")
ch=Child()
ch.details("Achu",24,"Male")
ch.print(1,"SM")
p=Parent()
p.details("Appu",23,"Male")
p.info(50000,4)
st=Student()
st.details("Kunju",23,"Female")
st.print(2,"HR")
st.det(5,"Python")