#prime numbers

num=int(input("enter a number"))
flag=0
for i in range(2,num):
    if(num%2==0):

        flag=1
if(flag>=1):
    print("not prime")
else:
    print(" prime")

