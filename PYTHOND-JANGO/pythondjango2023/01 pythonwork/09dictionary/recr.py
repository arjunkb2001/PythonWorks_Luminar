text="ABCDA"

#print first recrsive chracter
wc={}
for ch in text:

    if ch in wc:
        print("first recrsive ch :",ch)
        break
    else:
        wc[ch]=1