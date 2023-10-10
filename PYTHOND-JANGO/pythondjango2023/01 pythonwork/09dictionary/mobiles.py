phones=[
    {
        "name":"m13","brand":"samsung","network":"5g","colors":["black","grey"],
        "varients":[
            {"name":"4gb+64gb","price":10000},
            {"name":"8gb+128gb","price":12000},
        
        ]
    }, 
    {
        "name":"m30","brand":"samsung","network":"4g","colors":["black","white"],
        "varients":[
            {"name":"4gb+64gb","price":12000},
            {"name":"8gb+128gb","price":14000},
        
        ]
    },
    {
        "name":"oneplusnort2t","brand":"oneplus","network":"5g","colors":["black","grey"],
        "varients":[
            {"name":"4gb+64gb","price":2700},
            {"name":"8gb+128gb","price":30000},
        
        ]
    },
    {
        "name":"mi11i","brand":"mi","network":"5g","colors":["black","green"],
        "varients":[
            {"name":"4gb+64gb","price":25000},
            {"name":"8gb+128gb","price":28000},
        
        ]
    },



]

# # black color mobiles name:

# for m in phones:
#     if "black" in m.get("colors"):
#         print(m.get("name"))


# # print all mobile name available under 20k

# for m in phones:
#     for  v in m.get("varients"):
#         if v.get("price")<200000:
#             print(m.get("name"),v.get("name"))

for m in phones:
    if "black" in m.get("colors"):
         for  v in m.get("varients"):
            if v.get("name")=="8gb+128gb":
                print(m.get("name"))