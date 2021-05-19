lst=[15,1,0,8,876,100,54,23,-64,23,76]

def bsearch():
    lst.sort()
    print(lst)
    element=int(input("enter the element"))
    flag=0
    low=0
    upp=len(lst)-1
    while low<=upp:
        mid=(low+upp)//2
        if element>lst[mid]:
            low=mid+1
        elif element<lst[mid]:
            upp=mid-1
        elif element==lst[mid]:
            flag=1
            break
    if flag==1:
            print("element found")
    else:
            print("element not found")
bsearch()






