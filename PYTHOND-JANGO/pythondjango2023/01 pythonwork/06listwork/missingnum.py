lst=[3,1,5,6,4]
lst.sort()

if(lst[0]!=1):
    print("1 is missing")
else:



    for i in range(0,len(lst)):
        cur=lst[i]
        next=lst[i+1]
        diff=next - cur
        if diff !=1:
            print(cur+1,"is missing")
            break



      