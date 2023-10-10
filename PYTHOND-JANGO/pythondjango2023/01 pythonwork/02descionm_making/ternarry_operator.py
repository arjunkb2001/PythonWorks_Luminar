# num=8
# even_odd="even" if num%2==0 else "odd"
# print(even_odd)

# num=int(input("enter a number ; "))
# alp="abc" if num%5==0 else "cde"
# print(alp)

# n1=5
# n2=10
# result=n1-n2 if n1>n2 else n2-n1
# print(result)

year=int(input("enter a year"))

print(f"{year}is a leeaoyear") if (year%400==0) and (year%100==0) (f"{year}is a leeapyear") elif (year%100!=0) and (year%4==0) else (f"{year}is not a leeapyear")