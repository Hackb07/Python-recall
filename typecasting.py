#Type casting = the process of converting a  variable from one data type to another str(),int(),float(),bool()


from variable import is_student

name = "Tharun"
age = 21
height = 1.75
is_student = True

print(type(is_student),is_student)
print(type(name),name)
print(type(age),age)
print(type(height),height)

height = int(height)
print(type(height),height)
age = float(age)
print(type(age),age)
age = str(age)
print(type(age),age)
age += "1"
print(type(age),age)