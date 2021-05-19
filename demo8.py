held=int(input("enter class held"))
attended=int(input("enter class attended"))
avg=(attended/held)*100
print("total attendance percentage",avg)
if(avg<75):
    print("can't write the exam")
else:
    print("you can write")