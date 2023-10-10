n1=int(input("enter the num1: "))
n2=int(input("enter the num2: "))

# def smartsub (n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
#     # if(n1>n2):
#     #     x=n1-n2
#     #     print(x)
#     # elif(n2>n1):
#     #     x=n2-n1
#     #     print(x)
# smartsub(n1,n2)

smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1

print(smart_sub(n1,n2))