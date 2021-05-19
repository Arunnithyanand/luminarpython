# lowerrange=int(input("enter lower range"))
# upperrange=int(input("enter upper range"))
# for i in range(lowerrange,upperrange):
#     if(i%2==0):
#         for j in range(lowerrange,upperrange):
#             print()
#             for k in range(0,j):
#                 print(i,end=' ')
#     else:
#         for j in range(lowerrange, upperrange):
#             print()
#             for k in range(upperrange,j,-1):
#                 print(i, end=' ')



 # another method
# lowerrange=int(input("enter lower range"))
# upperrange=int(input("enter upper range"))
# for i in range(lowerrange,upperrange):
#     if(i%2==0):
#         r=6
#         for k in range(r,0,-1):
#             for j in range(0,k):
#                 print(i,end=" ")
#                 print("\r")
#     else:
#         r2=6
#         for l in range(r2):
#             for m in range(0,i+1):
#                 print(l, end=" ")
#             print("\r")


# s={1,2,3,4}
# print(s)
# its not keeping any order

# print which is the type
# a="abc"
# print(type(a))

# s=set()
# print(s)
# print(type(s))

s=set()
print(s)
print(type(s))
s.add(9)
s.add("hello")
s.add(True)
s.add(0.7)
print(s)