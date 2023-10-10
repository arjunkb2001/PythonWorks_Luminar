

num=int(input("enter a num: "))
y=2
primenum=True

if((num) in [0,1]):
    primenum=False
else:
    for i in range (y,num):
        if num%i==0:
            primenum=False
            break
print(primenum)