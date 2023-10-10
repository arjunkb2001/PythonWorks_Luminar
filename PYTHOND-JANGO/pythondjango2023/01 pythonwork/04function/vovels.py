name=input("enter a name: ")

def count(name):
    vc=0
    cc=0
    for i in range (len(name)):   
        if name[i] in ["a","e","i","o","u"]:
           vc=vc+1
        else:
            cc=cc+1
    print("vc=",vc)
    print("cc=",cc)            
count(name)
