class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Mobile:
    def print(self):
        print("i have 1+")
class Child(Person,Mobile):
    def info(self,college,place):
        self.college=college
        self.place=place
        print(self.college)
        print(self.place)
per=Person()
per.details("arun",23)
mob=Mobile()
mob.print()
ch=Child()
ch.details("maya",22)
ch.print()
ch.info("abcd","eranakulam")