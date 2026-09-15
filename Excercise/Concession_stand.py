#Concession stand Program
#dictionary {key : value }

menu = {
    "Pizza" : 6.99,
    "Coke" : 5.99,
    "Steak" : 24.55,
    "Idly" : 6.00,
    "Vada" : 10.99,
    "Dosa" : 35.00
}

cart = []
total = 0

print("=====Menu=====")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("=======================")

while True:
    food = input("What would you like(q to quit): ")
    if food == "q" or food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]



print()
print("================================")
print("          Your Order            ")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    print()
print()
print("================================")
print()

print(f"Total Cost : ${total:.2f}")