# maximum among 3 numbers
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if((num1>num2)&(num1>num3)):
    print("num 1 is greater than num2 and num 3")
elif((num2>num1)&(num2>num3)):
    print("num 2 is greater than num 1 and num3")
else:
    print("num 3 is greater than num1 and num 3")