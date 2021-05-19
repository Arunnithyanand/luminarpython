b=input("enter a string")
a="hello"
flag=0
for i in a:
    if i in b:
        flag+=1
print(flag)
