# add a word if that word is already present show the count of that word if it is not add that word

count={}
data=input("enter")
words=data.split(" ")
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)
