avg=[]

for i in range (0,5):
    num=int(input("enter the number: "))
    avg.append(num)

average=((sum(avg))//5)

print(f"avg of 5 numbers is {average}")