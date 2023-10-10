from re import*


phone=input("enetr variable")

rule="[a-zA-Z][\w_]*"

matcher=fullmatch(rule,phone)

if (matcher==None):
    print("valid")
else:
    print("valid")