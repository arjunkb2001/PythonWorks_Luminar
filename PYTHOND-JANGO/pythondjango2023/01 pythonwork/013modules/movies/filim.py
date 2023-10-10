from json import load
path="C:\\Users\\91974\\Desktop\\pythonwork\\013modules\\movies\\mdb.json"

# f=open(path,encoding="utf-8")

with open(path,encoding="utf-8") as f :

    movies=load(f)

    # print total number of movies

    # print all movie name ?
    
# for m in movies:
#     print(m.get("title"))

# movie_name=[m.get("title")for m in movies]

# print(movie_name)

# print movie title released in 2005?

# for m in movies:
#     if m.get("year")=="2005":
#         print(m.get("title"))

# year_2005=[m.get("title")for m in movies if m.get("year")=="2005"]
# print(year_2005)

# print movie title whose genre="comdey"?


# comdy_movie=[m.get("title")for m in movies if "Comedy" in m.get("genres")]
# print(comdy_movie)

#length movie title?


# length_movie=max(movies,key=lambda m:int (m.get("runtime")))
# print(length_movie)


# print all genres?


# all_genres={g for m in movies for g in m.get("genres") }
# print(all_genres)

# 2015 relsed genres="comedy" print movies name?

cmdmv=[m.get("title") for m in movies if "Comedy" in m.get("genres") and m.get("year")=="2015"]
print(cmdmv)

# highest movies relesed in which year?

wc={}

for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1

print(max(wc,key=lambda k: wc.get(k)))
