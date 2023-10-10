from json import load
path="C:\\Users\\91974\\Desktop\\pythonwork\\013modules\\countries\\countries.json"

with open(path,encoding="utf-8") as f :

    countries=load(f)

# all countriess ?

for c in countries:
    print(c.get("name"))

# population under 4L ?

for c in countries:
    if c.get("population")<4000000:

        print(c.get("name"))


# how many countries?

countrie=[c for c in countries]
print(len(countrie))

# print all countries and there capitals?

cap_con=[[c.get("name"),c.get("capital")]for c in countries ]
print(cap_con)

#start with c ?

startwith_c=[c.get("name") for c in countries if c.get("name").casefold().startswith("c")]
print(startwith_c)

# countries sharing more borders?

# max__borders_con=max(countries,key=lambda c: len(c.get("borders"))) 
# print(max__borders_con.get("name"))


countrieswithborders=[c for c in countries if "borders" in c]
max_cont=max(countrieswithborders,key=lambda c : len(c.get("borders")))
print(max_cont.get("name"))



#  indias borders?

india_borders=[c.get("borders") for c in countries if c.get("name")=="Afghanistan"][0]
india_borders=[c.get("name") for c in countries if c.get("alpha3Code") in india_borders]

# print(india_borders)



# print all regions

all_regions={c.get("region") for c in countries}
# print(all_regions)

depended_con=[c.get("name") for c in countries if c.get("independent")==False]
print(depended_con)





wc={}                       #region wise count
for c in countries:
    region=c.get("region")
    if region in wc:
        wc[region]+=1
    else:
        wc[region]=1
print(wc)