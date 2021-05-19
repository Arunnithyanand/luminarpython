# # set can contain different type of elements
# s=set()
# n=int(input("enter a number of elements"))
# for i in range(0,n):
#     num=int(input("enter a number"))
#     while(num not in s):
#         s.add(num)
#     print(s)


s={1,2,3,4,5,6,7,8,9}
print(s)
s.remove(3)
print(s)
s.clear()