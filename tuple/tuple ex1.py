# # tuple=1,2,3,4,5,6
# # print(tuple)
# # print("maximum value",max(tuple))
# # print("minimum value",min(tuple))
# # print("len",len(tuple))
# # print(tuple[1])  #tuple is immutable
# tuple1="arun",1,2
# print(tuple1)
#


lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
print(lst)
for i in lst:
    if i[3]>=15000:
        print(i)