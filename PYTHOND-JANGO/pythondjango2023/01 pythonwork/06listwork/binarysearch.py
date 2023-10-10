lst=[10,2,13,14,5]
element=14

lst.sort()
low=0
upp=len(lst)-1

ispresent=False

while(low<=upp):

    mid=(low+upp)//2
    if element==lst[mid]:
        ispresent=True
        break
    elif (element<lst[mid]):
        upp=mid-1
    elif (element>lst[mid]):
        low=mid+1
print(ispresent)  