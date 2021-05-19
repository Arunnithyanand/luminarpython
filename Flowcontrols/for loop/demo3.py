# lower limit and upper limit even numbers printing
# print lower and upper limit and find even numbers
lowerlimit=int(input("enter lowerlimit"))
upperlimit=int(input("enter upperlimit"))
for i in range(lowerlimit,(upperlimit+1)):
    if(i%2==0):
        print(i)

