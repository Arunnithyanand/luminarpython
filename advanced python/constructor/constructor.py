# constructor to iniatialize instance variables
# constructor automatically invoke when creating

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
per=Person("arun",24,"female")
per.printval()