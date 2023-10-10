# lower case...................\ 


# from re import*
# text="AVGTTAtghbgjg"

# pattern="[a-z]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())


# upper  case.....................


# from re import*
# text="AVGTTAtghbgjg"

# pattern="[A-Z]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())


# all alphabate....................

# from re import*
# text="AVGTTAtghbgjg"

# pattern="[A-Za-z]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

# all print..........................

# from re import*
# text="AVGTTA18514-5__tghbgjg"

# pattern="[A-Za-z0-9]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

# no numbers....................

# from re import*
# text="AVGTTA18514-5__tghbgjg"

# pattern="[^0-9]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())


# from re import*
# text="AVGTeiahdfghjeuuA18514-5__tghbgjg"

# pattern="[A E I O U a e i o u]"
# count=0
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())
#     count+=1
# print(count)


# couselen letters...................


from re import*
text="AVGTeiahdfghjeuuA18514-5__tghbgjg"

pattern="[^aeiouAEIOU_\W\d]"
count=0
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)