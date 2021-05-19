# check wheather a number is prime or not with in range
num1=int(input("enter the lower limit"))
num2=int(input("enter the upper limit"))
sum=0
for a in range(num1,num2):
    if a > 1:
        for i in range(2,a):
            if(a%i)==0:
                break
        else:
            print(a)
            sum+=a
print("sum of prime number in",num1,"to",num2,"is",sum)