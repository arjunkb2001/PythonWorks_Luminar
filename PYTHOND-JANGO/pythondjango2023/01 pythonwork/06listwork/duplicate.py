  # last=[2,1,5,3,6,3,]
        # print duplicate num

lst=[2,1,5,3,6,3]

lst.sort()
duplicatelst=[]


# for i in range(len(lst)-1):
#     diff=lst[i+1]-lst[i]
#     if diff==0:
#         print(lst[i],"is duplii")
for i in range (0,len(lst)-1):
    cur=lst[i]
    next=lst[i+1]
    if cur==next:
        if cur not in duplicatelst:
            duplicatelst.append(cur)
print(duplicatelst)


# for i in range (len(lst)-1):
#     if lst[i]==lst[i+1]:
#         print(lst[i])
