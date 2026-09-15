fruit =      ["apple", "banana", "cherry"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken","fish","turkey"]

groceries = [fruit,vegetables,meats]

print(groceries[0][1])

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()