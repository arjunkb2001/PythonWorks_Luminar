limit=int(input("enter the limit: "))
pre=0
cur=1

print(pre)
print(cur)


for i in range (1,limit+1):
    sum=pre+cur
    pre=cur
    cur=sum
    if sum<=limit:
        print(sum)
    else:
        break
