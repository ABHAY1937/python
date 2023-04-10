num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if(num1>num2) and (num1>num3):
    if(num2>num3):
        print("no 2 is the second largest",num2)
    else:
        print("num 3 is second largerst")
elif(num2>num1) and (num2> num3):
    if(num1>num3):
        print("second largest number is ",num1)
    else:
        print("second largesr number ",num2)
elif(num3>num2) and (num3>num1):
    if(num1>num2):
        print("second largest number is",num3)
    else:
        print("second largest number is",num1)