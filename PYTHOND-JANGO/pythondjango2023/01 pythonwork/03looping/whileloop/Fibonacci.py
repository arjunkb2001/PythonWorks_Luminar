range=int(input("enter the range: "))
pre=0
cur=1
sum=0
x=1
print(pre)
print(cur)

while(x<=range):
    sum=pre+cur
    pre=cur
    cur=sum
    print(sum)
    x+=1


