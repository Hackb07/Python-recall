#variables
#These are Strings
first_name = "Tharun"
last_name = 'Bala'
email = "balat4880@gmail.com"
print(first_name)
print(last_name)
print(email)

print(f"Hello {first_name} {last_name}")
print(f"Mail ID: {email}")
no_of_projects = 128
print(f"The Number of projects : {no_of_projects} completed")

#Integer
age =21
print(f"My age is {age}")

#Float
price = 10.99
distance = 72.5
print(f"the price is ${price}")
print(f"The distance between from Hosur to Bangalore {distance} miles.")

#Boolean
is_student = True
is_working_Professional = False
is_Professor = False

if is_student == is_working_Professional:
    print("you are a student.")
elif is_student == is_Professor:
    print("you are not a student.")
else:
    print("you are Professor.")