years=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\years.txt","w")

for y in range(1800,2050):
        years.write(str(y)+"\n")
years=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\years.txt","r")
leapyear=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\leapyear.txt","w")

for y in years:
        if (int(y)%4==0 and int(y)%100!=0)or(int(y)%400==0):
                leapyear.write(y)