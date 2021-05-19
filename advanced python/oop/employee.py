class Employee:
    company="luminar"
    def setval(self,name,id):
        self.name=name
        self.id=id

    def printval(self):
        print("name",self.name)
        print("id",self.id)
        print("company",Employee.company)
st=Employee()
st.setval("arun",55)
st.printval()
st=Employee()
st.setval("bijoy",66)
st.printval()
