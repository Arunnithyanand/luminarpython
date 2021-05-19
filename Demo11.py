# num1,num2,num3 and print second largest number
num1=int(input("Enter first Number"))
num2=int(input("Enter second Number"))
num3=int(input("Enter third Number"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"second largest number")
    else:
        print(num3,"second largest number")
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1)
    else:
        print(num2)