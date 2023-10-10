numbers=[1,2,3,5,11,44]

evenlist=[]

oddlist=[]

for n in numbers:
    evenlist.append(n) if n%2==0 else oddlist.append(n)
