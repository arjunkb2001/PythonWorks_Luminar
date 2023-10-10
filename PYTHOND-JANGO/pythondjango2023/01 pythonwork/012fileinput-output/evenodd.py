f_read=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\oddevendata.txt","r")
odd_write=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\odddata.txt","w")
even_write=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\evendata.txt",)

for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_write.write(str(num)+"\n")
    else:
        odd_write.write(str(num)+"\n")