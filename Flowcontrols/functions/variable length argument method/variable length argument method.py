def add(num1,num2):
    return num1+num2
res=add(10,20)
print(res)

def add(num1,num2,num3):
    return num1+num2
res=add(10,20,30)
print(res)

def add(*args):
    res=0
    for num in args:
        res+=num
    return res
print(add(10,20,30,40))

def print_employee(**kwargs):
    for k,v in kwargs.items():
        print(k,"=>",v)

print_employee(id=100,place="thrissur",job="kakkanad")


