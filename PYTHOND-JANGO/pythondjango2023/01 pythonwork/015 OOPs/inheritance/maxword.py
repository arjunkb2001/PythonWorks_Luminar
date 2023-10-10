def max_word(*args):
    lengthy_word=max(args,key=lambda w:len(w))
    return lengthy_word

print(max_word("hello","goodmorning","evening")) 



