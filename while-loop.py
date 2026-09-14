# while loop = execute some code while some condition remains true

num = int(input("Enter a number between 1 and 100: "))

while num < 1 or num>100:
    print(f"{num} is not between 1 and 100")
    num = int(input("Enter a number between 1 and 100: "))

print(f"Your number is {num}.")