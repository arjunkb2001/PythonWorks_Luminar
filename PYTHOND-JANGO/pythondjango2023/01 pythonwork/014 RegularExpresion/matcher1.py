# ..............numbers .................


# from re import *

# text="hellothere@42"

# pattern="\d"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())



# ...............except digits..............

# from re import *

# text="hellothere@42"

# pattern="\D"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())




# ...............alphanumeric.................

# from re import *

# text="hellothere@42"

# pattern="\w"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())


# ..............special characters................


from re import *

text="hellothere@42"

pattern="\W"

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())