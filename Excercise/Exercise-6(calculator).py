#Python Calculator
print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")
print("6. Modulo")

operator = input("Enter Your Operator:")
num1 = float(input("Enter Your Number 01:"))
num2 = float(input("Enter Your Number 02:"))

if operator == "1":
    print(num1 + num2)
elif operator == "2":
    print(num1 - num2)
elif operator == "3":
    print(num1 * num2)
elif operator == "4":
    print(num1 / num2)
elif operator == "5":
    print(num1 ** num2)
elif operator == "6":
    print(num1 % num2)
else:
    print("Invalid Operator")