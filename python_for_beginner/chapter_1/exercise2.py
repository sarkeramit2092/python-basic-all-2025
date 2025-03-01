user_name = input("Enter Your name: ")

if len(user_name) <= 12 and " " not in user_name and not user_name.isdigit():
    print("Valid username")
else:
    print("Invalid username")
