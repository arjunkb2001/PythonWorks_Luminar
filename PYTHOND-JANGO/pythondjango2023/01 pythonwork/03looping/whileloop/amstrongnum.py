n=8208
sum=0
x=n
while (n !=0):
    lastdigit=n%10
    cube=lastdigit**4
    sum=sum+cube
    n=n//10
print(sum)   
if x==sum:
    print("is amstrong number")

else:
    print("not a amstrong number")