start=int(input("enter the limit: "))
stop=int(input("enter the limit: "))


for num in range (start,stop+1):
    primenum=True
    for n in range (2,num):
        if num%n==0:
            primenum=False
            break
    if(primenum==True):
        print(num)


