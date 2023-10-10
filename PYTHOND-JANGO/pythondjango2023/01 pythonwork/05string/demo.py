text="am going for a trip"



vowels=('a',"e","i","o","u")
word=text.split(" ")
    
for w in word:
    if w.casefold().startswith(vowels):

        print(w)

