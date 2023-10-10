expenses=[120,100,140,150,200,220]
min=expenses[0]
for i in range(0,6):
    if min>expenses[i]:
        min = expenses[i]
print(min)