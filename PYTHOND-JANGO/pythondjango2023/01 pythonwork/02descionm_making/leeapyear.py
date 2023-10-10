# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

year=int(input("enter a year"))

# if year%4==0:
#     print(f"{year}is a leeapyear")
# else:
#     print(f"{year}not a leeapyear")

if(year%400==0) and (year%100==0):
    print(f"{year}is a leeaoyear")
elif(year%100!=0) and (year%4==0):
    print(f"{year}is a leeapyear")
else:
    print(f"{year}is not a leeapyear")