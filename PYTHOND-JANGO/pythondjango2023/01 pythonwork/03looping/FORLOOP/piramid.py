row = int(input("Enter number of rows: "))#6

for i in range(1,row):
    for space in range (row-i,1,-1):
        print(" ",end="")
    for str in range(i):
        print("* ", end="")
    print()