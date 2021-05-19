#type of variables
#instance variable related to methods
#class variables related to class
class Student:
    college="luminar"
    def setval(self,name,id):
        self.name=name
        self.id=id

    def printval(self):
        print("name",self.name)
        print("id",self.id)
        print("college",Student.college)
st=Student()
st.setval("arun",5)
st.printval()
st=Student()
st.setval("maya",6)
st.printval()
