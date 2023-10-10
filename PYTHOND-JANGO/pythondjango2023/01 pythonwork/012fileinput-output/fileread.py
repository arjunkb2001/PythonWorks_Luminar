# f=open("C:/Users/91974/Desktop/pythonwork/012fileinput-output/data.txt","r")
f=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\data.txt","r")
lst=[]

for line in f:
    lst.append(line.rstrip("\n"))
print(lst)
longestword=max(lst,key=lambda w:len(w))
print(longestword)


