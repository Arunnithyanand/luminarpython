salary=int(input("enter the salary"))
year=int(input("enter the year"))
if(year>5):
    salary=salary+(5/100)*salary
    print("salary is",salary)
else:
    print("salary is",salary)