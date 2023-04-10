n=int(input("enter a number"))
for i in range(1,n):
    for j in range(n,i):

       if(i==0 or j==0 or i==(n-1) or j==(n-1) or i==j or i+j ==(n-1)):
          print("*",end=" ")
print()
