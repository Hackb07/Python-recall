# dictionary = a collections of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {
    "USA" : "Washington DC",
    "India" : "Delhi",
    "China" : "Beijing",
    "Russia" : "Moscow"
}



if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")
capitals.update({"Germany" : "Berlin"})

for key,value in capitals.items():
    print(f"{key} => {value}")