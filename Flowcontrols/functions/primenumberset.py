# print prime number set
s={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22}
print(s)
prime=set()
nonprime=set()
for i in s:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                nonprime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(nonprime)
