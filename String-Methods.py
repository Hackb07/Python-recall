name = input("Enter your Full name: ")
# .find() = return the character by the index
# .rfind() = return the character if not found by negative indexing
# .capitalize() = return the sting wil capitalized th first character
# .upper() = return the entire capitalized string
# .lower() = return the entire sting to a lower cased string
# .isdigit() = returns True of False if int is found
# .alpha() = returns Boolean if it entirely contains Alphabetics characters without space
# .count() = returns number of repeated values
# .replace() = replace the character that is in the parathesis
# help() = give the additional functions that can be used by strings

print(f"The Length of the Full name : {len(name)}") #prints no of characters
result = name.find(" ")
name = name.replace("T","S"
                        "")
print(f"The space found in {result}")
print(name)

phone_number = input("Enter your phone number: ")
results = phone_number.count("-")
print(results)
print(help(str))