
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

# bmi = weight/(height**2)

# print("Your BMI is:", bmi)

# bmi value >19 underweight

# bmi value 19-25 normal weight

# bmi value 25-30 over weight

# >30 obesity

# weight_inkg=75
# height_incm=105

height=height/100
bmi=weight//height**2
print(bmi)

if(bmi<19):
    print("underweight")
elif(bmi<=25):
    print("normalweight")
elif(bmi<=30):
    print("overweight")
else:
    print("obesity")