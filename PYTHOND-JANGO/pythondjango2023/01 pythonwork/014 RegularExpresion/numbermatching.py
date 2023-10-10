from re import*
text="abcda54jhg64h6"
Pattern="[0-9]"
matcher=finditer(Pattern,text)

for m in matcher:
    # print(f"location {m.start()} match group {m.group()}")
    print(m.start(),m.group())