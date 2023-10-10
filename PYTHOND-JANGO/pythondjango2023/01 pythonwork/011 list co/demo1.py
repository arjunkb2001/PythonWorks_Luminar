#list comprehersion
lst=[5,2,4,6,9,11,21,10,7,8]

#cubes
cube=[n**3 for n in lst]
print(cube)

#squres
sque=[n**2 for n in lst]
print(sque)

#add two
add_two=[n+2 for n in lst]
print(add_two)

#greater five 
greater_five=[n for n in lst if n > 5]
print(greater_five)

#even
evem=[n for n in lst if n%2==0]
print(evem)

#odd
odd=[n for n in lst if n%2!=0]
print(odd)\

#year 
year=[y for y in range (1800,2026)]
print(year)

#century year
centy_years=[y for y in year if y%100==0]
print(centy_years)

#non century year
notcenty_years=[y for y in year if y%100!=0]
print(notcenty_years)