#Shopping Vart Program

foods = []
prices =[]
total = 0

while True:
    food = input("Enter food(q to Quit):")
    if food.lower() == "q" :
        break
    else :
        price = float(input(f"Enter price of {food} :$"))
        foods.append(food)
        prices.append(price)

print("========= Your Cart =========")
for food in foods:
    print(f"{food:10}")

for price in prices:
    total += price

print(f"Total Price: {total}")

