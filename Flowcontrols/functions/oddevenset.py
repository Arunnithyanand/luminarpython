s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}
print(s)
odd=set()
even=set()
for i in s:
    if(i%2==0):
        even.add(i)
    else:
        odd.add(i)
print("set of odd",odd)
print("set of even",even)