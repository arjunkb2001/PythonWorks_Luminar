#sting=>> sequence of characters

name="ab cd efg"

print(name.casefold()) # uppercase to lowercase

print(name.capitalize()) # converted first letter to capital

print(name.count("m")) # is used to take the count of a letter or character in the string 

print(name.startswith("ab")) # is used check start it return boolean value 

print(name.endswith("fg")) # is used check end it return boolean value

print(name.isalpha()) # to check all are alphabet 

print(name.isdigit()) # to check all are digit

print(name.isalnum()) # to check alphabet and number 

print(name.strip("")) # to remove a specific obect left or right

print(name.rstrip("g")) # its used to remove right side character not a sequenc of word

print(name.lstrip("a"))  # its used to remove left side character not a sequenc of word

print(name.index("a")) # find the position of the letter

print(name.split()) # split the sentences to words 

words=name.split(" ")
for w in words:
    print(w)