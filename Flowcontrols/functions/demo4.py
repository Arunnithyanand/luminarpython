a="luminar"
b=input("enter a string")
flag=0
for i in b:
    if i in a:
        flag+=1
if(flag==1):
    print("present")
else:
    print("not present")


