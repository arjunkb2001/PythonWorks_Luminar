text="ABBCCDAE"

#print second recrsive chracter
wc={}
duplist=[]
for ch in text:

    if ch in wc:
       duplist.append(ch)
    else:
        wc[ch]=1
print(duplist[1])