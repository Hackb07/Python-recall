#Excercise 2 shopping cart program

item = input("What items would you like to buy? :")
price = float(input("Enter the price :"))
quantity = int(input("Enter the quantity :"))
total = price * quantity


print(f"You have brought {quantity} x {item}/s ")
print(f"The total price is  ${total}")