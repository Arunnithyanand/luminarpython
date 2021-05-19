# import re
# n="hello"
# x='\w*'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter the number")
x='[+][9][1]\d{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")