# Employee
age=int(input("enter age"))
sex=input("Enter Sex")
maritalstatus=input("Enter Marital Status")
placeofservice=input("enter place of service")
if(sex=='F'):
    print("work in urban areas")
elif(sex=='M')&(20<=age<=40):
    print("work anywhere")
elif(sex=='M')&(40<age<=60):
    print("Work in urban areas only")
else:
    print("ERROR")