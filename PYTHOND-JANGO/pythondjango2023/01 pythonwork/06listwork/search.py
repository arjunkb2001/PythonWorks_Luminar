#linear searching

lst=[10,2,13,14,5]

element=13
i=0
limit=len(lst)

ispresent=False
while(i<limit):
    curval=lst[i]
    if curval==element:
        ispresent=True
        break
    i+=1
print(ispresent)