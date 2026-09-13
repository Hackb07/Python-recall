#conditional Expression = A one line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y
num = 98423
#print("Positive" if num > 0 else "Negative")
a =6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(f"The Maximum Number is {max_num}")
print(f"The Minimum Number is {min_num}")

age = 21
status = "Adult" if age >=18 else "child"
print(f"The Status is {status}")