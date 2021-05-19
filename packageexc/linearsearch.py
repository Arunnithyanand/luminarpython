def search():
    list=[1,2,3,4,5,6,7,8,9]
    num=int(input("enter a number"))
    flag=0
    for i in list:
        if (num==i):
            flag=1
            break
    if(flag>0):
        print("element  found")
    else:
        print("element not found")
search()
