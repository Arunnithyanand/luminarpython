# maximum among 2  numbers and if numbers are equal print both numbers are equal
num1=int(input("enter first number"))
num2=int(input("enter second number"))
if(num1<num2):
    print(num2,"greater than",num1)
elif(num1>num2):
    print(num1,"greater than",num2)
else:
    print("both numbers are equal")