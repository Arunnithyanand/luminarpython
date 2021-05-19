# def add():
#     num1=int(input("enter first number"))
#     num2=int(input("enter the second number"))
#     print(num1+num2)
# def sub():
#     num1=int(input("enter first number"))
#     num2=int(input("enter the second number"))
#     print(num1-num2)
# def mul():
#     num1=int(input("enter first number"))
#     num2=int(input("enter the second number"))
#     print(num1*num2)
# def div():
#     num1=int(input("enter first number"))
#     num2=int(input("enter the second number"))
#     print(num1/num2)
# operator=input("choose the operation(+,-,*,/)")
# if(operator=="+"):
#     add()
# elif(operator=="-"):
#     sub()
# elif(operator=="*"):
#     mul()
# elif(operator=="/"):
#     div()
# else:
#     print("invalid operator")


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operation")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
while True:
    choice=input("Enter the choice")
    if choice in('1','2','3','4'):
        num1=float(input("enter a number"))
        num2=float(input("enter a number"))
        if choice=='1':
            print(add(num1,num2))
        elif choice=='2':
            print(sub(num1,num2))
        elif choice=='3':
            print(mul(num1,num2))
        elif choice=='4':
            print(div(num1,num2))
        break
    else:
        print("invalid")