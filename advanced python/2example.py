try:
    a=int(input())
    b=int(input())
    print(a+b)
except:
    print("enter int values")
finally:
    print("in finally")