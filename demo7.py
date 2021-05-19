# 4 subjects marks and calculate total
# total
# 180-200 A+
# 160-179 A
# 140-159 B+
# 120-139 B
# 100-119 C+
# 80-99  C
# 60-79 D+
# else fail

num1=int(input("enter first subj mark"))
num2=int(input("enter second subj mark"))
num3=int(input("enter third subj mark"))
num4=int(input("enter fourth subj mark"))
total=num1+num2+num3+num4
if(180<=total<=200):
    print("GRADE IS A+")
elif(160<=total<=179):
    print("GRADE IS A")
elif(140<= total <= 159):
    print("GRADE IS B+")
elif(120<=total<=139):
    print("GRADE IS B")
elif(110<=total<=119):
    print("GRADE IS C+")
elif(80<=total<=99):
    print("GRADE IS C")
elif(60<=total<=79):
    print("GRADE IS D+")
else:
    print("FAILED")