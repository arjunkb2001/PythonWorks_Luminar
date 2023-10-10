# print all number 1 to 50 if num /by 3 print"a" 


s=1
e=10000
while(s<=10000):
    if s%15==0:
        print("a")
    elif s%5==0:
        print("cd")
    elif s%3==0:
        print("x")
    else:
        print(s)    
    s+=1
    