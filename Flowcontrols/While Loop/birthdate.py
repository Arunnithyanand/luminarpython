tyear=2021
tmnth=3
tday=25
print("today date",tday,"/",tmnth,"/",tyear)
year=int(input("enter the born year"))
mnth=int(input("enter the born month"))
day=int(input("enter the born day"))
print("given date",day,"/",mnth,"/",year)
y= tyear - year
m= tmnth - mnth
d= tday - day
if(tyear>=year):
    if(tmnth>=mnth):
        if(tday>=day):
            y=tyear-year
            m=tmnth-mnth
            d=tday-day
            d1=30-d
            print("you are",y,"years",m1,"months",d,"days old")
    elif (tmnth < mnth):
        if (tday >= day):
                y = tyear - year
                m = mnth - tmnth
                m1 = 12 - m
                d = tday - day
                print("you are", y, "years", m1, "months", d, "days old")
        else:
            y=tyear-year
            mnth=tmnth-mnth
            m1=12-m
            d=day-tday
            d1=30-d
            print("you are",y,"years",m1,"months",d1,"days old")

else:
    print("error")