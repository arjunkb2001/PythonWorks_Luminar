tweets="what a game ,hats, @arjun , @abhi , @tom "
word=tweets.split()

for w in word:
    if w.startswith("@"):
        print(w) 