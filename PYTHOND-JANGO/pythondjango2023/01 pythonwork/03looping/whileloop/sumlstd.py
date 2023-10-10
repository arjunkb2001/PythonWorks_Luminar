n=654
sum=0
while (n !=0):
    lastdigit=n%10
    sum=sum+lastdigit
    n=n//10
print(sum)
