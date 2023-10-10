n=int(input("Enter a number: "))
x=n
numdigits=len(str(n))
sum=0

while x!=0:
    digit=x%10
    sum+=digit**numdigits
    x//=10
    
if n==sum:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")