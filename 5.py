lower=int(input("enter numbers"))
upper=int(input("enter upper digit"))
sum=0
i=1
while(lower<=upper):
    if(lower%2 !=0):
        sum+=lower
    lower+=1
print(sum)