text="hello good goodmorning"

word=text.split(" ")

longestword=max(word,key=lambda w: len(w))


print(longestword)

