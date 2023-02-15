# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end=(" "))
#     for j in range(1, i):
#         print("*", end=(" "))
#     for j in range(1, j + i):
#         print(" ", end=(" "))
#     print()


n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end=(""))
    for j in range(2*i+1):
        print("*",end=(""))
    for j in range(j+1):
        print(" ",end=(""))
    print()