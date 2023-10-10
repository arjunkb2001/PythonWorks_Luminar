from re import*
text="abababacdgfhaaa"

# quantifiers

# pattern="a+" # one or more occurance of a

pattern="a*"  #  zero or more occurance of a

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())