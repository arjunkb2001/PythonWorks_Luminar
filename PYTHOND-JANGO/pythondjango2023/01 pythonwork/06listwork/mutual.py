alluser=["mohanlal","fahad","unny","mamooty","nivin","dq"]

nivinfrnd=["mohanlal","fahad","unny"]

fahadfrnd=["mohanlal","unny","mamooty"]

mutuallist=[]

for f in nivinfrnd:
    if f in fahadfrnd:
        mutuallist.append(f)

print(mutuallist)
