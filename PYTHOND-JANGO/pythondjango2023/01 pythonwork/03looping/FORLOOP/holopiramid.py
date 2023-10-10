row = int(input('Enter number of rows : '))

for i in range (row):
    for str in range(row-i ):
        print(' ',end=" ")
    for str in range(2*i+1):
        if str==1 or str==2*i or i==row-1:
            print("* " , end="")
        else:
            print(" ",end="")
    print()

# row = int(input('Enter number of rows : '))

# for i in range(row):
#     for j in range(row-i):
#         print(' ', end='')

#     for j in range(2*i+1):
#         if j==0 or j==2*i or i==row-1:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print() 