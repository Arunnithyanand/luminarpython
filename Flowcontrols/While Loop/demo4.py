# print lower and upper limit and find even numbers
lowerlimit=int(input("enter lowerlimit"))
upperlimit=int(input("enter upperlimit"))
while(lowerlimit<=upperlimit):
    if(lowerlimit%2==0):
        print(lowerlimit)
    lowerlimit+=1

