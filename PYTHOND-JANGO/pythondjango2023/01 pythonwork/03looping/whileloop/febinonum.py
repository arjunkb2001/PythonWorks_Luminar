num=int(input("enter the range: "))

pre=0
cur=1
is_fib=False

fnum=0

while(fnum<=num):
    fnum=pre+cur
    pre=cur
    cur=fnum
    if fnum==num:
        is_fib=True
        break
print(is_fib)
