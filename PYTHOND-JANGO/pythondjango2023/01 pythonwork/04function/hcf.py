num1 = int(input("enter the number1: "))
num2 = int(input("enter the number2: "))

def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

result = find_hcf(num1, num2)
print("the hcf of", num1, "and", num2, "is", result)
