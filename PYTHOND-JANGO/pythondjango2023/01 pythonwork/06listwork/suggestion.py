alluser=["anju","chinju","manju","kunju","sasi"]

manjufrnd=["chinju", "kunju"]
suglst=[]
for x in alluser:
    if x not in manjufrnd:
        suglst.append(x)
suglst.pop(suglst.index("manju"))
print(suglst)