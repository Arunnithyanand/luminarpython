lowerlimit=int(input("enter lowerlimit"))
upperlimit=int(input("enter upperlimit"))
sumeven=0
sumodd=0
for i in range(lowerlimit,(upperlimit+1)):
    if(i%2==0):
        sumeven=sumeven+i
    else:
        sumodd=sumodd+i
print(sumeven)
print(sumodd)