#Logical Operator = evaluate multiple conditions (or , and , not)
#   or = at least one condition must be True
#   and = both condition must be True
#   not = inverts the condition ( True => False ; False => True)

temp = 35
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("Raining")
else:
    print("Not Raining.")

is_student = False
is_teacher = False
is_Professor = True
if is_student and is_teacher:
    print("You are in School.")
elif is_student and is_Professor:
    print("You are a College.")
else:
    print("You are in Institution.")


if is_student and not is_Professor:
    print("You are a College.")