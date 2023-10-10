text="hello hai good oii goodmorning"

word=text.split(" ")

# smalestword=min(word,key=lambda w: len(w))


# print(smalestword)

srtword=sorted(word,key=lambda w:len(w),reverse=True)

print(srtword)