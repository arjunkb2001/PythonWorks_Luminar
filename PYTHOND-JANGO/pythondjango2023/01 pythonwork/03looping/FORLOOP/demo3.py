text="jhyghijijytfgyhujikolp;awertyuiop;lknbvcxsasdfghjk"
vc=0
cc=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
        vc+=1
    elif ch not in [" ",".",",",";",":"]:
        cc+=1
print("vc=",vc)
print("cc=",cc)