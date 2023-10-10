alluser=["akhil","nikil","mukil","vigil"]

akhilf=["mukil","vigil"]

# all=set(alluser)
# fl=set(akhilf)

suggwstion=set(alluser).difference(set(akhilf))

# suggwstionlst=list(suggwstion)
# akhilpos=suggwstionlst.index("akhil")
# suggwstionlst.pop(akhilpos)
print(suggwstion)

