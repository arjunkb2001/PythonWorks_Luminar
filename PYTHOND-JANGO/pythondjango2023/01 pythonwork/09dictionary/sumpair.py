lst=[2,3,5,7]
sum=11
lst.sort()

low=0
upper=len(lst)-1

while (low<upper):
    cursum=lst[low]+lst[upper]
    if cursum==sum:
        print("pairs",lst[low],lst[upper])
        break
    elif cursum<sum:
        low+=1
    else:
        upper-=1
