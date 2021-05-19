# dict={'Name':'Zara','Age':7,'Class':'First'}
# input=input("enter a key")
# flag=0
# for i in dict:
#     if i==input:
#         flag=1
#         break
# if flag==1:
#     print("key found")
# else:
#     print("key not found")

d={1:2,2:3,4:5,6:7,9:8}

def is_key_present(x):
    if x in d:
        print(x,'is present in the dictionary')
    else:
        print(x,'is not present in the dictionary')

is_key_present(9)
is_key_present(16)



