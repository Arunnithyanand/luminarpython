cube=lambda num:num**3

sub=lambda num1,num2:num1-num2

mul=lambda  num1,num2:num1*num2

div=lambda  num1,num2:num1/num2




#
# lst=[7,8,9,4,3,1]
#
#
# if num> 5 num+

# else num-1
# [8,9,10,3,2,0]

# lst=[10,20,21,22,23]
# lst2=[20,21,10,22,23] check wheather they are same


lst=[7,8,9,4,3,1]
# op=[]
# for num in lst:
#     if num>5:
#         op.append((num+1))
#     else:
#         op.append((num-1))
# print(op)
op=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(op)
# print names staring with a 
lst=["ajay","nikhil","arun","nivin"]
anames=list(filter(lambda name:name[0]=='a',lst))
print(anames)