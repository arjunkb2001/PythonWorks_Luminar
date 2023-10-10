num1 = int(input("enter the number1"))
num2 = int(input("enter the number2"))

def findlcm(a, b):

    maxnum = max(a, b)

    lcm = maxnum

    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += maxnum

    return lcm

result = findlcm(num1, num2)
print("the lcm of", num1, "and", num2, "is", result)
