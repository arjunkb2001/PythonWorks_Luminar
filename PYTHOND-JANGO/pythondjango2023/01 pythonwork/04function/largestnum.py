num1=int(input("entwr a num1= "))
num2=int(input("entwr a num2= "))
num3=int(input("entwr a num3= "))

def largestnum(num1,num2,num3):
    if (num1>num2)and(num1>num3):
        print("num1 is greater")
    elif (num2>num3)and(num2>num1):
        print("num2 is greater")
    elif(num1==num2)and(num2==num3):
        print("equeal")
    else :
        print("num3 is greater")
largestnum(num1,num2,num3)