# Validate Usr input exercise
# 1. username is no more 12 character
# 2. username must not contain space
# 3. username must not contain digits

username = input("Enter your username: ")


if len(username) > 12:
    print("Your UserName is longer than 12 characters")
elif not username.isalpha():
    print("Your UserName can't be alphanumeric")
elif not username.find(" ") == -1:
    print("Your UserName can't be a space")
else :
    print(f"Welcome {username}👍👍👍")