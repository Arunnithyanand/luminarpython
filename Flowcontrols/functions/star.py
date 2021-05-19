# def star():
#     for i in range(1,6):
#         print()
#         for j in range(6,i,-1):
#             print("*",end=" ")
# star()
#
#
# triangle star

def triangle(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
triangle(9)


