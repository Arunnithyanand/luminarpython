dict={}
f=open("text1","r")
for n in f:
    wr=n.split(" ")
    for word in wr:
        if word not in dict:
            dict.update({word:1})
        else:
             val=int(dict[word])
             val+=1
             dict.update({word:val})
print(dict)