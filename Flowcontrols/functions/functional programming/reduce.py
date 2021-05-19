import functools
arr=[1,2,3,4,5,6]
total=functools.reduce(lambda num1,num2:num1+num2,arr)
print(total)
highest=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
print(highest)