num=int(input("enter a number to be reverse"))
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("reverse of the num",rev)
