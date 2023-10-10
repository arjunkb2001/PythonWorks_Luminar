# predefined character sets
# [0-9]
# [^0-9]
# [a-z]
#［A-Z]
# [a-zA-ZI
# [^a-ZA-ZI
# [0-9a-ZA-Z]
# [40-9a-ZA-71
# consanants #10:
# predefined characters


from re import *

# text="hellothere@12"

# pattern="[^aeiou]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group())

text="hellothere@12"

pattern="b-df-hj-np-tv-z"

matcher=finditer(pattern,text)

for m in matcher:
    print(m.group(),m.start)