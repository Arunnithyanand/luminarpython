class Bmw:
    def intro(self):
        print("bmw have many verities")
    def hatchback(self):
        print("hatchback grand coupe")
class Child(Bmw):
    def hatchback(self):
        print(" Bmw having hatchback")
c=Child()
c.hatchback()