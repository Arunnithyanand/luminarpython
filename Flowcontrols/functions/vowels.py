a=input("enter a string")
vowels="a","e","i","o","u"
flag=0
for i in a:
    if i in vowels:
        flag=flag+1
print(flag)