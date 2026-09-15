# Collections = single "Variable" used to store multiple value
#   list = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove Ok. NO Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "cherry"] # list
vegetables = {"apple", "banana", "cherry"} # set
fast_food = ("fried_rice","gobi","noodles") # Tuples


#for Fruit in fruits:
  #  print(Fruit)

fruits.append("Avacoda")
print(fruits)

print("Kiwi" in fruits)
print(len(fruits) )
fruits[0] = "Tharun"
print(fruits)
print(fruits.index("Avacoda"))
print(fruits.count("Avacoda"))


#Set
vegetables = {"apple", "banana", "cherry"} #
print(vegetables)


