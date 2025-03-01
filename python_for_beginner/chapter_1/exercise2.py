user_name = input("Enter Your name: ")

if len(user_name) <= 12 and " " not in user_name and not user_name.isdigit():
    print("Valid username")
else:
    print("Invalid username")



credit_card = input("Enter Your Credit Card Number: ")

if all(char.isdigit() or char == "-" for char in credit_card) and "-" in credit_card:
    last_four_digits = credit_card.replace("-", "")[-4:]

    print(f"Last four digits: xxxx-xxxx-xxxx-{last_four_digits}")
else:
    print("Provide a valid Credit Card number (only digits and hyphens allowed).")