class Bank:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee:
    def print(self):
        print("all employees having bank account")
class Child(Bank,Employee):
    def information(self,company_name,place):
        self.company_name=company_name
        self.place=place
        print(self.company_name)
        print(self.place)
ch=Child()
ch.details("Arun",24,"male")
emp=Employee()
emp.print()
ch=Child()
ch.details("bijoy",23,"male")
ch.print()
ch.information("luminar","kochi")
ch.print()
