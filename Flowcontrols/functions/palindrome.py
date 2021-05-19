a=input("enter a string")
temp=a
for i in a:
    rev=a[::-1]
if(rev==temp):
    print("yes its a palindrome")
else:
    print("its not a palindrome")